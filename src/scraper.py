import requests
import settings
import re
from bs4 import BeautifulSoup, PageElement

def scrape():
    holidays = {}
    response = requests.get(settings.SCRAPE_URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        headers = soup.find(
            'div', class_='node-content').find('div').find_all('h2', limit=2) # Limit to 2, as currently there is only 2 years data available
        
        for header in headers:
            year = header.text
            holidays[year] = []
            current = header.next_sibling

            loop_count = settings.LOOP_SAFE_AMOUNT
            while loop_count >= 0:

                if current.name == 'h2':
                    break

                if current.name == 'p':
                    for content in current.contents:
                        starts_with_digit = re.search('^[\\d]', content.text)
                        if starts_with_digit:
                            date, description = content.text.split(':')
                            date = f'{date.strip()} {year}' 
                            description = description.replace('Public holiday', '').strip()
                            holidays[year] += [{ 'description': description, 'date': date }]

  
                loop_count = loop_count - 1
                current = current.next_sibling
            
        return holidays

    else:
        return "Failed to retrieve the web page"
