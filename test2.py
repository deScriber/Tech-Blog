import markdown

md = markdown.Markdown(extensions=["markdown.extensions.meta"])
data = """
title: My New Blog
author: Jane Q Hacker
Welcome to my ~~site~~ *blog*
"""
html = md.convert(data)
title = md.Meta["title"][0]
author = md.Meta["author"][0]
print(title, "by", author)
print(html)
print(md)
