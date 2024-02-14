import requests

from config import bible_key, bible_id


class SearchQuery:
    def __init__(self):
        self.bible_id = bible_id
        self.url = 'https://api.scripture.api.bible'

    def get_data(self, query):
        url = self.url + f'/v1/bibles/{self.bible_id}/search?query={query}&sort=relevance'
        response = requests.get(url, headers=bible_key)
        data = response.json()
        content = data['data']['verses']
        d = []
        for item in content:
            book = item.get('text')
            d.append(book)
        text = '\n'.join(d)
        return text

    @staticmethod
    def get_right():
        url = (f'https://api.scripture.api.bible/v1/bibles/{bible_id}/verses/MAT.1.3?content-type=json&include'
               f'-notes=false&include-titles=true&include-chapter-numbers=false&include-verse-numbers=true&include'
               f'-verse-spans=false&use-org-id=false')
        response = requests.get(url, headers=bible_key)
        data = response.json()
        content = data['data']['copyright']
        return content


