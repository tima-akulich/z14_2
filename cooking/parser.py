import requests
import re
from threading import Thread, Event


class VkusnoParser:
    base_url = 'http://vkusno.press'

    recipe_list = f'{base_url}/category/text/all/{{page}}'
    details_view = f'{base_url}/recipe/text/{{page_id}}'

    page_id_re = re.compile('\/recipe\/text\/(.+)"')

    page_title_re = re.compile('page-title">(.+)<')
    page_description_re = re.compile('text-left">(.+)<\/div')
    page_image_re = re.compile('<img src="(.+)" class="recipe-type-wrapper-img">')

    def make_request(self, url):
        response = requests.get(url)
        return response.text

    def get_page_ids_from_page(self, content):
        return self.page_id_re.findall(content)

    def get_list_page(self, page_number):
        return self.make_request(self.recipe_list.format(page=page_number))

    def get_details_page(self, page_id):
        return self.make_request(self.details_view.format(page_id=page_id))

    def get_recipe_list(self):
        page = 1
        all_ids = []
        page_ids = self.get_page_ids_from_page(self.get_list_page(page))

        while page_ids:
            print('Page', page)
            all_ids += page_ids
            page += 1
            page_ids = self.get_page_ids_from_page(self.get_list_page(page))
        return all_ids

    def parse_page(self, content):
        title = self.page_title_re.findall(content)
        # description = self.page_description_re.findall(content)
        image = self.page_image_re.findall(content)

        if title and image:
            return title[0], f'{self.base_url}{image[0]}'

    def parse_all_pages(self, page_ids):
        threads = []
        for page_id in page_ids[:10]:
            _tmp = lambda x: self.parse_page(self.get_details_page(x)) + (x,)
            threads.append(Thread(target=_tmp, args=(page_id,)))
        for _thread in threads:
            _thread.start()
        for _thread in threads:
            _thread.join()

    def parse(self):
        recipe_ids = self.get_recipe_list()
        data = self.parse_all_pages(recipe_ids)
        print('Done!')