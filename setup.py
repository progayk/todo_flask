from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'psycopg2'
]

setup(
    name='todo_flask',
    version='0.0',
    description='A to-do list app built with flask',
    author='mayk jony',
    author_email='mayk@jony.com',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)
