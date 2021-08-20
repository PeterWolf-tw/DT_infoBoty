#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Probe

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Probe = True
userDefinedDICT = {"JOB": ["工程師", "工人", "建築師", "律師", "法官"], "LOAN": ["信用貸款", "房貸", "車貸", "信貸"], "SCHOOL": ["台灣大學", "國立台灣大學"], "EDUCATION": ["phD", "博士", "博士候選", "學士", "碩士", "大學", "大專", "高中", "國中", "國小", "五專", "二技"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Probe:
        print("[Probe] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[我]想要辦貸款":
        resultDICT["msg"] = "你想辦哪種貸款？ (信用貸款、房屋貸款...)"
        pass

    if utterance == "有沒[有]什麼[房貸]的方案":
        if "房" in args[1]:
            resultDICT["msg"] = "有的，[房屋貸款]需要請您提供您的房屋相關資訊。"
            resultDICT["loan_type"] = "mortgage"
        else:
            resultDICT["msg"] = "有的，[個人信用貸款]需要請您提供您的個人資訊。"
            resultDICT["loan_type"] = "credit"
        pass

    if utterance == "申請[房屋]貸款需要準備哪些[資料]":
        if "房" in args[0]:
            resultDICT["msg"] = "需要請您提供您的房屋類型、屋齡、坪數、地址。"
            resultDICT["loan_type"] = "mortgage"
        else:
            resultDICT["msg"] = "需要請您提供您的教育程度、年收入、工作職位、工作年資。"
            resultDICT["loan_type"] = "credit"
        pass

    if utterance == "辦理[房屋]貸款":
        if "房" in args[0]:
            resultDICT["msg"] = "需要請您提供您的房屋類型、屋齡、坪數、地址。"
            resultDICT["loan_type"] = "mortgage"
        else:
            resultDICT["msg"] = "需要請您提供您的教育程度、年收入、工作職位、工作年資。"
            resultDICT["loan_type"] = "credit"
        pass

    if utterance == "辦理[房貸]":
        if "房" in args[0]:
            resultDICT["msg"] = "需要請您提供您的房屋類型、屋齡、坪數、地址。"
            resultDICT["loan_type"] = "mortgage"
        else:
            resultDICT["msg"] = "需要請您提供您的教育程度、年收入、工作職位、工作年資。"
            resultDICT["loan_type"] = "credit"
        pass

    if utterance == "需要準備哪些[資料]":
        resultDICT["msg"] = "[信用貸款]需要請您提供您的教育程度、年收入、工作職位、工作年資。\n[房屋貸款]需要請您提供您的房屋類型、屋齡、坪數、地址。"
        pass

    if utterance == "是":
        if len(inputSTR) < 2:
            resultDICT["confirm"] = True
        pass

    if utterance == "不是":
        if len(inputSTR) < 3:
            resultDICT["confirm"] = False
        pass

    if utterance == "對":
        if len(inputSTR) < 3:
            if "不" in args[0]:
                resultDICT["confirm"] = False
            else:
                resultDICT["confirm"] = True
            pass

    return resultDICT