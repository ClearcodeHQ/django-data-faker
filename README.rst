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

**Base import**

.. code-block:: python

    >>> from django_data_faker import fake


**Url with username**

.. code-block:: python

    >>> fake.url_with_username()
    'http://koeppledner.biz/curtis.lakin'


**Facebook url**

.. code-block:: python

    >>> fake.facebook_url()
    'http://facebook.com/rchristiansen'


**Twitter url**

.. code-block:: python

    >>> fake.twitter_url()
    'http://twitter.com/cummerata.norbert'

**LinkedIn url**

.. code-block:: python

    >>> fake.linkedin_url()
    'http://linkedin.com/pub/bweimann'


**Random file from directory**

.. code-block:: python

    # random avatar

    from myapp.models import UserProfile

    user = UserProfile.objects.get(id=100)
    user.avatar = fake.random_file_from_folder('/path/to/avatars/dir')
    user.save()


**Generate image placeholder**

.. code-block:: python

    # generate avatar placeholder

    from myapp.models import UserProfile

    user = UserProfile.objects.get(id=100)
    user.avatar = fake.placeholder_image(400, 200)
    user.save()

Example:

.. image:: http://i.imgur.com/wk8ZjIV.png?1
