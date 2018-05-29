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


# def search_dictionaries(key, value, list_of_dictionaries):
#     return [element for element in list_of_dictionaries if element[key] == value]


def main():
    for i in pages:
        read_template = open("templates/base.html").read()
        read_content = open(i["filename"]).read()
        global add_content
        add_content = read_template.replace("{{content}}", read_content)
        i["templated_content"] = add_content
        print(i["templated_content"])

        # finish_page = read_template.replace("{{content}}", read_content).replace("{{title}}", i["title"])
        # open(i["filepath"], "w+").write(finish_page)


# def templatify(templated_content, add_content, pages):
#     for i in pages:
#         global templated_content
#         templated_content = add_content.replace("{{title}}", i["title"])
#         i["templated_content"] = templated_content
#     return template_content


# def compilate():
#     for i in pages:
#         open(i["filepath"], "w+").write(templated_content)

if __name__ == "__main__":
    main()
    # templatify()
    # compilate()
# print(finish_page)
