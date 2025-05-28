from datetime import date
import xml.etree.ElementTree as ET

sitemap_path = "books_sitemap.xml"
tree = ET.parse(sitemap_path)
root = tree.getroot()

# Namespace handling
ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
ET.register_namespace('', ns['ns'])

today = date.today().isoformat()

for url in root.findall('ns:url', ns):
    lastmod = url.find('ns:lastmod', ns)
    if lastmod is not None:
        lastmod.text = today

tree.write(sitemap_path, encoding="utf-8", xml_declaration=True)
