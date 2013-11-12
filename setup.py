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

from setuptools import setup

setup(
    name='django-data-faker',
    version='0.0.1.5',
    description='Fake-factory to generate test data for Django models via model_mommy recipes.',
    author='Clearcode - The A Room',
    author_email='thearoom@clearcode.cc',
    url='https://github.com/ClearcodeHQ/django-data-faker',
    license='Lesser GPL',
    packages=['django_data_faker'],
    install_requires=[
        'Pillow>=2.2.1',
        'Django>=1.1',
        'model-mommy==1.2',
        'fake-factory==0.3.2',
    ],
    include_package_data=True,
    keywords='django testing factory python',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Widget Sets',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Framework :: Django'
    ],
)
