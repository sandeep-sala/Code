import os
from EasyChatApp.models import *
from EasyAssistApp.models import *

supervisor_list = [
("H12017","Noel Reddy","noel.reddy@hdfcsec.com"),
("H11814","Rupali Raut","Rupali.Raut@hdfcsec.com"),
("H11992","Ajay Prajapati","ajay.prajapati@hdfcsec.com"),
("H11408","Koustubh Joshi","koustubh.joshi@hdfcsec.com"),
("H10114","Juily Waradkar","juily.waradkar@hdfcsec.com"),
("H11990","Ajay Yadav","ajay1.yadav@hdfcsec.com"),
("H11989","CHIRANJEEV GUPTA","Chiranjeev.Gupta@hdfcsec.com"),
("H12115","Sachin Malusare","Sachin.Malusare@hdfcsec.com"),
("H12047","Kiran Chandanshive","kiran.chandanshive@hdfcsec.com"),
("H10513","Naved Khan","MohdNaved.Khan@hdfcsec.com"),
]

admin = CobrowseAgent.objects.get(user__username="admin")

for agent in supervisor_list:
    
    agent_id = agent[0].strip()
    agent_full_name = agent[1].strip()
    first_name = agent_full_name.split(" ")[0]
    last_name = agent_full_name.split(" ")[-1]
    user_name = email = agent[2].strip()

    print(agent_id,first_name,last_name,user_name)

    user = User.objects.create(
        username=user_name,
        password='Success$@123'+user_name,
        role=BOT_BUILDER_ROLE,
        status="2",
        is_chatbot_creation_allowed="3",
        first_name=first_name,
        last_name=last_name,
        email=email
    )

    cobrowse_agent = CobrowseAgent.objects.create(user=user, role='supervisor')
    cobrowse_agent.agent_code = agent_id
    cobrowse_agent.virtual_agent_code = agent_id
    cobrowse_agent.save()
    admin.agents.add(cobrowse_agent)
    admin.save()

all_list = [
    ("H12204","Aakash Giri","aakash.giri@hdfcsec.com"),
    ("H11803","Bhavik Kavi","bhavik.kavi@hdfcsec.com"),
    ("H11409","Mayur Mahadik","Mayur.Mahadik@hdfcsec.com"),
    ("H11328","Suhas Patil","suhas.patil@hdfcsec.com"),
    ("H12017","Noel Reddy","noel.reddy@hdfcsec.com"),
    ("H11814","Rupali Raut","Rupali.Raut@hdfcsec.com"),
    ("H11992","Ajay Prajapati","ajay.prajapati@hdfcsec.com"),
    ("H11408","Koustubh Joshi","koustubh.joshi@hdfcsec.com"),
    ("H10114","Juily Waradkar","juily.waradkar@hdfcsec.com"),
    ("H11990","Ajay Yadav","ajay1.yadav@hdfcsec.com"),
    ("H11989","CHIRANJEEV GUPTA","Chiranjeev.Gupta@hdfcsec.com"),
    ("H12115","Sachin Malusare","Sachin.Malusare@hdfcsec.com"),
    ("H12047","Kiran Chandanshive","kiran.chandanshive@hdfcsec.com"),
    ("H10513","Naved Khan","MohdNaved.Khan@hdfcsec.com"),
    ("HSLV2246","Ashok kumar Madaswmay","9653434163","H11328"),
    ("HSLV2177","Kanchan Rajput","7506154318","H11328"),
    ("HT4342","Ruchita Goriwale","8805910379","H11328"),
    ("HT4346","Vallery Alphonso","9653244950","H11328"),
    ("HT4021","Vishal Koli","9594227216","H11328"),
    ("HSLV2357","Priyanka Suryanath Yadav","8104853076","H11803"),
    ("HSLV2414","Dharmik Patel","7499348460","H11803"),
    ("HSLV2448","Kajal Gupta","9820312843","H11803"),
    ("HSLV2796","Sandesh Patil","9820829891","H11803"),
    ("HSLV2502","Aliya Khan","8451828269","H12017"),
    ("HSLV2607","pratiksha potekar","7506038350","H12017"),
    ("HSLV2608","sejal baikar","9158627191","H12017"),
    ("HSLV2176","Ashwitha Krishna Devadiga","7715996022","H11814"),
    ("HSLV2471","Aarti Dattaram Talekar","8097837289","H11814"),
    ("HSLV2522","Atul Bhimrao Lathe","8356814741","H11814"),
    ("HSLV2687","Rithik Sharma","7710846985","H12204"),
    ("HSLV2679","Narayan Goud","8108010463","H12204"),
    ("HSLV2711","Ankit Pandey","8767554866","H12204"),
    ("HSLV2454","AISHWARYA ANANT PATIL","9167654183","H11992"),
    ("HSLV2460","SHAGUN RAMESH SISODIYA","9167095722","H11992"),
    ("HSLV2505","Mohd Wahid Mohd Ikram Qureshi","7666863810","H11992"),
    ("HSLV2329","Sushil Gaud","8422071187","H11408"),
    ("HT4339","Riya jadhav","8591539734","H11408"),
    ("HT4344","Jyoti Prajapati ","8928088851","H11408"),
    ("HT4127","SEJAL JAIN","7208219709","H11408"),
    ("HT4349","Shubham More","7208738672","H10114"),
    ("HT4373","Kanchan Jaiswal","8097844683","H10114"),
    ("HT4377","Pooja kenjale","8928475516","H10114"),
    ("HSLV2507","Abhishek Yadav","9152957762","H11990"),
    ("HSLV2511","Neha Rangara","9850293875","H11990"),
    ("HSLV2514","Tanvi Lone","9960578779","H11990"),
    ("HSLV2458","Poonam Ashok Rajak","9987807938","H11990"),
    ("hslv2512","Satyam gupta","8850071394","H11989"),
    ("hslv2551","Saloni Dasavate","7400335875","H11989"),
    ("hslv2453","Afraha Shaikh","9029524804","H11989"),
    ("hslv2456","Lumika Dholi","9136365898","H11989"),
    ("HSLV2362","Bhavin Dinesh Solanki","9503456759","H11409"),
    ("HT4023","Samiksha Madhavi","8828275215","H11409"),
    ("HT4331","Vishaka Ghadghe","8850209363","H11409"),
    ("HSLV2709","Wasim ansari","9892839171","H12115"),
    ("HSLV2576","Manisha Chouhan","7738505686","H12115"),
    ("HSLV2570","Saurav Karbal","7506967451","H12115"),
    ("HSLV2628","Akshata Dayal","9284553044","H12115"),
    ("HSLV2656","Nivedita Jadhav","8792812232","H12047"),
    ("HSLV2660","Abhay  Tiwari","8286669395","H12047"),
    ("HSLV2667","Deepak Murugan Udaiyar","7045360127","H12047"),
    ("HSLV2235","Soundarya Subramani","8097302141","H10513"),
    ("HSLV2270","Shifa bano","9321464727","H10513"),
    ("HSLV2273","Tejas Kamat","9987357852","H10513"),
    ("HSLV2282","Prachi Pramod shirke","7738611705","H10513"),
]

