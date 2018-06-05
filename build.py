import glob


pages = [
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
    # },
]

def find_page():
    all_html_files = glob.glob("content/*.html")
    pages = [all_html_files]



# The build_page function opens and reads the base.html file and the value of the key
# "filename" for each page contains each pages respective html file paths.
# It then uses the replace method to replace the {{content}} placeholder on the
# base.html and stores that as a string in a variable. We then take that variable
# and give the key "templated_content" the string as it's value.
def build_page():
    for page in pages:
        read_template = open("templates/base.html").read()
        read_content = open(page["filename"]).read()
        add_content = read_template.replace("{{content}}", read_content)
        page["templated_content"] = add_content
    template_update()
    publish()


# The template update function updates each string stored in the
# "templated_content" key for each of our pages with the value from the key
# "title" in the placeholder {{title}}. It then assigns the value of the updated
# string to the "templated_content" key for further use. We can use this function
#  to inject any more bells and whistles for templating in the future.
def template_update():
    for page in pages:
        templated_content = page["templated_content"].replace("{{title}}", page["title"])
        page["templated_content"] = templated_content


# The publish function then takes the value of the key "templated_content" and
# writes it to the value of the key "filepath" for each dict in the list pages,
# which routes to the websites html file paths.
def publish():
    for page in pages:
        open(page["filepath"], "w+").write(page["templated_content"])


if __name__ == "__main__":
    build_page()
