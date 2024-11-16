import os
import csv
import time
from selenium import webdriver
from bs4 import BeautifulSoup

def fetch_apple_trademarks():
    # URL of Apple's trademark list
    url = 'https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html'

    # Configure Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Headless mode to avoid opening a browser window
    driver = webdriver.Chrome(options=options)

    try:
        # Load the page
        driver.get(url)
        time.sleep(5)  # Wait for JavaScript rendering to complete

        # Get the page's HTML content
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        # Find the tables containing the trademarks
        tables = soup.find_all('tbody')

        if len(tables) < 2:
            print("Error: Expected tables not found on the page.")
            return

        # Extract data from the tables
        trademarks_data = extract_table_data(tables[0])
        servicemarks_data = extract_table_data(tables[1])

        # Determine the file path in the Documents folder
        save_path = get_documents_path("Apple_Trademarks.csv")

        # Save the data to a CSV file
        save_to_csv(save_path, trademarks_data, servicemarks_data)

        print(f"Data successfully saved to '{save_path}'.")

    except Exception as e:
        print(f"Error fetching data: {e}")
    finally:
        driver.quit()

def extract_table_data(table):
    """Extracts data from a table."""
    rows = table.find_all('tr')[1:]  # Skip the header row
    data = []

    for row in rows:
        cols = row.find_all('td')
        if len(cols) < 2:  # Ensure there are at least two columns
            continue
        trademark = cols[0].text.strip()
        generic_term = cols[1].text.strip()
        data.append((trademark, generic_term))

    return data

def save_to_csv(filepath, trademarks, servicemarks):
    """Saves trademark data to a CSV file."""
    with open(filepath, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["Trademark Type", "Trademark Name", "Generic Term"])

        # Write trademark data
        for trademark, generic_term in trademarks:
            writer.writerow(["Trademark", trademark, generic_term])

        # Write servicemark data
        for servicemark, generic_term in servicemarks:
            writer.writerow(["Service Mark", servicemark, generic_term])

def get_documents_path(filename):
    """Constructs the path to the user's Documents folder."""
    home_dir = os.path.expanduser("~")
    documents_dir = os.path.join(home_dir, "Documents")
    return os.path.join(documents_dir, filename)

if __name__ == "__main__":
    fetch_apple_trademarks()
