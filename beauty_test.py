# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
# BeautifulSoup 的优势是获取数据的时候是树节点一样，一层一层的


if __name__ == '__main__':


    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>

    """

    soup = BeautifulSoup(html_doc)

    print soup.title

    print soup.title.name

    print soup.title.string

    print soup.p

    print soup.a
    # 可进行遍历
    print soup.find_all('a')

    print soup.find(id='link3')
    # 获取这段html片段中的内容，不区分标签
    print soup.get_text()
    #遍历 根据 class 的值查找
    # <p class="story">Once upon a time there were three little sisters;
    print soup.find_all('p', 'story')

    #用 BeautifulSoup 处理的数据多半是格式相同的一系列数据，多用 find_all的情况比较多
    # eg:
    # data = driver.page_source
    #     soup = BeautifulSoup(data, 'lxml')  # 声明BeautifulSoup对象
    #     result = []
    #     searchlist = soup.find_all('div','search-work-info')
    #     for search in searchlist:
    #         textlist = search.find_all('span','ng-binding')[:-2]
    #         tmp = []
    #         for text in textlist:
    #             info = text.get_text()
    #             tmp.append(info)
    #         result.append(tmp)
    #     print result















