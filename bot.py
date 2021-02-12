from rivescript import RiveScript
import os.path

file = os.path.dirname(__file__)
mind = os.path.file(file, 'brain')

bot = RiveScript()
bot.load_directory(mind)
bot.sort_replies()

while True:
  msg = str(input('You> '))
  
  if msg == 'q':
    break
    
  else:
    print('Bot>'+bot.reply('localuser', msg))
