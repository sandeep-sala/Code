from EasyChatApp.models import AuditTrail,Intent,User,Category
from EasyChatApp.utils import *
import json

shrikant   = User.objects.get(pk=4)
date_range = ["2020-10-01", "2020-10-08"]

Audit_list = AuditTrail.objects.filter(user=shrikant,datetime__range=date_range,action="3").order_by("datetime")


def identify_intent(name):
    user    = Profile.objects.all().last()
    bot_obj = Bot.objects.get(pk=1)
    channel = Channel.objects.get(name="Web")
    tree, status_re_sentence, suggestion_list = return_next_tree(
        user, bot_obj, name, channel, 'None')
    if tree:
        try:
            intent_pk = Intent.objects.get(tree=tree).pk
            return intent_pk
        except:
            try:
                tree, status_re_sentence, suggestion_list = return_next_tree(
                    user, bot_obj, suggestion_list[0], channel, 'None')
                if tree is not None:
                    intent_pk = Intent.objects.get(tree=tree).pk
                    return intent_pk
            except:
                pass



pk_list = {
 833: 1039,
 919: 1125,
 803: 1009,
 967: 1186,
 840: 1046,
 974: 1154,
 651: 1156,
 981: 1183,
 977: 1157,
 973: 1153,
 817: 1023,
 694: 1150,
 982: 1184,
 970: 1150,
 727: 1059,
 966: 1181,
 862: 1068,
 686: 1171,
 980: 1182,
 965: 1180,
 725: 1057,
 865: 1071,
 781: 1047,
 737: 1069,
 728: 1060,
 984: 1086,
 732: 1064,
 684: 1063,
 796: 1002}




pk_list = {587: 1154,
 931: 1137,
 906: 1112,
 894: 1100,
 889: 1095,
 885: 1090,
 654: 1174,
 743: 1075,
 850: 1056,
 653: 1157,
 861: 1067,
 671: 1080,
 684: 1063,
 694: 1150,
 748: 1080,
 651: 1156,
 822: 1028,
 890: 1096,
 666: 1175,
 665: 1175,
 825: 1031,
 933: 1139,
 872: 1078,
 794: 1000,
 784: 1079,
 913: 1119,
 676: 1153,
 880: 1084,
 942: 1017,
 793: 999,
 680: 1173,
 708: 1186,
 714: 1151,
 817: 1023,
 710: 1148,
 711: 1149,
 960: 1175,
 953: 1168,
 962: 1177,
 831: 1037,
 828: 1034,
 824: 1030,
 781: 1047,
 978: 1178,
 980: 1182,
 979: 1185,
 843: 1049,
 833: 1039,
 919: 1125,
 803: 1009,
 967: 1186,
 840: 1046,
 974: 1154,
 981: 1183,
 977: 1157,
 973: 1153,
 982: 1184,
 970: 1080,
 727: 1059,
 966: 1181,
 862: 1157,
 686: 1171,
 965: 1180,
 725: 1057,
 865: 1071,
 737: 1069,
 728: 1060,
 984: 1086,
 732: 1064,
 697: 1150,
 796: 1002}






for audit in Audit_list:
    DATA = json.loads(audit.data)
    data_list = DATA['change_data']
    pk        = DATA['intent_pk']
    if pk in [675,652,707,664,990]: continue
    for data in data_list:
        print(pk_list[pk])
        intent_obj = Intent.objects.get(pk= pk_list[pk])
        if data["heading"] == "Training questions":
            intent_obj.training_data = json.dumps(data["new_data"])
            print(intent_obj.training_data)
        if data["heading"] in ["Category changed","Category Added"]:
            print(data["new_data"])
            category = Category.objects.filter(name=data["new_data"])
            if category:
                intent_obj.category = category[0]
            print(intent_obj.category)
        intent_obj.save()
        
            
















for audit in Audit_list:
    DATA = json.loads(audit.data)
    data_list = DATA['change_data']
    pk        = DATA['intent_pk']
    if pk in [990,697]: continue
    for data in data_list:
        if data["heading"] == "Training questions":
            identified_intent = identify_intent(data["old_data"]["0"])
            if not identified_intent:
                print("Intent Failed to Identify")
                print(audit.pk)
                print(data["old_data"])
            Old_Intent[pk] = identified_intent
            
            # print(data["old_data"])
            #print(data["new_data"])
        if data["heading"] in ["Category changed","Category Added"]:
            pass
            #print(data["old_data"])
            #print(data["new_data"])
        # print("  END ".center(40, '$'))
















"""
990---

2519
{'0': 'Goodbye', '1': 'Thank you', '2': 'TY', '3': 'Thanks', '4': 'Bye'}



697----

2535
{'0': 'Is it possible to deposit cash', '1': 'I want to deposit cash can it be done', '2': 'How can I deposit cash', '3': 'Can I deposit cash ?'}











{'0': 'How Full KYC is important', '1': 'Why Full KYC is important', '2': 'Necessity of Full KYC', '3': 'Why Full KYC is necessay', '4': 'Why Full KYC is given priority', '5': 'Why is Full KYC necessary?'}

----

{'0': 'see my account balance', '1': 'Help me where can I see my account balance', '2': 'Can you tell where can I see my account balance', '3': 'Guide from where can i see my account balance', '4': 'Explain from where can I see my account balance', '5': 'Where can see my account balance?'}

----

{'0': 'Steps to make online payments through my Kotak 811 Account', '1': 'Process to make online payments through my Kotak 811 Account', '2': 'Guide me on how to make online payments through my Kotak 811 Account', '3': 'I want to make online payments through my Kotak 811 Account please help', '4': 'How can I make online payments through my Kotak 811 Account'}

----

{'0': 'Apply for Debit Card', '1': 'Help me to Apply for Debit Card', '2': 'Can you tell how to Apply for Debit Card', '3': 'guide me to Apply for Debit Card', '4': 'Explain how to Apply for Debit Card', '5': 'How to Apply for Debit Card?'}

----

{'0': 'Goodbye', '1': 'Thank you', '2': 'TY', '3': 'Thanks', '4': 'Bye'}










"""