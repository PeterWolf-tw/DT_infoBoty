#!/usr/bin/env python
# -*- coding:utf-8 -*-

import discord
import json

from ArticutAPI import Articut
articut = Articut(username="loveyoosic4ever@gmail.com", apikey="=Zs6wI!L_KRO&_Ff3H5VQx3Fx145A%v")

from ChingShin_Drink import runLoki

with open("account.info", encoding="utf-8") as f:
    accountDICT = json.loads(f.read())

class BotClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {} with id {}'.format(self.user, self.user.id))

    async def on_message(self, message):
        # Don't respond to bot itself. Or it would create a non-stop loop.
        # 如果訊息來自 bot 自己，就不要處理，直接回覆 None。不然會 Bot 會自問自答個不停。
        if message.author == self.user:
            return None

        print("收到來自 {} 的訊息".format(message.author))
        print("訊息內容是 {}。".format(message.content))
        if self.user.mentioned_in(message):
            print("本 bot 被叫到了！")
            msg = message.content.replace("<@!{}> ".format(self.user.id), "")
            if msg == 'ping':
                await message.reply('pong')
            elif msg == 'ping ping':
                await message.reply('pong pong')
            else:
                #從這裡開始接上 NLU 模型
                responseSTR = "我是預設的回應字串…你會看到我這串字，肯定是出了什麼錯！"

                inputLIST = [msg]
                filterLIST = []
                resultDICT = runLoki(inputLIST, filterLIST)
                print("Result => {}".format(resultDICT))

                for amt in range(0,len(resultDICT["amount"])):
                    articutDICT = articut.parse(resultDICT["amount"][amt], level="lv3")
                    amount = articutDICT["number"][resultDICT["amount"][amt]]
                    resultDICT["amount"] = amount

                if "sugar" not in resultDICT:
                    resultDICT["sugar"] = "預設正常甜"

                if "ice" in resultDICT and "temperature" in resultDICT:
                    responseSTR = "hello \n您點的總共是：{} X {} ({}) \n 不好意思，沒有辦法做又冰又熱，請重新選擇溫度或冰塊".format(resultDICT["item"], resultDICT["amount"], resultDICT["sugar"])

                if "ice" not in resultDICT and "temperature" not in resultDICT:
                    resultDICT["ice"] = "預設正常冰"

                if "ice" in resultDICT and "temperature" not in resultDICT:
                    responseSTR = "hello~ \n您點的總共是：\n"
                    for k in range(0,len(resultDICT["amount"])):
                        responseSTR = responseSTR + "{} X {} ({}、{})\n".format(resultDICT["item"][k],resultDICT["amount"][k],resultDICT["sugar"],resultDICT["ice"])
                    responseSTR = responseSTR + "謝謝您的訂購\n"

                if "temperature" in resultDICT and "ice" not in resultDICT:
                    responseSTR = "hello~~ \n您點的總共是：\n"
                    for k in range(0,len(resultDICT["amount"])):
                        responseSTR = responseSTR + "{} X {} ({}、{})\n".format(resultDICT["item"][k],resultDICT["amount"][k],resultDICT["sugar"],resultDICT["temperature"][0])
                    responseSTR = responseSTR + "謝謝您的訂購\n"

                await message.reply(responseSTR)


if __name__ == "__main__":
    client = BotClient()
    client.run(accountDICT["discord_token"])