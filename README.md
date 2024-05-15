# Webpage to PDF Converter in Print Media Format

This Python script is designed to generate clean, printable PDFs from web pages. It utilizes Selenium WebDriver with Chrome to navigate to specified URLs, apply some basic cleanup to the page structure (optional), and then generates a PDF using Chrome's built-in PDF printing capabilities.

## Features

- **Headless Chrome:** Operates without a visible browser window (can be disabled for debugging).
- **@media print Optimization:** Takes advantage of websites' print stylesheets for cleaner PDFs.
- **Customizable:** Easily modify the script to remove specific elements or adjust page settings.
- **Error Handling:** Includes basic error handling for timeouts and other exceptions.

## Demo Usage

This script was used to download and convert the VISA pages from the Australian Department of Home Affairs website ([https://immi.homeaffairs.gov.au](https://immi.homeaffairs.gov.au)) into PDFs.

## Installation & Setup

1. **Clone the Repository:**

    ```bash
    git clone https://your-repository-url.git
    cd your-repository-name
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Download Chrome Driver:**

    - Visit the [Chrome for Testing](https://sites.google.com/a/chromium.org/chromedriver/downloads) website.
    - Download the ChromeDriver version that matches your Chrome browser installation.
    - Place the ChromeDriver executable (`chromedriver`) in your project's root folder (or modify the `chrome_driver_path` variable in the script accordingly).

4. **Verify Chrome Version:**

    - Open your Chrome browser and type `chrome://version/` in the address bar.
    - Make sure the version of Chrome Driver matches the version of your Chrome browser.

## Usage

1. **Modify URL List (Optional):**

    Edit the `urls` array in the script to include the web pages you want to convert.

2. **Customize Cleaning (Optional):**

    The script includes example functions (`remove_elements_by_id`, `remove_elements_by_class`) to demonstrate how to remove specific elements from the page before generating the PDF. Modify or add your own functions to tailor the cleaning process.

3. **Run the Script:**

    ```bash
    python your_script_name.py
    ```

## Output

The generated PDFs will be saved in a folder named `generated_pdfs` in your project directory.

## Important Notes

- **Print Media Optimization:** This script works best with websites that are well-optimized for printing (using `@media print` CSS). If a website's print view isn't ideal, you'll need to customize the cleaning process to remove unwanted elements.
- **DOM Manipulation:** You can use Selenium's powerful DOM manipulation capabilities to interact with and modify the page content before generating the PDF. Refer to the Selenium documentation for more information.
- **Error Handling:** While the script includes basic error handling, it's recommended to add more robust error checks and logging for production use.
