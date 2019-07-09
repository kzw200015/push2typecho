import xmlrpc.client, sys, getopt, os, yaml, re
from config import *


class TypechoXmlrpcCLient(object):
    def __init__(self, url, user, passwd):
        # self.url = url
        self.user = user
        self.passwd = passwd
        self.proxy = xmlrpc.client.ServerProxy(url)

    def metaWeblog_newPost(self, content, publish):
        self.proxy.metaWeblog.newPost(0, self.user, self.passwd, content,
                                      publish)

    def blogger_getRecentPosts(self):
        res = self.proxy.blogger.getRecentPosts(0, self.user, self.passwd, 1)
        print(res)


if __name__ == "__main__":
    input_file = sys.argv[1]
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
        data = re.search(r'---.*---', text, flags=re.DOTALL)  #正则匹配文章信息
        conf = yaml.load(data[0][4:-3], Loader=yaml.FullLoader)
        body = text[data.span()[1] + 1:]  #获取文章正文

    #构造content结构
    content = dict()
    content["title"] = conf['title']
    content["categories"] = conf['categories'] if isinstance(
        conf['categories'], list) else [
            conf['categories'],
        ]
    content["mt_keywords"] = conf['tags']
    content["description"] = body

    #推送
    push = TypechoXmlrpcCLient(url, user, passwd)
    push.metaWeblog_newPost(content, True)
