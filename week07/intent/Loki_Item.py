#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Item

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Item = True
userDefinedDICT = {"糖": ["果糖"], "全糖": ["正常糖", "超甜", "正常"], "冰塊": ["冰"], "半糖": ["五分糖", "五分甜"], "去冰": ["小碎冰", "碎冰"], "少冰": ["少一點冰"], "少糖": ["八分糖", "八分甜"], "常溫": ["不冰", "室溫"], "微冰": ["一點冰", "微微"], "微糖": ["兩分糖", "兩分甜", "微甜", "微微"], "溫飲": ["溫溫", "溫熱", "暖暖", "不要太熱", "溫的", "溫"], "無糖": ["0分糖", "不要糖", "不要甜", "去糖", "不加糖", "不要加糖"], "熱飲": ["熱的", "燒的", "有點燙", "熱一點", "熱"], "正常冰": ["全冰"], "原鄉四季": ["原鄉", "四季", "四季茶", "原鄉茶", "原四", "原季", "鄉季"], "極品菁茶": ["極品菁", "極菁", "品菁", "極品茶", "菁茶", "極品"], "烏龍綠茶": ["烏龍綠", "烏綠", "烏綠茶"], "特級綠茶": ["特級綠", "特綠"], "特選普洱": ["特選普", "普洱", "普洱茶", "特普", "特普洱", "特選普洱茶"], "翡翠烏龍": ["翡翠", "翡翠烏", "斐烏", "翠烏"], "錫蘭紅茶": ["錫蘭", "錫蘭紅", "錫紅", "錫蘭茶", "紅茶"], "嚴選高山茶": ["嚴選高山", "嚴高", "高山茶"]}

itemLIST = ["原鄉四季","原鄉", "四季", "四季茶", "原鄉茶", "原四", "原季", "鄉季", "極品菁茶", "極品菁", "極菁", "品菁", "極品茶", "菁茶", "極品", "烏龍綠茶", "烏龍綠", "烏綠", "烏綠茶", "特級綠茶", "特級綠", "特綠", "特選普洱", "特選普", "普洱", "普洱茶", "特普", "特普洱", "特選普洱茶", "翡翠烏龍","翡翠", "翡翠烏", "斐烏", "翠烏", "錫蘭紅茶","錫蘭", "錫蘭紅", "錫紅", "錫蘭茶", "紅茶", "嚴選高山茶","嚴選高山", "嚴高", "高山茶"]

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Item:
        print("[Item] {} ===> {}".format(inputSTR, utterance))

def getItem(argsLIST):
    for a in argsLIST:
        if a in itemLIST:
            return argsLIST.index(a)

def getFullName(teaAliasSTR):
    if teaAliasSTR in userDefinedDICT.keys():
        return teaAliasSTR
    else:
        for k in userDefinedDICT.keys():
            if teaAliasSTR in userDefinedDICT[k]:
                return k

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["item"] = []
    resultDICT["amount"] = []

    if utterance == "[兩杯][熱的][錫蘭紅茶]":
        resultDICT["amount"].append(args[0])
        if args[1] in itemLIST:
            for k in userDefinedDICT.keys():
                if args[1] == k:
                    resultDICT["item"].append(k)
                elif args[1] in userDefinedDICT[k]:
                    resultDICT["item"].append(k)
                    pass
        elif args[2] in itemLIST:
            for k in userDefinedDICT.keys():
                if args[2] == k:
                    resultDICT["item"].append(k)
                elif args[2] in userDefinedDICT[k]:
                    resultDICT["item"].append(k)
                    pass


    if utterance == "[兩杯][錫蘭][微糖][去冰]":
        resultDICT["amount"].append(args[0])
        resultDICT["item"].append(getFullName(args[getItem(args)]))

    if utterance == "[錫蘭][兩杯][微糖][去冰]":
        resultDICT["amount"].append(args[1])
        resultDICT["item"].append(getFullName(args[getItem(args)]))


    if utterance == "[五杯][原鄉]":
        resultDICT["amount"].append(args[0])
        resultDICT["item"].append(getFullName(args[1]))

    if utterance == "[原鄉][兩杯]":
        resultDICT["amount"].append(args[1])
        resultDICT["item"].append(getFullName(args[0]))


    if utterance == "[一杯][錫蘭紅茶]和[烏龍綠茶]":
        for a in args[1:3]:
            if a in itemLIST:
                resultDICT["item"].append(getFullName(a))
                resultDICT["amount"].append(args[0])


    if utterance == "錫蘭":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("錫蘭紅茶")


    if utterance == "原鄉":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("原鄉四季")


    if utterance == "原鄉四季":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("原鄉四季")


    if utterance == "原鄉茶":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("原鄉四季")


    if utterance == "嚴選高山":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("嚴選高山茶")


    if utterance == "嚴選高山茶":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("嚴選高山茶")


    if utterance == "嚴高":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("嚴選高山茶")


    if utterance == "四季":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("原鄉四季")


    if utterance == "四季茶":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("原鄉四季")


    if utterance == "普洱":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("特選普洱")


    if utterance == "普洱茶":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("特選普洱")


    if utterance == "極品":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("極品菁茶")


    if utterance == "極品菁":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("極品菁茶")


    if utterance == "極品菁茶":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("極品菁茶")


    if utterance == "極菁":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("極品菁茶")


    if utterance == "烏綠":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("烏龍綠茶")


    if utterance == "烏龍綠":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("烏龍綠茶")


    if utterance == "烏龍綠茶":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("烏龍綠茶")


    if utterance == "特普":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("特選普洱")


    if utterance == "特級綠":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("特級綠茶")


    if utterance == "特級綠茶":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("特級綠茶")


    if utterance == "特綠":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("特級綠茶")


    if utterance == "特選普洱":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("特選普洱")


    if utterance == "紅茶":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("錫蘭紅茶")


    if utterance == "翡烏":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("翡翠烏龍")


    if utterance == "翡翠":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("翡翠烏龍")


    if utterance == "翡翠烏":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("翡翠烏龍")


    if utterance == "翡翠烏龍":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("翡翠烏龍")


    if utterance == "菁茶":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("極品菁茶")


    if utterance == "錫紅":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("錫蘭紅茶")


    if utterance == "錫蘭紅":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("錫蘭紅茶")


    if utterance == "錫蘭紅茶":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("錫蘭紅茶")


    if utterance == "錫蘭茶":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("錫蘭紅茶")


    if utterance == "高山茶":
        resultDICT["amount"].append("一杯")
        resultDICT["item"].append("嚴選高山茶")


    return resultDICT
