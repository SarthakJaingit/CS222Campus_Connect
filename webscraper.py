import requests
from bs4 import BeautifulSoup

url = 'https://www.examplecommunity.com/clubs'

try:
    
    response = requests.get(url)
    response.raise_for_status()  
    soup = BeautifulSoup(response.text, 'html.parser')
    club_list = soup.find('div', class_='club-list')
    club_cards = club_list.find_all('div', class_='club-card')
    for card in club_cards:
        name = card.find('h3', class_='club-name').text
        description = card.find('p', class_='club-description').text
        meeting_times = card.find('span', class_='meeting-times').text
        print(f'Club Name: {name}\nDescription: {description}\nMeeting Times: {meeting_times}\n')
except requests.HTTPError as e:
    print(f'HTTP Error: {e}')
except Exception as e:
    print(f'An error occurred: {e}')