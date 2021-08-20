#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Education

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Education = True
userDefinedDICT = {"JOB": ["工程師", "工人", "建築師", "律師", "法官"], "LOAN": ["信用貸款", "房貸", "車貸", "信貸"], "SCHOOL": ["台灣大學", "國立台灣大學"], "EDUCATION": ["phD", "博士", "博士候選", "學士", "碩士", "大學", "大專", "高中", "國中", "國小", "五專", "二技"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Education:
        print("[Education] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    if "credit" not in resultDICT:
        resultDICT["credit"] = {}

    if utterance == "[台灣大學][碩士]":
        if args[1] in userDefinedDICT["EDUCATION"]:
            resultDICT["credit"]["education"] = args[1]
        pass

    if utterance == "[大學]畢業":
        if args[0] in userDefinedDICT["EDUCATION"]:
            resultDICT["credit"]["education"] = args[0]
        pass

    if utterance == "[碩士]畢業於[台灣大學]":
        if args[0] in userDefinedDICT["EDUCATION"]:
            resultDICT["credit"]["education"] = args[0]
        pass

    if utterance == "畢業於[台灣大學]":    # Need more information
        resultDICT["msg"] = "請問您取得學位是？"
        pass

    if utterance == "畢業於[台灣大學][碩士]":
        if args[1] in userDefinedDICT["EDUCATION"]:
            resultDICT["credit"]["education"] = args[1]
        pass

    return resultDICT