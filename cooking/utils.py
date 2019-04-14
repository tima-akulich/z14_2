import base64
import re
import requests

from cooking.models import Recipe


def convert_image_to_base64(image):
    return 'data:{content_type};base64,{data}'.format(
        content_type=image.content_type,
        data=base64.b64encode(image.file.read()).decode()
    )


def parsing_site():
    reg = re.compile(r'(?<=<a href=\"/recipe/text/).+(?=\")')
    k = 1
    parsing = []
    while True:
        response = requests.get(f'http://vkusno.press/category/text/all/{k}')
        k += 1
        pars_reg = reg.findall(response.text)
        if not pars_reg:
            break
        parsing.append(set(pars_reg))

    title_reg = re.compile(r'(?<=<div class=\"recipe-type-page-title\">).+(?=</div>)')
    text_reg = re.compile(r'(?<=<div class=\"recipe-type-wrapper-block-text-desc\"> <p></p><p>).+(?=</p> <p>)')

    for i in parsing:
        for j in i:
            response = requests.get(f'http://vkusno.press/recipe/text/{j}')
            img_reg = re.compile(rf'(?<=<img src=\")/content/text/{j}.+(?=\" )')
            parsing_title = title_reg.findall(response.text)
            parsing_text = text_reg.findall(response.text)
            parsing_img = img_reg.findall(response.text)

            if Recipe.objects.filter(title=parsing_title[0], text=parsing_text[0] if parsing_text else ''):
                continue

            img_reg = re.compile(rf'(?<={j}/).+')
            parsing_img_reg = img_reg.findall(parsing_img[0])
            save_img(parsing_img, parsing_img_reg)

            create_recipe(parsing_title, parsing_text, parsing_img_reg)


def save_img(parsing_img, parsing_img_reg):
    response = requests.get(f'http://vkusno.press/{parsing_img[0]}')
    with open(f'media/{parsing_img_reg[0]}', 'wb') as img:
        img.write(response.content)


def create_recipe(parsing_title, parsing_text, parsing_img_reg):
    Recipe.objects.create(
        title=parsing_title[0],
        text=parsing_text[0] if parsing_text else '',
        image=f'{parsing_img_reg[0]}'
    )
