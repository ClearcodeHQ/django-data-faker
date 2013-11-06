import os
import uuid
from StringIO import StringIO
from random import choice
from PIL import Image, ImageDraw, ImageFont

from model_mommy import mommy
from faker import Factory

from django.core.files.base import ContentFile
from django.db.models import (
    CharField, EmailField, SlugField, TextField, URLField
)


fake = Factory.create()

# Set those mappings according to project needs:

# Value generators based on field type
mommy.default_mapping.update({
    CharField: fake.sentence,
    TextField: fake.text,
    SlugField: lambda: None,
    URLField: fake.url,
    EmailField: fake.email,
})

# Value generators based on field name
mommy.Mommy.attr_mapping = {
    'first_name': fake.firstName,
    'firstname': fake.firstName,
    'last_name': fake.lastName,
    'lastname': fake.lastName,
    'username': fake.userName,
    'login': fake.userName,
    'nickname': fake.userName,
    'name': fake.userName,
    'email': fake.email,
    'email_address': fake.email,
    'phone': fake.phoneNumber,
    'phone_number': fake.phoneNumber,
    'phonenumber': fake.phoneNumber,
    'slug': lambda: None,
    'address': fake.address,
    'city': fake.city,
    'zipcode': fake.postcode,
    'state': fake.state,
    'country': fake.country,
    'title': fake.sentence,
    'description': fake.text,
    'summary': fake.text,
    'domain': fake.url,
}


# value generators
def get_url_with_username(url=None, username=None):
    return (url or fake.url()) + (username or fake.userName())


def gen_fb_url(username=None):
    return get_url_with_username('http://facebook.com/', username)


def gen_tw_url(username=None):
    return get_url_with_username('http://twitter.com/', username)


def gen_ln_url(username=None):
    return get_url_with_username('http://linkedin.com/pub/', username)


def random_file_from_folder(abs_path):
    file_name = choice(os.listdir(abs_path))
    content = ContentFile(open(os.path.join(abs_path, file_name), 'r').read())
    return file_name, content


def gen_placeholder_image(width, height, background_color=None,
                          font_color='#FFFFFF'):
    ''' Generate image placeholder with text eg. 200x300 '''

    if background_color is None:
        background_color = choice([
            '#7289A6', '#485922', '#A67721', '#D99C2B', '#A64029', '#011640',
            '#123273', '#1F628C', '#718C0F', '#88A61B', '#69374D', '#232326',
            '#FF3F94', '#FF483F', '#F89E00', '#9F9F9F', '#7FCD74', '#AE74CD',
        ])

    base_font_size = 40
    text_margin = 20
    dir = os.path.dirname(__file__)
    font_path = os.path.join(dir, 'TTF', 'DejaVuSans.ttf')
    msg = '%sx%s' % (width, height)

    im = Image.new('RGBA', (width, height), background_color)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(font_path, base_font_size)
    w, h = draw.textsize(msg, font=font)

    # adjust the text size to the size of the image
    while w > width - text_margin or h > height - text_margin:
        base_font_size -= 2
        font = ImageFont.truetype(font_path, base_font_size)
        w, h = draw.textsize(msg, font=font)

    draw.text(
        ((width - w) / 2, (height - h) / 2), msg, fill=font_color, font=font
    )

    tmp_content = StringIO()
    im.save(tmp_content, format='png')
    content = ContentFile(tmp_content)
    file_name = uuid.uuid4().__str__() + '.png'

    return file_name, content
