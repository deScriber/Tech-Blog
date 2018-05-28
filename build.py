page_name = [
    {
        "filename": "content/index.html",
        "title": "Index"
    }
    {
        "filename": "content/blog.html",
        "title": "Blog"
    }
    {
        "filename": "content/projects.html",
        "title": "Projects"
    }
    {
        "filename": "content/connect.html",
        "title": "Connect"
    }
]

def main():
    read_top = open('templates/top.html').read()
    read_mid = open("content/index.html").read()
    read_bottom = open("templates/bottom.html").read()
    read_file = read_top + read_mid + read_bottom
    open("docs/index.html", "w+").write(read_file)
    read_top = open("templates/top.html").read()
    read_mid = open("content/blog.html").read()
    read_bottom = open("templates/bottom.html").read()
    read_file = read_top + read_mid + read_bottom
    open("docs/blog.html", "w+").write(read_file)
    read_top = open("templates/top.html").read()
    read_mid = open("content/projects.html").read()
    read_bottom = open("templates/bottom.html").read()
    read_file = read_top + read_mid + read_bottom
    open("docs/projects.html", "w+").write(read_file)
    read_top = open("templates/top.html").read()
    read_mid = open("content/connect.html").read()
    read_bottom = open("templates/bottom.html").read()
    read_file = read_top + read_mid + read_bottom
    open("docs/connect.html", "w+").write(read_file)







if __name__ = '__main__':
    main()





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
