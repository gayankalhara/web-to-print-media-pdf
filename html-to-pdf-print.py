import base64
import os

from selenium import webdriver
from selenium.common import TimeoutException
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

        # Check for 404 in title before waiting
        if "404" in driver.title:
            print(f"Skipping 404 page: {url}")
            return  # Skip to the next URL

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
    except TimeoutException:
        print(f"Timeout error on page: {url}")
    except Exception as e:
        print(f"An error occurred on page: {url}")
        print(e)
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
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/permanent-residence-skilled-regional-191",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/pacific-engagement-visa-192",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/regional-sponsored-migration-scheme-187",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/skilled-employer-sponsored-regional-provisional-494",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/skilled-independent-189",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/skilled-nominated-190",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/skilled-recognised-graduate-476",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/skilled-regional-provisional-489",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/skilled-regional-887",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/skilled-work-regional-provisional-491",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/state-or-territory-sponsored-business-owner-892",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/state-or-territory-sponsored-investor-893",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/temporary-activity-408",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/temporary-graduate-485",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/temporary-work-international-relations-403",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/temporary-work-short-stay-specialist-400",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/temporary-skill-shortage-482",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/global-special-humanitarian-202",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/protection-866",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/refugee-visas",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/temporary-protection-785",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/safe-haven-enterprise-visa-790",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/resolution-of-status-visa-851",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/bridging-visa-a-bva-010",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/bridging-visa-b-bvb-020",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/bridging-visa-c-bvc-030",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/bridging-visa-e-bve-050-051",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/crew-travel-authority-visa-942",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/former-resident-visa-151",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/maritime-crew-visa-988",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/medical-treatment-602",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/resident-return-visa-155-157",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/special-category-visa-444",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/special-purpose-visa",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/investor-retirement-visa-405",
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/confirmatory-residence-visa-808"
]

output_folder = "generated_pdfs"  # Specify output folder
os.makedirs(output_folder, exist_ok=True)  # Create folder if it doesn't exist

for url in urls:
    generate_pdf_from_url(url, output_folder)