import random

import requests

from config import BIBLE_ID, BIBLE_KEY, BIBLE_URL


class BibleApi:
    def __init__(self,
                 book_id: str = None,
                 chapter_id: str = None,
                 verses: str = None,
                 index: str = None,
                 query: str = None
                 ) -> None:
        self.name_book = BIBLE_URL + f'/v1/bibles/{BIBLE_ID}/books'
        self.book = BIBLE_URL + f'/v1/bibles/{BIBLE_ID}/books/{book_id}/chapters'
        self.chapter = BIBLE_URL + f'/v1/bibles/{BIBLE_ID}/chapters/{chapter_id}/verses'
        self.verse = BIBLE_URL + (f"/v1/bibles/{BIBLE_ID}/verses/{verses}?content-type=text&include-notes=false&include"
                                  f"-titles=true&include-chapter-numbers=false&include-verse-numbers=true&include"
                                  f"-verse-spans=false&use-org-id=false")
        self.index = BIBLE_URL + (f'/v1/bibles/{BIBLE_ID}/verses/{index}?content-type=text&include-notes=false&include'
                                  f'-titles=true&include-chapter-numbers=false&include-verse-numbers=true&include'
                                  f'-verse-spans=false&use-org-id=false')
        self.query = BIBLE_URL + f'/v1/bibles/{BIBLE_ID}/search?query={query}&sort=relevance'

    def get_book_name(self) -> dict:
        response = requests.get(self.name_book, headers=BIBLE_KEY)
        data = response.json()
        data_books = data['data']
        data_dict = {item['name']: item['id'] for item in data_books}
        data_name_book = dict(list(data_dict.items())[:-1])
        return data_name_book

    def get_book(self) -> dict:
        response = requests.get(self.book, headers=BIBLE_KEY)
        data = response.json()
        data_book = data['data']
        data_dict = {item['reference']: item['id'] for item in data_book}
        return data_dict

    def get_chapter(self) -> dict:
        response = requests.get(self.chapter, headers=BIBLE_KEY)
        data = response.json()
        data_chapter = data['data']
        data_dict = {item['reference']: item['id'] for item in data_chapter}
        return data_dict

    def get_verse(self):
        response = requests.get(self.verse, headers=BIBLE_KEY)
        data = response.json()
        data_txt = []
        name_verses = data['data']['reference']
        data_verses = data['data']['content']
        data_txt.append(data_verses)
        txt = ' '.join(data_txt).strip()
        return f'{name_verses}\n{txt.upper()}'

    def get_index_data(self):
        response = requests.get(self.index, headers=BIBLE_KEY)
        data = response.json()
        index: str = data['data']['reference']
        data_txt: str = data['data']['content']
        return f'{index}\n\n{data_txt.upper()}'

    def get_query_data(self):
        response = requests.get(self.query, headers=BIBLE_KEY)
        data = response.json()
        data_query = data['data']['verses']
        data_dict = {item['reference']: item['text'] for item in data_query}
        key, value = random.choice(list(data_dict.items()))
        return f'{key}\n{value}'

    def get_list_index(self):
        pass





# a = BibleApi()
# b = a.get_book_name()['Матвія']
# print(b)



