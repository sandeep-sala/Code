from EasyChatApp.models import *
from EasyChatApp.utils import *
import json

old_bot =  Bot.objects.get(pk=2)
old_bot.pk = 276
old_bot.save()


old_bot =  Bot.objects.get(pk=2)
new_bot =  Bot.objects.get(pk=276)


x = NPS.objects.filter(bot=old_bot)
for i in x:
    i.bot = new_bot 
    i.save()

x = WordMapper.objects.filter(bots__in=[old_bot])
for i in x:
    i.bots.add(new_bot) 
    i.save()


x = Intent.objects.filter(bots__in=[new_bot])
for i in x:
    i.bots.set([new_bot]) 
    i.save()

x = MISDashboard.objects.filter(bot=old_bot)
for i in x:
    i.bot = new_bot 
    i.save()


x = TimeSpentByUser.objects.filter(bot=old_bot)
for i in x:
    i.bot = new_bot 
    i.save()


x = Category.objects.filter(bot=old_bot)
for i in x:
    i.bot = new_bot 
    i.save()


x = Category.objects.filter(bot=old_bot)
for i in x:
    i.bot = new_bot 
    i.save()


