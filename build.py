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


def main():
    for i in pages:
        global read_template
        global read_content
        read_template = open("templates/base.html").read()
        read_content = open(i["filename"]).read()
        global add_content
        add_content = read_template.replace("{{content}}", read_content)
    return add_content
        # finish_page = read_template.replace("{{content}}", read_content).replace("{{title}}", i["title"])
        # open(i["filepath"], "w+").write(finish_page)


def templatify():
    for i in pages:
        global templated_content
        templated_content = add_content.replace("{{title}}", i["title"])
    return templated_content


# def compilate():
#     for i in pages:
#         open(i["filepath"], "w+").write(str(i["templated_content"]))

if __name__ == "__main__":
    main()
    templatify()
    # compilate()
print(templated_content)
