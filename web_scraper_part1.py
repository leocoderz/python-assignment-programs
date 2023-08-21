import requests
from bs4 import BeautifulSoup
import re

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

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all product containers on the page
    product_containers = soup.find_all('div', {'data-component-type': 's-search-result'})

    # Loop through each product container and extract the desired information
    for container in product_containers:
        product_url = container.find('a', class_='a-link-normal')['href']
        product_name = container.find('span', class_='a-text-normal').get_text()

        # Extract the price (handling cases with and without discounts)
        price_element = container.find('span', class_='a-offscreen')
        if price_element:
            product_price = price_element.get_text()
        else:
            product_price = container.find('span', class_='a-price').find('span', class_='a-offscreen').get_text()

        # Extract the rating
        rating_element = container.find('span', class_='a-icon-alt')
        if rating_element:
            product_rating = re.search(r'\d\.\d', rating_element.get_text()).group()
        else:
            product_rating = "N/A"

        # Extract the number of reviews
        num_reviews_element = container.find('span', {'aria-label': re.compile(r'\d+ customer reviews')})
        if num_reviews_element:
            num_reviews = re.search(r'\d+', num_reviews_element['aria-label']).group()
        else:
            num_reviews = "0"

        # Store the scraped data in a dictionary
        product_data = {
            'Product URL': 'https://www.amazon.in' + product_url,
            'Product Name': product_name,
            'Product Price': product_price,
            'Rating': product_rating,
            'Number of Reviews': num_reviews
        }

        # Append the dictionary to the list of scraped data
        scraped_data.append(product_data)

# Print the scraped data
for data in scraped_data:
    print(data)
