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
        read_template = open("template/base.html").read()
        read_content = open(i["filename"]).read()
        finish_page = read_template.replace("{{content}}", read_content)
        open(i["filepath"], "w+").write(finish_page)
    # read_top = open('templates/top.html').read()
    # read_mid = open("content/index.html").read()
    # read_bottom = open("templates/bottom.html").read()
    # read_file = read_top + read_mid + read_bottom
    # open("docs/index.html", "w+").write(read_file)
    # read_top = open("templates/top.html").read()
    # read_mid = open("content/blog.html").read()
    # read_bottom = open("templates/bottom.html").read()
    # read_file = read_top + read_mid + read_bottom
    # open("docs/blog.html", "w+").write(read_file)
    # read_top = open("templates/top.html").read()
    # read_mid = open("content/projects.html").read()
    # read_bottom = open("templates/bottom.html").read()
    # read_file = read_top + read_mid + read_bottom
    # open("docs/projects.html", "w+").write(read_file)
    # read_top = open("templates/top.html").read()
    # read_mid = open("content/connect.html").read()
    # read_bottom = open("templates/bottom.html").read()
    # read_file = read_top + read_mid + read_bottom
    # open("docs/connect.html", "w+").write(read_file)
    #
    #
    #
    #
    #

main()

# if __name__ = '__main__':
#     main()





# read_top = open("templates/top.html").read()
# read_mid = open("content/index.html").read()
# read_bottom = open("templates/bottom.html").read()
# read_file = read_top + read_mid + read_bottom
# open("docs/index.html", "w+").write(read_file)
#
# read_top = open("templates/top.html").read()
# read_mid = open("content/blog.html").read()
# read_bottom = open("templates/bottom.html").read()
# read_file = read_top + read_mid + read_bottom
# open("docs/blog.html", "w+").write(read_file)
#
# read_top = open("templates/top.html").read()
# read_mid = open("content/projects.html").read()
# read_bottom = open("templates/bottom.html").read()
# read_file = read_top + read_mid + read_bottom
# open("docs/projects.html", "w+").write(read_file)
#
# read_top = open("templates/top.html").read()
# read_mid = open("content/connect.html").read()
# read_bottom = open("templates/bottom.html").read()
# read_file = read_top + read_mid + read_bottom
# open("docs/connect.html", "w+").write(read_file)
