import scraper
import data_cleaner
import report_generator

def main():
    scraper.scrape_data()
    data_cleaner.clean_data()
    report_generator.generate_reports()

if __name__ == "__main__":
    main()