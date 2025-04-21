# Automated Web Scraping and Reporting Project

## Overview
This project scrapes data from a sample e-commerce site, cleans it, and generates reports in CSV and HTML formats.

## Components
- scraper.py: Scrapes the data using Selenium and BeautifulSoup.
- data_cleaner.py: Cleans and prepares the data using Pandas.
- report_generator.py: Creates final reports.
- run_all.py: Runs all steps together.

## Power Automate Integration
Use Power Automate Desktop to:
1. Run these 3 Python scripts in sequence.
2. Email the output/report.csv and output/report.html using the "Send Email via Outlook" action.

## Setup Instructions
1. Install Chrome and ChromeDriver.
2. Install Python packages:
   pip install -r requirements.txt
3. Run:
   python run_all.py