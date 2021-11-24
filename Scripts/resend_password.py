from EasyAssistApp.utils import *
from EasyAssistApp.models import *
from EasyChatApp.models import *
import time

email_list = [
    "sandeep.s@getcogno.ai",
    "ajay.bhajantri_hgs@idfcbank.com",
    "kunal.shelar_hgs@idfcbank.com",
    "krishna.vamshi_hgs@idfcbank.com",
]

for username in email_list:
    user = User.objects.get(username=username)
    agent_email = user.email
    agent_name = user.first_name
    password = generate_random_password()
    user.password = password
    user.save()
    print(f"UserName : {username} || PassWord : {password}")
    send_password_over_email(agent_email, agent_name, password)
    time.sleep(2)
