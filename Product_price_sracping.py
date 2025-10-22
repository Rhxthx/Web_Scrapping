# importing libraries
from bs4 import BeautifulSoup
import requests
import csv
import os
import time

def main(URL):
    # specify CSV file name
    filename = "out.csv"

    # check if file exists; if not, write headers
    file_exists = os.path.isfile(filename)

    # open file in append mode
    with open(filename, "a", newline='', encoding="utf-8") as File:
        writer = csv.writer(File)

        # write header row only once
        if not file_exists:
            writer.writerow(["Title", "Price", "Rating", "Total Reviews", "Availability"])

        # specify user agent
        HEADERS = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.5'
        }

        # request the webpage
        webpage = requests.get(URL.strip(), headers=HEADERS)
        soup = BeautifulSoup(webpage.content, "lxml")

        # ---------------- PRODUCT TITLE ----------------
        try:
            title = soup.find("span", attrs={"id": "productTitle"})
            title_string = title.get_text(strip=True).replace(",", "")
        except AttributeError:
            title_string = "NA"

        # ---------------- PRODUCT PRICE ----------------
        try:
            price = None
            price_ids = ["priceblock_ourprice", "priceblock_dealprice", "priceblock_saleprice"]
            for pid in price_ids:
                price_tag = soup.find("span", attrs={"id": pid})
                if price_tag:
                    price = price_tag.get_text(strip=True)
                    break

            # if not found, try "a-price" class
            if not price:
                price_span = soup.find("span", class_="a-price")
                if price_span and price_span.find("span", class_="a-offscreen"):
                    price = price_span.find("span", class_="a-offscreen").get_text(strip=True)

            price = price.replace(",", "") if price else "NA"
        except Exception:
            price = "NA"

        # ---------------- PRODUCT RATING ----------------
        try:
            rating_tag = soup.find("span", class_="a-icon-alt")
            rating = rating_tag.get_text(strip=True).split(" ")[0] if rating_tag else "NA"
        except Exception:
            rating = "NA"

        # ---------------- TOTAL REVIEWS ----------------
        try:
            review_tag = soup.find("span", attrs={"id": "acrCustomerReviewText"})
            review_count = review_tag.get_text(strip=True).replace(",", "") if review_tag else "NA"
        except AttributeError:
            review_count = "NA"

        # ---------------- AVAILABILITY ----------------
        try:
            availability = soup.find("div", attrs={"id": "availability"})
            availability = availability.get_text(strip=True) if availability else "NA"
        except AttributeError:
            availability = "NA"

        # print to console
        print(f"\nProduct Title = {title_string}")
        print(f"Product Price = {price}")
        print(f"Overall Rating = {rating}")
        print(f"Total Reviews = {review_count}")
        print(f"Availability = {availability}")

        # write data to CSV
        writer.writerow([title_string, price, rating, review_count, availability])


if __name__ == "__main__":
    with open("amazon.txt", "r", encoding="utf-8") as file:
        for link in file.readlines():
            main(link)
            time.sleep(2)  # avoid being blocked by Amazon
