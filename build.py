pages = [
    {
        "filename": "content/index.html",
        "title": "Tyler Holsclaw",
        "filepath": "docs/index.html",
        "templated_content": None,
    },
    {
        "filename": "content/blog.html",
        "title": "Logic at Work",
        "filepath": "docs/blog.html",
        "templated_content": None,
    },
    {
        "filename": "content/projects.html",
        "title": "Projects",
        "filepath": "docs/projects.html",
        "templated_content": None,
    },
    {
        "filename": "content/connect.html",
        "title": "Connect",
        "filepath": "docs/connect.html",
        "templated_content": None,
    },
]


# The main function opens and reads the base.html file and the value of the key
# "filename" for each page contains each pages respective html file paths.
# It then uses the replace method to replace the {{content}} placeholder on the
# base.html and stores that as a string in a variable. We then take that variable
# and give the key "templated_content" the string as it's value.
def main():
    for i in pages:
        read_template = open("templates/base.html").read()
        read_content = open(i["filename"]).read()
        add_content = read_template.replace("{{content}}", read_content)
        i["templated_content"] = add_content
    template_update()
    publish()


# The template update function updates each string stored in the
# "templated_content" key for each of our pages with the value from the key
# "title" in the placeholder {{title}}. It then assigns the value of the updated
# string to the "templated_content" key for further use. We can use this function
#  to inject any more bells and whistles for templating in the future.
def template_update():
    for i in pages:
        templated_content = i["templated_content"].replace("{{title}}", i["title"])
        i["templated_content"] = templated_content


# The publish function then takes the value of the key "templated_content" and
# writes it to the value of the key "filepath" for each dict in the list pages,
# which routes to the websites html file paths.
def publish():
    for i in pages:
        open(i["filepath"], "w+").write(i["templated_content"])


if __name__ == "__main__":
    main()
