# import glob
# all_html_files = glob.glob("content/*.html")
# print(all_html_files)

import glob
import os

file_path = glob.glob("content/*.html")
print(file_path)
# file_name = os.path.basename(file_path)
# print(file_name)
# name_only, extension = os.path.splitext(file_name)
# print(name_only)


site = {
    'base': 'templates/base.html',
    'pages': [

    ],
}


def find_page():
    all_html_files = glob.glob("content/*.html")
    site['pages'] = [all_html_files]
    print(site['pages'])
    # for page in site['pages']:
    #     print(str(site['pages']['filename'])
        # file_name = os.path.basename(file_path)
        # read_template = open("templates/base.html").read()
        # read_content = open(file_path).read()
        # add_content = read_template.replace("{{content}}", read_content)
        # page["templated_content"] = add_content
        # print(add_content)
find_page()
