import glob
import os
import markdown
import jinja2
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
        # gather_markdown(page, file_name)
        # format_post(page, section_id)#TODO
        format_page(name_only)
        template_content(page)
        # open(site['pages']["filepath"], "w+").write(site['pages']["templated_content"])
        print(site['pages']['title'])
        print(site['pages']['sub_title'])
        print(site['pages']['bottom_post_button'])

# Pulls filename/filepath and stores as key/value pairs in a dict.
def gather_content(page, file_name):
    site['pages'] = {
        "filename": str(page),
        "filepath": "docs/"+str(file_name),
    }


def gather_markdown(page, file_name):
    md = markdown.Markdown(extensions=["markdown.extensions.meta"])
    page_md = open(page).read(),
    html = md.convert(page_md)
    # import IPython; IPython.embed()
    post_title = md.Meta["title"][0]
    post_content = md.Meta["author"][0]
    print(post_title, "by", post_content)
    print(md.Meta["author"][0])


# Formats Page
def format_page(name_only):
    name_only = name_only.capitalize()
    slogan = "Logic at Work"
    title_img = ""
    bottom_post_button = "<a href='#' class='btn btn-default btn-lg strong_text'>Back to Top</a>"
    if name_only == ("Index"):
        name_only = ("Tyler Holsclaw")
        # bottom_post_button = post_link #TODO
    if name_only == ("Blog"):
        name_only = ("Logic at Work")
        slogan = "A Blog"
    if name_only == ("Connect"):
        slogan = "Tyler Holsclaw"
        title_img = "<img id='connect-profile' src='img/me-thumb.jpeg'>"
        bottom_post_button = "<a href='mailto:tholsclaw@protonmail.com' class='btn btn-default btn-lg strong_text'>Email Me</a>"
    site['pages'].update({
        "title": name_only,
        "sub_title": slogan,
        "title_img": title_img,
        "bottom_post_button": bottom_post_button,
        })


# Compiles both content and template for each page, stores into key/value pair
def template_content(page):
    page_html = open(page).read()
    template_html = open(site['base']).read()
    template = Template(template_html)
    finished_page = template.render(
        content = page_html, #TODO turn this into jinja2 for loop template in body
        title = site['pages']['title'],
        sub_title = site['pages']['sub_title'],
        title_img = site['pages']['title_img'],
        post_title = site['pages']['post_title'],
        post_content = site['pages']['post_content'],
        recent_title = site['pages']['recent_title'],
        recent_post = site['pages']['recent_post'],
        bottom_post_button = site['pages']["bottom_post_button"],
        year = datetime.now().year,

    )
    site['pages'].update({"templated_content": finished_page})

if __name__ == "__main__":
    build_site()
