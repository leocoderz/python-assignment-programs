import requests
from bs4 import BeautifulSoup
import re
import csv


# Function to scrape additional product details from the product page
def scrape_product_details(product_url):
    response = requests.get(product_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    asin_element = soup.find('th', string='ASIN')
    asin = asin_element.find_next('td').get_text() if asin_element else "N/A"

    product_description_element = soup.find('div', id='productDescription')
    product_description = product_description_element.get_text() if product_description_element else "N/A"

    manufacturer_element = soup.find('th', string='Manufacturer')
    manufacturer = manufacturer_element.find_next('td').get_text() if manufacturer_element else "N/A"

    return asin, product_description, manufacturer


# Base URL of the Amazon product listing
base_url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_"

# Number of pages to scrape
num_pages = 20

# Initialize an empty list to store the scraped data
scraped_data = []

# Loop through each page
for page_number in range(1, num_pages + 1):
    # Construct the URL for the current page
    url = base_url + str(page_number)

    # Send an HTTP GET request to the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all product containers on the page
    product_containers = soup.find_all('div', {'data-component-type': 's-search-result'})

    # Loop through each product container and extract the desired information
    for container in product_containers:
        product_url = 'https://www.amazon.in' + container.find('a', class_='a-link-normal')['href']
        product_name = container.find('span', class_='a-text-normal').get_text()
        product_price = container.find('span', class_='a-price').find('span', class_='a-offscreen').get_text()
        product_rating = re.search(r'\d\.\d', container.find('span', class_='a-icon-alt').get_text()).group()

        num_reviews_element = container.find('span', {'aria-label': re.compile(r'\d+ customer reviews')})
        num_reviews = num_reviews_element.get_text().split()[0] if num_reviews_element else "0"

        # Scrape additional product details using the function
        asin, product_description, manufacturer = scrape_product_details(product_url)

        # Store the scraped data in a dictionary
        product_data = {
            'Product URL': product_url,
            'Product Name': product_name,
            'Product Price': product_price,
            'Rating': product_rating,
            'Number of Reviews': num_reviews,
            'ASIN': asin,
            'Product Description': product_description,
            'Manufacturer': manufacturer
        }

        # Append the dictionary to the list of scraped data
        scraped_data.append(product_data)

# Export the scraped data to a CSV file
csv_filename = 'scraped_data.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Product URL', 'Product Name', 'Product Price', 'Rating', 'Number of Reviews', 'ASIN',
                  'Product Description', 'Manufacturer']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for data in scraped_data:
        writer.writerow(data)

print(f"Data has been exported to {csv_filename}")
