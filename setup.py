from setuptools import setup

setup(
    name='django-data-faker',
    version='0.0.1.6',
    description='Fake-factory to generate test data for Django models via model_mommy recipes.',
    author='Clearcode - The A Room',
    author_email='thearoom@clearcode.cc',
    url='https://github.com/trojkat/django-data-faker',
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
