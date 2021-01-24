from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='auscultor',
    version='0.0.1',
    description='Toy NLP module to extract topic from English text',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Daniel Arato',
    author_email='nil.the.human@gmail.com',
    url='https://github.com/nilthehuman/auscultor',
    license=license,
    packages=find_packages(exclude=('tests')),
    python_requires='>=3.6'
)

