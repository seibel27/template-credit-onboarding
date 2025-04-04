from abstra.tasks import get_trigger_task, send_task
from time import sleep

task = get_trigger_task()
payload = task.get_payload()

name = payload["name"]
email = payload["email"]
income = payload["income"]
employer = payload["employer"]
loan_amount = payload["loan_amount"]
installments = payload["installments"]
score = payload["score"]

if loan_amount < 100000000:
    result = "approved"
else:
    result = "rejected"
    payload["rejection_reason"] = "Loan amount too high"

send_task(result, payload)
task.complete()
sleep(10)