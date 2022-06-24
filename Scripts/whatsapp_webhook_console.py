from EasyChatApp.utils import *
from EasyChatApp.models import *
from LiveChatApp.models import *
from CampaignApp.models import CampaignAnalytics, CampaignAudienceLog
from EasyChatApp.utils_bot import process_response_based_on_language
from LiveChatApp.utils import *
from django.conf import settings
import emoji
import time
import json
import sys
import copy
import requests
import http.client
import mimetypes
import datetime
import hashlib
from bs4 import BeautifulSoup
from django.utils import timezone as tz

log_param={'AppName': 'EasyChat', 'user_id': 'None', 'source': 'None', 'channel': 'WhatsApp', 'bot_id': 'None'}

# ========================== TEXT FORMATTING FUNCTIONS =========================
def convert_timestamp_to_normal(timestamp):
    from datetime import datetime
    dt_object = datetime.fromtimestamp(timestamp)
    return dt_object


def youtube_link_formatter(message):
    if "https://www.youtube.com" in message:
        message =  message.replace("embed/","").replace("www.youtube.com","youtu.be")
    return message

def html_list_formatter(sent):
    try:
        logger.info("---Html list string found---", extra=log_param)
        list_strings = []
        ul_end_position = 0
        ol_end_position = 0
        if "<ul>" in sent:
            for i in range(sent.count("<ul>")): 
                list_strings_dict = {}
                ul_position = sent.find("<ul>", ul_end_position)
                ul_end_position  = sent.find("</ul>", ul_position)
                list_str = sent[ul_position:ul_end_position+5]
                logger.info("HTML LIST STRING %s : %s", str(i+1), str(list_str), extra=log_param)
                list_str1 = list_str.replace("<ul>","").replace("</ul>","").replace("<li>","")
                items = list_str1.split("</li>")
                items[-2] = items[-2]+"<br><br>"
                formatted_list_str = ""
                for item in items:
                    if item.strip()!= "":
                        formatted_list_str += "\n\n- "+item.strip()+"\n" 
                sent = sent.replace(list_str,formatted_list_str).replace("<br>","\n")+"\n"
                sent = sent.strip()
                logger.info("---Html list string formatted---", extra=log_param)
        if "<ol>" in sent:
            # print("yes ol")
            for i in range(sent.count("<ol>")): 
                list_strings_dict = {}
                ol_position = sent.find("<ol>", ol_end_position)
                ol_end_position  = sent.find("</ol>", ol_position)
                list_str = sent[ol_position:ol_end_position+5]
                logger.info("HTML LIST STRING %s : %s", str(i+1), str(list_str), extra=log_param)
                list_str1 = list_str.replace("<li>","").replace("<ol>","").replace("</ol>","")
                items = list_str1.split("</li>")
                items[-2] = items[-2]+"<br><br>"
                formatted_list_str = ""
                for j,item in enumerate(items[:-1]):
                    if item.strip()!= "":
                        formatted_list_str += "\n"+str(j+1)+". "+item.strip()
                sent = sent.replace(list_str,formatted_list_str)
                sent = sent.strip().replace("<br>","\n")
                logger.info("---Html list string formatted---", extra=log_param)            
    except Exception as E:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("Failed to format html list string: %s at %s", str(E), str(exc_tb.tb_lineno), extra=log_param)
        # print("Failed to format html list string: %s", str(E))
    return sent

def html_tags_formatter(message):
    tags = {
        "<br>":"\n", "<br/>":"\n", "<br />":"\n",
        "<b>":"*", "</b>":"*",
        "<em>":" _", "</em>":"_ ",
        "<i>":" _", "</i>":"_ ", 
        "<strong> ":" *", " </strong>":"* ", "<strong>":" *", "</strong>":"* ", 
        "<p>":"","</p>":"",
        "<div>": "", "</div>": "",
        "<u>": "", "</u>":"",
    }
    for tag in tags:
        message = message.replace(tag+"<a", "<a")
        message = message.replace("</a>"+tag, "</a>")
        message = message.replace("</a>\n"+tag, "</a>")
        message = message.replace(tag, tags[tag])
        
    if "</a>" in message:
        end = " \n"
        if "tel:" in message or "mailto:" in message:
            end = ""
        message = message.replace("mailto:","").replace("tel:","")
        soup = BeautifulSoup(message, "html.parser")
        for link in soup.findAll('a'):
            href = link.get('href')
            link_name = link.string
            link_element = message[message.find("<a"):message.find("</a>")]+"</a>"
            if link_name.replace("http://","").replace("https://","").strip() == href.replace("http://","").replace("https://","").strip():
                message = message.replace(link_element, href+end)
            else:
                message = message.replace(link_element, link_name+" "+href+end)
                
        whatsapp_codes = "*_"
        for code in whatsapp_codes:
            message = message.replace(code + "\n", code)
            message = message.replace("\n" + code, code)
            message = message.replace(code + " ", code)
            message = message.replace(" " + code, code)
                
    return message

def unicode_formatter(message):
    unicodes = {"&nbsp;":" ", "&#39;":"\'", "&rsquo;":"\'", "&amp;":"&", "&hellip;":"...", "&quot;":"\"", "\\n":"\n",
                "\\u2019":"'", "\\u2013":"'", "\\u2018":"'", "&ldquo":"\"", "&rdquo;":"\""}
    for code in unicodes:
        message = message.replace(code, unicodes[code])
    return message    

def get_hindi_to_english_number(message):
    hindi_numbers_map = {"१":"1", "२":"2", "३":"3", "४":"4", "५":"5","६":"6", "७":"7", "८":"8", "९":"9"}
    for num in hindi_numbers_map:
        message = message.replace(num, hindi_numbers_map[num])
    return message
    
def get_emojized_message(message):
    return emoji.emojize(message, use_aliases=True)    

def get_demojized_message(message):
    try:
        import emoji
        return emoji.demojize(message)
    except Exception as e:
        return ""

def whatsappify_text(message):
    message = html_tags_formatter(message)
    message = html_list_formatter(message)
    message = unicode_formatter(message)
    message = get_emojized_message(message)

    validation_obj = EasyChatInputValidation()
    message = validation_obj.remo_html_from_string(message)
    return message

# ====================== end ===================================================

# ====================== Utils =================================================
#	Valid Video URL:
def check_valid_video_url(file_url):
    is_valid = False
    try:
        file_ext = file_url.split(".")[-1].upper()
        if file_ext in ["WEBM", "MPG", "MP2", "MPEG", "MPE", "MPV", "OGG", "MP4", "M4P", "M4V", "AVI", "WMV", "MOV", "QT", "FLV", "SWF", "AVCHD"]:
            is_valid = True
    except Exception:
        pass
    return is_valid
        
#	Valid Image URL:
def check_valid_image_url(file_url):
    is_valid = False
    try:
        file_ext = file_url.split(".")[-1].upper()
        if file_ext in["PNG", "JPG", "JPEG", "SVG", "BMP", "GIF", "TIFF", "EXIF", "JFIF"]:
            is_valid = True
    except Exception:
        pass
    return is_valid

#	Calculate difference b/w datetime objects
def get_time_delta(date_str1, date_str2):
    delta_obj = {"minutes":0.0, "hours":0.0}
    try:
        from datetime import date, datetime
        if "." in date_str1:
            date_str1 = str(date_str1).split(".")[0]
        if "." in date_str2:
            date_str2 = str(date_str2).split(".")[0]
        date_str1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
        date_str2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")
        delta = date_str2 - date_str1 # 2nd date is greater
        duration_in_s = delta.total_seconds()
        delta_obj = {
            "seconds":duration_in_s,
            "minutes":round(duration_in_s/60,1), #divmod(duration_in_s, 60)[0],
            "hours":divmod(duration_in_s, 3600)[0],
            "days":divmod(duration_in_s, 86400)[0],
            "years":divmod(duration_in_s, 31536000)[0]
        }
        return delta_obj
    except Exception as E:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("get_time_delta: %s at %s", str(E), str(exc_tb.tb_lineno), extra=log_param)
        return delta_obj

def save_file_from_remote_server_to_local(api_token, remote_url, local_path, max_file_size_mb=5.0):
    is_saved = False
    try:
        start_time = time.time()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+api_token
        }
        response = requests.get(url=remote_url, headers=headers, timeout=10)
        response_time = response.elapsed.total_seconds()
        logger.info("save_file_from_remote_server_to_local: API response time: %s secs", str(response_time),extra=log_param)
        raw_data = response.content
        file_to_save = open(local_path, "wb")
        file_to_save.write(raw_data)
        file_to_save.close()
        end_time = time.time()
        response_time = end_time - start_time
        logger.info("save_file_from_remote_server_to_local: Total response time: %s secs", str(response_time),extra=log_param)
        file_size = os.path.getsize(local_path)/(1024*1024)
        is_saved = True
        if file_size > max_file_size_mb:
            os.remove(local_path)            
            logger.info("save_file_from_remote_server_to_local: File Size Exceeded, Max Allowed: %s", str(max_file_size_mb),extra=log_param)
            is_saved = False
    except Exception as E:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("save_file_from_remote_server_to_local: %s at %s", str(E), str(exc_tb.tb_lineno), extra=log_param)
    return is_saved


#   GET WMESSAGE FROM REVERSE MAPPING
def get_message_from_reverse_whatsapp_mapping(user_message, mobile, bot_obj):
    message = None
    try:
        is_suggestion = False
        user = Profile.objects.get(user_id=str(mobile), bot=bot_obj)
        data_obj = Data.objects.filter(
            user=user, variable="REVERSE_WHATSAPP_MESSAGE_DICT").first()
        data_dict = json.loads(str(data_obj.get_value()))
        logger.info("reverse message: %s", str(data_dict), extra=log_param)
        user_message = str(user_message).lower().strip()
        if user_message in data_dict:
            message = data_dict[str(user_message)]
            try:
                message = json.loads(message.replace("'", '"'))
                message = message["id"]
                is_suggestion = True
            except:
                is_suggestion = False

        logger.info(str(message), extra=log_param)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        
        logger.error("get_message_from_reverse_whatsapp_mapping: %s %s" +
                     str(e), str(exc_tb.tb_lineno), extra=log_param)
    logger.info("final message: %s", str(message), extra=log_param)
    return message, is_suggestion

#   Check Intent Level Feedback:
def check_intent_level_feedback(mobile, user_message, bot_obj, lang="en"):
    logger.info(" === Inside check_intent_level_feedback mapping === ",  extra=log_param)
    is_intent_feedback_asked = False
    message = user_message
    feedback_type = 0 
    try:
        is_suggestion = False
        user = Profile.objects.get(user_id=str(mobile), bot=bot_obj)
        data_obj = Data.objects.filter(
            user=user, variable="is_intent_feedback_asked")[0]
        try:
            is_intent_feedback_asked = json.loads(str(data_obj.get_value()))
        except Exception:
            is_intent_feedback_asked = json.loads(str(data_obj.value))
        logger.info("is_intent_feedback_asked: %s", str(is_intent_feedback_asked), extra=log_param)
        if user_message != None and user_message.strip() != "" and is_intent_feedback_asked == True:
            helpful_multilingual_name = get_translated_text("helpful", lang, EasyChatTranslationCache)
            unhelpful_multilingual_name = get_translated_text("unhelpful", lang, EasyChatTranslationCache)
            if user_message.lower() == "helpful" or user_message == helpful_multilingual_name:
                feedback_type = 1
            elif user_message.lower() == "unhelpful" or user_message == unhelpful_multilingual_name:
                feedback_type = -1
            if feedback_type in [1, -1]:
                logger.info("feedback_type: %s", str(feedback_type), extra=log_param)
                mis_obj = MISDashboard.objects.filter(user_id=user.user_id).latest('id')
                mis_obj.feedback_info = json.dumps(
                    {"is_helpful": int(feedback_type), "comments": ""})
                mis_obj.is_helpful_field = feedback_type
                mis_obj.save()
                logger.info("Intent level feedback saved: %s", str(feedback_type), extra=log_param)
                feedback_dict = {"is_intent_feedback_asked":False}
                save_data(user, json_data=feedback_dict,  src="None", channel="WhatsApp", bot_id=mis_obj.bot.id,  is_cache=True)
    except Exception as E:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("check_intent_level_feedback: %s at %s", str(E), str(exc_tb.tb_lineno), extra=log_param)
    return message
    
    
def change_language_response_required(sender, bot_id, bot, is_whatsapp_welcome_response=False):
    try:
        bot_obj = Bot.objects.get(pk=int(bot_id))
        channel = Channel.objects.filter(name="WhatsApp")[0]
        bot_channel_obj = BotChannel.objects.filter(
             bot=bot_obj, channel=channel)[0]
        languages_supported = bot_channel_obj.languages_supported.all()
        
        profile_obj = Profile.objects.get(user_id=str(sender), bot=bot)

        if languages_supported.count() == 1:
            profile_obj.selected_language = languages_supported[0]
            profile_obj.save()
        
        if profile_obj.selected_language and not is_whatsapp_welcome_response:
            return False

        if not bot_channel_obj.is_enable_choose_language_flow_enabled_for_welcome_response:
            default_lang = languages_supported.filter(lang="en").first()
            profile_obj.selected_language = default_lang
            profile_obj.save()
            return False

        return True
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("change_language_response_required: %s at %s", str(e), str(exc_tb.tb_lineno), extra=log_param)

    return True


