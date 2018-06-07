import markdown

md = markdown.Markdown(extensions=["markdown.extensions.meta"])
data = """title: My New Blog
author: Jane Q Hacker

Welcome to my ~~site~~ *blog*
"""
html = md.convert(data)
# import IPython; IPython.embed()
blah = md.Meta["title"][0]
boo = md.Meta["author"][0]
print(blah, "by", boo)
print(html)
