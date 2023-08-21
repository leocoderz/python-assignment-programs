Python Internship Assignment

Amazon Product Web Scraping
These Python scripts demonstrate web scraping product information from the Amazon India website. The first script scrapes basic product details from search result pages, and the second script further scrapes additional details from individual product pages.

Requirements
Python 3.x
Required Python libraries: requests, beautifulsoup4
Install the required libraries using the following command:

bash
Copy code
pip install requests beautifulsoup4
Usage
Script 1 - Scraping Product Information

Open web_scraper_part1.py in a text editor or IDE.

Adjust the base_url and num_pages variables according to your needs.

Run the script using the following command:

bash
Copy code
python web_scraper_part1.py
The script will print the scraped product information to the console.

Script 2 - Scraping Additional Details

Open web_scraper_part2.py in a text editor or IDE.

Adjust the base_url and num_pages variables according to your needs.

Run the script using the following command:

bash
Copy code
python web_scraper_part2.py
The script will print the scraped product information to the console and export it to a CSV file named scraped_data.csv.

Notes
Web scraping involves making HTTP requests to websites. Always ensure that your web scraping activities comply with the website's terms of use and robots.txt file.
The scripts might need adjustments if the structure of the Amazon website changes.
The product details scraped may vary depending on changes to Amazon's website structure.