from django.db.models import Q
all_code_list = [i[0].strip() for i in all_list]

CobrowseAgent.objects.filter(agent_code__)

CobrowseAgent.objects.filter(~Q(agent_code__in=all_code_list)).exclude(user__username="admin")

admin = CobrowseAgent.objects.get(user__username="admin")
postfix = "@hdfcsec.com"
for agent in agent_list:
    agent_id = agent[0].strip()
    agent_full_name = agent[1].strip()
    first_name = agent_full_name.split(" ")[0]
    last_name = agent_full_name.split(" ")[-1]
    user_name = email = ".".join(agent_full_name.split(" "))+postfix

    supervisor_id = agent[-1].strip()
    supervisor_obj = CobrowseAgent.objects.get(agent_code=supervisor_id)

    agent_objs = CobrowseAgent.objects.filter(
        agent_code=agent_id
    )

    if agent_objs.count() > 0:
        cobrowse_agent = agent_objs.first()
    else:
        cobrowse_agent = None


    if cobrowse_agent == None:
        user_obj = User.objects.filter(username=user_name)

        if user_obj.count() > 0:
            user_obj = user_obj.first()
        else:
            user_obj = None

        if user_obj:
            user = user_obj
        else:
            user = User.objects.create(
                username=user_name,
                password='Success$@123'+user_name,
                role=BOT_BUILDER_ROLE,
                status="2",
                is_chatbot_creation_allowed="3",
                first_name=first_name,
                last_name=last_name,
                email=email
            )
        
        cobrowse_agent_obj = CobrowseAgent.objects.filter(user=user)

        if cobrowse_agent_obj.count() > 0:
            cobrowse_agent_obj = cobrowse_agent_obj.first()
        else:
            cobrowse_agent_obj = None

        if cobrowse_agent_obj:
            cobrowse_agent = cobrowse_agent_obj
        else:
            cobrowse_agent = CobrowseAgent.objects.create(
                user=user,
                role='agent',
                )

    cobrowse_agent.mobile_number=agent[-2].strip()
    cobrowse_agent.agent_code = agent_id
    cobrowse_agent.virtual_agent_code = agent_id
    cobrowse_agent.save()

    supervisor_obj.agents.add(cobrowse_agent)
    supervisor_obj.save()