# Automated Web Scraping & Reporting Pipeline

This project automates the process of scraping product data from an e-commerce website, cleaning and structuring the data, generating reports, and emailing them via Power Automate.

## 🚀 Features
- Web scraping with **Selenium** and **BeautifulSoup**
- Data cleaning and transformation using **Pandas**
- Report generation in **CSV** and **HTML** formats
- Automated email reporting using **Power Automate Desktop**

## 📁 Project Structure
```
.
├── scraper.py             # Scrapes product data from the website
├── data_cleaner.py        # Cleans and formats the scraped data
├── report_generator.py    # Generates CSV and HTML reports
├── run_all.py             # Runs all scripts sequentially
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── output/                # Contains raw and cleaned data, reports
```

## 🔧 Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/automated-scraping-reporting.git
cd automated-scraping-reporting
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Project
```bash
python run_all.py
```

## 📨 Automating Email Reports with Power Automate
Use **Power Automate Desktop** to:
1. Run `run_all.py` using the "Run Python Script" action
2. Use "Send Email via Outlook" action to send `output/report.csv` and `output/report.html`

## 📌 Notes
- Make sure you have **ChromeDriver** installed and it matches your Chrome version.
- Reports are saved in the `output/` folder.

## 📄 License
This project is open source under the MIT License.
