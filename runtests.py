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


#!/usr/bin/env python

import sys
import unittest
from os.path import dirname


def configure_settings():
    from django.conf import settings

    # If DJANGO_SETTINGS_MODULE envvar exists the settings will be
    # configured by it. Otherwise it will use the parameters bellow.
    if not settings.configured:
        params = dict(
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': ':memory:',
                }
            },
            SITE_ID=1,
            TEST_RUNNER='django.test.simple.DjangoTestSuiteRunner',
            TEST_ROOT=dirname(__file__),
        )

        # Configure Django's settings
        settings.configure(**params)

    return settings


def runtests():
    settings = configure_settings()
    testsuite = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=1).run(testsuite)


if __name__ == '__main__':
    runtests()
