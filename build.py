page_name = [
    {
        "filename": "content/index.html",
        "title": "Index",
        "filepath": "docs/index.html",
    },
    {
        "filename": "content/blog.html",
        "title": "Blog",
        "filepath": "docs/blog.html",
    },
    {
        "filename": "content/projects.html",
        "title": "Projects",
        "filepath": "docs/projects.html",
    },
    {
        "filename": "content/connect.html",
        "title": "Connect",
        "filepath": "docs/connect.html",
    },
]


def main():
    for i in page_name:
        read_template = open("templates/base.html").read()
        read_content = open(i["filename"]).read()
        finish_page = read_template.replace("{{content}}", read_content)
        open(i["filepath"], "w+").write(finish_page)


if __name__ == "__main__":
    main()
