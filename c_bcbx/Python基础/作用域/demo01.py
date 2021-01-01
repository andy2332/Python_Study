# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/6 16:31


# global
def fun(**kv):
    """全局变量"""
    global new_kv
    new_kv = kv
    return kv


kv = fun(name='cai', age=21)
print(kv)
print(new_kv)

help(fun)
