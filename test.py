# import glob
# all_html_files = glob.glob("content/*.html")
# print(all_html_files)

# import os
# file_path = "content/index.html"
# file_name = os.path.basename(file_path)
# print(file_name)
# name_only, extension = os.path.splitext(file_name)
# print(name_only)

import glob
import os


site = {
    'base': 'templates/base.html',
    'pages': [],
}

# pages =
    #
    # {
    #     "filename": "content/index.html",
    #     "title": "Tyler Holsclaw",
    #     "filepath": "docs/index.html",
    #     "templated_content": None,
    # },
    # {
    #     "filename": "content/blog.html",
    #     "title": "Logic at Work",
    #     "filepath": "docs/blog.html",
    #     "templated_content": None,
    # },
    # {
    #     "filename": "content/projects.html",
    #     "title": "Projects",
    #     "filepath": "docs/projects.html",
    #     "templated_content": None,
    # },
    # {
    #     "filename": "content/connect.html",
    #     "title": "Connect",
    #     "filepath": "docs/connect.html",
    #     "templated_content": None,
    # }


def find_page():
    all_html_files = glob.glob("content/*.html")
    site['pages']['filename'] = [all_html_files]
    print(str(site['pages']['filename']))
    # for page in site['pages']:
    #     print(str(site['pages']['filename'])
        # file_name = os.path.basename(file_path)
        # read_template = open("templates/base.html").read()
        # read_content = open(file_path).read()
        # add_content = read_template.replace("{{content}}", read_content)
        # page["templated_content"] = add_content
        # print(add_content)
find_page()
