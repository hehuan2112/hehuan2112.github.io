"""Pelican Configuration

For a simple conference 
"""
import json
from datetime import datetime

AUTHOR = 'Huan He'
SITENAME = 'Huan He Box'

# just set this to relative path due to deployment issue
SITEURL = './'

# where to store the markdown contents and other materials
PATH = 'content'

# I'm here
TIMEZONE = 'America/Chicago'

# by default
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# customized plugins
PLUGINS = [
    'myplugins'
]

# Social widget if needed.
SOCIAL = (('https://twitter.com/', '#'),
          ('https://facebook.com/', '#'),)

# we don't need pagination as there is no blog
DEFAULT_PAGINATION = False

# put all contents under year folder
ARTICLE_URL = "{category}/{slug}.html"
ARTICLE_SAVE_AS = "{category}/{slug}.html"

# for page
PAGE_URL = "page/{slug}.html"
PAGE_SAVE_AS = "page/{slug}.html"

# for conference site author category is not needed
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""

# no need for tags page
TAGS_SAVE_AS = ""

# no need for archive page
ARCHIVES_SAVE_AS = ""

# no need for categorys page
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""

# current year of this site
CURRENT_YEAR = datetime.today().strftime('%Y')

# specify the customized theme
THEME = "./themes/hh-theme"

# my works and each content
WORKS = json.load(open('content/works.json'))
WORKS['news'] = json.load(open('content/works.news.json'))
WORKS['tools'] = json.load(open('content/works.tools.json'))
WORKS['awards'] = json.load(open('content/works.awards.json'))
WORKS['projects'] = json.load(open('content/works.projects.json'))
WORKS['patents'] = json.load(open('content/works.patents.json'))
WORKS['work_exp'] = json.load(open('content/works.work_exp.json'))
WORKS['academic_exp'] = json.load(open('content/works.academic_exp.json'))
WORKS['publications'] = json.load(open('content/works.publications.json'))

# links
LINKS = [
    ['GitHub', 'https://github.com/']
]

# YEARS
YEARS = ['%s' % y for y in range(2018, 2022 + 1)]
YEARS.reverse()
YEARS.append('Before 2018')