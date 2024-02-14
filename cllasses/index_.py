import requests

from config import bible_id, bible_key


class IndexSearch:
    def __init__(self):
        self.bible_id = bible_id
        self.url = 'https://api.scripture.api.bible'

    def get_index(self, index):
        url = self.url + (f'/v1/bibles/{bible_id}/verses/{index}?content-type=text&include-notes=false&include'
                          f'-titles=true&include-chapter-numbers=false&include-verse-numbers=true&include'
                          f'-verse-spans=false&use-org-id=false')
        response = requests.get(url=url, headers=bible_key)
        data = response.json()
        content = data['data']['content']
        return content
