django-data-faker
=================

Fake-factory to generate test data for Django models.

This is a mix of:

* Python Faker - https://github.com/deepthawtz/faker
* Model Mommy - https://github.com/vandersonmota/model_mommy


Installation
------------

To install Django-data-faker you can use pip::

    pip install django-data-faker


Extra generators
----------------

**Url with username**

.. code-block:: python

    >>> from django_data_faker import get_url_with_username
    >>> get_url_with_username()
    'http://koeppledner.biz/curtis.lakin'


**Facebook url**

.. code-block:: python

    >>> from django_data_faker import gen_fb_url
    >>> gen_fb_url()
    'http://facebook.com/rchristiansen'


**Twitter url**

.. code-block:: python

    >>> from django_data_faker import gen_tw_url
    >>> gen_tw_url()
    'http://twitter.com/cummerata.norbert'

**LinkedIn url**

.. code-block:: python

    >>> from django_data_faker import gen_tw_url
    >>> gen_ln_url()
    'http://linkedin.com/pub/bweimann'


**Random file from directory**

.. code-block:: python

    # random avatar

    from django_data_faker import random_file_from_folder
    from myapp.models import UserProfile

    file_name, file_content = random_file_from_folder('/path/to/avatars/dir')
    user = UserProfile.objects.get(id=100)
    user.avatar.save(file_name, file_content)


**Generate image placeholder**

.. code-block:: python

    # generate avatar placeholder

    from django_data_faker import gen_placeholder_image
    from myapp.models import UserProfile

    file_name, file_content = gen_placeholder_image(400, 200)
    user = UserProfile.objects.get(id=100)
    user.avatar.save(file_name, file_content)

Example:

.. image:: http://i.imgur.com/wk8ZjIV.png?1
