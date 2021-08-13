#!/usr/bin/env python
# -*- coding:utf-8 -*-

import discord
import json

with open("account.info", encoding="utf-8") as f:
    accountDICT = json.loads(f.read())

class BotClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

if __name__ == "__main__":
    client = BotClient()
    client.run(accountDICT["discord_token"])