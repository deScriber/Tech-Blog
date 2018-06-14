import glob
import os
import markdown
import jinja2
from jinja2 import Template
from datetime import datetime


my_pages = {}


site = {
    'base': 'templates/base.html',
}


# Main function, builds site by looking for content, template, and storing the
# data for each page into their own dicts within the nested list site['pages']
def build_site():
    all_md_files = glob.glob("content/*.md")
    for page in all_md_files:
        file_name = os.path.basename(page)
        name_only, extension = os.path.splitext(file_name)
        gather_path(page, name_only)
        gather_markdown(page, name_only)
        template_template(page, name_only)
    site.update({'pages': my_pages})
    page_dict = site['pages']
    page_dict_list = page_dict.keys()
    final_template(page_dict, page_dict_list)


# Pulls filename/filepath/template and stores as key/value pairs in a dict.
def gather_path(page, name_only):
    site['pages'] = {
        "page_template": "templates/"+str(name_only)+".html",
        "filename": str(page),
        "filepath": "docs/"+str(name_only)+".html",
        "current_page": name_only,
    }


def gather_markdown(page, name_only):
    md = markdown.Markdown(extensions=["markdown.extensions.meta"])
    page_md = open(page).read()
    html = md.convert(page_md)
    page_title = md.Meta['page_title']
    page_subtitle = md.Meta['page_subtitle']
    post_title = md.Meta['post_title']
    post_number = md.Meta['post_number']
    post_content = md.Meta['post_content']
    sub_title = md.Meta['sub_title']
    section_id = md.Meta['section_id']
    bottom_post_button = {
        "default": "<a href='#' class='btn btn-default btn-lg strong_text'>Back to Top</a>",
        "blog1": "<a href='blog.html#blog-1' class='btn btn-default btn-lg strong_text'>Open Article</a>",
        "blog2": "<a href='blog.html#blog-2' class='btn btn-default btn-lg strong_text'>Open Article</a>",
        "blog3": "<a href='blog.html#blog-3' class='btn btn-default btn-lg strong_text'>Open Article</a>",
        "project1": "<a href='projects.html#project-1' class='btn btn-default btn-lg strong_text'>Open Project</a>",
        "project2": "<a href='projects.html#project-2' class='btn btn-default btn-lg strong_text'>Open Project</a>",
        "project3": "<a href='projects.html#project-3' class='btn btn-default btn-lg strong_text'>Open Project</a>",
        }
    my_pages.update({
        name_only: {
            "page_template": "templates/"+str(name_only)+".html",
            "page_title": page_title,
            "page_subtitle": page_subtitle,
            "post_title": post_title,
            "post_subtitle": sub_title,
            "post_number": post_number,
            "section_id": section_id,
            "post_content": post_content,
            "bottom_post_button": bottom_post_button,
            }
        })


# Compiles both content and template for each page, stores into key/value pair
def template_template(page, name_only):
    page_html = open(site['pages']['page_template']).read()
    template_html = open(site['base']).read()
    template = Template(template_html)
    finished_page_template = template.render(
        content=page_html,
        year=datetime.now().year,
        page_title=my_pages[name_only]['page_title'],
        page_subtitle=my_pages[name_only]['page_subtitle'],
    )
    site.update({
        name_only+"_template": finished_page_template
    })


def final_template(page_dict, page_dict_list):
    for page in page_dict_list:
        page_html = site[page+"_template"]
        print(page_html)
        template = Template(page_html)
        bottom_post_button = "<a href='#' class='btn btn-default btn-lg strong_text'>"
        finished_page_template = template.render(
            section_id=site['pages'][page]['section_id'],
            page_title=site['pages'][page]['page_title'],
            page_subtitle=site['pages'][page]['page_subtitle'],
            post_title=site['pages'][page]['post_title'],
            post_subtitle=site['pages'][page]['post_subtitle'],
            post_content=site['pages'][page]['post_content'],
            post_number=site['pages'][page]['post_number'],
            bottom_post_button=site['pages'][page]['bottom_post_button'],
        )
        site.update({
            page+"_template": finished_page_template
        })
        print(site["connect_template"])

if __name__ == "__main__":
    build_site()
