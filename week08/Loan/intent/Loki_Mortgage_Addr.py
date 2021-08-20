#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Mortgage_Addr

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Mortgage_Addr = True
userDefinedDICT = {"JOB": ["工程師", "工人", "建築師", "律師", "法官"], "LOAN": ["信用貸款", "房貸", "車貸", "信貸"], "SCHOOL": ["台灣大學", "國立台灣大學"], "EDUCATION": ["phD", "博士", "博士候選", "學士", "碩士", "大學", "大專", "高中", "國中", "國小", "五專", "二技"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Mortgage_Addr:
        print("[Mortgage_Addr] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    if "mortgage" not in resultDICT:
        resultDICT["mortgage"] = {}

    if utterance == "[台北市信義區有錢路一段10號]":
        resultDICT["mortgage"]["address"] = args[0]
        pass

    return resultDICT