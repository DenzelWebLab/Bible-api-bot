import requests

from config import bible_id, bible_key


class BibleTree:
    def __init__(self):
        self.bible_id = bible_id
        self.url_books = 'https://api.scripture.api.bible'

    def get_name(self):
        url = self.url_books + f'/v1/bibles/{bible_id}/books'
        response = requests.get(url=url, headers=bible_key)
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
        url = self.url_books + f'/v1/bibles/{bible_id}/books/{book_id}/chapters'
        response = requests.get(url=url, headers=bible_key)
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
        url = self.url_books + f'/v1/bibles/{bible_id}/chapters/{chapters_id}/verses'
        response = requests.get(url=url, headers=bible_key)
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
        url = self.url_books + (f"/v1/bibles/{bible_id}/verses/{verses}?content-type=text&include-notes=false&include"
                                f"-titles=true&include-chapter-numbers=false&include-verse-numbers=true&include"
                                f"-verse-spans=false&use-org-id=false")
        response = requests.get(url=url, headers=bible_key)
        data = response.json()
        list_text = []
        content = data['data']['content']
        list_text.append(content)
        full = ' '.join(list_text)
        return full


# a = BibleTree()
# b = a.get_name()
# print(b)