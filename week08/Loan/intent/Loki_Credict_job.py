#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Credict_job

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Credict_job = True
userDefinedDICT = {"JOB": ["工程師", "工人", "建築師", "律師", "法官"], "LOAN": ["信用貸款", "房貸", "車貸", "信貸"], "SCHOOL": ["台灣大學", "國立台灣大學"], "EDUCATION": ["phD", "博士", "博士候選", "學士", "碩士", "大學", "大專", "高中", "國中", "國小", "五專", "二技"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Credict_job:
        print("[Credict_job] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    if "credit" not in resultDICT:
        resultDICT["credit"] = {}

    if utterance == "[我]是[一位][會計師]":
        resultDICT["credit"]["job"] = args[2]
        pass

    if utterance == "[軟體]工程師":
        resultDICT["credit"]["job"] = args[0]+"工程師"
        pass

    if utterance == "[餐廳]的負責人":
        resultDICT["credit"]["job"] = args[0]+"負責人"
        pass

    return resultDICT