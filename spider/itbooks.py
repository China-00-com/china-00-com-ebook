# coding:utf-8

import re
import requests


class ItBooksDetail(object):
    title_re = re.compile(r'<h1 class="single-title">(.*?)</h1>')
    subtitle_re = re.compile(r'<h4>(.*?)</h4>')
    cover_re = re.compile(r'<img width="381" height="499" src="(.*?)" class="attachment-post-thumbnail')
    author_re = re.compile(r'<dt>Author:</dt><dd> <a.*?>(.*?)</a>')
    isbn_10_re = re.compile(r'<dt>ISBN-10:</dt><dd>(.*?)</dd>')
    publish_re = re.compile(r'<dt>Year:</dt><dd>(.*?)</dd>')
    pages_re = re.compile(r'<dt>Pages:</dt><dd>(.*?)</dd>')
    language_re = re.compile(r'<dt>Language:</dt><dd>(.*?)</dd>')
    file_size_re = re.compile(r'<dt>File size:</dt><dd>(.*?)</dd>')
    file_format_re = re.compile(r'<dt>File format:</dt><dd>(.*?)</dd>')
    cate_re = re.compile(r'<dt>Category:</dt><dd> <a.*?>(.*?)</a>')
    desc_re = re.compile(r'<h3>Book Description:</h3>(.*?)</div>', re.S)
    down_link_re = re.compile(r'"download-links">.*?<a href="(.*?)" target="_blank"><i class="fa fa-download"', re.S)

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
        result = cls.subtitle_re.findall(html)
        if result:
            sub_title = result[0].strip()
        else:
            sub_title = ""
        return sub_title

    @classmethod
    def get_cover(cls, html):
        result = cls.cover_re.findall(html)
        if result:
            cover = result[0].strip()
        else:
            cover = ""
        return cover

    @classmethod
    def get_author(cls, html):
        result = cls.author_re.findall(html)
        if result:
            author = result[0].strip()
        else:
            author = ""
        return author

    @classmethod
    def get_isbn_10(cls, html):
        result = cls.isbn_10_re.findall(html)
        if result:
            isbn_10 = result[0].strip()
        else:
            isbn_10 = ""
        return isbn_10

    @classmethod
    def get_publish(cls, html):
        result = cls.publish_re.findall(html)
        if result:
            publish = result[0].strip()
        else:
            publish = ""
        return publish

    @classmethod
    def get_language(cls, html):
        result = cls.language_re.findall(html)
        if result:
            language = result[0].strip()
        else:
            language = ""
        return language

    @classmethod
    def get_pages(cls, html):
        result = cls.pages_re.findall(html)
        if result:
            pages = result[0].strip()
        else:
            pages = ""
        return pages

    @classmethod
    def get_file_size(cls, html):
        result = cls.file_size_re.findall(html)
        if result:
            file_size = result[0].strip()
        else:
            file_size = ""
        return file_size

    @classmethod
    def get_file_format(cls, html):
        result = cls.file_format_re.findall(html)
        if result:
            file_format = result[0].strip()
        else:
            file_format = ""
        return file_format

    @classmethod
    def get_cate(cls, html):
        result = cls.cate_re.findall(html)
        if result:
            cate = result[0].strip()
        else:
            cate = ""
        return cate

    @classmethod
    def get_description(cls, html):
        result = cls.desc_re.findall(html)
        if result:
            desc = result[0].strip()
        else:
            desc = ""
        return desc

    @classmethod
    def get_download_link(cls, html):
        result = cls.down_link_re.findall(html)
        if result:
            down_link = result[0].strip()
        else:
            down_link = ""
        return down_link


def test_detail():
    content = requests.get("http://www.allitebooks.com/test-driven-development-with-python-2nd-edition/").content
    print "title:", ItBooksDetail.get_title(content)
    print "subtitle:", ItBooksDetail.get_subtitle(content)
    print "cover:", ItBooksDetail.get_cover(content)
    print "author:", ItBooksDetail.get_author(content)
    print "isbn_10:", ItBooksDetail.get_isbn_10(content)
    print "publish:", ItBooksDetail.get_publish(content)
    print "pages:", ItBooksDetail.get_pages(content)
    print "language:", ItBooksDetail.get_language(content)
    print "file_size:", ItBooksDetail.get_file_size(content)
    print "file_format:", ItBooksDetail.get_file_format(content)
    print "cate:", ItBooksDetail.get_cate(content)
    print "desc:", ItBooksDetail.get_description(content)
    print "down_link:", ItBooksDetail.get_download_link(content)


class ItBookList(object):
    side_bar_re = re.compile(r'<ul id="menu-categories"(.*?)</ul>', re.S)
    cate_re = re.compile(r'<li id="menu-item.*?<a href="(.*?)">(.*?)</a></li>')
    detail_link = re.compile(r'entry-title"><a href="(.*?)"')
    last_page_re = re.compile(r'title="Last Page &rarr;">(.*?)</a>')

    @classmethod
    def get_pages(cls, url):
        content = requests.get(url).content
        pages = cls.last_page_re.findall(content)[0].strip()
        return int(pages)

    @classmethod
    def get_cate_list(cls, url):
        print "获取分类链接信息..."
        content = requests.get(url).content
        result = cls.side_bar_re.findall(content)
        sidebar = result[0]
        cate_list = cls.cate_re.findall(sidebar)
        cates = list()
        for cate in cate_list:
            cate_name = cate[1].replace('&#038;', "&")
            cate_link = cate[0]
            print "提取", cate_name, "分类分页详情"
            cate_pages = cls.get_pages(cate_link)
            cates.append(
                {
                    "cate_name": cate_name,
                    "cate_link": cate_link,
                    "cate_pages": cate_pages
                }
            )
        return cates

    @classmethod
    def get_detail_link(cls):
        pass

    @classmethod
    def run(cls):
        cate_list = cls.get_cate_list("http://www.allitebooks.com")
        for cate in cate_list:
            print cate


if __name__ == "__main__":
    ItBookList.run()
