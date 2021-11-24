
# Run for First Time START
from EasyChatApp.models import *
from django.contrib.auth import get_user_model

p_word = 'allincall@123'
u_list = ['sandeep.s@allincall.in','vraj.sheth@allincall.in','anuj.shah@allincall.in','vinay.tomar@allincall.in',]

AccessType.objects.create(name="Full Access")
AccessType.objects.create(name="Intent Related")
AccessType.objects.create(name="Bot Setting Related")
AccessType.objects.create(name="Lead Gen Related")
AccessType.objects.create(name="Form Assist Related")
AccessType.objects.create(name="Self Learning Related")
AccessType.objects.create(name="Analytics Related")
AccessType.objects.create(name="EasyDrive Related")
AccessType.objects.create(name="EasyDataCollection Related")

full_access = AccessType.objects.all()[0]
for u in u_list:
    user = User.objects.create(
            username=u, 
            password=p_word,
            is_staff=True, 
            is_superuser=True, 
            role=BOT_BUILDER_ROLE,
            status="1",
            is_chatbot_creation_allowed="1")

    for bot in Bot.objects.all():
        bot.users.add(user)
        obj = AccessManagement.objects.create(user=user, bot=bot)
        obj.access_type.add(full_access)
        obj.save()

# Run for First Time END

# Initial Recommendation STARTS
from EasyChatApp.models import *
from EasyChatApp.utils import *
import json


user = Profile.objects.all().last()
for bot_r in BotChannel.objects.all():
    k = json.loads(bot_r.initial_messages)
    pk_list = []
    initial_messages_name_list = k["items"]
    #print(initial_messages_name_list)
    if initial_messages_name_list != []:
        bot_obj = bot_r.bot
        channel = bot_r.channel
        for name in initial_messages_name_list:
            tree, status_re_sentence, suggestion_list = return_next_tree(user, bot_obj, name, channel,"None")
            if tree:
                try:
                    intent_obj = Intent.objects.get(tree=tree)
                    pk_list.append(intent_obj.pk)
                except:
                    try:
                        tree, status_re_sentence, suggestion_list = return_next_tree(user, bot_obj, suggestion_list[0], channel, "None")
                        if tree:
                            intent_obj = Intent.objects.get(tree=tree)
                            pk_list.append(intent_obj.pk)
                    except:
                        pass
        k['items'] = pk_list
        #print(pk_list)
        bot_r.initial_messages = json.dumps(k)
        print(bot_r.initial_messages)
        bot_r.save()

# Initial Recommendation ENDS



# WebHook
from EasyChatApp.utils import *
from EasyChatApp.models import *
from django.conf import settings

import time
import json
import sys
import requests
import threading

def clevertap_upload_profile(data, clever_tap_auth):
    """Function to be called when user comes for the first time and is authenticated"""
    logger.error("INSIDE CLEVER TAP UPLOAD PROFILE")
    is_send = False
    try:
        clever_tap_id = clever_tap_auth["clever_tap_id"]
        clever_tap_pass = clever_tap_auth["clever_tap_pass"]    
        profile_data = data["profile"]
        identity = data["identity"]
        url = "https://in1.api.clevertap.com/1/upload"
        headers = {
        'X-CleverTap-Account-Id': clever_tap_id,
        'X-CleverTap-Passcode': clever_tap_pass,
        'Content-Type': 'application/json'
        }
        payload = json.dumps({
            "d":[
                {	"identity": identity,
                    "objectId": identity,
                    "type":"profile",
                    "profileData":profile_data
                }
            ]
        })
        logger.error(str(payload))
        r = requests.request("POST", url, headers=headers, data = payload)
        content = json.loads(r.text)
        print(content)
        if str(r.status_code) == "200":
            if content["status"] == "success":
                is_send = True
        else:
            is_send = False
    except Exception as E:
        print(E)
        pass
    return is_send

