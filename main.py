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

markdown = converter.convert(html, 'markdown', format='html')

print markdown

