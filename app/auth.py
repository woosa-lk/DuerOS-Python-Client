# -*- coding: utf-8 -*-
'''
OAuth2.0认证
'''
import sdk.auth as auth

# 开发者注册信息
CLIENT_ID = 'Quu50aPGeAlYE4UT2UQtnwodRIfS5Djf'
CLIENT_SECRET = 'wuhuMtZ2VbKElocnuCVHw2WHsTE4QPk6'




def main():
    # 使用开发者注册信息
    auth.auth_request(CLIENT_ID, CLIENT_SECRET)

    # 使用默认的CLIENT_ID和CLIENT_SECRET
    #auth.auth_request()


if __name__ == '__main__':
    main()