def clevertap_upload_event(data, clever_tap_auth):
    """Function to be called whenever there is input from user and output from bot"""
    logger.error("INSIDE CLEVER TAP UPLOAD EVENT")
    
    is_send = False
    try:
        clever_tap_id = clever_tap_auth["clever_tap_id"]
        clever_tap_pass = clever_tap_auth["clever_tap_pass"]    
        evtName = data["evtName"]
        evtData = data["evtData"]
        identity = data["identity"]
        url = "https://in1.api.clevertap.com/1/upload"
        headers = {
        'X-CleverTap-Account-Id': clever_tap_id,
        'X-CleverTap-Passcode': clever_tap_pass,
        'Content-Type': 'application/json'
        }
        payload = json.dumps({
            "d": [
                {
                    "identity": identity,
                    "type": "event",
                    "evtName": evtName,
                    "evtData": evtData
                }
            ]
        })
        logger.error(str(payload))
        r = requests.request("POST", url, headers=headers, data = payload)
        content = json.loads(r.text)
        logger.error(str(content))
        print(content)
        if str(r.status_code) == "200":
            if content["status"] == "success":
                is_send = True
        else:
            is_send = False      
        logger.error(str(is_send))    
    except Exception as E:
        print(E)
        pass
    return is_send

def get_whatsapp_file_attachment_v1(userid, password, message):
    filename = None
    try:
        message_dict = json.loads(message)
        attachment_id = message_dict["id"]
        mime_type = message_dict["mime_type"]
        ext = mime_type.split("/")[-1]
        filename = attachment_id+"."+ext
        filename = settings.MEDIA_ROOT+"WhatsAppMedia/"+filename
        remote_url = "https://unify.smsgupshup.com/WhatsApp/apis/getMedia.php?userid="+str(userid)+"&password="+str(password)+"&mediaid="+str(attachment_id)
        logger.info("Remote URL: %s", remote_url)
        save_file_from_remove_server_to_local(remote_url, filename)
    except Exception as e:
        logger.error("is_whatsapp_file_attachment: %s", e)

    return filename


def get_whatsapp_file_attachment(userid, password, message):
    filename = None
    try:
        message_dict = json.loads(message)
        signature = message_dict["signature"]
        mime_type = message_dict["mime_type"]
        remote_url = message_dict["url"]+str(signature)
        ext = mime_type.split("/")[-1]
        
        filename = None
        if "caption" in message_dict:
            filename = message_dict["caption"]
        else:
            filename = signature+"."+ext
            
        filename_bkp = filename
        filename = settings.MEDIA_ROOT+"WhatsAppMedia/"+filename
        save_file_from_remove_server_to_local(remote_url, filename)
        
        filename = settings.EASYCHAT_HOST_URL+"/files/WhatsAppMedia/"+filename_bkp
    except Exception as e:
        logger.error("is_whatsapp_file_attachment: %s", e)

    return filename

def get_message_from_reverse_whatsapp_mapping(user_message, mobile):
    message = None
    try:
        user = Profile.objects.get(user_id=str(mobile))
        data_obj = Data.objects.filter(user=user, variable="REVERSE_WHATSAPP_MESSAGE_DICT")[0]
        data_dict = json.loads(str(data_obj.value))
        if str(user_message) in data_dict:
            message = data_dict[str(user_message)]
    except Exception as e:
        logger.error("get_message_from_reverse_whatsapp_mapping: %s", e)

    return message

def is_user_employee(mobile_number):
    from EasyChatApp.models import EmployeeDetails
    import json
    import requests

    is_verified_user = None
    employee_details = {}
    try:
        employee_details_obj = EmployeeDetails.objects.get(mobile_number=str(mobile_number)[-10:])
        employee_details = json.loads(employee_details_obj.details)
        return True, employee_details
    except Exception as e:
        logger.error("is_user_employee: %s", e)
        return None, {}


def get_verified_employee_details_obj(mobile_number):
    from EasyChatApp.models import EmployeeDetails
    try:
        return EmployeeDetails.objects.get(mobile_number=str(mobile_number)[-10:])
    except Exception as e:
        return None

def recursive_call(text, mobile_number, waNumber):
    try:
        data = {'mobile': mobile_number, 'type': 'text', 'text': text, 'timestamp': str(int(time.time())), 'waNumber': waNumber}
        r = requests.post(url=settings.EASYCHAT_HOST_URL + "/chat/query/whatsapp", data=json.dumps(data), headers={"Content-Type":"application/json"})
    except Exception as e:
        logger.error(e)

