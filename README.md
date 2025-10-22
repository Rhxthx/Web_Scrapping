"# Web_Scrapping" 
🛒 Amazon Product Scraper

A Python script to scrape product details from Amazon (Title, Price, Rating, Reviews, Availability) and save them to out.csv.

🚀 Features

1. Extracts Title, Price, Rating, Reviews, Availability

2. Handles multiple Amazon price formats

3. Adds CSV headers automatically

4. Includes delay to prevent blocking

⚙️ Setup

1. Install dependencies: pip install requests beautifulsoup4 lxml

2. Add product URLs to amazon.txt (one per line).

3. Run the scraper: python amazon_scraper.py

📄 Output Example
Title,Price,Rating,Total Reviews,Availability
Tata Sampann Raisins,₹210,4.3,4030 ratings,In stock

⚠️ Note
Use responsibly — scraping Amazon too frequently may trigger blocking.
