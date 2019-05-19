import xmlrpc.client
import sys, getopt
import os
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
    #处理命令行参数
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:c:t:")
    except getopt.GetoptError:
        print("main.py -f <MarkdownFile> -c <category> -t <tags>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("main.py -f <MarkdownFile> -c <category> -t <tags>")
            sys.exit()
        elif opt == "-f":
            input_file = arg
        elif opt == "-c":
            category = arg.split(" ")
        elif opt == "-t":
            tags = arg
            #tags = arg.split(" ")

    #构造content结构
    content = dict()
    content["title"] = "".join(os.path.basename(input_file).split(".")[:-1])
    content["categories"] = category
    content["mt_keywords"] = tags
    with open(input_file, "r", encoding="utf-8") as f:
        content["description"] = f.read()
    #推送
    push = TypechoXmlrpcCLient(url, user, passwd)
    push.metaWeblog_newPost(content, True)
