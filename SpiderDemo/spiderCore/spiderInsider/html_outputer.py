from .. import models

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        print(data)
        #views.add_article(data)

        models.Article.objects.create(title=data['title'], content=data['summary'], url=data['url'])
        self.datas.append(data)

