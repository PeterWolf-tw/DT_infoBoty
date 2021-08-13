#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 2.0 Template For Python3

    [URL] https://api.droidtown.co/Loki/BulkAPI/

    Request:
        {
            "username": "your_username",
            "input_list": ["your_input_1", "your_input_2"],
            "loki_key": "your_loki_key",
            "filter_list": ["intent_filter_list"] # optional
        }

    Response:
        {
            "status": True,
            "msg": "Success!",
            "version": "v223",
            "word_count_balance": 2000,
            "result_list": [
                {
                    "status": True,
                    "msg": "Success!",
                    "results": [
                        {
                            "intent": "intentName",
                            "pattern": "matchPattern",
                            "utterance": "matchUtterance",
                            "argument": ["arg1", "arg2", ... "argN"]
                        },
                        ...
                    ]
                },
                {
                    "status": False,
                    "msg": "No Match Intent!"
                }
            ]
        }
"""

from requests import post
from requests import codes

import math
try:
    from intent import Loki_temperature
    from intent import Loki_Ice
    from intent import Loki_Item
    from intent import Loki_Sugar
except:
    from .intent import Loki_temperature
    from .intent import Loki_Ice
    from .intent import Loki_Item
    from .intent import Loki_Sugar


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
USERNAME = "loveyoosic4ever@gmail.com"
LOKI_KEY = "bIL69%69lGmvcunvYfU*pQJZ#sI335j"
# 意圖過濾器說明
# INTENT_FILTER = []        => 比對全部的意圖 (預設)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖
INTENT_FILTER = []

class LokiResult():
    status = False
    message = ""
    version = ""
    balance = -1
    lokiResultLIST = []

    def __init__(self, inputLIST, filterLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.balance = -1
        self.lokiResultLIST = []
        # filterLIST 空的就採用預設的 INTENT_FILTER
        if filterLIST == []:
            filterLIST = INTENT_FILTER

        try:
            result = post(LOKI_URL, json={
                "username": USERNAME,
                "input_list": inputLIST,
                "loki_key": LOKI_KEY,
                "filter_list": filterLIST
            })

            if result.status_code == codes.ok:
                result = result.json()
                self.status = result["status"]
                self.message = result["msg"]
                if result["status"]:
                    self.version = result["version"]
                    self.balance = result["word_count_balance"]
                    self.lokiResultLIST = result["result_list"]
            else:
                self.message = "Connect failed."
        except Exception as e:
            self.message = str(e)

    def getStatus(self):
        return self.status

    def getMessage(self):
        return self.message

    def getVersion(self):
        return self.version

    def getBalance(self):
        return self.balance

    def getLokiStatus(self, index):
        rst = False
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["status"]
        return rst

    def getLokiMessage(self, index):
        rst = ""
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["msg"]
        return rst

    def getLokiLen(self, index):
        rst = 0
        if index < len(self.lokiResultLIST):
            if self.lokiResultLIST[index]["status"]:
                rst = len(self.lokiResultLIST[index]["results"])
        return rst

    def getLokiResult(self, index, resultIndex):
        lokiResultDICT = None
        if resultIndex < self.getLokiLen(index):
            lokiResultDICT = self.lokiResultLIST[index]["results"][resultIndex]
        return lokiResultDICT

    def getIntent(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["intent"]
        return rst

    def getPattern(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["pattern"]
        return rst

    def getUtterance(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["utterance"]
        return rst

    def getArgs(self, index, resultIndex):
        rst = []
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["argument"]
        return rst

def runLoki(inputLIST, filterLIST=[]):
    resultDICT = {}
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # temperature
                if lokiRst.getIntent(index, resultIndex) == "temperature":
                    resultDICT = Loki_temperature.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # Ice
                if lokiRst.getIntent(index, resultIndex) == "Ice":
                    resultDICT = Loki_Ice.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # Item
                if lokiRst.getIntent(index, resultIndex) == "Item":
                    resultDICT = Loki_Item.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # Sugar
                if lokiRst.getIntent(index, resultIndex) == "Sugar":
                    resultDICT = Loki_Sugar.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)


if __name__ == "__main__":
    # temperature
    #print("[TEST] temperature")
    #inputLIST = ['溫','熱','室溫','常溫','溫的','溫飲','熱的','熱飲','溫溫的']
    #testLoki(inputLIST, ['temperature'])
    #print("")

    # Ice
    #print("[TEST] Ice")
    #inputLIST = ['全冰','去冰','少冰','微冰','微微','正常','碎冰','不加冰','不要冰','小碎冰','正常冰','不要冰塊','少一點冰','不要加冰塊','冰塊少一點','不要糖跟冰塊','甜度冰塊正常','不要加糖跟冰塊','糖和冰塊都正常']
    #testLoki(inputLIST, ['Ice'])
    #print("")

    # Item
    #print("[TEST] Item")
    #inputLIST = ['原鄉','嚴高','四季','普洱','極品','極菁','烏綠','特普','特綠','紅茶','翡烏','翡翠','菁茶','錫紅','錫蘭','原香茶','四季茶','普洱茶','極品菁','烏龍綠','特級綠','翡翠烏','錫蘭紅','錫蘭茶','高山茶','五杯原鄉','原鄉兩杯','原鄉四季','嚴選高山','極品菁茶','烏龍綠茶','特級綠茶','特選普洱','翡翠烏龍','錫蘭紅茶','嚴選高山茶','兩杯熱的錫蘭紅茶','錫蘭紅跟烏龍綠各一杯','一杯錫蘭紅茶和烏龍綠茶','三杯烏龍綠跟五杯錫蘭紅','烏龍綠三杯跟錫蘭紅五杯','嚴選高山、特級綠跟四季茶各三杯']
    #testLoki(inputLIST, ['Item'])
    #print("")

    # Sugar
    #print("[TEST] Sugar")
    #inputLIST = ['全糖','半糖','少糖','微微','微甜','微糖','正常','無糖','不加糖','不要甜','不要糖','五分甜','五分糖','兩分甜','兩分糖','八分甜','八分糖','正常糖','不要加糖','甜度正常','甜度冰塊正常','不要加糖跟冰塊','糖和冰塊都正常']
    #testLoki(inputLIST, ['Sugar'])
    #print("")



    # 輸入其它句子試看看
    inputLIST = ["一杯熱錫蘭紅茶"]
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    print("Result => {}".format(resultDICT))

    from ArticutAPI import Articut
    articut = Articut(username="loveyoosic4ever@gmail.com", apikey="=Zs6wI!L_KRO&_Ff3H5VQx3Fx145A%v")

    #for amt in range(0,len(resultDICT["amount"])):
        #articutDICT = articut.parse(resultDICT["amount"][amt], level="lv3")
        #amount = articutDICT["number"][resultDICT["amount"][amt]]
        #resultDICT["amount"] = amount


    if "sugar" not in resultDICT:
        resultDICT["sugar"] = "預設正常甜"

    if "ice" in resultDICT and "temperature" in resultDICT:
        print("hello")
        print("您點的總共是：")
        print(resultDICT["item"],"X",resultDICT["amount"],"(",resultDICT["sugar"],")")
        print("不好意思，沒有辦法做又冰又熱，請重新選擇溫度或冰塊")

    if "ice" not in resultDICT and "temperature" not in resultDICT:
        resultDICT["ice"] = "預設正常冰"

    if "ice" in resultDICT and "temperature" not in resultDICT:
        print("hello~")
        print("您點的總共是：")
        for k in range(0,len(resultDICT["amount"])):
            print(resultDICT["item"][k],"X",resultDICT["amount"][k],"(",resultDICT["sugar"],"、",resultDICT["ice"],")")
        print("謝謝您的訂購")

    if "temperature" in resultDICT and "ice" not in resultDICT:
        print("hello~~")
        print("您點的總共是：")
        for k in range(0,len(resultDICT["amount"])):
            print(resultDICT["item"],"X",resultDICT["amount"],"(",resultDICT["sugar"],"、",resultDICT["temperature"][0],")")
        print("謝謝您的訂購")


