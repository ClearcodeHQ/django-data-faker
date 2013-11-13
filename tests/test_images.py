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

from django.test import TestCase

from django_data_faker import fake


class ImageGenerator(TestCase):

    def test_url_with_username(self):
        username = fake.user_name()
        url = fake.url_with_username(username=username)
        self.assertTrue(username in url)

    def test_facebook_url(self):
        username = fake.user_name()
        url = fake.facebook_url(username=username)
        self.assertTrue(username in url)
        self.assertTrue('facebook.com' in url)

    def test_twitter_url(self):
        username = fake.user_name()
        url = fake.twitter_url(username=username)
        self.assertTrue(username in url)
        self.assertTrue('twitter.com' in url)

    def test_linkedin_url(self):
        username = fake.user_name()
        url = fake.linkedin_url(username=username)
        self.assertTrue(username in url)
        self.assertTrue('linkedin.com' in url)

    def test_random_html_color(self):
        color = fake.random_html_color()
        self.assertTrue('#' in color)
        self.assertTrue(len(color) == 7)

    def test_image_generator(self):
        content_file = fake.placeholder_image(100, 100)
        self.assertTrue('.png' in content_file.name)
        self.assertTrue(content_file.size > 0)
