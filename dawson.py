from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
from bs4 import BeautifulSoup

links = [
    'anthropology/faculty-staff-list/',
    'music/faculty-staff-list/',
    'electronics-engineering-technology/faculty-staff-list/',
    'economics/faculty-staff-list/',
    'political-science/faculty-staff-list/',
    'geography/faculty-staff-list/',
    'industrial-design/faculty-staff-list/',
    'religion/faculty-staff-list/',
    '3d/faculty-staff-list/',
    'diagnostic-imaging-technology/faculty-staff-list/',
    'mechanical-engineering-technology/faculty-staff-list/',
    'community-recreation-leadership-training-crlt/faculty-staff-list/',
    'accounting-and-management-technology/faculty-staff-list/',
    'psychology/faculty-staff-list/',
    'physics/faculty-staff-list/',
    'medical-ultrasound-technology/contact/',
    'radiation-oncology/faculty-staff-list/',
    'illustration/faculty-staff-list/',
    'professional-photography/faculty-staff-list/',
    'humanities/faculty-list/',
    'interior-design/faculty-staff-list/',
    'civil-engineering-technology/faculty-staff-list/',
    'sociology/faculty-staff-list/',
    'philosophy/faculty-staff-list/',
    'french/faculty-list/',
    'computer-science-technology/faculty-staff-list/',
    'mathematics/faculty-staff-list/',
    'modern-languages/faculty-staff-list/',
    'social-service/faculty-list/',
    'biology/faculty-staff-list/',
    'visual-arts/faculty-staff-list/',
    'graphic-design/faculty-staff-list/',
    'physical-education/faculty-list/',
    'nursing/faculty-staff-list/',
    'professional-theatre/faculty-staff-list/',
    'cinema-communications/faculty-staff-list/',
    'marketing-management-technology/faculty-staff-list/',
    'english/faculty-list/',
    'biomedical-laboratory-technology/faculty-staff-list/',
    'history/faculty-staff-list/',
    'physiotherapy-technology/faculty-staff-list/'
]

# Write headers
with open('data/dawson.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'E-Mail', 'Department', 'Office', 'Local'])

# Instantiate driver
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for link in links:
    department = link.split('/')[0]
    department = ' '.join(word.capitalize() for word in department.split('-'))
    driver.get(f'https://www.dawsoncollege.qc.ca/{link}')
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')


    # Find the table element with the specified class
    table = soup.find('table', class_='top-label-table')

    rows = []
    for row in table.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) == 4:
            rows.append(row)

    with open('data/dawson.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in rows:
            cells = row.find_all('td')
            row_data = [cell.text.strip() for i, cell in enumerate(cells)]
            row_data.insert(2, department)
            writer.writerow(row_data)

driver.quit()

