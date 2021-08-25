import xml.etree.ElementTree

from flask import Response


def test_int_site_mapped_urls(client):
    text = get_sitemap_text(client)
    x = xml.etree.ElementTree.fromstring(text)
    urls = [
        href.text.strip().replace('http://127.0.0.1:5000', '').replace('http://localhost', '')
        for href in list(x.findall('url/loc'))
    ]
    urls = [
        u if u else '/'
        for u in urls
    ]
    print('Testing {} urls from sitemap...'.format(len(urls)), flush=True)

    has_tested_projects = False
    for url in urls:
        if '/project/' in url and has_tested_projects:
            continue

        if '/project/' in url:
            has_tested_projects = True

        print('Testing url at ' + url)
        resp: Response = client.get(url)
        assert resp.status_code == 200


def get_sitemap_text(client):
    # <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    #     <url>
    #         <loc>http://talkpython.fm/episodes/show/37/python-cybersecurity-and-penetration-testing</loc>
    #         <lastmod>2015-12-08</lastmod>
    #         <changefreq>weekly</changefreq>
    #         <priority>1.0</priority>
    #     </url>
    #     <url>
    #         ...
    #     </url>
    res: Response = client.get("/sitemap.xml")
    text = res.data.decode("utf-8")
    text = text.replace('xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"', '')
    return text
