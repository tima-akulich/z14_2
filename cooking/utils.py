import base64


def convert_image_to_base64(image):
    return 'data:{content_type};base64,{data}'.format(
        content_type=image.content_type,
        data=base64.b64encode(image.file.read()).decode()
    )
