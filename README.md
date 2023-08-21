#Python Internship Assignment

# Amazon Product Web Scraping

These Python scripts demonstrate how to perform web scraping to gather product information from the Amazon India website. The first script scrapes basic product details from search result pages, and the second script further scrapes additional details from individual product pages.

## Prerequisites

- Python 3.x
- Required Python libraries: `requests`, `beautifulsoup4`

You can install the required libraries using the following command:

```bash
pip install requests beautifulsoup4
```

#Usage
#Script 1 - Scraping Product Information

Open web_scraper_part1.py in a text editor or IDE.

Adjust the base_url and num_pages variables according to your requirements.

Run the script using the following command:
```bash
python web_scraper_part1.py
```
The script will print the scraped product information to the console.

#Script 2 - Scraping Additional Details

Open web_scraper_part2.py in a text editor or IDE.

Adjust the base_url and num_pages variables according to your requirements.

Run the script using the following command:

```bash
python web_scraper_part2.py
```
The script will print the scraped product information to the console and export it to a CSV file named scraped_data.csv.
