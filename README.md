# Apple Trademark Scraper

This Python script extracts all trademarks and service marks listed on Apple's [Trademark List page](https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html). The data is saved into a CSV file in the user's **Documents** folder, including the trademark name and its associated generic term.

## Features

- Extracts all trademarks and service marks from Apple's trademark list page.
- Saves data in a CSV file with the following columns:
  - `Trademark Type` (`Trademark` or `Service Mark`)
  - `Trademark Name`
  - `Generic Term`
- Automatically saves the output file in the **Documents** folder of the user.

## Prerequisites

Ensure the following Python libraries are installed:

- `selenium`
- `beautifulsoup4`

You will also need a compatible WebDriver for Selenium. For example, download [ChromeDriver](https://chromedriver.chromium.org/) if using Google Chrome.

## Installation

1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/your-username/apple-trademark-scraper.git
   cd apple-trademark-scraper

2.	Install the required Python libraries:

  '''pip install selenium beautifulsoup4'''

## Usage

1.	Run the script:
 '''python fetch_apple_trademarks.py'''

## Important Notes

- The trademarks and service marks are the property of Apple Inc..
- This script does not modify or infringe upon any intellectual property rights. It only provides publicly available information in a structured format for easier analysis.

  This script does not modify or infringe upon any intellectual property rights. It only provides publicly available information in a structured format for easier analysis.

If you plan to use the extracted data for commercial or legal purposes, ensure you comply with Apple’s Terms of Use. https://www.apple.com/legal/internet-services/terms/site.html
