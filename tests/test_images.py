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

from django_data_faker import placeholder_image


class ImageGenerator(TestCase):

    def test_image_generator(self):
        file_name, file_content = placeholder_image(100, 100)
        self.assertTrue('.png' in file_name)
        self.assertTrue(file_content.size > 0)
