import requests

from config import BIBLE_ID, BIBLE_KEY, BIBLE_URL


class IndexSearch:
    def __init__(self):
        self.bible_id = BIBLE_ID
        self.url = BIBLE_URL

    def get_index(self, index):
        url = self.url + (f'/v1/bibles/{BIBLE_ID}/verses/{index}?content-type=text&include-notes=false&include'
                          f'-titles=true&include-chapter-numbers=false&include-verse-numbers=true&include'
                          f'-verse-spans=false&use-org-id=false')
        response = requests.get(url=url, headers=BIBLE_KEY)
        data = response.json()
        content = data['data']['content']
        return content
