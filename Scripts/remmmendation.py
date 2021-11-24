from EasyChatApp.models import *
from EasyChatApp.utils import *
import json

# objs = BotResponse.objects.all()
user = Profile.objects.all().last()
bot_obj = Bot.objects.get(pk=1)
channel = Channel.objects.get(name="Web")



for o in p:
    kk = BotResponse.objects.get(pk=o[0])
    k = o[1]
    pk_list = []
    initial_messages_name_list = k["items"]
    if initial_messages_name_list != []:
        for name in initial_messages_name_list:
            tree, status_re_sentence, suggestion_list = return_next_tree(
                user, bot_obj, name, channel, 'None')
            if tree:
                try:
                    intent_obj = Intent.objects.get(tree=tree)
                    pk_list.append(intent_obj.pk)
                except:
                    try:
                        tree, status_re_sentence, suggestion_list = return_next_tree(
                            user, bot_obj, suggestion_list[0], channel, 'None')
                        if tree is not None:
                            intent_obj = Intent.objects.get(tree=tree)
                            pk_list.append(intent_obj.pk)
                    except:
                        pass
    k['items'] = pk_list
    kk.recommendations = json.dumps(k)
    kk.save()


objs = BotResponse.objects.all()
for obj in objs:
    if obj.table != "{\"items\":[]}":
        print(obj.pk)
        print(obj.table)
        obj.table = "{\"items\":[]}"
        obj.save()

obj = BotResponse.objects.get(pk=4835)
obj.table = p


user = Profile.objects.all().last()

for i,j in p.items():
    channel_obj = BotChannel.objects.get(pk = i)
    channel = channel_obj.channel
    k = j.copy()
    pk_list = []
    initial_messages_name_list = k["items"]
    print(initial_messages_name_list)
    if initial_messages_name_list != []:
        for name in initial_messages_name_list:
            tree, status_re_sentence,  suggestion_list = return_next_tree(user, bot_obj, name, channel,"None")
            if tree:
                try:
                    intent_obj = Intent.objects.get(tree=tree)
                    pk_list.append(intent_obj.pk)
                except:
                    try:
                        tree, status_re_sentence, suggestion_list = return_next_tree(user, bot_obj, suggestion_list[0], channel, "None")
                        if tree is not None:
                            intent_obj = Intent.objects.get(tree=tree)
                            pk_list.append(intent_obj.pk)
                    except:
                        pass
        k['items'] = pk_list
        print(pk_list)
        channel_obj.initial_messages = json.dumps(k)
        print(channel_obj.initial_messages)
        channel_obj.save()











recom = {}
objs = BotResponse.objects.all()
for obj in objs:
    r = json.loads(obj.recommendations)["items"]
    if r != [] :
        for i in r:
            try:
                recom[i] = Intent.objects.get(pk=i).name
            except: pass


recom = {}
objs = BotResponse.objects.all()
for obj in objs:
    try:
        r = json.loads(obj.recommendations)["items"]
        print(r)
        pk_list = []
        if r != [] :
            for ppk in r:
                if ppk in p:
                    tree, status_re_sentence, suggestion_list = return_next_tree(
                        user, bot_obj, p[ppk], channel, 'None')
                    if tree:
                        try:
                            intent_obj = Intent.objects.get(tree=tree)
                            pk_list.append(intent_obj.pk)
                        except:
                            try:
                                tree, status_re_sentence, suggestion_list = return_next_tree(
                                    user, bot_obj, suggestion_list[0], channel, 'None')
                                if tree is not None:
                                    intent_obj = Intent.objects.get(tree=tree)
                                    pk_list.append(intent_obj.pk)
                            except:
                                pass
        obj.recommendations = json.dumps({"items":pk_list})
        obj.save()
    except: pass
    
    
    pk_list = []
    initial_messages_name_list = k["items"]
    if initial_messages_name_list != []:
        for name in initial_messages_name_list:
            tree, status_re_sentence, suggestion_list = return_next_tree(
                user, bot_obj, name, channel, 'None')
            if tree:
                try:
                    intent_obj = Intent.objects.get(tree=tree)
                    pk_list.append(intent_obj.pk)
                except:
                    try:
                        tree, status_re_sentence, suggestion_list = return_next_tree(
                            user, bot_obj, suggestion_list[0], channel, 'None')
                        if tree is not None:
                            intent_obj = Intent.objects.get(tree=tree)
                            pk_list.append(intent_obj.pk)
                    except:
                        pass
    k['items'] = pk_list
    kk.recommendations = json.dumps(k)
    kk.save()



p =[707,
 423,
 616,
 553,
 602,
 774,
 732,
 694,
 735,
 746,
 571,
 493,
 441,
 714,
 341,
 881,
 539,
 372,
 372,
 554,
 418,
 450,
 850,
 849,
 828,
 358,
 585,
 358,
 585,
 872,
 872,
 481,
 481,
 481,
 697,
 423,
 697,
 423,
 423,
 383,
 847,
 697,
 591,
 886,
 887,
 888,
 889,
 890,
 891,
 892,
 893,
 894,
 895,
 896,
 897,
 898,
 899,
 900,
 901,
 902,
 903,
 904,
 905,
 906,
 907,
 908,
 909,
 910,
 911,
 912,
 913,
 914,
 915,
 916,
 917,
 918,
 919,
 920,
 921,
 922,
 923,
 924,
 925,
 926,
 927,
 928,
 929,
 930,
 931,
 932,
 933,
 934,
 935,
 936,
 937,
 938,
 939,
 940,
 941,
 942,
 943,
 944,
 945,
 946,
 947,
 948,
 949,
 950,
 951,
 952,
 953,
 954]