def is_change_language_triggered(sender, bot_obj):
    try:
        user = Profile.objects.get(user_id=sender, bot=bot_obj)
        data_obj = Data.objects.filter(
            user=user, variable="CHANGE_LANGUAGE_TRIGGERED")[0]
        
        try:
            data_obj_value = data_obj.get_value()
        except Exception:
            data_obj_value = data_obj.value

        if data_obj_value == 'true':
            data_obj.value = False
            data_obj.save()
            return True

        return False
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("is_change_language_triggered: %s at %s", str(e), str(exc_tb.tb_lineno), extra=log_param)
    return False


def get_language_change_response(user_id, bot_id, REVERSE_WHATSAPP_MESSAGE_DICT):
    try:
        bot_obj = Bot.objects.get(pk=int(bot_id))

        profile_obj = Profile.objects.filter(user_id=str(user_id), bot=bot_obj).first()

        selected_language = profile_obj.selected_language.lang if profile_obj.selected_language else "en"

        channel = Channel.objects.filter(name="WhatsApp")[0]
        bot_channel_obj = BotChannel.objects.filter(
             bot=bot_obj, channel=channel)[0]
        languages_supported = bot_channel_obj.languages_supported.all()
        
        language_key_list = []
        if languages_supported.count() > 1:

            please_choose_str = "Please choose your language"
            please_choose_translated = get_translated_text(please_choose_str, selected_language, EasyChatTranslationCache)
            recommendation_str = please_choose_translated + "\n\n"

            for language in languages_supported:
                language_key_list.extend([f"*_{str(language.lang)}_* :point_right:"])
                REVERSE_WHATSAPP_MESSAGE_DICT[str(language.lang).lower().strip()] = str(language.lang)

                single_language_text = "Please type {} {/language_name/}"
                tarnslated_text = get_translated_text(
                    single_language_text, selected_language, EasyChatTranslationCache)
                tarnslated_text = tarnslated_text.replace("{/language_name/}", str(language.display))
                tarnslated_text += "\n\n"
                recommendation_str += tarnslated_text

            tarnslated_text = recommendation_str
            tarnslated_text = tarnslated_text.format(*language_key_list)

        return tarnslated_text, REVERSE_WHATSAPP_MESSAGE_DICT
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("get_language_change_response: %s at %s", str(e), str(exc_tb.tb_lineno), extra=log_param)

    return "", REVERSE_WHATSAPP_MESSAGE_DICT


def check_interative_capability_for_quick_reply(options, options_type):
    logger.info(" === check_interative_capability_for_quick_reply === ",  extra=log_param)
    logger.info("check_interative_capability_for_quick_reply options: %s",  str(options), extra=log_param)
    #max_text_length = 20
    max_text_length = 50
    max_option_count = 3
    capability = True
    if options == [] or len(options) > max_option_count:
        return False
    for option in options:
        if options_type == "choices":
            if len(option["display"]) > max_text_length:
                capability = False
                break
        if options_type == "recommendations":          
            if len(option) > max_text_length:
                capability = False
                break
    logger.info("check_interative_capability_for_quick_reply capability: %s",  str(capability), extra=log_param)
    return capability


def check_interative_capability_for_list(options, options_type):
    logger.info(" === check_interative_capability_for_list === ",  extra=log_param)
    logger.info("check_interative_capability_for_list options: %s",  str(options), extra=log_param)
    max_text_length = 24
    max_option_count = 10
    capability = True
    if options == [] or len(options) > max_option_count:
        return False
    for option in options:
        if options_type == "choices":
            if len(option["display"]) > max_text_length:
                capability = False
                break
        if options_type == "recommendations":          
            if len(option) > max_text_length:
                capability = False
                break
    logger.info("check_interative_capability_for_list capability: %s",  str(capability), extra=log_param)
    return capability


def check_is_attachment_required(user_id, bot_obj):
    is_required = False
    try:
        logger.info(" === check_is_attachment_required === ",  extra=log_param)
        user = Profile.objects.get(user_id=str(user_id), bot=bot_obj)
        data_obj = Data.objects.filter(user=user, variable="is_whatsapp_attachment_required")[0]
        try:
            data_value = json.loads(str(data_obj.value))
        except Exception:
            data_value = json.loads(str(data_obj.get_value()))
        logger.info(str(data_value), extra=log_param)
        is_required = bool(data_value)
    except Exception as E:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("check_is_attachment_required: %s", str(E),  extra=log_param)
    return is_required
# ====================== end ===================================================

# ====================== Vendor Specifics ======================================
def get_whatsapp_file_attachment(api_token, ameyo_host, attachment_packet, max_attachment_size_allowed):
    attachment_path = None
    is_saved = False
    try:
        from urllib.parse import urlparse
        from urllib.parse import parse_qs
        signature = attachment_packet["id"]
        remote_url = ameyo_host + "/v1/media/" + signature
        mime_type = attachment_packet["mime_type"]
    
        if "caption" in attachment_packet:
            caption  = attachment_packet["caption"]
            filename = caption
        else:
            filename = signature+".unknown"

        if filename.split('.')[-1] not in ["jpg", "png", "jpeg", "doc", "docx", "ppt", "xls", "pdf", "mp4"]:
            ext = "."+mime_type.split("/")[-1]
            if mime_type in ["application/msword","application/vnd.ms-pwerpoint","application/vnd.ms-excel", "vnd.openxmlformats-officedocument.wordprocessingml.document"]:
                if mime_type == "application/msword":
                    ext = ".doc"
                elif mime_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                    ext = ".docx"
                elif mime_type == "application/vnd.ms-pwerpoint":
                    ext = ".ppt"
                elif mime_type == "application/vnd.ms-excel":
                    ext = ".xls"
            filename = filename.split('.')[0] + ext

        filename = filename.replace(" ","-")
        if not os.path.exists(settings.MEDIA_ROOT + 'WhatsAppMedia'):
            os.makedirs(settings.MEDIA_ROOT + 'WhatsAppMedia')
        file_path = settings.MEDIA_ROOT+"WhatsAppMedia/"+filename
        file_path_rel = "files/WhatsAppMedia/"+filename
        is_saved = save_file_from_remote_server_to_local(api_token, remote_url, file_path)
        attachment_path = settings.EASYCHAT_HOST_URL+"/"+file_path_rel
        logger.info("is_whatsapp_file_attachment: Filename %s", filename, extra=log_param)
        logger.info("is_whatsapp_file_attachment: Filepath %s", attachment_path, extra=log_param)
    except Exception as E:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("save_file_from_remote_server_to_local: %s at %s", str(E), str(exc_tb.tb_lineno), extra=log_param)
    return attachment_path, is_saved
    

#   GET AMEYO API KEY: 
def GET_API_KEY(ameyo_host,username,password):
    log_param={'AppName': 'EasyChatApp', 'user_id': 'None', 'source': 'en', 'channel': 'WhatsApp', 'bot_id': 'None'}
    API_KEY = ""
    try:
        from base64 import b64encode
        logger.info("=== Inside AMEYO_GET_API_KEY API ===", extra=log_param)
        url = ameyo_host+"/v1/users/login"
        
        userAndPass = b64encode((username+":"+password).encode()).decode("ascii")
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic '+userAndPass
        }
        logger.info("AMEYO_GET_API_KEY Headers: %s", str(headers), extra=log_param)
        r = requests.request("POST", url, headers=headers, timeout=25, verify=True)
        content = json.loads(r.text)
        logger.info("AMEYO_GET_API_KEY Response: %s", str(content), extra=log_param)
        if str(r.status_code) == "200":
            if "users" in content and content["users"] != []:
                API_KEY = content["users"][0]["token"]
        logger.info("AMEYO_GET_API_KEY API Key generated: %s", str(API_KEY), extra=log_param)
    except requests.Timeout as RT:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("AMEYO_GET_API_KEY Timeout error: %s", str(RT), extra=log_param)
    except Exception as E:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("AMEYO_GET_API_KEY Failed: %s", str(E), extra=log_param)
    return API_KEY


# CACHING AMEYO API KEY:       
def GET_API_KEY_CACHED(ameyo_host,username, password, vendor_object):
    from EasyChatApp.models import WhatsAppVendorConfig
    from django.utils import timezone as tz
    import sys
    API_KEY = None
    log_param={'AppName': 'Campaign'}
    try:
        logger.info("=== Inside GET_AMEYO_JWT_TOKEN ===", extra=log_param)

        token_obj = vendor_object
            
        if token_obj.dynamic_token == None or token_obj.dynamic_token == "" or token_obj.dynamic_token == "token":
            API_KEY = GET_API_KEY(ameyo_host, username, password)
            token_obj.dynamic_token = API_KEY
            token_obj.dynamic_token_datetime = tz.now()
            token_obj.save()
        else:
            token_generated_on = token_obj.dynamic_token_datetime
            current_time = tz.now()
            time_diff = token_generated_on-current_time
            time_diff = time_diff.seconds//60
            API_KEY = token_obj.dynamic_token
            logger.info("--- getting token from cached db", extra=log_param)
            if float(time_diff) > token_obj.dynamic_token_refresh_time:
                API_KEY = GET_API_KEY(ameyo_host, username, password)
                token_obj.dynamic_token = API_KEY
                token_obj.dynamic_token_datetime = tz.now()
                token_obj.save()

        logger.info("=== END GET_AMEYO_JWT_TOKEN ===", extra=log_param)
        return API_KEY    
    except Exception as E:    
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("GET_AMEYO_JWT_TOKEN API  Failed: %s at %s", str(E), str(exc_tb.tb_lineno), extra=log_param)
        logger.info("=== END GET_AMEYO_JWT_TOKEN ===", extra=log_param)
    return API_KEY     

