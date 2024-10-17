from bs4 import BeautifulSoup
import requests, json

url = 'https://streak-stats.demolab.com/?user='
username = str(input('Escribe tu username: '))
response = requests.get(f'{url}{username}')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    streak = soup.find_all('text')

    data = {
    "streaks": [
            {
                "header": streak[4].text.strip(),
                "text": [
                    streak[3].text.strip(),
                    streak[5].text.strip()
                ]
            },
            {
                "header": streak[1].text.strip(),
                "text": [
                    streak[0].text.strip(),
                    streak[2].text.strip()
                ]
            },
            {
                "header": streak[7].text.strip(),
                "text": [
                    streak[6].text.strip(),
                    streak[8].text.strip()
                ]
            }
        ]
    }

    json_output = json.dumps(data, indent=1)
    print(json_output)

else:
    print('Error 404')