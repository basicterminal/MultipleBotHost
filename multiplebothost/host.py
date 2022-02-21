import discord, random, asyncio
from discord.ext import commands

class multiplebothost:
      loop = asyncio.get_event_loop()
    
      def AddClient(token = ""): 
          ## Client Setup ##
          bot = commands.Bot(self_bot = True, command_prefix = "..")
          bot.remove_command('help')
          
          ## Magic Starts Here ##
          print('[!] Hosted %s...' % (token[:10]))
          multiplebothost.loop.create_task(bot.start(token))
        
      def Start():
          ## Multiple Bot Host ##
          multiplebothost.loop.run_forever()