#   WHATSAPP SEND TEXT MESSAGE API:
def sendWhatsAppTextMessage(ameyo_host, api_key, message, phone_number, preview_url=False, recipient_type="individual"):
    log_param={'AppName': 'EasyChat', 'user_id': 'None', 'source': 'None', 'channel': 'WhatsApp', 'bot_id': 'None'}
    try:
        if message.strip() == "":
            return False
            
        logger.info("=== Inside Send WA Text Message API ===", extra=log_param)

        url = ameyo_host + "/v1/messages"

        headers = {
            'Authorization': 'Bearer '+api_key,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        payload = {
            "to": phone_number,
            "type": "text",
            "recipient_type": recipient_type,
            "text": {"body": message}
        }
        
        if preview_url == True:
            payload["preview_url"] = True
            
        logger.info("Send WA Text API URL: %s", str(url), extra=log_param)
        logger.info("Send WA Text API Headers: %s", str(headers), extra=log_param)
        logger.info("Send WA Text API Request: %s", str(payload), extra=log_param)
        r = requests.request("POST", url, headers=headers, data = json.dumps(payload), timeout=20, verify=True)
        logger.info("Send WA Text API Response: %s", str(r.text), extra=log_param)
        if str(r.status_code) == "200" or str(r.status_code) == "201":
            content = json.loads(r.text)
            logger.info("Text message sent succesfully", extra=log_param)
            return True
        else:
            logger.error("Failed to Send Text Message.", extra=log_param)
            logger.error("Send WA Text API Response: %s", str(r.text), extra=log_param)
            return False
    except requests.Timeout as RT:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("SendWhatsAppText API Timeout error: %s at %s", str(RT), str(exc_tb.tb_lineno), extra=log_param)
        return False    
    except Exception as E:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("SendWhatsAppText API Failed: %s at %s", str(E), str(exc_tb.tb_lineno), extra=log_param)
    return False


# WHATSAPP SEND MEDIA MESSAGE API:
def sendWhatsAppMediaMessage(ameyo_host, api_key, media_type, media_url, phone_number, caption = None, recipient_type="individual"):
    try:
        logger.info("=== Inside Send WA Media Message API ===", extra=log_param)

        logger.info("Media Type: %s", media_type, extra=log_param)

        if caption == None:
            caption = ""

        url = ameyo_host + "/v1/messages"

        headers = {
            'Authorization': 'Bearer '+api_key,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        contentType = mimetypes.guess_type(media_url)
        payload = {
            "to": phone_number,
            "type": media_type,
            "recipient_type": recipient_type,
        }

        media_object = {
                "provider": {
                    "name": ""
                },
                "link": media_url,
                "caption": caption
            }

        medianame = media_url.split("/")[-1]
        if media_type == "document":
            media_object["filename"] = medianame

        payload[media_type] = media_object

        logger.info("Send WA "+media_type.upper()+" API Request: %s", str(payload), extra=log_param)
        r = requests.request("POST", url, headers=headers, data = json.dumps(payload), timeout=20, verify=True)
        logger.info("Send WA "+media_type.upper()+" API Response: %s", str(r.text), extra=log_param)
        if str(r.status_code) == "200" or str(r.status_code) == "201":
            content = json.loads(r.text)
            logger.info(media_type.upper()+" message sent successfully", extra=log_param)
            return True
        else:
            logger.error("Failed to send "+media_type.upper()+" message",extra=log_param)
            return False
    except requests.Timeout as RT:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("SendWhatsAppMediaMessage Timeout error: %s at %s", str(RT), str(exc_tb.tb_lineno), extra=log_param)
        return False    
    except Exception as E:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("SendWhatsAppMediaMessage Failed: %s at %s", str(E), str(exc_tb.tb_lineno), extra=log_param)
    return False


#   WHATSAPP SEND SESSION BASED QUICK REPLY MESSAGE API:
def sendWhatsAppQuickReplyMessage(ameyo_host, api_key, reply_buttons, message_head, message_body, message_foot, phone_number, media_type="text", media_link=None, extra="None",lang="en", recipient_type="individual"):
    import requests
    import urllib
    log_param={'AppName': 'EasyChat', 'user_id': 'None', 'source': 'None', 'channel': 'WhatsApp', 'bot_id': 'None'}
    try:
        logger.info("=== Inside Send WA Session Based Quick Reply Message API ===", extra=log_param)

        url = ameyo_host + "/v1/messages"

        headers = {
            'Authorization': 'Bearer '+api_key,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        if len(reply_buttons) == 0 or len(reply_buttons) > 3:
            return False

        payload = {
            "recipient_type": recipient_type,
            "to" : phone_number,
            "type": "interactive",
            "interactive":{
                    "type": "button",
                    "body": {"text":message_body},
                    "action": {}
            }
        }

        interactive_header = {}
        if media_type == "text":
            interactive_header = {"type": "text", media_type:message_head}
        else:
            medianame = media_link.split("/")[-1]
            interactive_header = {
                media_type:{
                    "link": media_link,
                    "provider": {
                    "name": ""
                    }
                }
            }
            if media_type == "document":
                interactive_header[media_type]["filename"] = medianame
        
        # Uncomment below lines if you want to add header and footer for a message.
        # payload["interactive"]["header"] = interactive_header
        # payload["interactive"]["footer"] = {"text": message_foot}

        interactive_action = {"buttons":[]}
        count = 1
        for button in reply_buttons:
            button_dict = {}
            button_dict["type"] = "reply"
            button_dict["reply"] = {
                "id":str(count),
                "title":str(button)
            }
            interactive_action["buttons"].append(button_dict)
            count += 1
        payload["interactive"]["action"] = interactive_action

        logger.info("Send WA Session Based Quick Reply Message API Headers: %s", str(headers), extra=log_param)
        logger.info("Send WA Session Based Quick Reply Message API Request: %s", str(payload), extra=log_param)
        r = requests.request("POST", url, headers=headers, data = json.dumps(payload), timeout=20, verify=True)
        content = json.dumps(r.text)
        logger.info("Send WA Session Based Quick Reply Message API Response: %s", str(content), extra=log_param)
        if str(r.status_code) == "200" or str(r.status_code) == "201":
            logger.info("Quick Reply message sent succesfully", extra=log_param)
            return True
        else:
            logger.error("Failed to Send Quick Reply Message.", extra=log_param)
            return False
    except requests.Timeout as RT:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("sendWhatsAppQuickReplyMessage API Timeout error: %s at %s", str(RT), str(exc_tb.tb_lineno), extra=log_param)
        # print("sendWhatsAppQuickReplyMessage API Failed: %s", str(E), str(exc_tb.tb_lineno))
        return False    
    except Exception as E:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("sendWhatsAppQuickReplyMessage API Failed: %s at %s", str(E), str(exc_tb.tb_lineno), extra=log_param)
        return False

#   WHATSAPP SEND MENU LIST MESSAGE API:
def sendWhatsAppInteractiveListMessage(ameyo_host, api_key, list_title, reply_buttons, message_head, message_body, message_foot, phone_number, menu_button_text="Select", extra="None",lang="en", recipient_type="individual"):
    import requests
    import urllib
    log_param={'AppName': 'EasyChat', 'user_id': 'None', 'source': 'None', 'channel': 'WhatsApp', 'bot_id': 'None'}
    try:
        logger.info("=== Inside Send WA Session Based Interactive List Message API ===", extra=log_param)
        logger.info(f"reply_buttons = {reply_buttons}", extra=log_param)

        url = ameyo_host + "/v1/messages"

        headers = {
            'Authorization': 'Bearer '+api_key,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        if len(reply_buttons) == 0 or len(reply_buttons) > 10:
            return False

        payload = {
            "recipient_type": recipient_type,
            "to" : phone_number,
            "type": "interactive",
            "interactive":{
                    "type": "list",
                    "header": {"type": "text", "text":message_head},
                    "body": {"text":message_body},
                    "footer": {"text":message_foot},
                    "action": {}
            }
        }

        interactive_action = {
            "button":menu_button_text, 
            "sections":[{"title":list_title,"rows": []}]
        }
        count = 1
        for button in reply_buttons:
            button_dict = {}
            button_dict["id"] = str(count)
            if "$$$" in str(button):
                button_dict["title"] = str(button).split("$$$")[0]
                button_dict["description"] = str(button).split("$$$")[1]
            else:
                button_dict["title"] = str(button)
            interactive_action["sections"][0]["rows"].append(button_dict)
            count += 1
        payload["interactive"]["action"] = interactive_action

        logger.info("Send WA Session Based Interactive List Message API Request: %s", str(payload), extra=log_param)
        r = requests.request("POST", url, headers=headers, data = json.dumps(payload), timeout=20, verify=True)
        content = json.dumps(r.text)
        logger.info("Send WA Session Based Interactive List Message API Response: %s", str(content), extra=log_param)
        logger.info("Send WA Session Based Interactive List Message API Status Code: %s",str(r.status_code), extra=log_param)
        if str(r.status_code) == "200" or str(r.status_code) == "201":
            logger.info("Interactive List message sent succesfully", extra=log_param)
            return True
        else:
            logger.error("Failed to Send Interactive List Message.", extra=log_param)
            return False
    except requests.Timeout as RT:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("sendWhatsAppInteractiveListMessage API Timeout error: %s", str(RT), str(exc_tb.tb_lineno), extra=log_param)
        return False    
    except Exception as E:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("sendWhatsAppInteractiveListMessage API Failed: %s", str(E), str(exc_tb.tb_lineno), extra=log_param)
        return False


#   WHATSAPP SEND MENU LIST MESSAGE API:
def sendWhatsAppInteractiveListMessageCustom(ameyo_host, api_key, phone_number, interactive_data):
    import requests
    import urllib
    log_param={'AppName': 'EasyChat', 'user_id': 'None', 'source': 'None', 'channel': 'WhatsApp', 'bot_id': 'None'}
    try:
        logger.info("=== Inside sendWhatsAppInteractiveListMessageCustom ===", extra=log_param)

        url = ameyo_host + "/v1/messages"
        headers = {
            'Authorization': 'Bearer '+api_key,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        payload = {
            "recipient_type": "individual",
            "to" : phone_number,
            "type": "interactive",
            "interactive": json.loads(interactive_data)
        }

        logger.info("Send WA Session Based Interactive List Message API Request: %s", str(payload), extra=log_param)

        r = requests.request("POST", url, headers=headers, data = json.dumps(payload), timeout=20, verify=True)

        logger.info("Send WA Session Based Interactive List Message API Response: %s", str(r.text), extra=log_param)

        content = json.dumps(r.text)

        logger.info("Send WA Session Based Interactive List Message API Status Code: %s",str(r.status_code), extra=log_param)

        if str(r.status_code) == "200" or str(r.status_code) == "201":
            logger.info("Interactive List message sent succesfully", extra=log_param)
            return True
        else:
            logger.error("Failed to Send Interactive List Message.", extra=log_param)
            return False
    except requests.Timeout as RT:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("sendWhatsAppInteractiveListMessageCustom API Timeout error: %s", str(RT), str(exc_tb.tb_lineno), extra=log_param)
        return False
    except Exception as E:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("sendWhatsAppInteractiveListMessageCustom API Failed: %s", str(E), str(exc_tb.tb_lineno), extra=log_param)
        return False


def check_and_create_time_spent_by_user(user_id, session_id, start_datetime, bot_id):
    try:
        time_spent_by_user_objs = TimeSpentByUser.objects.filter(
            user_id=user_id, session_id=session_id)

        if time_spent_by_user_objs.exists():
            return

        bot_obj = Bot.objects.get(pk=int(bot_id))

        TimeSpentByUser.objects.create(user_id=user_id, session_id=session_id,
                                       start_datetime=start_datetime, end_datetime=start_datetime, bot=bot_obj)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("check_and_create_time_spent_by_user: %s at %s",
                     str(e), str(exc_tb.tb_lineno), extra=log_param)


def update_mis_and_time_spent_objects(user_id, session_id):
    try:
        time_spent_by_user_objs = TimeSpentByUser.objects.filter(
            user_id=user_id, session_id=session_id)
        curr_datetime = timezone.now()
        if time_spent_by_user_objs.exists():
            time_spent_obj = time_spent_by_user_objs.first()
            time_spent_obj.start_datetime = curr_datetime
            time_spent_obj.end_datetime = curr_datetime
            time_spent_obj.save()

        mis_objs = MISDashboard.objects.filter(
            user_id=user_id, session_id=session_id, is_session_started=False)

        mis_objs.update(is_session_started=True)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("check_and_create_time_spent_by_user: %s at %s",
                     str(e), str(exc_tb.tb_lineno), extra=log_param)


def update_whatsapp_session_obj(whatsapp_user_session_obj, easychat_session_obj):
    try:
        if not easychat_session_obj:
            easychat_session_obj = EasyChatSessionIDGenerator.objects.create()

        whatsapp_user_session_obj.session_obj = easychat_session_obj
        whatsapp_user_session_obj.is_session_started = True
        whatsapp_user_session_obj.save()

        return str(easychat_session_obj.token)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("update_whatsapp_session_obj: %s at %s",
                     str(e), str(exc_tb.tb_lineno), extra=log_param)
        return ""


def get_session_id_based_on_user_session(user_id, bot_id):

    try:
        whatsapp_user_session_obj = WhatsAppUserSessionMapper.objects.filter(
            user_id=user_id).first()

        if whatsapp_user_session_obj and whatsapp_user_session_obj.session_obj:

            session_id = whatsapp_user_session_obj.session_obj.token

            if (whatsapp_user_session_obj.is_current_session_obj_is_longer_than_tweenty_four_hours()):
                session_id = update_whatsapp_session_obj(whatsapp_user_session_obj, None)

            return str(session_id), True
        else:
            easychat_session_obj = EasyChatSessionIDGenerator.objects.create()
            if not whatsapp_user_session_obj:
                WhatsAppUserSessionMapper.objects.create(
                    user_id=user_id, session_obj=easychat_session_obj, is_session_started=True)
            else:
                whatsapp_user_session_obj.session_obj = easychat_session_obj
                whatsapp_user_session_obj.save()

            session_id = str(easychat_session_obj.token)
            check_and_create_time_spent_by_user(
                user_id, session_id, timezone.now(), bot_id)

            return session_id, False
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("get_session_id_based_on_user_session: %s at %s",
                     str(e), str(exc_tb.tb_lineno), extra=log_param)

        return "", False


def check_and_create_session_if_required(user_id, bot_id):
    try:
        whatsapp_user_session_obj = WhatsAppUserSessionMapper.objects.filter(
            user_id=user_id).first()
        session_id = whatsapp_user_session_obj.session_obj.token
        if (not whatsapp_user_session_obj) or (not whatsapp_user_session_obj.session_obj):

            easychat_session_obj = EasyChatSessionIDGenerator.objects.create()
            session_id = str(easychat_session_obj.token)
            if not whatsapp_user_session_obj:
                WhatsAppUserSessionMapper.objects.create(
                    user_id=user_id, session_obj=easychat_session_obj, is_session_started=True)
            else:
                update_whatsapp_session_obj(
                    whatsapp_user_session_obj, easychat_session_obj)

        elif whatsapp_user_session_obj.is_current_session_obj_is_longer_than_tweenty_four_hours():
            session_id = update_whatsapp_session_obj(
                whatsapp_user_session_obj, None)

        check_and_create_time_spent_by_user(
            user_id, session_id, timezone.now(), bot_id)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("check_and_create_session_if_required: %s at %s",
                     str(e), str(exc_tb.tb_lineno), extra=log_param)


#   MAIN FUNCTION    
def whatsapp_webhook(request_packet):
    log_param={'AppName': 'EasyChat', 'user_id': 'None', 'source': 'None', 'channel': 'WhatsApp', 'bot_id': 'None'}
    send_status = False
    response = {}
    response["status_code"] = 500
    response["status_message"] = "Internal server issues"
    response["mobile_number"] = ""
    try:
    #   WEBHOOK INIT
        logger.info("INSIDE AMEYO WA WEBHOOK", extra=log_param)
        logger.error("AMEYO WA WEBHOOK INCOMING_REQUEST_PACKET: %s",str(request_packet), extra=log_param)

    #   AMEYO DELIVERY STATUS:
        if "statuses" in request_packet.keys() or "delivery_status" in request_packet.keys():
            logger.error("INCOMING_DELIVERY_PACKET WA WEBHOOK: %s", str(request_packet), extra=log_param)

            extra = ""
            if "extra" in request_packet["statuses"][0]:
                extra = request_packet["statuses"][0]["extra"]		
            try:
                mobile_number	= request_packet["statuses"][0]["recipient_id"]
                request_id		= request_packet["statuses"][0]["id"]
                status			= request_packet["statuses"][0]["status"]
                timestamp		= request_packet["statuses"][0]["timestamp"]
                BOT_ID          = request_packet["bot_id"]
                
                pricing_model = ""
                billable = ""
                if "pricing" in request_packet["statuses"][0]:
                    billable		= request_packet["statuses"][0]["pricing"]["billable"]
                    pricing_model	= request_packet["statuses"][0]["pricing"]["pricing_model"]

                if status == "delivered" or status == "read":
                    check_and_create_session_if_required(mobile_number, BOT_ID)

                if extra != "Allincall" and extra != "":
                    try:
                        campaign = Campaign.objects.get(name=extra,partner=extra)
                    except Exception as e:
                        campaign = Campaign.objects.create(name=extra,status="in_progress",partner=extra)
                        logger.info("Creating campaign: %s",str(e), extra=log_param)
                    try:
                        audience = CampaignAudience.objects.get(audience_id=mobile_number)
                    except Exception as e:
                        audience = CampaignAudience.objects.create(audience_id=mobile_number)
                        logger.info("Creating audience: %s",str(e), extra=log_param)
                    try:
                        audience_log_obj = CampaignAudienceLog.objects.get(recepient_id=request_id)
                    except Exception as e:
                        audience_log_obj = CampaignAudienceLog.objects.create(recepient_id=request_id,campaign=campaign,audience=audience)
                        logger.info("Creating audience_log_obj: %s",str(e), extra=log_param)
                        

                normal_timestamp = convert_timestamp_to_normal(int(timestamp))

                audience_log_obj = CampaignAudienceLog.objects.get(
                    recepient_id=request_id)
                campaign = audience_log_obj.campaign
                analytics_obj = CampaignAnalytics.objects.get(
                    campaign=campaign)

                if status == "sent" and audience_log_obj.is_sent == False:
                    audience_log_obj.is_sent = True
                    audience_log_obj.sent_datetime = normal_timestamp
                    audience_log_obj.sent_date = normal_timestamp.date()

                if status == "delivered" and audience_log_obj.is_delivered == False:
                    if audience_log_obj.is_sent == False:
                        audience_log_obj.is_sent = True
                        audience_log_obj.sent_datetime = normal_timestamp
                        audience_log_obj.sent_date = normal_timestamp.date()

                    audience_log_obj.is_delivered = True
                    audience_log_obj.delivered_datetime = normal_timestamp
                    audience_log_obj.delivered_date = normal_timestamp.date()

                if status == "read" and audience_log_obj.is_read == False:
                    if audience_log_obj.is_sent == False:
                        audience_log_obj.is_sent = True
                        audience_log_obj.sent_datetime = normal_timestamp
                        audience_log_obj.sent_date = normal_timestamp.date()

                    if audience_log_obj.is_delivered == False:
                        audience_log_obj.is_delivered = True
                        audience_log_obj.delivered_datetime = normal_timestamp
                        audience_log_obj.delivered_date = normal_timestamp.date()

                    audience_log_obj.is_read = True
                    audience_log_obj.read_datetime = normal_timestamp
                    audience_log_obj.read_date = normal_timestamp.date()

                audience_log_obj.save()
                analytics_obj.message_sent = CampaignAudienceLog.objects.filter(
                    campaign=campaign, is_sent=True).count()
                analytics_obj.message_read = CampaignAudienceLog.objects.filter(
                    campaign=campaign, is_read=True).count()
                analytics_obj.message_delivered = CampaignAudienceLog.objects.filter(
                    campaign=campaign, is_delivered=True).count()

                analytics_obj.save()

                response["mobile_number"] = request_packet["statuses"][0]["recipient_id"]
            except Exception:
                pass
            response["status_code"] = 200
            response["status_message"] = "Request processed successfully."
            logger.info("AmeyoDeliveryCheck: %s", str(response), extra=log_param)
            return response


    # == CREDENTIALS AND DETAILS: ==============================================
#        ameyo_username              = 'admin' 
#        ameyo_password              = 's&uQ,22$U/gXG>Q4'
#        ameyo_host                  = 'https://cogno2.ameyo.net:9500'
        ameyo_username              = 'admin' 
        ameyo_password              = 'Ameyo@1234'
        ameyo_host                  = 'https://medops.ameyo.net:2204'
        BOT_ID                      = request_packet["bot_id"]
        DEFAULT_BOT_ID              = request_packet["bot_id"]
        sender                      = str(request_packet["messages"][0]["from"])
        mobile                      = sender
        receiver                    = response["mobile_number"]
        response["mobile_number"]   = sender
        log_param["user_id"]        = sender
        log_param["bot_id"]         = BOT_ID
        logger.info("Sender: %s",str(sender), extra=log_param)
        logger.info("Reciever: %s",str(receiver), extra=log_param)
        whatsapp_mobile_number      = receiver
        vendor_object = None
        try:
            vendor_object = WhatsAppVendorConfig.objects.get(mobile_number=whatsapp_mobile_number)
        except Exception:
            pass
        if vendor_object != None:
            ameyo_username = vendor_object.api_username
            ameyo_password = vendor_object.api_password
            ameyo_host = vendor_object.session_api_host
        if vendor_object == None:
            ameyo_api_key = GET_API_KEY(ameyo_host, ameyo_username, ameyo_password)
        else:
            ameyo_api_key = GET_API_KEY_CACHED(ameyo_host, ameyo_username, ameyo_password, vendor_object)
        logger.info("AMEYO API_KEY: %s",str(ameyo_api_key), extra=log_param)
        bot_obj = Bot.objects.get(pk=int(BOT_ID))
        default_bot_obj = Bot.objects.get(pk=int(DEFAULT_BOT_ID))
    # ==========================================================================  

        session_id, is_session_started = get_session_id_based_on_user_session(mobile, BOT_ID)

        bot_channel_obj = BotChannel.objects.get(bot=bot_obj, channel=Channel.objects.get(name="WhatsApp"))

        user_id = sender
        if bot_channel_obj.mobile_number_masking_enabled and bot_obj.masking_enabled:
            user_id = hashlib.md5(sender.encode()).hexdigest()

    #   CHECK FOR NEW USER:
        first_time_user = "false"
        check_user = Profile.objects.filter(user_id=str(user_id), bot=bot_obj).first()
        if not check_user:
            first_time_user = "true"
            check_user = Profile.objects.create(user_id=str(user_id), bot=bot_obj)
        default_user_obj = check_user
        logger.info("Is New User: %s", first_time_user, extra=log_param)

        #   GET PREVIOUS BOT ID
        user_obj = Profile.objects.filter(user_id=str(user_id), bot=bot_obj)
        if user_obj:
            user_obj = user_obj[0]
            data_obj = Data.objects.filter(
                user=user_obj, variable="bot_id")
            data_obj =data_obj.first()
            if data_obj:
                
                BOT_ID = json.loads(data_obj.get_value())
                bot_obj = Bot.objects.get(pk=int(BOT_ID))
                logger.info("Bot id " + str(BOT_ID), extra=log_param)
                log_param["bot_id"] = BOT_ID

    #   CHECK USER MESSAGE TYPE: text, image, document, voice, location
        message_type = request_packet["messages"][0]["type"]
        logger.info("Message Type: %s", message_type, extra=log_param)   


    #   GLOBAL CONFIGURATION VARIABLES:
        MESSAGE_HEADER                              = "BOT"    # e.g bot name 'Maya :'
        MESSAGE_FOOTER                              = "BOT"    # e.g '© Kotak Securities Limited.'
        LIST_HEADER_FOOTER_VISIBLE                  = False
        send_default_quick_reply                    = True
        send_default_list_options                   = True
        list_interactive_menu_button_text           = "Select"
        list_interactive_options_title              = "Options"
        main_menu_intent_name                       = "Main Menu"
        max_attachment_size_allowed                 = 5.0 # In MBs
        outflow_attachment_intent_name              = "Collect User Attachment"   # intent to be triggered during outflow attachment. e.g Collect User Attachment
        save_outflow_attachment                     = False # Whether to save outflow attachments or not
        invalid_attachment_notification             = get_emojized_message(":warning: *Failed to send file attachment!* \nYour file is either invalid or greater than "+str(max_attachment_size_allowed)+" MB.")
        trigger_outflow_attachment_intent           = False
        sticky_recommendations                      = []    # recommendation that will be appended as options when flow ends
        sticky_choices                              = []    # choices that will be appended as options when flow ends
        is_compact_recommendations_choices          = True  # Single new line after each option
        max_choices_recommendations_bubble_size     = 15    # max bubble size after which options will be appended in new bubble(s)
        choices_recommendations_header              = "To select from the below option(s), enter the *option number*:\n\n"
        choices_recommendations_footer              = "" 
        max_cards_bubble_size                       = 20    # max bubble size for cards after which it will append new bubble(s).
        go_back_text                                = "Go Back"
        feedback_question                           = "Was this helpful?"
        feedback_option_yes                         = get_emojized_message(":thumbs_up:")+" Yes" 
        feedback_option_no                          = get_emojized_message(":thumbs_down:")+ " No"
        customer_ends_livechat_text                 = "LiveChat Session has ended."
        customer_ends_livechat_err_text             = "Failed to end the session due to some connectivity issue. Please type 'end chat' again."
        helpful_intent_name                         = "Helpful"
        unhelpful_intent_name                       = "Unhelpful"
        ask_to_enter_text                           = "Please type"
        livechat_terminate_message                  = "end chat"
        recommendations_after_language_change       = []
        authentication_intent_names                 = []    # Add the name of authentication intents to avoid looping when the same is called direclty.
        greeting_intent_names                       = []
        language_change_query_list                  = ["change language", "change the language", "language change", "switch language"]         

    #   GET USER ATTACHMENTS AND MESSAGES:
        selected_language = "en"
        is_location = True
        is_attachement = True
        is_attachment_saved = False
        message = None
        filepath = None
        is_suggestion = False
        file_caption = None
        REVERSE_WHATSAPP_MESSAGE_DICT = {}
        is_feedback_required = False
        is_go_back_enabled = False
        reverse_mapping_index = 0

        is_whatsapp_attachment_required = check_is_attachment_required(user_id, bot_obj)
        if message_type == "text" or message_type == "button" or message_type == "interactive":
            is_attachement = False
            is_location = False
        if is_attachement:
            # image, document, voice
            attachment_packet = request_packet["messages"][0][message_type]
            attachment_type = message_type
            logger.info(" Whatsapp attachment packet: %s",str(attachment_packet), extra=log_param)
            if attachment_type != "document" and "caption" in attachment_packet:
                file_caption = attachment_packet["caption"]
            
            livechat_user = Profile.objects.filter(user_id=str(user_id), bot=bot_obj).first()
            if is_whatsapp_attachment_required == True or save_outflow_attachment == True:
                filepath, is_attachment_saved = get_whatsapp_file_attachment(ameyo_api_key, ameyo_host, attachment_packet, max_attachment_size_allowed)
            else:
                if first_time_user == "false" and livechat_user and livechat_user.livechat_connected:
                    filepath, is_attachment_saved = get_whatsapp_file_attachment(ameyo_api_key, ameyo_host, attachment_packet, max_attachment_size_allowed)
            message = "attachment"
        else:
            #   Regular Message:
            if message_type == "text":
                message = request_packet["messages"][0]["text"]["body"]
            #   Quick Reply Message:
            elif message_type == "button":
                message = request_packet["messages"][0]["button"]["text"]
                logger.info("User quick reply: %s", str(message), extra=log_param)  
            #   Interactive List Reply Message:
            elif message_type == "interactive":
                if "button_reply" in request_packet["messages"][0]["interactive"]:
                    message = request_packet["messages"][0]["interactive"]["button_reply"]["title"]
                    logger.info("User quick reply: %s", str(message), extra=log_param)
                elif "list_reply" in request_packet["messages"][0]["interactive"]:
                    message = request_packet["messages"][0]["interactive"]["list_reply"]["title"]
                    logger.info("User list reply: %s", str(message), extra=log_param)

            reverse_message = None
            reverse_message, is_suggestion = get_message_from_reverse_whatsapp_mapping(message, user_id, default_bot_obj)
            if reverse_message != None:
                message = reverse_message
            else:
                is_suggestion = False
            logger.info("User Message: %s", str(message), extra=log_param)                

            #   Intent Level Feedback Check
            message = check_intent_level_feedback(user_id, message, bot_obj)

            #   Go Back Check
            if first_time_user == "false":
                user = Profile.objects.get(user_id=str(user_id), bot=bot_obj)
                check_go_back_enabled = Data.objects.filter(user=user, variable="is_go_back_enabled")
                if len(check_go_back_enabled) > 0 and str(check_go_back_enabled[0].value) == 'true':
                    is_go_back_enabled = True

        logger.info("User Message(final): %s", str(message), extra=log_param)     

        bot_channel_obj = BotChannel.objects.get(bot=bot_obj, channel=Channel.objects.get(name="WhatsApp"))

        if bot_channel_obj.mobile_number_masking_enabled and bot_obj.masking_enabled:
            user_id = hashlib.md5(sender.encode()).hexdigest()

        languages_supported = bot_channel_obj.languages_supported.all()

    #   CHECK IF CHANGE LANGUAGE WAS TRIGGERED
        if is_change_language_triggered(user_id, default_bot_obj):
            logger.info("is_change_language_triggered: True", extra=log_param)
            try:
                is_supported = False
                lang_codes = list(languages_supported.values('lang'))
                for code in lang_codes:
                    if code["lang"].strip().lower() == message.strip().lower():
                        is_supported = True
                        break
                if is_supported:
                    lang_obj = Language.objects.filter(lang=message).first()
                    profile_obj = Profile.objects.filter(user_id=str(user_id), bot=bot_obj).first()
                    profile_obj.selected_language = lang_obj
                    profile_obj.save()
                    text_message = "You have selected " + \
                        str(lang_obj.display) + \
                        ". If you want to change your language again please type"
                    text_message = get_translated_text(
                        text_message, lang_obj.lang, EasyChatTranslationCache)
                    text_message = text_message + ' "Change Language"'
                    if recommendations_after_language_change:
                        translated_recommendations_after_language_change = []
                        if lang_obj.lang != "en":
                            for item in recommendations_after_language_change:
                                option_name = get_translated_text(str(item), lang_obj.lang, EasyChatTranslationCache)
                                translated_recommendations_after_language_change.append(option_name)
                            recommendations_after_language_change = translated_recommendations_after_language_change
                        empty_recommendations = False
                        if send_default_quick_reply or send_default_list_options:
                            total_options_count = len(recommendations_after_language_change)
                            TEMP_REVERSE_WHATSAPP_MESSAGE_DICT = {}
                            BUTTON_DISPLAY_NAMES = []
                            if send_default_quick_reply == True:
                                if total_options_count <= 3 and len(text_message) < 1024:
                                    if check_interative_capability_for_quick_reply(options=recommendations_after_language_change, options_type="recommendations"):                        
                                        for recommendation in recommendations_after_language_change:
                                            if recommendation not in BUTTON_DISPLAY_NAMES:
                                                option_name = recommendation
                                                BUTTON_DISPLAY_NAMES.append(option_name)
                                                TEMP_REVERSE_WHATSAPP_MESSAGE_DICT[recommendation] = recommendation
                                        empty_recommendations = True
                                        is_send = sendWhatsAppQuickReplyMessage(ameyo_host, ameyo_api_key, BUTTON_DISPLAY_NAMES, MESSAGE_HEADER, text_message, MESSAGE_FOOTER, mobile, "text", None, lang=lang_obj.lang)
                                        REVERSE_WHATSAPP_MESSAGE_DICT = TEMP_REVERSE_WHATSAPP_MESSAGE_DICT
                            if send_default_list_options == True:
                                if total_options_count > 3 and total_options_count < 11 and len(text_message) < 1024:
                                    if check_interative_capability_for_list(options=recommendations_after_language_change, options_type="recommendations"):
                                        if lang_obj.lang != "en":
                                            list_interactive_menu_button_text       = get_translated_text(list_interactive_menu_button_text, selected_language, EasyChatTranslationCache)
                                            list_interactive_options_title          = get_translated_text(list_interactive_options_title, selected_language, EasyChatTranslationCache)
                                        for recommendation in recommendations_after_language_change:
                                            if recommendation not in BUTTON_DISPLAY_NAMES:
                                                option_name = recommendation
                                                BUTTON_DISPLAY_NAMES.append(option_name)
                                                TEMP_REVERSE_WHATSAPP_MESSAGE_DICT[recommendation] = recommendation
                                        BUTTON_HEADER = MESSAGE_HEADER
                                        BUTTON_FOOTER = MESSAGE_FOOTER
                                        if LIST_HEADER_FOOTER_VISIBLE == False:
                                            BUTTON_HEADER = " "
                                            BUTTON_FOOTER = " "
                                        logger.info("Calling sendWhatsAppInteractiveListMessage", extra=log_param)
                                        is_send = sendWhatsAppInteractiveListMessage(ameyo_host, ameyo_api_key, list_interactive_options_title, BUTTON_DISPLAY_NAMES, BUTTON_HEADER, message, BUTTON_FOOTER, mobile, menu_button_text=list_interactive_menu_button_text, extra="None")
                                        empty_recommendations = True                                
                                        REVERSE_WHATSAPP_MESSAGE_DICT = TEMP_REVERSE_WHATSAPP_MESSAGE_DICT
                        if empty_recommendations == False:
                            send_status = sendWhatsAppTextMessage(ameyo_host, ameyo_api_key, text_message, mobile, preview_url=False)
                            if lang_obj.lang != "en":
                                ask_to_enter_text               = get_translated_text(ask_to_enter_text, lang_obj.lang, EasyChatTranslationCache)
                                choices_recommendations_header  = get_translated_text(choices_recommendations_header, lang_obj.lang, EasyChatTranslationCache) + "\n"
                                choices_recommendations_footer  = get_translated_text(choices_recommendations_footer, lang_obj.lang, EasyChatTranslationCache)
                            recommendation_str = ""
                            for index in range(len(recommendations_after_language_change)):
                                if index%max_choices_recommendations_bubble_size==0 and index != 0:
                                    recommendation_str +="$$$"
                                option_name = get_translated_text(str(recommendations_after_language_change[index]), lang_obj.lang, EasyChatTranslationCache)
                                REVERSE_WHATSAPP_MESSAGE_DICT[str(index+1)]=str(option_name)
                                recommendation_str += ask_to_enter_text+" *"+str(index+1)+"* :point_right:  "+str(option_name)+"\n"
                                if is_compact_recommendations_choices == False:
                                    recommendation_str =+"\n"
                            recommendation_str = choices_recommendations_header + recommendation_str + choices_recommendations_footer
                            recommendation_str = get_emojized_message(recommendation_str)    
                            send_status = sendWhatsAppTextMessage(ameyo_host, ameyo_api_key, recommendation_str, mobile, preview_url=False)
                        
                        logger.info("REVERSE_WHATSAPP_MESSAGE_DICT: %s", str(
                            REVERSE_WHATSAPP_MESSAGE_DICT), extra=log_param)
                        save_data(default_user_obj, json_data={"REVERSE_WHATSAPP_MESSAGE_DICT":REVERSE_WHATSAPP_MESSAGE_DICT},  src="None", channel="WhatsApp", bot_id=DEFAULT_BOT_ID,  is_cache=True)

                    else:
                        send_status = sendWhatsAppTextMessage(ameyo_host, ameyo_api_key, text_message, mobile, preview_url=False)
                    response["status_code"] = 200
                    response["status_message"] = "Request processed successfully."
                    return response
            except Exception as e:
                logger.error("is_change_language_triggered: %s",str(e), extra=log_param)
        
        user_obj = Profile.objects.filter(user_id=str(user_id), bot=bot_obj)
        if languages_supported.count() == 1 and user_obj.count()>0 and user_obj[0].selected_language == None:
            user_obj[0].selected_language = languages_supported[0]
        if languages_supported.count() > 1 and user_obj.count()>0 and user_obj[0].selected_language == None:
            user_obj[0].selected_language = languages_supported.filter(lang="en")[0]


    #   CHECK IF CHANGE LANGUAGE IS CALLED
        language_change_query_list += list(EasyChatTranslationCache.objects.filter(input_text__iexact="change language").values_list('translated_data',flat=True).distinct())
        if isinstance(message, str) and message.lower().strip() in language_change_query_list:
            REVERSE_WHATSAPP_MESSAGE_DICT = {}
            language_str, REVERSE_WHATSAPP_MESSAGE_DICT = get_language_change_response(str(user_id), BOT_ID, REVERSE_WHATSAPP_MESSAGE_DICT)
            if language_str != "":
                language_str = get_emojized_message(language_str)
                send_status = sendWhatsAppTextMessage(ameyo_host, ameyo_api_key, language_str, str(sender), preview_url=False)
                logger.info("Is change language response sent: %s", str(send_status), extra=log_param)

                user = set_user(str(sender), message, "None", "WhatsApp", BOT_ID)
                save_data(default_user_obj, json_data={"CHANGE_LANGUAGE_TRIGGERED": True}, src="None", channel="WhatsApp", bot_id=DEFAULT_BOT_ID, is_cache=True)

                logger.info("REVERSE_WHATSAPP_MESSAGE_DICT: %s", str(
                    REVERSE_WHATSAPP_MESSAGE_DICT), extra=log_param)
                save_data(default_user_obj, json_data={"REVERSE_WHATSAPP_MESSAGE_DICT": REVERSE_WHATSAPP_MESSAGE_DICT}, src="None", channel="WhatsApp", bot_id=DEFAULT_BOT_ID, is_cache=True)
                
                response["status_code"] = 200
                response["status_message"] = "Request processed successfully."
                return response


    #   GET LANGUAGE SELECTED BY USER
        try:
            selected_language = Profile.objects.get(
                user_id=str(user_id), bot=bot_obj).selected_language

            if not selected_language:
                selected_language = "en"
            else:
                selected_language = selected_language.lang
                languages_supported = Bot.objects.get(
                    pk=int(BOT_ID)).languages_supported
                languages_supported = languages_supported.filter(
                    lang=selected_language)

                if not languages_supported:
                    selected_language = "en"
        except Exception:
            selected_language = 'en'
            user = set_user(str(sender), message, "None", "WhatsApp", BOT_ID)            
            languages_supported = Language.objects.get(lang="en")
            if user.selected_language == None:
                user.selected_language = languages_supported
                user.save()

        mobile = str(sender)  # User mobile
        waNumber = str(receiver)  # Bot Whatsapp Number


    #   Invalid Attachment Notifcation:
        if is_attachement and is_attachment_saved == False:
            send_status = sendWhatsAppTextMessage(ameyo_host, ameyo_api_key, invalid_attachment_notification, str(mobile), preview_url=False)
            if send_status:
                logger.info("Invalid Attachment Notifcation Sent:", extra=log_param)
                response["status_code"] = 200
                response["status_message"] = "Request processed successfully."
                return response

    #   WEBHOOK EXECUTE FUNCTION CALL
        channel_params = {"user_mobile":mobile, "bot_wa_number":waNumber, "attached_file_path":filepath, "whatsapp_file_caption":file_caption, "is_new_user":first_time_user, "QueryChannel":"WhatsApp", "is_go_back_enabled": is_go_back_enabled, "entered_suggestion": is_suggestion, "session_id": session_id, "is_session_started": is_session_started}
        logger.info("AMEYOCallBack Channel params:  %s",str(channel_params), extra=log_param)
        logger.info("Bot id " + str(BOT_ID), extra=log_param)
        whatsapp_response = execute_query(user_id, BOT_ID, "uat", str(message), selected_language, "WhatsApp", json.dumps(channel_params), message)
        logger.info("AMEYOCallBack execute_query response %s and selected_language : %s",str(whatsapp_response),str(selected_language), extra=log_param)
        
        if "whatsapp_list_message_header" in whatsapp_response["response"]:
            list_interactive_menu_button_text = whatsapp_response["response"]["whatsapp_list_message_header"]
            if selected_language != "en":
                list_interactive_menu_button_text = get_translated_text(list_interactive_options_title, selected_language, EasyChatTranslationCache)
            if whatsapp_response["response"]["last_identified_intent_name"] == "Schedule Call Back":
                list_interactive_menu_button_text = "Call Me Back 👍"
                list_interactive_options_title = "Tomorrow"
        
        if 'bot_id' in whatsapp_response:
            bot_id = whatsapp_response['bot_id']

            default_bot_obj = Bot.objects.get(pk=int(DEFAULT_BOT_ID))
            profile_obj = Profile.objects.filter(
                user_id=str(user_id), bot=default_bot_obj)

            if profile_obj and bot_id != "":
                save_data(profile_obj[0], {
                          "LAST_SELECTED_BOT": bot_id}, "None", "WhatsApp", bot_id, is_cache=True)

                save_data(profile_obj[0], {"bot_id": str(bot_id)},
                          "None", "WhatsApp", bot_id, is_cache=True)

                bot_obj = Bot.objects.get(pk=bot_id)

        if "is_bot_switched" in whatsapp_response and whatsapp_response["is_bot_switched"]:
            profile_obj = Profile.objects.filter(
                user_id=user_id, bot=bot_obj).first()
            profile_obj.selected_language = Language.objects.filter(
                lang="en").first()
            profile_obj.save()
            selected_language = "en"

        
    #   Change Response based on language selected:
        # for language auto detection
        if "language_src" in whatsapp_response["response"]:
            selected_language = whatsapp_response["response"]["language_src"]
            user_obj = user_obj[0]
            user_obj.selected_language = Language.objects.filter(
                lang=selected_language).first()
            user_obj.save()

        #   Change default texts based on language selected
        if selected_language != "en":
            main_menu_intent_name                   = get_translated_text(main_menu_intent_name, selected_language, EasyChatTranslationCache)
            outflow_attachment_intent_name          = get_translated_text(outflow_attachment_intent_name, selected_language, EasyChatTranslationCache)
            invalid_attachment_notification         = get_translated_text(invalid_attachment_notification, selected_language, EasyChatTranslationCache)
            choices_recommendations_header          = get_translated_text(choices_recommendations_header, selected_language, EasyChatTranslationCache) +"\n"
            choices_recommendations_footer          = get_translated_text(choices_recommendations_footer, selected_language, EasyChatTranslationCache) +"\n"
            go_back_text                            = get_translated_text(go_back_text, selected_language, EasyChatTranslationCache)
            feedback_question                       = get_translated_text(feedback_question, selected_language, EasyChatTranslationCache)
            feedback_option_yes                     = get_translated_text(feedback_option_yes, selected_language, EasyChatTranslationCache)
            feedback_option_no                      = get_translated_text(feedback_option_no, selected_language, EasyChatTranslationCache)
            customer_ends_livechat_text             = get_translated_text(customer_ends_livechat_text, selected_language, EasyChatTranslationCache)
            customer_ends_livechat_err_text         = get_translated_text(customer_ends_livechat_err_text, selected_language, EasyChatTranslationCache)
            helpful_intent_name                     = get_translated_text(helpful_intent_name, selected_language, EasyChatTranslationCache)
            unhelpful_intent_name                   = get_translated_text(unhelpful_intent_name, selected_language, EasyChatTranslationCache)
            ask_to_enter_text                       = get_translated_text(ask_to_enter_text, selected_language, EasyChatTranslationCache)
            list_interactive_menu_button_text       = get_translated_text(list_interactive_menu_button_text, selected_language, EasyChatTranslationCache)
            list_interactive_options_title          = get_translated_text(list_interactive_options_title, selected_language, EasyChatTranslationCache)
            #   From Bot Language Template:
            bot_language_template = RequiredBotTemplate.objects.filter(bot=Bot.objects.get(pk=BOT_ID), language=Language.objects.get(lang=selected_language))
            if bot_language_template.count() > 0:
                go_back_text = bot_language_template[0].go_back_text

        is_whatsapp_welcome_response = False
        if "is_whatsapp_welcome_response" in whatsapp_response["response"]:
            is_whatsapp_welcome_response = whatsapp_response["response"]["is_whatsapp_welcome_response"]

        is_response_to_be_language_processed = True

        if "is_response_to_be_language_processed" in whatsapp_response["response"]:
            is_response_to_be_language_processed = whatsapp_response[
                "response"]["is_response_to_be_language_processed"]
                
        if selected_language != "en" and is_response_to_be_language_processed:
            whatsapp_response = process_response_based_on_language(whatsapp_response, selected_language, EasyChatTranslationCache)


    #   USER OBJECT:    
        user = Profile.objects.get(user_id=str(user_id), bot=bot_obj)
        # user.is_session_exp_msg_sent = False
        # user.save()


    #   Check LiveChat:
        if "is_livechat" in whatsapp_response and whatsapp_response["is_livechat"] == "true":
            if selected_language != "en":
                livechat_terminate_message = get_translated_text(livechat_terminate_message, selected_language, EasyChatTranslationCache)
            if message.lower() == "end chat" or message.lower() == livechat_terminate_message:
                livechat_notification = customer_ends_livechat_text
                send_status = sendWhatsAppTextMessage(ameyo_host, ameyo_api_key, livechat_notification, str(mobile), preview_url=False)
            return whatsapp_response


    #   Auto Trigger Last Intent after Authentication:
        try:
            if whatsapp_response != {}:
                if str(whatsapp_response['status_code']) == '200' and whatsapp_response['response'] != {}:
                    if 'modes' in whatsapp_response['response']["text_response"] and whatsapp_response['response']["text_response"]['modes'] != {}:
                        if 'auto_trigger_last_intent' in whatsapp_response['response']["text_response"]['modes'] and whatsapp_response['response']["text_response"]['modes']['auto_trigger_last_intent'] == 'true':
                            if 'last_identified_intent_name' in whatsapp_response['response'] and whatsapp_response['response']['last_identified_intent_name'] != '':
                                auth_message = whatsappify_text(whatsapp_response["response"]["text_response"]["text"])     
                                send_status = sendWhatsAppTextMessage(ameyo_host, ameyo_api_key, auth_message, mobile, preview_url=False)
                                message = whatsapp_response['response']['last_identified_intent_name']
                                if message not in  authentication_intent_names:
                                    whatsapp_response = execute_query(user_id, BOT_ID, "uat", str(message), selected_language, "WhatsApp", json.dumps(channel_params), message)
                                    logger.info("AMEYOCallBack: execute_query after Auth response %s",str(whatsapp_response), extra=log_param)
        except  Exception as E:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            logger.error("Cannot identify Last Intent: %s at %s", str(E), str(exc_tb.tb_lineno), extra=log_param)



    #   Check OutFlow Attachment: 
        # Attachments which are received when user is not in attachment required flow and livechat session is off.
        logger.info("AmeyoCallBack is_whatsapp_attachment not required:  %s",str(is_whatsapp_attachment_required == False), extra=log_param)
        logger.info("AmeyoCallBack Is LiveChat OFF :  %s",str(user.livechat_connected == False), extra=log_param)
        logger.info("AmeyoCallBack Is Attachment Recieved :  %s",str(is_attachement), extra=log_param)
        logger.info("AmeyoCallBack trigger_outflow_attachment_intent :  %s",str(trigger_outflow_attachment_intent), extra=log_param)
        if is_whatsapp_attachment_required == False and is_attachement == True and user.livechat_connected == False and trigger_outflow_attachment_intent == True:
            message = outflow_attachment_intent_name
            logger.info("AmeyoCallBack OutFlow Attachment Detected and Query Selected:  %s",str(message), extra=log_param)
            whatsapp_response = execute_query(user_id, BOT_ID, "uat", str(message), selected_language, "WhatsApp", json.dumps(channel_params), message)
            logger.info("AmeyoCallBack execute_query After OutFlow attachment %s",str(whatsapp_response), extra=log_param)
        if "is_attachment_required" in whatsapp_response:
            save_data(user, json_data={"is_whatsapp_attachment_required":whatsapp_response["is_attachment_required"]},  src="en", channel="WhatsApp", bot_id=BOT_ID,  is_cache=True)
        else:
            save_data(user, json_data={"is_whatsapp_attachment_required":False},  src="en", channel="WhatsApp", bot_id=BOT_ID,  is_cache=True)        
            

    #   BOT RESPONSES: images, videos, cards, choices, recommendations
        message			= whatsapp_response["response"]["text_response"]["text"]
        modes			= whatsapp_response["response"]["text_response"]["modes"]
        modes_param		= whatsapp_response["response"]["text_response"]["modes_param"]
        recommendations = whatsapp_response["response"]["recommendations"]
        images			= whatsapp_response["response"]["images"]
        videos			= whatsapp_response["response"]["videos"]
        cards			= whatsapp_response["response"]["cards"]
        choices			= whatsapp_response["response"]["choices"]
        is_flow_ended   = whatsapp_response["response"]["is_flow_ended"]
        
        cleaned_recommendations = []
        for recm in recommendations:
            if isinstance(recm,dict) and "name" in recm:
                cleaned_recommendations.append(recm["name"])
            else:
                cleaned_recommendations.append(recm)
        recommendations = cleaned_recommendations

        cleaned_choices = []
        for choice in choices:
            if choice["display"] == helpful_intent_name or choice["display"] == unhelpful_intent_name:
                continue
            else:
                cleaned_choices.append(choice)
        choices = cleaned_choices


        logger.info("recommendations: %s", str(recommendations), extra=log_param)
        logger.info("choices: %s", str(choices), extra=log_param)
        logger.info("modes: %s", str(modes), extra=log_param)


    #   TEXT FORMATTING AND EMOJIZING:
        logger.info("Bot Message(Original): %s", str(message), extra=log_param)
        message							= whatsappify_text(message)
        choices_recommendations_header	= whatsappify_text(choices_recommendations_header)
        choices_recommendations_footer	= whatsappify_text(choices_recommendations_footer)
        logger.info("Bot Message(Formatted): %s", str(message), extra=log_param)

    #	Empty message check:
        if message is None or message == "":
            message = "None"
        
        logger.info("message to be sent  %s",str(message), extra=log_param)
    #   Push Message Responses:
        if "template message was sent" in message.lower():
            message = ""
            recommendations = []
            choices = []


    #   Check FeedBack Required:
        if "is_feedback_required" in whatsapp_response["response"]:
            is_feedback_required = whatsapp_response["response"]["is_feedback_required"]


    #   Modes & Modes Params Based Actions:
        if "hide_bot_response" in modes.keys() and modes['hide_bot_response'] == "true":
            message = ""
        
        if "drop_down_choices" in modes_param and modes_param["drop_down_choices"] != [] and recommendations == []:
            for item in modes_param["drop_down_choices"]:
                recommendations.append(item)

    #   OPERATIONS WHEN WHEN FLOW IS ENDED:
        logger.info("is_flow_ended: %s", str(is_flow_ended), extra=log_param)
        logger.info("last_identified_intent_name: %s", str(whatsapp_response["response"].get("last_identified_intent_name")), extra=log_param)
        if is_flow_ended:
            #	Append Sticky Recommendations and choices when flow is ended.
            if "last_identified_intent_name" in whatsapp_response["response"] and whatsapp_response["response"]["last_identified_intent_name"] != None and whatsapp_response["response"]["last_identified_intent_name"] not in greeting_intent_names:
                for sticky_choice in sticky_choices:
                    if sticky_choice not in choices and sticky_choice not in recommendations and sticy_choice != whatsapp_response["response"]["last_identified_intent_name"]:
                        choices.append({"display":sticky_choice,"value":sticky_choice})
                for sticky_recommendation in sticky_recommendations:
                    if sticky_recommendation not in choices and sticky_recommendation not in recommendations and sticky_recommendations != whatsapp_response["response"]["last_identified_intent_name"]:
                        recommendations.append(sticky_recommendation)					

    #	Go Back Check
        is_go_back_enabled = False
        if "is_go_back_enabled" in whatsapp_response["response"]:
            is_go_back_enabled = whatsapp_response["response"]["is_go_back_enabled"]
            save_data(user, json_data={"is_go_back_enabled":is_go_back_enabled},  src="None", channel="WhatsApp", bot_id=BOT_ID, is_cache=True)
            if is_go_back_enabled:
                recommendations.append(go_back_text)


    #   Sending Interactive List for Custom Cards        
        if "is_custom_cards" in modes and modes["is_custom_cards"]=="true":
            list_title = list_interactive_options_title
            if "custom_cards_title" in modes_param:
                list_title = modes_param["custom_cards_title"]
            if "custom_cards" in modes_param:
                custom_cards = modes_param["custom_cards"]
                reply_buttons = []
                TEMP_REVERSE_WHATSAPP_MESSAGE_DICT = {}
                for custom_card in custom_cards:
                    choices.append({"display":custom_card["comment"],"value":custom_card["click"]})    
                    TEMP_REVERSE_WHATSAPP_MESSAGE_DICT[custom_card["comment"]] = custom_card["click"]
                    reply_buttons.append(custom_card["comment"])
                total_options_count = len(reply_buttons)
                is_interactive_sent = False
                if total_options_count <= 3 and len(message) < 1024:
                    if check_interative_capability_for_quick_reply(options=reply_buttons, options_type="recommendations"):
                        sendWhatsAppQuickReplyMessage(ameyo_host, ameyo_api_key, reply_buttons, MESSAGE_HEADER, message, MESSAGE_FOOTER, mobile, "text", None, lang=selected_language)
                        total_options_count = 0   
                        is_interactive_sent = True
                if total_options_count > 3 and total_options_count < 11 and len(message) < 1024:
                    if check_interative_capability_for_list(options=reply_buttons, options_type="recommendations"):
                        BUTTON_HEADER = MESSAGE_HEADER
                        BUTTON_FOOTER = MESSAGE_FOOTER
                        if LIST_HEADER_FOOTER_VISIBLE == False:
                            BUTTON_HEADER = " "
                            BUTTON_FOOTER = " "
                        logger.info("Calling sendWhatsAppInteractiveListMessage", extra=log_param)
                        sendWhatsAppInteractiveListMessage(ameyo_host, ameyo_api_key, list_title, reply_buttons, BUTTON_HEADER, message, BUTTON_FOOTER, mobile, menu_button_text=list_interactive_menu_button_text, extra="None")
                        total_options_count = 0
                        is_interactive_sent = True
                if is_interactive_sent:
                    choices = []
                    recommendations = []
                    message = ""
                    REVERSE_WHATSAPP_MESSAGE_DICT = TEMP_REVERSE_WHATSAPP_MESSAGE_DICT
                    TEMP_REVERSE_WHATSAPP_MESSAGE_DICT = {}


    #   Sending Interactive List for Custom Cards
        if "is_custom_interactive_list" in modes and modes["is_custom_interactive_list"]=="true":
            interactive_data =  modes["interactive_data"]
            logger.info("Calling sendWhatsAppInteractiveListMessageCustom", extra=log_param)
            sendWhatsAppInteractiveListMessageCustom(ameyo_host, ameyo_api_key, mobile, interactive_data)



    #   Sending default Quick reply Buttons and Lists:
        if send_default_quick_reply or send_default_list_options:
            total_options_count = len(choices) + len(recommendations)
            total_media = len(images) + len(videos)
            TEMP_REVERSE_WHATSAPP_MESSAGE_DICT = {}
            BUTTON_DISPLAY_NAMES = []
            message_body = message.replace("$$$","\n\n")
            empty_choices = False
            empty_recommendations = False
            #   QUICK REPL BUTTONS
            if send_default_quick_reply == True:
                if total_options_count <= 3 and len(message_body) < 1024:
                    if check_interative_capability_for_quick_reply(options=choices, options_type="choices") and check_interative_capability_for_quick_reply(options=recommendations, options_type="recommendations"):
                        for choice in choices:
                            if choice["display"] not in BUTTON_DISPLAY_NAMES and len(choice["display"]):
                                BUTTON_DISPLAY_NAMES.append(choice["display"])
                                TEMP_REVERSE_WHATSAPP_MESSAGE_DICT[choice["display"]] = choice["value"]
                            empty_choices = True
                        for recommendation in recommendations:
                            if recommendation not in BUTTON_DISPLAY_NAMES:
                                BUTTON_DISPLAY_NAMES.append(recommendation)
                                TEMP_REVERSE_WHATSAPP_MESSAGE_DICT[recommendation] = recommendation
                            empty_recommendations = True
                    elif check_interative_capability_for_quick_reply(options=choices, options_type="choices") and recommendations == []:
                        for choice in choices:
                            if choice["display"] not in BUTTON_DISPLAY_NAMES and len(choice["display"]):
                                BUTTON_DISPLAY_NAMES.append(choice["display"])
                                TEMP_REVERSE_WHATSAPP_MESSAGE_DICT[choice["display"]] = choice["value"]
                            empty_choices = True
                    elif check_interative_capability_for_quick_reply(options=recommendations, options_type="recommendations") and choices == []:
                        for recommendation in recommendations:
                            if recommendation not in BUTTON_DISPLAY_NAMES and len(recommendation):
                                BUTTON_DISPLAY_NAMES.append(recommendation)
                                TEMP_REVERSE_WHATSAPP_MESSAGE_DICT[recommendation] = recommendation
                            empty_recommendations = True
                    if BUTTON_DISPLAY_NAMES != []:
                        #   Check for Media:
                        button_media_available = False
                        button_media_type = "text"
                        button_media_link = None
                        if total_media == 1:
                            if len(images) == 1 and isinstance(images[0], str) and check_valid_image_url(images[0]):
                                button_media_type = "image"
                                button_media_link = images[0]
                                button_media_available = True
                            elif len(videos) == 1 and isinstance(videos[0], str) and check_valid_video_url(videos[0]):
                                button_media_type = "video"
                                button_media_link = videos[0]
                                button_media_available = True
                        is_send = sendWhatsAppQuickReplyMessage(ameyo_host, ameyo_api_key, BUTTON_DISPLAY_NAMES, MESSAGE_HEADER, message_body, MESSAGE_FOOTER, mobile, button_media_type, button_media_link, lang=selected_language)
                        if is_send:
                            REVERSE_WHATSAPP_MESSAGE_DICT = TEMP_REVERSE_WHATSAPP_MESSAGE_DICT
                            if empty_choices == True:
                                choices = []
                            if empty_recommendations == True:
                                recommendations = []
                            message = ""
                                    
            #   List Interactive Buttons
            if send_default_list_options == True:
                if total_options_count > 3 and total_options_count < 11 and len(message_body) < 1024:
                    if check_interative_capability_for_list(options=choices, options_type="choices") and check_interative_capability_for_list(options=recommendations, options_type="recommendations"):
                        for choice in choices:
                            if choice["display"] not in BUTTON_DISPLAY_NAMES and len(choice["display"]):
                                BUTTON_DISPLAY_NAMES.append(choice["display"])
                                TEMP_REVERSE_WHATSAPP_MESSAGE_DICT[choice["display"]] = choice["value"]
                            empty_choices = True
                        for recommendation in recommendations:
                            if recommendation not in BUTTON_DISPLAY_NAMES:
                                BUTTON_DISPLAY_NAMES.append(recommendation)
                                TEMP_REVERSE_WHATSAPP_MESSAGE_DICT[recommendation] = recommendation
                            empty_recommendations = True
                    elif check_interative_capability_for_list(options=choices, options_type="choices") and recommendations == []:
                        for choice in choices:
                            if choice["display"] not in BUTTON_DISPLAY_NAMES and len(choice["display"]):
                                BUTTON_DISPLAY_NAMES.append(choice["display"])
                                TEMP_REVERSE_WHATSAPP_MESSAGE_DICT[choice["display"]] = choice["value"]
                            empty_choices = True
                    elif check_interative_capability_for_list(options=recommendations, options_type="recommendations") and choices == []:
                        for recommendation in recommendations:
                            if recommendation not in BUTTON_DISPLAY_NAMES and len(recommendation):
                                BUTTON_DISPLAY_NAMES.append(recommendation)
                                TEMP_REVERSE_WHATSAPP_MESSAGE_DICT[recommendation] = recommendation
                            empty_recommendations = True
                    if BUTTON_DISPLAY_NAMES != []:
                        BUTTON_HEADER = MESSAGE_HEADER
                        BUTTON_FOOTER = MESSAGE_FOOTER
                        if LIST_HEADER_FOOTER_VISIBLE == False:
                            BUTTON_HEADER = " "
                            BUTTON_FOOTER = " "
                        logger.info("Calling sendWhatsAppInteractiveListMessage", extra=log_param)
                        is_send = sendWhatsAppInteractiveListMessage(ameyo_host, ameyo_api_key, list_interactive_options_title, BUTTON_DISPLAY_NAMES, BUTTON_HEADER, message_body, BUTTON_FOOTER, mobile, menu_button_text=list_interactive_menu_button_text, extra="None",lang=selected_language)
                        if is_send:
                            REVERSE_WHATSAPP_MESSAGE_DICT = TEMP_REVERSE_WHATSAPP_MESSAGE_DICT
                            if empty_choices == True:
                                choices = []
                            if empty_recommendations == True:
                                recommendations = []
                            message = ""
    


    #   CHOICES:
        choice_dict = {}
        choice_display_list = []
        for choice in choices:
            choice_dict[choice["display"]] = choice["value"]
            choice_display_list.append(choice["display"])
        choice_str = ""
        if choice_display_list != []:
            for index in range(len(choice_display_list)):
                if index%max_choices_recommendations_bubble_size==0 and index != 0:
                    choice_str += "$$$"
                REVERSE_WHATSAPP_MESSAGE_DICT[str(index+1)]=str(choice_dict[choice_display_list[index]])
                choice_str += ask_to_enter_text+" *"+str(index+1)+"* :point_right:  "+str(choice_display_list[index])+"\n"
                if is_compact_recommendations_choices == False:
                    choice_str =+"\n"
            choice_str = whatsappify_text(choice_str)
            reverse_mapping_index = len(choice_display_list)
        logger.info("Choices: %s", str(choice_str), extra=log_param)

        
    #   RECOMMENDATIONS:    
        recommendation_str = ""
        if recommendations != []:
            cleaned_recommendations = []
            for recm in recommendations:
                if isinstance(recm,dict) and "name" in recm:
                    cleaned_recommendations.append(recm["name"])
                else:
                    cleaned_recommendations.append(recm)
            recommendations = cleaned_recommendations
            if choice_str!="":
                for index in range(len(recommendations)):
                    if index%max_choices_recommendations_bubble_size==0:
                        recommendation_str +="$$$"
                    REVERSE_WHATSAPP_MESSAGE_DICT[str(reverse_mapping_index+index+1)]=str(recommendations[index])
                    recommendation_str += ask_to_enter_text+" *"+str(reverse_mapping_index+index+1)+"* :point_right:  "+str(recommendations[index])+"\n"
                    if is_compact_recommendations_choices == False:
                        recommendation_str =+"\n"
            else:
                for index in range(len(recommendations)):
                    if index%max_choices_recommendations_bubble_size==0 and index != 0:
                        recommendation_str +="$$$"
                    REVERSE_WHATSAPP_MESSAGE_DICT[str(index+1)]=str(recommendations[index])
                    recommendation_str += ask_to_enter_text+" *"+str(index+1)+"* :point_right:  "+str(recommendations[index])+"\n"
                    if is_compact_recommendations_choices == False:
                        recommendation_str =+"\n"
            recommendation_str = get_emojized_message(recommendation_str)

        logger.info("Recommendations: %s", str(recommendation_str), extra=log_param)
        logger.info("Choices: %s", str(choice_str), extra=log_param)
        logger.info("Reverse Mapper: %s", str(REVERSE_WHATSAPP_MESSAGE_DICT), extra=log_param)

    #   RESPONSE MODES:
    #   1.SANDWICH CHOICES: sending choices in between to small texts in a single bubble:
        is_sandwich_choice = False # is sandwich choice sent flag: 
        if "is_sandwich_choice" in modes.keys() and modes['is_sandwich_choice'] == "true":
            choice_position = "1" # 2nd position          
            is_single_message = True
            is_sandwich_choice = True
        else:
            choice_position = ""
            is_single_message = False
            
    #   2.STICKY CHOICES: sending choices and message in same bubble.
        message_with_choice = False 
        if "message_with_choice" in modes.keys() and modes["message_with_choice"] == "true":
            message_with_choice = True
        if recommendation_str == "" and choice_str == "":
            message_with_choice = False

    #   3. BOT LINK CARDS: sending cards containing urls/links
        if "card_for_links" in modes.keys() and modes["card_for_links"] == "true":
            card_text = ""
            for card in cards:
                redirect_url = str(card["link"]) if card["link"] is not None else ""
                title = str(card["title"] if card["title"] is not None else "")
                card_text += " :point_right: *"+title+"* \n   " 
                card_text += " :link: "+redirect_url+"$$$"
            message+= get_emojized_message("$$$"+ card_text)
            cards = []


    #   SEND SINGLE BUBBLE TEXT:
        final_text_message = ""
        for count, small_message in enumerate(message.split("$$$"), 0):
            if str(choice_position)!="" and str(choice_position) == str(count):
        # 1. Sandwich choices text:
                if len(choice_str)>0 and len(recommendation_str)>0:
                    final_text_message += choice_str + recommendation_str
                    choice_str = ""
                    recommendation_str = ""
                if len(choice_str)>0:
                    final_text_message += choices_recommendations_header + choice_str + choices_recommendations_footer
                if len(recommendation_str)>0:    
                    final_text_message += choices_recommendations_header + recommendation_str + choices_recommendations_footer
                final_text_message += small_message + "$$$"
            else:
                final_text_message += small_message + "$$$"
        if is_single_message:
            final_text_message = final_text_message.replace("$$$", "")
            if final_text_message!= "":
                if "http://" in final_text_message or "https://" in final_text_message :
                    final_text_message = youtube_link_formatter(final_text_message)
                    send_status = sendWhatsAppTextMessage(ameyo_host, ameyo_api_key, final_text_message, str(mobile), preview_url=True)
                    is_sandwich_choice = True
                else:
                    send_status = sendWhatsAppTextMessage(ameyo_host, ameyo_api_key, final_text_message, str(mobile), preview_url=False)
                    is_sandwich_choice = True
                recommendation_str = ""
                choice_str = ""
        else:
            if message_with_choice == True:
        # 2. Sticky choices text:
                final_text_message = message.replace("$$$", "")
                if len(choice_display_list)>0 and len(recommendations)>0:
                    final_text_message = final_text_message.strip("\n") + "\n\n" + choices_recommendations_header + choice_str.replace("$$$",  "").strip("\n") + recommendation_str.replace("$$$", "").strip("\n") + choices_recommendations_footer
                    choice_display_list = []
                    recommendations = []
                    logger.info("Sticky choices + recommendations : %s", str(final_text_message), extra=log_param)
                if len(choice_display_list)>0:
                    final_text_message = final_text_message.strip("\n") + "\n\n" + choices_recommendations_header + choice_str.replace("$$$",  "").strip("\n") + choices_recommendations_footer
                    logger.info("Sticky choices: %s", str(final_text_message), extra=log_param)
                    
                if len(recommendations)>0:
                    final_text_message = final_text_message.strip("\n")+ "\n\n" + choices_recommendations_header + recommendation_str.replace("$$$", "").strip("\n") + choices_recommendations_footer
                    final_text_message = final_text_message.replace("\n\n\n","\n")
                    logger.info("Sticky recommendations: %s", str(final_text_message), extra=log_param)

                if len(choice_display_list)>0:
                    final_text_message = final_text_message + choice_str.replace("$$$",  "")
                    logger.info("Sticky choices: %s", str(final_text_message), extra=log_param)

                if "http://" in final_text_message or "https://" in final_text_message :
                    final_text_message = youtube_link_formatter(final_text_message)
                    send_status = sendWhatsAppTextMessage(ameyo_host, ameyo_api_key, final_text_message, str(mobile), preview_url=True)
                else:
                    send_status = sendWhatsAppTextMessage(ameyo_host, ameyo_api_key, final_text_message, str(mobile), preview_url=False)
                recommendation_str = ""
                choice_str = ""
            else:
        # 3. Regular single text:
                logger.info("Regular Small Text: %s", str(final_text_message), extra=log_param)
                for small_message in final_text_message.split("$$$"):
                    if small_message != "":
                        if "http://" in small_message or "https://" in small_message :
                            small_message = youtube_link_formatter(small_message)
                            send_status = sendWhatsAppTextMessage(ameyo_host, ameyo_api_key, small_message, str(mobile), preview_url=True)
                        else:
                            send_status = sendWhatsAppTextMessage(ameyo_host, ameyo_api_key, small_message, str(mobile), preview_url=False)
                        time.sleep(0.07)


    #   SENDING CARDS, IMAGES, VIDEOS:
        logger.info("Cards: %s", str(cards), extra=log_param)
        logger.info("Images: %s", str(images), extra=log_param)
        logger.info("Videos: %s", str(videos), extra=log_param)

        if len(cards) > 0:
            # Cards with documnet links:  Use 'card_with_document:true' in modes
            if "card_with_document" in modes.keys() and modes["card_with_document"] == "true":
                logger.info("Inside Cards with documents", extra=log_param)
                for card in cards:
                    doc_caption = str(card["title"])
                    doc_url = str(card["link"])
                    logger.info("DOCUMENT NAME: %s", str(doc_caption), extra=log_param)
                    logger.info("DOCUMENT URL: %s",str(doc_url), extra=log_param)
                    try:
                        send_status = sendWhatsAppMediaMessage(ameyo_host, ameyo_api_key, "document",str(doc_url), str(mobile), caption = None)
                        logger.info("Is Card sent: %s", str(send_status), extra=log_param)
                    except  Exception as E:
                        logger.error("Cannot send card with document: %s", str(E), extra=log_param)
            else:     
                #Cards with text, link or images
                card_str = ""
                for index, card in enumerate(cards):
                    logger.info("Inside Regular Card", extra=log_param)
                    title = str(card["title"])
                    content = str("\n" + card["content"] + "\n") if card["content"] != "" else ""
                    image_url = str(card["img_url"])
                    redirect_url = youtube_link_formatter(str(card["link"]))
                    caption = "*" + title + "* " + content + " " + redirect_url
                    if image_url != "":
                        logger.info("Card Image available", extra=log_param)
                        if "https:" in caption and "/?" in caption:
                            send_status = sendWhatsAppMediaMessage(ameyo_host, ameyo_api_key, "image",str(image_url), str(mobile), caption = caption)
                            logger.info("Is Card with image sent: %s", str(send_status), extra=log_param)
                            if send_status == False:
                                send_status = sendWhatsAppMediaMessage(ameyo_host, ameyo_api_key, 'image', str(image_url), mobile, caption=None)
                                logger.info("Is Card with image sent: %s", str(send_status), extra=log_param)
                                send_status = sendWhatsAppTextMessage(ameyo_host, ameyo_api_key, str(get_emojized_message(caption)), mobile, preview_url=True)
                                logger.info("Is Card with image 's caption sent: %s", str(send_status), extra=log_param)
                        else:
                            send_status = sendWhatsAppMediaMessage(ameyo_host, ameyo_api_key, 'image', str(image_url), mobile, caption=caption)
                            logger.info("Is Card with image sent: %s", str(send_status), extra=log_param)
                    else:
                        if index%max_cards_bubble_size == 0:
                            card_str += "$$$"
                        card_str += caption + "\n\n"
                        logger.info("Is Card with link sent: %s", str(send_status), extra=log_param)
                if card_str!= "":
                    time.sleep(0.05)
                    for card_bubble in card_str.split("$$$"):
                        if card_bubble.strip() == "":
                            continue
                        send_status = sendWhatsAppTextMessage(ameyo_host, ameyo_api_key, str(get_emojized_message(card_bubble)), str(mobile), preview_url=True)
                    
        if len(videos) > 0:
            logger.info("== Inside Videos ==", extra=log_param)
            for i in range(len(videos)):
                logger.info("== Inside Videos ==", extra=log_param)
                if isinstance(videos[i], dict) and 'video_link' in str(videos[i]):
                    video_url = str(videos[i]['video_link'])
                    video_caption = None
                    if  'content' in videos[i] and videos[i]["content"] != "":
                        logger.info("== Video with caption ==", extra=log_param)
                        video_caption = videos[i]["content"]
                    if check_valid_video_url(video_url):
                        send_status = sendWhatsAppMediaMessage(ameyo_host, ameyo_api_key, 'video', str(video_url), mobile, caption=video_caption)
                    else:
                        video_url = youtube_link_formatter(video_url)
                        video_link_with_caption = video_caption + "\n\n" + video_url if video_caption != None else video_url
                        send_status = sendWhatsAppTextMessage(ameyo_host, ameyo_api_key, video_link_with_caption, mobile, preview_url=True)
                    logger.info("Is Video sent: %s", str(send_status), extra=log_param)
                else:
                    video_url = youtube_link_formatter(str(videos[i]))
                    send_status = sendWhatsAppTextMessage(ameyo_host, ameyo_api_key, video_url, str(mobile), preview_url=True)
                    logger.info("Is Video sent: %s", str(send_status), extra=log_param)

        if len(images) > 0:
            logger.info("== Inside Images ==", extra=log_param)
            for i in range(len(images)):
                if isinstance(images[i], dict) and 'img_url' in images[i]:
                    image_url = images[i]["img_url"]
                    image_caption = None
                    if  'content' in images[i] and images[i]["content"] != "":
                        logger.info("== Image with caption ==", extra=log_param)
                        image_caption = images[i]["content"] 
                    send_status = sendWhatsAppMediaMessage(ameyo_host, ameyo_api_key, 'image', str(image_url), mobile, caption=image_caption)
                    logger.info("Is Image sent: %s", str(send_status), extra=log_param)
                else:
                    logger.info("== Image without caption ==")
                    send_status = sendWhatsAppMediaMessage(ameyo_host, ameyo_api_key, 'image', str(images[i]), mobile, caption=None)
                    logger.info("Is Image sent: %s", str(send_status), extra=log_param)


    #   SENDING CHOICES AND RECOMMENDATIONS BOTH:
        if len(choice_str)>0 and len(recommendation_str)>0:
            mixed_choice = choice_str+""+recommendation_str
            time.sleep(0.05)
            send_status = sendWhatsAppTextMessage(ameyo_host, ameyo_api_key, mixed_choice.replace("\n\n\n","").replace("$$$",""), str(mobile), preview_url=False)
            logger.info("Is Mixed Choices sent: %s", str(send_status), extra=log_param)
            choice_str = ""
            recommendation_str = ""


    #   SENDING CHOICES:
        if len(choice_str)>0:
            choice_str = choices_recommendations_header + choice_str + choices_recommendations_footer
            if "$$$" in choice_str:
                for bubble in choice_str.split("$$$"):
                    if bubble.strip() == "":
                        continue
                    time.sleep(0.07)
                    send_status = sendWhatsAppTextMessage(ameyo_host, ameyo_api_key, bubble, str(mobile), preview_url=False)
                logger.info("Is choices sent: %s", str(send_status), extra=log_param)
            else:
                time.sleep(0.07)
                send_status = sendWhatsAppTextMessage(ameyo_host, ameyo_api_key, choice_str, str(mobile), preview_url=False)
                logger.info("Is choices sent: %s", str(send_status), extra=log_param)


    #   SENDING RECOMMENDATIONS:
        if len(recommendation_str)>0:
            recommendation_str = choices_recommendations_header + recommendation_str + choices_recommendations_footer
            if "$$$" in recommendation_str:
                for bubble in recommendation_str.split("$$$"):
                    if bubble.strip() == "":
                        continue
                    time.sleep(0.05)
                    send_status = sendWhatsAppTextMessage(ameyo_host, ameyo_api_key, bubble, str(mobile), preview_url=False)
                    logger.info("Is recommendations sent: %s", str(send_status), extra=log_param)
            else:
                time.sleep(0.05)
                send_status = sendWhatsAppTextMessage(ameyo_host, ameyo_api_key, recommendation_str, str(mobile), preview_url=False)
                logger.info("Is recommendations sent: %s", str(send_status), extra=log_param)


    #   SENDING LIVECHAT NOTIFICATION:        
        # if "is_livechat" in modes and modes["is_livechat"] == "true":
        #     logger.info("INSIDE LIVECHAT NOTIFICATION", extra=log_param)
        #     livechat_notification = create_and_enable_livechat(mobile,"-1", "WhatsApp", bot_obj, message)
        #     logger.info("LIVECHAT NOTIFICATION: %s", str(livechat_notification), extra=log_param)
        #     if livechat_notification != "":
        #         if selected_language != "en":
        #             livechat_notification = get_translated_text(livechat_notification, selected_language, EasyChatTranslationCache)
        #         sendWhatsAppTextMessage(ameyo_host, ameyo_api_key, livechat_notification, str(mobile))


    #   CHECK IF LANGUAGE RESPONSE REQUIRED
        if change_language_response_required(user_id, BOT_ID, bot_obj, is_whatsapp_welcome_response):
            language_str, REVERSE_WHATSAPP_MESSAGE_DICT = get_language_change_response(str(user_id), BOT_ID, REVERSE_WHATSAPP_MESSAGE_DICT)
            logger.info("change_language_response_required: "+str(language_str), extra=log_param)
            logger.info("change_language_response_required: "+str(REVERSE_WHATSAPP_MESSAGE_DICT), extra=log_param)
            if language_str != "":
                language_str = get_emojized_message(language_str)
                send_status = sendWhatsAppTextMessage(ameyo_host, ameyo_api_key, language_str, str(mobile), preview_url=False)
                logger.info("Is change language response sent: %s",
                            str(send_status), extra=log_param)
                save_data(user, json_data={"CHANGE_LANGUAGE_TRIGGERED": True},
                          src="None", channel="WhatsApp", bot_id=BOT_ID, is_cache=True)


    #   SENDING Helpful_Unhelpful_Choices:
        if is_feedback_required:
            helpful = helpful_intent_name
            unhelpful = unhelpful_intent_name

            feedback_str = feedback_question #get_emojized_message("Enter :thumbs_up: for "+helpful+"\n\nEnter :thumbs_down: for "+unhelpful)
            feedback_buttons = [feedback_option_yes, feedback_option_no]
            time.sleep(0.8)
            is_send = sendWhatsAppQuickReplyMessage(ameyo_host, ameyo_api_key, feedback_buttons, MESSAGE_HEADER, feedback_str, MESSAGE_FOOTER, mobile, lang=selected_language)
            if is_send:
                REVERSE_WHATSAPP_MESSAGE_DICT[feedback_option_yes] = helpful
                REVERSE_WHATSAPP_MESSAGE_DICT[feedback_option_no] = unhelpful
                feedback_dict = {"is_intent_feedback_asked":True}
                save_data(user, json_data=feedback_dict,  src="None", channel="WhatsApp", bot_id=BOT_ID,  is_cache=True)

        logger.info("REVERSE_WHATSAPP_MESSAGE_DICT: %s", str(REVERSE_WHATSAPP_MESSAGE_DICT), extra=log_param)
        save_data(default_user_obj, json_data={"REVERSE_WHATSAPP_MESSAGE_DICT":REVERSE_WHATSAPP_MESSAGE_DICT},  src="None", channel="WhatsApp", bot_id=DEFAULT_BOT_ID,  is_cache=True)

        
        response["status_code"] = 200
        response["status_message"] = "Request processed successfully."
        logger.info("AMEYOCallBack: %s",str(response), extra=log_param)
        return response    
    except Exception as E:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        response["status_message"] = str(E) + str(exc_tb.tb_lineno)
        logger.error("AMEYOCallBack: %s at %s", str(E), str(exc_tb.tb_lineno), extra=log_param)
        return response