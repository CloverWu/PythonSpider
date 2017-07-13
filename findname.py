# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 17:29:20 2017

@author: xiaobin_wu
"""
#dsa
def find_person(dict_users, strU):
    if strU in dict_users:
        return dict_users.get(strU)
    else:
        return 'Not Found'

