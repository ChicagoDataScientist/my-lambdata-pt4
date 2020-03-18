# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="peterson-lambdata-pt4",
    version="1.0",
    author="AJ Peterson",
    author_email="sonotony@gmail.com",
    description="For practice purposes",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc yes
    #license="MIT",
    url="https://github.com/ChicagoDataScientist/my-lambdata-pt4",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)
