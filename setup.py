from codecs import open
from os.path import join, abspath, dirname
from setuptools import setup, find_packages
import os

here = abspath(dirname(__file__))

with open(join(here, 'README.md'), encoding='utf-8') as buff:
    long_description = buff.read()

setup(
    name="TextProcessing",
    version="1.0",
    description="Projeto 2 - TAP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/diogocorreia01/PublicNewsArchive.git",
    author="Diogo Correia"
    "João Alexandre",
    author_email="diogo.correia01@outlook.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    'beautifulsoup4==4.12.2',
    'blis==0.7.9',
    'bs4==0.0.1',
    'catalogue==2.0.8',
    'certifi==2022.12.7',
    'charset-normalizer==3.1.0',
    'cleantext==1.1.4',
    'click==8.1.3',
    'colorama==0.4.6',
    'confection==0.0.4',
    'cymem==2.0.7',
    'idna==3.4',
    'Jinja2==3.1.2',
    'joblib==1.2.0',
    'langcodes==3.3.0',
    'MarkupSafe==2.1.2',
    'murmurhash==1.0.9',
    'nltk==3.8.1',
    'numpy==1.24.3',
    'packaging==23.1',
    'pathy==0.10.1',
    'preshed==3.0.8',
    'pt-core-news-sm @ https://github.com/explosion/spacy-models/releases/download/pt_core_news_sm-3.5.0/pt_core_news_sm-3.5.0-py3-none-any.whl',
    'pydantic==1.10.7',
    'regex==2023.3.23',
    'requests==2.29.0',
    'smart-open==6.3.0',
    'soupsieve==2.4.1',
    'spacy==3.5.2',
    'spacy-legacy==3.0.12',
    'spacy-loggers==1.0.4',
    'srsly==2.4.6',
    'thinc==8.1.9',
    'tqdm==4.65.0',
    'typer==0.7.0',
    'typing_extensions==4.5.0',
    'urllib3==1.26.15',
    'wasabi==1.1.1',
        'daal4py'
    ]
)