import base64
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def generate_pdf_from_url(url, output_folder):
    """Generates a PDF from a URL using headless Chrome and CDP command."""
    options = Options()
    # options.add_argument("--headless")  # Remove for visual inspection
    options.add_argument("--disable-gpu")
    options.add_argument("--enable-javascript")

    # Path to the Chrome driver executable (replace with your path)
    chrome_driver_path = "/Users/gayankalhara/projects/links-to-docx-print/chromedriver"
    service = Service(chrome_driver_path)

    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)

        # Wait for a specific element to ensure page load (example)
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located((By.ID, "authWrapper")))

        # Remove unwanted divs
        remove_elements_by_id(driver, "nuanMessagingFrame")
        remove_elements_by_class(driver, "clickbot")

        # Generate PDF using CDP command
        pdf_data = driver.execute_cdp_cmd("Page.printToPDF", {"printBackground": False})
        pdf_bytes = base64.b64decode(pdf_data["data"])

        # Extract filename from URL
        filename = os.path.basename(url) + ".pdf"
        output_filename = os.path.join(output_folder, filename)

        with open(output_filename, "wb") as f:
            f.write(pdf_bytes)

        print(f"PDF generated successfully: {output_filename}")

    finally:
        driver.quit()


# Helper functions to remove elements
def remove_elements_by_id(driver, id):
    elements = driver.find_elements(By.ID, id)
    for element in elements:
        driver.execute_script("""
            var element = arguments[0];
            element.parentNode.removeChild(element);
        """, element)


def remove_elements_by_class(driver, class_name):
    elements = driver.find_elements(By.CLASS_NAME, class_name)
    for element in elements:
        driver.execute_script("""
            var element = arguments[0];
            element.parentNode.removeChild(element);
        """, element)

# Example Usage:
urls = [
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/electronic-travel-authority-601",
]

output_folder = "generated_pdfs"  # Specify output folder
os.makedirs(output_folder, exist_ok=True)  # Create folder if it doesn't exist

for url in urls:
    generate_pdf_from_url(url, output_folder)