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
