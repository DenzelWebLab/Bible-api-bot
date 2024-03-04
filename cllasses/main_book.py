import requests

from config import BIBLE_ID, BIBLE_KEY, BIBLE_URL


class BibleTree:
    def __init__(self):
        self.bible_id = BIBLE_ID
        self.url_books = BIBLE_URL

    def get_name(self):
        url = self.url_books + f'/v1/bibles/{BIBLE_ID}/books'
        response = requests.get(url=url, headers=BIBLE_KEY)
        data = response.json()
        content = data['data']
        name_list = []
        index_list = []
        for items in content:
            name = items.get('name')
            name_list.append(name)
            index = items.get('id')
            index_list.append(index)
        dict_content = dict(zip(name_list, index_list))
        clear = dict(list(dict_content.items())[:-1])
        return clear

    def get_book(self, book_id):
        url = self.url_books + f'/v1/bibles/{BIBLE_ID}/books/{book_id}/chapters'
        response = requests.get(url=url, headers=BIBLE_KEY)
        data = response.json()
        content = data['data']
        name_list = []
        id_list = []
        for items in content:
            name = items.get('reference')
            name_list.append(name)
            id_index = items.get('id')
            id_list.append(id_index)
        dict_content = dict(zip(name_list, id_list))
        return dict_content

    def get_chapters(self, chapters_id):
        url = self.url_books + f'/v1/bibles/{BIBLE_ID}/chapters/{chapters_id}/verses'
        response = requests.get(url=url, headers=BIBLE_KEY)
        data = response.json()
        content = data['data']
        name_list = []
        index_list = []
        for items in content:
            name = items.get('reference')
            name_list.append(name)
            index = items.get('id')
            index_list.append(index)
        dict_content = dict(zip(name_list, index_list))
        return dict_content

    def get_text_verses(self, verses):
        url = self.url_books + (f"/v1/bibles/{BIBLE_ID}/verses/{verses}?content-type=text&include-notes=false&include"
                                f"-titles=true&include-chapter-numbers=false&include-verse-numbers=true&include"
                                f"-verse-spans=false&use-org-id=false")
        response = requests.get(url=url, headers=BIBLE_KEY)
        data = response.json()
        list_text = []
        name = data['data']['reference']
        content = data['data']['content']
        list_text.append(content)
        full = ''.join(list_text).strip()
        return f'{name}\n{full}'

    def get_psalm(self):
        url = self.url_books + f'/v1/bibles/{BIBLE_ID}/books'
        response = requests.get(url=url, headers=BIBLE_KEY)
        data = response.json()
        content = data['data']
        list_name = []
        list_index = []
        for items in content:
            name = items.get('name')
            list_name.append(name)
            index = items.get('id')
            list_index.append(index)
        dict_content = dict(zip(list_name, list_index))
        clear = dict(list(dict_content.items())[-1:])
        return clear
