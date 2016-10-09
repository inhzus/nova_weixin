# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import logging

from urllib import quote

from nova_weixin.app.lib.database import mysql
from nova_weixin.app.weixin.template import send_common_template_msg
from nova_weixin.app.nova.get_user_info import get_openid
from nova_weixin.app.config import ADDRESS as address



def note_index(stu_list, nid):
    stu_text = ''
    for i in stu_list:
        stu_text = stu_text+i
    sql = "insert into noteindex values(%s,%s,0,'','%s',0)" % (nid, nid, stu_text)

    @mysql(sql)
    def insert(results=''):
        return results

    result = insert()
    return 0


def note_content(article_url, image_url, title, nid):
    sql = "insert into notecontent values(%s,'%s','cac','','%s','%s',0)" % (nid, title, image_url, article_url)

    @mysql(sql)
    def insert(results=''):
        return results
    result = insert()
    return 0


def note_response(nid):
    sql = "insert into noteresponse values(%s,0,0,'','',0)" % nid

    @mysql(sql)
    def insert(results=''):
        return results

    result = insert()
    return 0


def send(_title, article_url, stu_list):
    url = quote(article_url)
    post_url = 'https://open.weixin.qq.com/connect/oauth2/authorize?' \
        'appid=wx92a9c338a5d02f38&redirect_uri=%s/code/' \
        '%s&response_type=code&scope=snsapi_base&state=123#wechat_redirect' % (address,url)
    cnt = 0
    for i in stu_list:
        openid = get_openid(i)
        if openid != -1:
            openid = openid.encode('utf8')
        result = send_common_template_msg(post_url, title=_title, touser=openid)
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='./log/sendmsg.log',
                            filemode='w')
        logging.warning("sending template msg error --send() noteprocess.py:" + str(result))
        if result.get('errcode') != 0:
            logging.warning("sending template msg error --send() noteprocess.py:"+str(result))
            cnt = cnt+1
    if 0<cnt<len(stu_list):
        return -2                #说明部分人发送成功
    elif cnt == len(stu_list):
        return -1                #说明一个都上不去
    else:
        return 0
