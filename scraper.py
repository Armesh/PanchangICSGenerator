import requests
from bs4 import BeautifulSoup

# Function to fetch panchang data

def fetch_panchang_data(date):
    url = f'https://example.com/panchang/{date}'  # Replace with the actual URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the required data (modify selectors as necessary)
    panchang_data = {
        'tithi': soup.find('div', class_='tithi').text,
        'nakshatra': soup.find('div', class_='nakshatra').text,
        'yoga': soup.find('div', class_='yoga').text,
        'karana': soup.find('div', class_='karana').text,
    }
    return panchang_data

# Example usage
if __name__ == '__main__':
    date = '2026-02-09'  # Example date
    data = fetch_panchang_data(date)
    print(data)