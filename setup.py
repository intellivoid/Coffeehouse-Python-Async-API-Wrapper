from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name='aiocf',
    version='1.0.0',
    description='Asynchronous Python Wrapper for Coffeehouse',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['aiocf', 'aiocf.lydia'],
    package_dir={
        'aiocf': 'aiocf'
    },
    author='Intellivoid Technologies',
    author_email='netkas@intellivoid.net',
    python_requires='>=3.5.3',
    url='https://coffeehouse.intellivoid.net/',
    install_requires=[
        'aiohttp'
    ]
)
