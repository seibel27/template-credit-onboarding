from abstra.forms import *
from abstra.tasks import get_tasks, send_task

display_markdown("""
<img src="https://abstracloud-webflow-assets.s3.amazonaws.com/7626icon.png" width="50" height="50" />

# CreditOps
### Loan request review 🔍
                 """, button_text="Start")


user = get_user()

### Add authentication straight into the code, or in our Access Control feature

# if not user.email.endswith("abstra.io"):
#     display("You don't have permission to access this review ❌")
#     exit()

tasks = get_tasks()
task = tasks[0]
payload = task.get_payload()

name = payload["name"]
email = payload["email"]
income = payload["income"]
employer = payload["employer"]
loan_amount = payload["loan_amount"]
installments = payload["installments"]
score = payload["score"]
reason_low_score = payload["reason_low_score"]

payload["reviewing_user"] = user.email


markdown_text = f"""
# Loan Request

----------------------------

## Personal Data

### Name: 
{name}
### Email: 
{email}

----------------------------

## Income Data

### Income: 
$ {income:,.2f}
### Employer: 
{employer}

----------------------------

## Loan Data

### Loan amount: 
$ {loan_amount:,.2f}
### Installments: 
{installments}

----------------------------

## Credit Engine Result

### Score: 
{score}
### Reason: 
{reason_low_score}

----------------------------
"""


selection = Page() \
    .display_markdown(markdown_text) \
    .read_multiple_choice("Do you want to approve this request?",["Yes", "No"], key="approval") \
    .run()

if selection['approval'] == "No":
    rejection_reason = read_textarea("Rejection reason")
    result = "rejected"
    payload["rejection_reason"] = rejection_reason
else:
    result = "approved"

send_task(result, payload)
task.complete()

display_markdown(f"""
# Request {result}

Review completed by {user.email}
                 """, end_program=True, button_text=None)