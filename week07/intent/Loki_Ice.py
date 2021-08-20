#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Ice

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Ice = True
userDefinedDICT = {"糖": ["果糖"], "全糖": ["正常糖", "超甜", "正常"], "冰塊": ["冰"], "半糖": ["五分糖", "五分甜"], "去冰": ["小碎冰", "碎冰"], "少冰": ["少一點冰"], "少糖": ["八分糖", "八分甜"], "常溫": ["不冰", "室溫"], "微冰": ["一點冰", "微微"], "微糖": ["兩分糖", "兩分甜", "微甜", "微微"], "溫飲": ["溫溫", "溫熱", "暖暖", "不要太熱", "溫的", "溫"], "無糖": ["0分糖", "不要糖", "不要甜", "去糖", "不加糖", "不要加糖"], "熱飲": ["熱的", "燒的", "有點燙", "熱一點", "熱"], "正常冰": ["全冰"], "原鄉四季": ["原鄉", "四季", "四季茶", "原鄉茶", "原四", "原季", "鄉季"], "極品菁茶": ["極品菁", "極菁", "品菁", "極品茶", "菁茶", "極品"], "烏龍綠茶": ["烏龍綠", "烏綠", "烏綠茶"], "特級綠茶": ["特級綠", "特綠"], "特選普洱": ["特選普", "普洱", "普洱茶", "特普", "特普洱", "特選普洱茶"], "翡翠烏龍": ["翡翠", "翡翠烏", "斐烏", "翠烏"], "錫蘭紅茶": ["錫蘭", "錫蘭紅", "錫紅", "錫蘭茶", "紅茶"], "嚴選高山茶": ["嚴選高山", "嚴高", "高山茶"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Ice:
        print("[Ice] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["ice"] = []
    
    if utterance == "不加冰":
        resultDICT["ice"].append("去冰") 
        

    if utterance == "不加冰塊":
        resultDICT["ice"].append("去冰")
        

    if utterance == "不要冰":
        resultDICT["ice"].append("去冰")
        

    if utterance == "不要冰塊":
        resultDICT["ice"].append("去冰")
        

    if utterance == "全冰":
        resultDICT["ice"].append("正常冰")
        

    if utterance == "冰塊少[一點]":
        resultDICT["ice"].append("少冰")
        

    if utterance == "去冰":
        resultDICT["ice"].append("去冰")
        

    if utterance == "小碎冰":
        resultDICT["ice"].append("微冰")
        

    if utterance == "少一點冰":
        resultDICT["ice"].append("少冰")
        

    if utterance == "少冰":
        resultDICT["ice"].append("少冰")
        

    if utterance == "微冰":
        resultDICT["ice"].append("微冰")
        

    if utterance == "微微":
        resultDICT["ice"].append("微冰")
        

    if utterance == "正常冰":
        resultDICT["ice"].append("正常冰")
        

    if utterance == "碎冰":
        resultDICT["ice"].append("微冰")
        
    
    if utterance == "甜度冰塊正常":
        resultDICT["ice"].append("正常冰")
        
    
    if utterance == "糖和冰塊[都]正常":
        resultDICT["ice"].append("正常冰")
        
    
    if utterance == "不要加冰塊":
        resultDICT["ice"].append("去冰")
            
    
    if utterance == "不要加糖跟冰塊":
        resultDICT["ice"].append("去冰")
            
    
    if utterance == "不要糖跟冰塊":
        resultDICT["ice"].append("去冰")
              
        
    if utterance == "冰塊正常":
        resultDICT["ice"].append("正常冰")
        

    return resultDICT