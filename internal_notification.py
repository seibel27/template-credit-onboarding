from abstra.tasks import get_trigger_task
from dotenv import load_dotenv
from abstra.connectors import get_access_token
import os
import requests

load_dotenv()
slack_token = get_access_token("slack").token

task = get_trigger_task()
payload = task.get_payload()

name = payload["name"]
email = payload["email"]
income = payload["income"]
employer = payload["employer"]
loan_amount = payload["loan_amount"]
installments = payload["installments"]
score = payload["score"]
rejection_reason = payload["rejection_reason"]
reviewing_user = payload.get("reviewing_user", "Automatically Reviewed")

res = requests.post(
        'https://slack.com/api/chat.postMessage',
    json={
        'channel': os.environ.get("SLACK_CHANNEL_NAME"),
        'text': f"""
💰🚫 New loan request denied. Information:

- *Name*: {name}, 
- *Email*: {email}, 
- *Declared income*: ${income:,.2f}, 
- *Employer*: {employer}, 
- *Loan amount*: ${loan_amount:,.2f}, 
- *Number of installments*: {installments}, 
- *Score*: {score}, 
- *Reason for rejection*: {rejection_reason}
- *Reviewer*: {reviewing_user}
"""},
    headers={
        'Authorization': 'Bearer ' + slack_token,
        'Content-type': 'application/json; charset=utf-8'
    })

print(res)

task.complete()