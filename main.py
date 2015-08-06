from lxml import html, etree
import requests

page = requests.get('http://nfcmusa.org/sunday-readings-questions')
tree = html.fromstring(page.text)

#This will create a list of prices
reflection_html = tree.xpath('//div[@class="moduleBody"]')[0]

print etree.tostring(reflection_html, pretty_print=True)
