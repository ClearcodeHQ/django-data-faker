from django.test import TestCase

from django_data_faker import placeholder_image


class ImageGenerator(TestCase):

    def test_image_generator(self):
        file_name, file_content = placeholder_image(100, 100)
        self.assertTrue('.png' in file_name)
        self.assertTrue(file_content.size > 0)
