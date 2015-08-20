#!/usr/bin/env python

from lxml import html, etree
import requests

try:
    import pypandoc as converter
except ImportError:
    import pydocverter as converter

page = requests.get('http://nfcmusa.org/sunday-readings-questions')
tree = html.fromstring(page.text)

#This will create a list of prices
reflection_html = tree.xpath('//div[@class="moduleBody"]')[0]
html = etree.tostring(reflection_html, pretty_print=True)

html = html.replace('\r\n', '\n')
html = html.replace('<br/>', '\n').replace('&#160;', ' ').replace('\n \n', '\n\n')

new_html = ""
for line in html:
    new_html += line.strip()
    new_html += "\r"
#html = new_html

parts = html.split("<h1> </h1>")


#with open("reflection.html", 'w') as out:
#    out.write(html.encode('utf8'))
#print "{} parts.".format(len(parts))

with open('output.markdown', 'w') as out_all:
    for count, part in enumerate(parts):
        markdown = converter.convert(html, 'markdown', format='html')
        out_all.write(part.encode('utf8'))
        if count+1 < len(parts):
            out_all.write("\n\\pagebreak\n")
        with open('output{}.markdown'.format(count), 'w') as out:
            out.write(part.encode('utf8'))

