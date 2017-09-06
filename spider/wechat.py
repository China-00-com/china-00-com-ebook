# coding:utf-8

# coding: utf-8
""" 微信公众号文章获取
利用 itchat 包，获取微信公众号推送的信息，从中获得公众号文章的永久链接
"""
import json
import itchat
from itchat.content import SHARING, TEXT

mp_mapping = dict()  # 公众号 user_name: nick_name 对照表
room_mapping = dict()  # 微信群 user_name: nick_name 对照表



@itchat.msg_register(TEXT, isGroupChat=True)
def get_group_message(msg):
    """ 在'微信爬虫测试群'里发 update, info 更新,获取相关信息 """
    user_name = msg["ToUserName"]
    nick_name = room_mapping.get(user_name)
    if nick_name == "xxxx":
        text = msg["Content"]
        if text == "update":
            update_mp_map()
            update_rooms_map()
            message = u"更新完成, %s个公众号, %s个群" % (len(mp_mapping), len(room_mapping))
            itchat.send(message, toUserName=user_name)
        elif text == "info":
            message = u"%s个公众号, %s个群" % (len(mp_mapping), len(room_mapping))
            itchat.send(message, toUserName=user_name)
        elif text == "dump":
            with open("mp.json", "w") as f:
                json.dump(mp_mapping, f)
            message = u"序列化公众号列表成功，请登录服务器查看"
            itchat.send(message, toUserName=user_name)


@itchat.msg_register(SHARING, isMpChat=True)
def get_mp_message(msg):
    """ 处理公众号推送的信息 """
    user_name = msg["FromUserName"]
    if user_name not in mp_mapping:
        update_mp_map()
    nick_name = mp_mapping.get(user_name, "")
    if not nick_name:
        print("not found user name %s" % user_name)
    else:
        msg["__nick_name"] = nick_name
    after_action(msg)


def after_action(msg):
    pass


def update_mp_map():
    mps = itchat.get_mps()
    for mp in mps:
        mp_mapping[mp["UserName"]] = mp["NickName"]


def update_rooms_map():
    rooms = itchat.get_chatrooms()
    for room in rooms:
        room_mapping[room["UserName"]] = room["NickName"]


def main():
    itchat.auto_login(hotReload=True, enableCmdQR=2)
    update_rooms_map()
    update_mp_map()
    itchat.run()
    itchat.dump_login_status()


if __name__ == "__main__":
    main()
