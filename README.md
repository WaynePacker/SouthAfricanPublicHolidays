## South African Public Holidays
A simple application to scrape the public holiday names and dates for South Africa.

Dates are scraped from `https://www.gov.za/about-sa/public-holidays` which is the official public documentation for public holidays.

## Installing dependencies

Run the following commands to install dependencies

```
python -m venv venv

./venv/Scripts/active

pip install -r requirements.txt
```

## Running the application
```
python main.py
```

### Dependencies
```
- beautifulsoup4==4.13.3
- requests==2.32.3
```