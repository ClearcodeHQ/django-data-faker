django-data-faker
=================

Fake-factory to generate test data for Django models.

This is a mix of:

* Python Faker - https://github.com/joke2k/faker
* Model Mommy - https://github.com/vandersonmota/model_mommy


Installation
------------

To install Django-data-faker you can use pip::

    pip install django-data-faker


Extra generators
----------------

**Url with username**

.. code-block:: python

    >>> from django_data_faker import url_with_username
    >>> url_with_username()
    'http://koeppledner.biz/curtis.lakin'


**Facebook url**

.. code-block:: python

    >>> from django_data_faker import facebook_url
    >>> facebook_url()
    'http://facebook.com/rchristiansen'


**Twitter url**

.. code-block:: python

    >>> from django_data_faker import twitter_url
    >>> twitter_url()
    'http://twitter.com/cummerata.norbert'

**LinkedIn url**

.. code-block:: python

    >>> from django_data_faker import linkedin_url
    >>> linkedin_url()
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

    from django_data_faker import placeholder_image
    from myapp.models import UserProfile

    file_name, file_content = placeholder_image(400, 200)
    user = UserProfile.objects.get(id=100)
    user.avatar.save(file_name, file_content)

Example:

.. image:: http://i.imgur.com/wk8ZjIV.png?1
