page_name = [
    {
        "filename": "content/index.html",
        "title": "Tyler Holsclaw",
        "filepath": "docs/index.html",
    },
    {
        "filename": "content/blog.html",
        "title": "Logic at Work",
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


def templateify():
    for i in page_name:
        read_template = open("templates/base.html").read()
            return read_template


def contentor():
    for i in page_name:
        read_content = open(i["filename"]).read()
            return read_content

def main():
    for i in page_name:
        # read_template = open("templates/base.html").read()
        # read_content = open(i["filename"]).read()
        finish_page = read_template.replace("{{content}}", read_content).replace("{{title}}", i["title"])
        open(i["filepath"], "w+").write(finish_page)



if __name__ == "__main__":
    main()
