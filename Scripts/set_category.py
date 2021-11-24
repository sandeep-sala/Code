from EasyChatApp.models import *
import xlrd ,json


def identify_intent(name):
    user    = Profile.objects.all().last()
    bot_obj = Bot.objects.get(pk=1)
    channel = Channel.objects.get(name="Web")
    tree, status_re_sentence, suggestion_list = return_next_tree(
        user, bot_obj, name, channel, 'None')
    if tree:
        try:
            intent_pk = Intent.objects.get(tree=tree).pk
            intent_name = Intent.objects.get(tree=tree).name
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


pk_list = [182,
 183,
 184,
 185,
 186,
 187,
 188,
 189,
 190,
 191,
 192,
 193,
 194,
 195,
 196,
 197,
 198,
 199,
 200,
 201,
 202,
 203,
 204,
 205,
 206,
 207,
 208,
 209,
 210,
 211,
 212,
 213,
 214,
 215,
 216,
 217,
 218,
 219,
 220,
 221,
 222,
 223,
 224,
 225,
 226,
 227,
 228,
 229,
 230,
 231,
 232,
 233,
 234,
 235,
 236,
 237,
 238,
 239,
 240,
 241,
 242,
 243,
 244,
 245,
 246,
 247,
 248,
 249,
 250]



Intent_List = Intent.objects.filter(bots=Bot.objects.get(pk=2),is_deleted=False)
hr_cat = Category.objects.get(pk=19)
kyc_cat = Category.objects.get(pk=18)

for intent in Intent_List:
	if intent.pk in pk_list:
		intent.category = kyc_cat
	else:
		intent.category = hr_cat
	intent.save()


loc   = ("KYC Related.xlsx") 
wb    = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)

row = sheet.nrows
col = sheet.ncols
for i in range(1,row):
    question = sheet.cell_value(i,0)
    intent_pk = identify_intent(question)
    print(intent_pk) 
    