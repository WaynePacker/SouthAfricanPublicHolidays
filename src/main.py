from scraper import scrape

try:
    holidays = scrape()
    print(holidays)
except Exception as e:
    print("Failed to fetch holidays", e)


