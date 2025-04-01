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

if loan_amount > income * 0.3:
    payload["score"] = "low"
    payload["reason_low_score"] = "Value of the loan greater than 1/3 of the income"
else:
    payload["score"] = "high"

task_type = payload["score"]+"_score"

send_task(task_type, payload)
task.complete()
sleep(10)