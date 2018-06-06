import glob
import os
from jinja2 import Template
from datetime import datetime

site = {
    'base': 'templates/base.html',
    'pages': [],
}


def build_site():
    all_html_files = glob.glob("content/*.html")
    for page in all_html_files:
        file_name = os.path.basename(page)
        gather_content(page, file_name)
        print(site['pages'])
        name_only, extension = os.path.splitext(file_name)
        format_title(name_only)
        print(site['pages']['title'])
# Reads content/template and templates pages.
        # page_html = open(page).read()
        # template_html = open(site['base']).read()
        # template = Template(template_html)
        # finished_page = template.render(
        #     title = name_only,
        #     content = page_html,
        #     year = datetime.now().year
        # )
        # site['pages'] = {
        #     "filename": str(page),
        #     "filepath": "docs/"+str(file_name),
        # }

# Pulls filename/filepath and stores as key/value pairs in a dict.
def gather_content(page, file_name):
    site['pages'] = {
        "filename": str(page),
        "filepath": "docs/"+str(file_name),
    }
    # return(site['pages'])


    # Formats Title Text
def format_title(name_only):
    name_only = name_only.capitalize()
    if name_only == ("Index"):
        name_only = ("Tyler Holsclaw")
    if name_only == ("Blog"):
        name_only = ("Logic at Work")
    site['pages'].update({"title": str(name_only)})
    # print(site['pages'])


        # print(finished_page)
        # print(site['pages'])
        # print(file_name)
        # print(page)
        # print(site['pages']['filepath'])


    # for page in site['pages']:
    #     print(str(site['pages']['filename'])
        # file_name = os.path.basename(file_path)
        # read_template = open("templates/base.html").read()
        # read_content = open(file_path).read()
        # add_content = read_template.replace("{{content}}", read_content)
        # page["templated_content"] = add_content
        # print(add_content)
build_site()