def whatsapp_webhook(request_packet):
    response = {}
    response["status_code"] = 500
    response["status_message"] = ""
    try:
        mobile = request_packet["mobile"]
        mobile = remo_html_from_string(str(mobile))

        AUTHENTICATION_NUMBER = settings.AUTHENTICATION_NUMBER
        AUTHENTICATION_KEY = settings.AUTHENTICATION_KEY
        
        # CLEVER TAP AUTH:
        clever_tap_auth = {
            "clever_tap_id":"TEST-K99-R79-575Z",
            "clever_tap_pass":"CRS-IMV-UTKL"
        }

        is_attachement = True
        message = None
        filepath = None
        
        # if "type" not in request_packet:
        #     if request_packet["text"].find("mime_type")!=-1:
        #         request_packet["type"] = "document"
        #         request_packet["document"] = request_packet["text"]
        #         filepath = get_whatsapp_file_attachment_v1(AUTHENTICATION_NUMBER, AUTHENTICATION_KEY, request_packet["text"])
        #         message = "attachment"
        #     else:
        #         request_packet["type"] = "text"
        #         message = request_packet["text"]
        #         is_attachement = False
        # else:

        if request_packet["type"]=="text":
            is_attachement = False
            
        if is_attachement:
            document = request_packet[request_packet["type"]]
            filepath = get_whatsapp_file_attachment(AUTHENTICATION_NUMBER, AUTHENTICATION_KEY, document)
            message = "attachment"
        else:
            message = request_packet["text"]

        waNumber = request_packet["waNumber"]
        waNumber = remo_html_from_string(str(waNumber))
        channel_params = {}

        logger.info("Mobile Number: %s", mobile)
        logger.info("Text: %s", message)

        bot_search_id = 4
        is_verified_user = None
        employee_details = {}
        
        
        
        #logger.error("All Started Here 0001")
        is_verified_user, employee_details = is_user_employee(str(mobile))
        #logger.error(f"All Started Here 0002 ::is_verified_user -  {is_verified_user} || employee_details - {employee_details}")
        channel_params = employee_details.copy()
        channel_params["is_verified_employee"] = is_verified_user
        logger.info("is_verified_user: %s", is_verified_user)
        logger.info("employee_details: %s", json.dumps(employee_details))

        if not check_whether_user_exist(str(mobile)):
            logger.info(" == FIRST TIME USER ==")
            #logger.error("All Started Here 0004")
            # call upload profile api here: 
            #logger.error(f"All Started Here 007 = employee_details {str(type(employee_details))} - {employee_details}")
            if employee_details:
                #logger.error("All Started Here 0005")
                user_profile_data = {
                    "profile":{
                        "User_id":employee_details["EmployeeId"] if employee_details["EmployeeId"] is not None else "N.A",               # Emp id
                        "Name": employee_details["EmpName"] if employee_details["EmpName"] is not None else "N.A",                    # Emp Name
                        "Email": employee_details["EmailId"] if employee_details["EmailId"] is not None else "N.A",                   # Emp email  
                        "Phone": employee_details["EmployeeMobileNumber"] if employee_details["EmployeeMobileNumber"] is not None else "N.A",      # Emp Phone
                        "is_user_verified":is_verified_user                     # is Emp verified
                    },
                    "identity":str(mobile)                                           # User Chat Id: e.g Mobile number incase of whatsapp  
                }  
                #logger.error(f"All Started Here 0007  PD - {str(user_profile_data)}")
            else:
                #logger.error("All Started Here 0006")
                user_profile_data = {
                    "profile":{
                        "User_id":"N.A",                                        # Emp id
                        "Name": "N.A",                                          # Emp Name
                        "Email": "N.A",                                         # Emp email  
                        "Phone": "N.A",                                         # Emp Phone
                        "is_user_verified":is_verified_user                     # is Emp verified
                    },
                    "identity":str(mobile)                                           # User Chat Id: e.g Mobile number incase of whatsapp  
                }
            logger.info("CLEVER PROFILE DATA: %s", str(user_profile_data))    
            profile_upload_status = clevertap_upload_profile(user_profile_data, clever_tap_auth)
            logger.info("Clever Tap Profile Upload Status: %s", str(profile_upload_status))
            
            welcome_message = """Welcome to ICICI Bank’s Automated Chatbot Service for applicants and employees. By continuing the conversation you are accepting our terms and conditions.\n\n Terms and conditions: https://www.icicicareers.com/website/pdf/TC_ChatBOT.pdf\n\nType 1 to proceed further."""
            sendWhatsAppTextMessage(AUTHENTICATION_NUMBER, AUTHENTICATION_KEY, welcome_message, str(mobile))
            set_user(str(mobile), message)
            user = Profile.objects.get(user_id=str(mobile))
            response["status_code"]="200"
            response["status_message"]="SUCCESS"
            save_data(user, json_data={"REVERSE_WHATSAPP_MESSAGE_DICT":{"1":message}}, is_cache=True)
            return response
        
        #logger.error("All Started Here 0003")
        if filepath!=None:
            logger.info("Media Attachment found filepath: %s", filepath)
            message = "attachment"
        else:
            logger.info("No media file attachment in WhatsApp message.")

        reverse_message=get_message_from_reverse_whatsapp_mapping(message, mobile)
        is_message_clicked = False
        if reverse_message!=None:
            message=reverse_message
            is_message_clicked = True


        channel_params["is_message_clicked"] = is_message_clicked
        channel_params["AttachmentFile"] = filepath
        user_query = str(message)

        # AUthenticate OJP BOT Invocation:
        invokers = ['internal transfer', 'ojp flow', 'ojp at icici bank', 'talk to ojp', 'open job postings', 'ojp', 'open job posting', 'talk to o j p', 'talk to o.j.p', '?talk to ojp?']
        if message.lower() in invokers: 
            logger.error("INVOKE QUERY: %s", str(message.lower()))
            logger.error("INSIDE CHECK FOR OJP  AUTH")
            logger.error("IS VERFIIED USER: %s", str(is_verified_user))
            if is_verified_user is None:
                logger.error("Sending OJP AUTH MSG....")
                message = "Apply for OJP"
            else:
                message = "Talk to OJP"
                logger.error("EMPLOYEE IS VERIFIED FOR OJP")
            whatsapp_response = execute_query(mobile, bot_search_id, "uat", message, "en", "WhatsApp", json.dumps(channel_params))
            logger.error("OJP WHATSAPP RESPONSE: %s", str(whatsapp_response))
        else:
            whatsapp_response = execute_query(mobile, bot_search_id, "uat", message, "en", "WhatsApp", json.dumps(channel_params))
            logger.info("WHATSAPP RESPONSE: %s", str(whatsapp_response))
        
        message = whatsapp_response["response"]["text_response"]["text"]
        message = message.replace("<br>","\n")
        message = message.replace("<b>","*")
        message = message.replace("</b>","*")
        message = message.replace("<i>","_")
        message = message.replace("</i>","_")


        # Go Back Check
        is_go_back_enabled = False
        if "is_go_back_enabled" in whatsapp_response["response"]:
            is_go_back_enabled = whatsapp_response["response"]["is_go_back_enabled"]
            save_data(user, json_data={"is_go_back_enabled":is_go_back_enabled},  src="None", channel="WhatsApp", bot_id="2", is_cache=True)


        message = get_emojized_message(message)
        bot_response = message
        
        # import re
        # all_url_in_message = re.findall(r"""(?<=<a href=')[^']*""", message)
        # logger.info("--------------3333333333-----*********8")
        # logger.info(all_url_in_message)
        # if len(all_url_in_message):
        #     message = "Please click here https://icicihr.allincall.in"+all_url_in_message[0]+" to download the responses."
        
        
        for small_message in message.split("$$$"):
            send_status = sendWhatsAppTextMessage(AUTHENTICATION_NUMBER, AUTHENTICATION_KEY, small_message, str(mobile), is_unicode_text=True)
            time.sleep(5)

        recommendations = whatsapp_response["response"]["recommendations"]

        for choice in whatsapp_response["response"]["choices"]:
            recommendations.append(choice["display"])

        if "Helpful" in recommendations:
            recommendations.remove("Helpful")

        if "Unhelpful" in recommendations:
            recommendations.remove("Unhelpful")

        user = Profile.objects.get(user_id=str(mobile))

        is_conversation_continue = False
        if "continue_conversation" in whatsapp_response["response"]["text_response"]["modes"]:
            if whatsapp_response["response"]["text_response"]["modes"]["continue_conversation"]=="true":
                is_conversation_continue = True
                
        logger.info("is_conversation_continue: %s", is_conversation_continue)

        if send_status:

            response["status_code"] = 200
            response["status_message"] = "Request processed successfully."
            
            images = whatsapp_response["response"]["images"]
            videos = whatsapp_response["response"]["videos"]
            cards = whatsapp_response["response"]["cards"]
        
            if len(cards)>0:
                for card in cards:
                    image_url = card["img_url"]
                    redirect_url = card["link"]
                    caption = card["title"]
                    if redirect_url != '':
                        caption_redirect_url = str(caption)+"\n"+str(redirect_url)
                    else:
                        caption_redirect_url = str(caption)
                    
                    sendWhatsAppMediaMessage(AUTHENTICATION_NUMBER, AUTHENTICATION_KEY, "Image", str(
                        image_url), caption_redirect_url, "ICICI Bank", str(mobile))
                        
            if len(images) > 0 and len(videos) > 0:
                sendWhatsAppMediaMessage(AUTHENTICATION_NUMBER, AUTHENTICATION_KEY, "Image", str(
                    images[0]), str(videos[0]), "ICICI Bank", str(mobile))
            elif len(videos) > 0:
                sendWhatsAppTextMessage(AUTHENTICATION_NUMBER, AUTHENTICATION_KEY, str(
                    videos[0]), str(mobile), preview_url="true")
            elif len(images) > 0:
                caption = "ICICI Bank"
                if str(whatsapp_response["bot_id"])=="52":
                    caption = "Digital ER Service"
                if str(whatsapp_response["bot_id"])=="53":
                    caption = "Hello and Welcome to OJP"
                
                sendWhatsAppMediaMessage(AUTHENTICATION_NUMBER, AUTHENTICATION_KEY, "Image", str(
                    images[0]), caption, caption, str(mobile))

            time.sleep(1)
            REVERSE_WHATSAPP_MESSAGE_DICT = {}
            
            if len(recommendations)>0:
                recommendation_str = ""
                if whatsapp_response["response"]["is_flow_ended"]:
                    recommendation_str += "\n\nYou can also ask me queries as follows :point_down::\n\n"
                else:
                    recommendation_str += "\n\nSelect one of the following :point_down::\n\n"
                for index in range(len(recommendations)):
                    REVERSE_WHATSAPP_MESSAGE_DICT[str(index+1)]=str(recommendations[index])
                    recommendation_str += "Enter *"+str(index+1)+"* :point_right:  "+str(recommendations[index])+"\n"
                if is_go_back_enabled:
                    REVERSE_WHATSAPP_MESSAGE_DICT[ str(len(recommendations)) ]= "Go Back"
                    recommendation_str += "Enter *"+str(len(recommendations))+"* :point_right:  Go Back \n\n"
                message = recommendation_str
                bot_response += "<br><br><br>"+str(recommendation_str)
                message = get_emojized_message(message)
                send_status = sendWhatsAppTextMessage(AUTHENTICATION_NUMBER, AUTHENTICATION_KEY, message, str(mobile), is_unicode_text=True)
                time.sleep(1.5)
                
            elif is_go_back_enabled:
                REVERSE_WHATSAPP_MESSAGE_DICT["1"]= "Go Back"
                recommendation_str += "Enter *1* :point_right:  Go Back \n\n"
                message = recommendation_str
                bot_response += "<br><br><br>"+str(recommendation_str)
                message = get_emojized_message(message)
                send_status = sendWhatsAppTextMessage(AUTHENTICATION_NUMBER, AUTHENTICATION_KEY, message, str(mobile), is_unicode_text=True)
                time.sleep(1.5)

                
                
                #if str(whatsapp_response["bot_id"])=="48":
                    #message = recommendation_str
                #elif str(whatsapp_response["bot_id"])=="52":
                    #message = recommendation_str + "\n\nFor more information,\n:earth_americas: Visit - ICICI Universe Page > Human Resources\n:phone: Call us at +91 22-7187-2500"
                #elif str(whatsapp_response["bot_id"])=="53":
                    #message = recommendation_str + "\n\nFor more information,\n:earth_americas: Visit - ICICI Universe Page > Human Resources\n:phone: Call us at +91-22-71872500"
                #elif str(whatsapp_response["bot_id"])=="47":
                    #message = recommendation_str + "\n\nFor more information,\n:earth_americas: Call us at +91-22-71872500"    
                #elif str(whatsapp_response["bot_id"])=="55":
                    #message = recommendation_str  
                #else:
                    #message = recommendation_str + "\n\nFor more information,\n:earth_americas: Visit at www.icicicareers.com\n:email: email us at icicicareers@icicibank.com\n:phone: Call us at +91 22-7187-2500"


                if is_conversation_continue==False and str(whatsapp_response["bot_id"])!="54":
                    send_status = sendWhatsAppTextMessage(AUTHENTICATION_NUMBER, AUTHENTICATION_KEY, message, str(mobile), is_unicode_text=True)
                    time.sleep(1.5)

                
                    


            save_data(user, json_data={"REVERSE_WHATSAPP_MESSAGE_DICT":REVERSE_WHATSAPP_MESSAGE_DICT}, is_cache=True)
            user_obj = Profile.objects.get(user_id=str(mobile))
            
            # call clevertap user event upload api -------------------------------------------
            intent_identified = Data.objects.filter(user=user_obj, variable="last_identified_intent_name")[0].value
            if employee_details != {}:
                user_event_data = {
                    "evtName":intent_identified,                                    # intent identified             
                    "evtData":{
                        "User_id":employee_details["EmployeeId"] if employee_details["EmployeeId"] is not None else "N.A",                   # emp id
                        "User_query":user_query,                                    # user query 
                        "Bot_response":str(bot_response).replace("$$$", "<br><br><br>")+" "+str(bot_response)  # bot response 
                    },
                    "identity":str(mobile)                                          # User Chat Id: e.g Mobile number incase of whatsapp
                }
            else:
                user_event_data = {
                    "evtName":intent_identified,                                    # intent identified             
                    "evtData":{
                        "User_id":"N.A",                                            # emp id
                        "User_query":user_query,                                    # user query 
                        "Bot_response":str(bot_response).replace("$$$", "<br><br><br>")+" "+str(bot_response)                                 # bot response 
                    },
                    "identity":str(mobile)                                          # User Chat Id: e.g Mobile number incase of whatsapp
                }
            logger.error("CLEVER EVENT DATA: ",str(user_event_data))    
            event_upload_status = clevertap_upload_event(user_event_data, clever_tap_auth)
            logger.error("Clever Tap Event Upload Status: ", str(event_upload_status))
            
            
            
            
            
            is_authentication_completed = None
            try:
                is_authentication_completed = Data.objects.filter(user=user_obj, variable="is_authentication_completed")[0].value
            except:
                pass
            
            if is_authentication_completed != None and str(is_authentication_completed).lower() == "true":
                last_identified_intent_name = Data.objects.filter(user=user_obj, variable="last_identified_intent_name")[0].value
                data_obj = Data.objects.filter(user=user_obj, variable="is_authentication_completed")[0]
                data_obj.value = False
                data_obj.save()
                recursive_call(last_identified_intent_name, mobile, waNumber)
                
        else:
            response["status_code"] = 301
            response["status_message"] = "Unable to send the message."

        
        if is_conversation_continue:
            logger.info("Continue Conversation...")
            task = threading.Thread(target=recursive_call, args=("continue", mobile, waNumber, ), daemon=True)
            task.start()

        # elif "bot_start_conversation_intent" in whatsapp_response["response"] and whatsapp_response["response"]["bot_start_conversation_intent"]!=None:
        #     bot_start_conversation_intent = whatsapp_response["response"]["bot_start_conversation_intent"]
        #     if is_verified_user==None:
        #         send_status = sendWhatsAppTextMessage(AUTHENTICATION_NUMBER, AUTHENTICATION_KEY, "Please wait...we are performing one time authentication of your details as employee.", str(mobile), is_unicode_text=True)
        #         r = requests.get(url= settings.EASYCHAT_HOST_URL + "/chat/query/whatsapp?mobile="+str(mobile)+"&text="+bot_start_conversation_intent+"&timestamp=1234&waNumber="+str(waNumber))

        #         task = threading.Thread(target=recursive_call, args=(bot_start_conversation_intent, mobile, waNumber, ), daemon=True)
        #         task.start()
        #     else:
        #         task = threading.Thread(target=recursive_call, args=("how can I help you", mobile, waNumber, ), daemon=True)
        #         task.start()

    except Exception as e:
        response["status_message"] = str(e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("GubShupWhatsAppCallBackURL: %s", str(e), str(exc_tb.tb_lineno))

    return response

