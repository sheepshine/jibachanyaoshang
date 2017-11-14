# coding:utf8
from . import url_manage, html_downloader, html_parser, html_outputer


class SpiderMan(object):
    def __init__(self):
        self.urls = url_manage.UrlManage()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url, _countn):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            print 'cras %d : %s' %(count, new_url)
            html_cont = self.downloader.download(new_url)
            new_urls, new_data = self.parser.parser(new_url, html_cont)
            self.urls.add_new_urls(new_urls)
            print(new_data)
            self.outputer.collect_data(new_data)

            if count == _countn:
                break

            count = count + 1