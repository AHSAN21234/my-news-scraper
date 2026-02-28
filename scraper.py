import requests
from bs4 import BeautifulSoup
import datetime

# This function goes to a news site and gets headlines
def get_news():
    url = "https://news.ycombinator.com/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Get top 5 headlines
    headlines = soup.find_all('span', class_='titleline')[:5]
    
    # Save them to a file called results.txt
    with open("results.txt", "a") as f:
        f.write(f"\nUpdate: {datetime.datetime.now()}\n")
        for h in headlines:
            f.write(h.get_text() + "\n")

if __name__ == "__main__":
    get_news()
