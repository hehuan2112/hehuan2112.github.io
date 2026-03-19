import re
import markdown
from pelican import signals

REGEX_YEAR = r"\b(\d{4})\b"

###########################################################
# Filters
###########################################################
def filter_sort_mycates(categories, desc=True):
    '''
    Sort categories 
    '''
    return sorted(categories, key=lambda v: v[0], reverse=True)


def filter_md2html(s):
    '''
    Convert a Markdown string to HTML
    '''
    return markdown.markdown(s)


def filter_highlight_me(authors):
    '''
    Highlight myself in authors
    '''
    return authors.replace('Huan He', '<b>Huan He</b>')


def filter_get_year(date_str):
    '''
    Get the year in a string
    '''
    ms = re.findall(REGEX_YEAR, date_str)

    if len(ms) == 0:
        return ''
    else:
        return ms[0]


def filter_pg2path(page_name):
    '''
    Get the path according to page_name
    '''
    if page_name == 'index':
        # ok it's the homepage
        return '.'
    else:
        return '..'


def filter_pg2act_nav(output_file, target):
    '''
    Get the active nav item
    '''
    if output_file == target:
        return 'active'

    return ''


def add_all_filters(pelican):
    """Add (register) all filters to Pelican."""
    pelican.env.filters.update({"pg2path": filter_pg2path})
    pelican.env.filters.update({"pg2act_nav": filter_pg2act_nav})
    pelican.env.filters.update({"md2html": filter_md2html})
    pelican.env.filters.update({"get_year": filter_get_year})
    pelican.env.filters.update({"highlight_me": filter_highlight_me})
    pelican.env.filters.update({"sort_mycates": filter_sort_mycates})


###########################################################
# Plugin for make special pages
###########################################################


def register():
    """Plugin registration."""
    signals.generator_init.connect(add_all_filters)