import glob
import os
from jinja2 import Template
from datetime import datetime


site = {
    'base': 'templates/base.html',
    'pages': [],
}

# Main function, builds site by looking for content, template, and storing the
# data for each page into their own dicts within the nested list site['pages']
def build_site():
    all_html_files = glob.glob("content/*.html")
    for page in all_html_files:
        file_name = os.path.basename(page)
        gather_content(page, file_name)
        name_only, extension = os.path.splitext(file_name)
        format_title(name_only)
        template_content(page)
        open(site['pages']["filepath"], "w+").write(site['pages']["templated_content"])


# Pulls filename/filepath and stores as key/value pairs in a dict.
def gather_content(page, file_name):
    site['pages'] = {
        "filename": str(page),
        "filepath": "docs/"+str(file_name),
    }


# Formats Title Text
def format_title(name_only):
    name_only = name_only.capitalize()
    if name_only == ("Index"):
        name_only = ("Tyler Holsclaw")
    if name_only == ("Blog"):
        name_only = ("Logic at Work")
    site['pages'].update({"title": str(name_only)})


# Compiles both content and template for each page, stores into key/value pair
def template_content(page):
    page_html = open(page).read()
    template_html = open(site['base']).read()
    template = Template(template_html)
    finished_page = template.render(
        title = site['pages']['title'],
        content = page_html,
        year = datetime.now().year
    )
    site['pages'].update({"templated_content": finished_page})

# if __name__ == "__main__":
#     build_site()
