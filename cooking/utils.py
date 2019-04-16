import base64

import re
import requests

from cooking.models import Recipe


def convert_image_to_base64(image):
    return 'data:{content_type};base64,{data}'.format(
        content_type=image.content_type,
        data=base64.b64encode(image.file.read()).decode()
    )


def get_recipe(href):
    recipe_response = requests.get(href).text
    title_r = re.compile(
        r'\<div class=\"recipe\-type\-page\-title\"\>([\w\s]+)\<\/div\>'
    )
    title = title_r.findall(recipe_response)

    text_r = re.compile(
        r'\<div class=\"recipe\-type\-wrapper\-block\-text\-desc\"\>(\s*)'
        r'\<p\>(\s*)\<\/p\>(\s*)\<p\>(.*)(\s*)\<\/p\>(\s*)\<p\>(\s*)\<\/p\>'
        r'(\s*)\<\/div\>'
    )

    result = text_r.findall(recipe_response)
    raw_text = result[0][3] if result else ''
    text = re.sub(r'\<(\/*)(\w+)\>', '', raw_text)
    if title and text:
        return title[0], text
    return None, None


def parse_recipes():
    response = requests.get('http://vkusno.press/category/text/all/')
    r = re.compile(r'\<a href=\"(\/recipe\/text\/(\w+)\/(\w+))\"\>')
    result = r.findall(response.text)
    for href in result:
        title, text = get_recipe(''.join(('http://vkusno.press', href[0])))
        if not Recipe.objects.filter(
                title=title
        ).all() and title and text:
            Recipe.objects.create(title=title, text=text)



