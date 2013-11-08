# Copyright (C) 2013 by Clearcode <http://clearcode.cc>
# and associates (see AUTHORS).
#
# This file is part of django-data-faker.
#
# django-data-faker is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# django-data-faker is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with django-data-faker.  If not, see <http://www.gnu.org/licenses/>.

import os
import uuid
from StringIO import StringIO
from random import choice
from django import VERSION
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
    'last_name': fake.lastName,
    'username': fake.userName,
    'email': fake.email,
    'phone': fake.phoneNumber,
    'slug': lambda: None,
    'state': fake.state,
    'description': fake.text,
    'summary': fake.text,
}


# value generators
def url_with_username(url=None, username=None):
    return (url or fake.url()) + (username or fake.userName())


def facebook_url(username=None):
    return url_with_username('http://facebook.com/', username)


def twitter_url(username=None):
    return url_with_username('http://twitter.com/', username)


def linkedin_url(username=None):
    return url_with_username('http://linkedin.com/pub/', username)


def random_file_from_folder(abs_path):
    '''
        Random file from given folder as a Django's ContentFile object

        returns ContentFile object
    '''
    file_name = choice(os.listdir(abs_path))
    content = open(os.path.join(abs_path, file_name), 'r').read()
    if VERSION < (1, 4):
        return ContentFile(content)
    file_name = choice(os.listdir(abs_path))
    return ContentFile(content, name=file_name)


def random_html_color():
    ''' Random color in HTML notation '''

    return choice([
        '#7289A6', '#485922', '#A67721', '#D99C2B', '#A64029', '#011640',
        '#123273', '#1F628C', '#718C0F', '#88A61B', '#69374D', '#232326',
        '#FF3F94', '#FF483F', '#F89E00', '#9F9F9F', '#7FCD74', '#AE74CD',
    ])


def placeholder_image(width, height, background_color=None,
                      font_color='#FFFFFF', base_font_size=40, text_margin=20,
                      font_path=None, image_format='png'):
    '''
        Generate image placeholder with text (eg. 200x300)
        as a Django's ContentFile object

        returns ContentFile object
    '''

    if background_color is None:
        background_color = random_html_color()

    if font_path is None:
        dir = os.path.abspath(os.path.dirname(__file__))
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
    im.save(tmp_content, format=image_format)

    if VERSION < (1, 4):
        return ContentFile(tmp_content.getvalue())
    file_name = uuid.uuid4().__str__() + '.%s' % image_format
    return ContentFile(tmp_content.getvalue(), name=file_name)
