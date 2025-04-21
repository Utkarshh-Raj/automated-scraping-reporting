from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd
import os

def scrape_data():
    url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    products = soup.select(".thumbnail")

    data = []
    for product in products:
        title = product.select_one(".title").get("title")
        price = product.select_one(".price").text.strip()
        description = product.select_one(".description").text.strip()
        availability = "In stock" if product.select_one(".ratings") else "Unknown"
        data.append({
            "Title": title,
            "Price": price,
            "Description": description,
            "Availability": availability
        })

    os.makedirs("output", exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv("output/raw_data.csv", index=False)
    return df

if __name__ == "__main__":
    scrape_data()