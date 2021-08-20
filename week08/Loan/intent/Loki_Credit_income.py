#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Credit_income

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Credit_income = True
userDefinedDICT = {"JOB": ["工程師", "工人", "建築師", "律師", "法官"], "LOAN": ["信用貸款", "房貸", "車貸", "信貸"], "SCHOOL": ["台灣大學", "國立台灣大學"], "EDUCATION": ["phD", "博士", "博士候選", "學士", "碩士", "大學", "大專", "高中", "國中", "國小", "五專", "二技"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Credit_income:
        print("[Credit_income] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    if "credit" not in resultDICT:
        resultDICT["credit"] = {}

    if utterance == "[100萬]":
        resultDICT["credit"]["annual_income"] = args[0]
        pass

    if utterance == "[去年]有[100萬]":
        resultDICT["credit"]["annual_income"] = args[1]
        pass

    if utterance == "[年]收[100萬]":
        resultDICT["credit"]["annual_income"] = args[1]
        pass

    if utterance == "[新台幣][100萬]":
        resultDICT["credit"]["annual_income"] = args[1]
        pass

    if utterance == "[新台幣][100萬元]":
        resultDICT["credit"]["annual_income"] = args[1]
        pass

    if utterance == "年收入[100萬]":
        resultDICT["credit"]["annual_income"] = args[0]
        pass

    return resultDICT