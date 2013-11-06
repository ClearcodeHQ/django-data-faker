django-data-faker
=================

Fake-factory to generate test data for Django models via _model_mommy recipes.


Installation
------------

To install Django-data-faker you can use pip::

    pip install django-data-faker


How to use
----------

Random one file from directory

.. code-block:: python

    # random avatar

    from django_data_faker import random_file_from_folder
    from myapp.models import UserProfile

    file_name, file_content = random_file_from_folder('/path/to/avatars/dir')
    user = UserProfile.objects.get(id=100)
    user.avatar.save(file_name, file_content)


Generate image placeholder:

.. code-block:: python

    # generate avatar placeholder

    from django_data_faker import gen_placeholder_image
    from myapp.models import UserProfile

    file_name, file_content = gen_placeholder_image(200, 200)
    user = UserProfile.objects.get(id=100)
    user.avatar.save(file_name, file_content)
