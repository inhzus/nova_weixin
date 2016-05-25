# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import time
import config
import urllib2
import json


def get_token():
    with open('acc_token') as f:
        data = f.read()
    if data:
        past_time = int(data[0:10])
        acc_token = data[10:]
    else:
        past_time = 1400000000
    now_time = int(time.time())
    if now_time-past_time > 1000:
        app_id = config.APP_ID
        app_secret = config.SECRET
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % \
              (app_id, app_secret)
        result = urllib2.urlopen(url).read()
        if json.loads(result).get('errcode'):
            print "fail to get acc_token --get_acc_token.py"
            acc_token = "fail to get acc_token --get_acc_token.py"
            pass
        else:
            acc_token = json.loads(result).get('access_token')
            string = str(int(time.time()))+acc_token
            with open('acc_token', 'w') as f:
                f.write(string)
    return acc_token

if __name__ == "__main__":
    get_token()





