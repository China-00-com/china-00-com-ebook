# coding:utf-8

import re
import requests


class ItBooksDetail(object):
    title_re = re.compile(r'<h1 class="single-title">(.*?)</h1>')
    subtitle_re = re.compile(r'')
    @classmethod
    def get_title(cls, html):
        result = cls.title_re.findall(html)
        if result:
            title = result[0].strip()
        else:
            title = ""
        return title

    @classmethod
    def get_subtitle(cls, html):
        pass

    @classmethod
    def get_cover(cls, html):
        pass

    @classmethod
    def get_author(cls, html):
        pass

    @classmethod
    def get_isbn_10(cls, html):
        pass

    @classmethod
    def get_publish(cls, html):
        pass

    @classmethod
    def get_language(cls, html):
        pass

    @classmethod
    def get_pages(cls, html):
        pass

    @classmethod
    def get_file_size(cls, html):
        pass

    @classmethod
    def get_file_format(cls, html):
        pass

    @classmethod
    def get_cate(cls, html):
        pass

    @classmethod
    def get_description(cls, html):
        pass

    @classmethod
    def get_download_link(cls, html):
        pass


if __name__ == "__main__":
    content = requests.get("http://www.allitebooks.com/microsoft-sql-server-2012-performance-tuning-cookbook/").content
    print content
    print "title", ItBooksDetail.get_title(content)
