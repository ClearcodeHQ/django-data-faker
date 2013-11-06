from django.test import TestCase

from django_data_faker import gen_placeholder_image


class ImageGenerator(TestCase):

    def test_image_generator(self):
        file_name, file_content = gen_placeholder_image(100, 100)
        self.assertTrue('.png' in file_name)
        self.assertTrue(file_content.size > 0)
