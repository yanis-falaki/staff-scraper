from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import csv
from bs4 import BeautifulSoup
import string

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
service = Service(executable_path="/Users/yanisfalaki/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(options=chrome_options, service=service)

for letter in string.ascii_uppercase:
    driver.get(f'https://www.vaniercollege.qc.ca/staff-directory/?index={letter}')

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'html.parser')
    table = soup.find('table', class_="directoryTable")

    try: rows = table.find_all('tr')
    except: continue

    if letter == 'A':
        mode = 'w'  # Overwrite the file for letter 'A'
    else:
        mode = 'a'  # Append to the file for other letters

    with open('data/vanier.csv', mode, newline='') as csvfile:
        writer = csv.writer(csvfile)

        if mode == 'w':
            # Write the header row only for letter 'A'
            header_row = rows[0]
            headers = [cell.text.strip() for cell in header_row.find_all('th')]
            writer.writerow(headers)

        # Iterate over the data rows and append '@vaniercollege.qc.ca' to the second cell
        for row in rows[1:]:
            cells = row.find_all('td')
            row_data = [cell.text.strip() + '@vaniercollege.qc.ca' if i == 1 else cell.text.strip() for i, cell in enumerate(cells)]
            writer.writerow(row_data)



# Close the browser
driver.quit()