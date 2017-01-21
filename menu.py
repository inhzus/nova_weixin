# -*- coding:utf8 -*- 
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import json
import sys

from nova_weixin.app.config import PY2

if PY2:
    reload(sys)
    sys.setdefaultencoding('utf8')

from nova_weixin.app.weixin.get_acc_token import get_token
from nova_weixin.app.weixin.weixinconfig import MENU
from nova_weixin.packages.nova_wxsdk import WxApiUrl, CommunicateWithApi


def create_menu():
    acc_token = get_token()
    if acc_token:
        url = WxApiUrl.create_menu.format(access_token=acc_token)
        data = MENU
        return CommunicateWithApi.post_data(url, data=json.dumps(data, ensure_ascii=False).encode('utf8'))
    else:
        # log
        return -1


if __name__ == "__main__":
    print(create_menu())
