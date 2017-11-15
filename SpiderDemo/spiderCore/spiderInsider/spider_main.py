# coding:utf8
import sys
import gc
import threading
from . import url_manage, html_downloader, html_parser, html_outputer

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class SpiderMan(object):
    def __init__(self):
        self.urls = url_manage.UrlManage()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url, _countn):
        count = 1
        self.urls.add_new_url(root_url)
        while True:
            #self.loop_request(count)
            t = threading.Thread(target=self.loop_request, args=(count,))
            t.start()
            count = count + 1

            if len(threading.enumerate()) > 200:
                t.join()

            if count == _countn:
                break

            gc.collect()

    def loop_request(self, count):
        new_url = self.urls.get_new_url()
        print 'cras %d : %s' % (count, new_url)
        html_cont = self.downloader.download(new_url)
        new_urls, new_data = self.parser.parser(new_url, html_cont)
        self.urls.add_new_urls(new_urls)
        self.outputer.collect_data(new_data)