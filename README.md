# Credit Onboarding Workflow Template
## How it works:
This project includes a custom credit onboarding system implemented with Abstra and Python scripts. The requester fills out a form with their personal data to apply for credit. The request is then either automatically approved or manually evaluated, depending on the individual's credit score. The system integrates with Slack to send alerts about rejected requests and with SendGrid to notify users of approved requests via email.

Integrations:
  - Slack
  - Sendgrid

To customize this template for your team and build a lot more, [book a demonstration here.](https://meet.abstra.app/demo?url=template-credit-onboarding)

![A credit onboarding workflow built in Abstra](https://github.com/user-attachments/assets/1b881474-bd44-4dd9-aa2b-4b74bf548267)

## Initial Configuration
To use this project, some initial configurations are necessary:

1. **Python Version**: Ensure Python version 3.9 or higher is installed on your system.
2. **Environment Variables**:

   The following environment variables are required for both local development and online deployment:

   - `SLACK_BOT_TOKEN`: Slack Token to send alerts on Slack about rejected requests
   - `SEDGRID_API_KEY`: API Token to use Sendgrid email service
   - `SENDER_EMAIL`: Email address from which the credit approval notification will be sent.
  
   For local development, create a `.env` file at the root of the project and add the variables listed above (as in `.env.examples`). For online deployment, configure these variables in your [environment settings](https://docs.abstra.io/cloud/envvars).

3. **Dependencies**: To install the necessary dependencies for this project, a `requirements.txt` file is provided. This file includes all the required libraries.

   Follow these steps to install the dependencies:

   1. Open your terminal and navigate to the project directory.
   2. Run the following command to install the dependencies from `requirements.txt`:
  
      ```sh
      pip install -r requirements.txt
      ```

## General Workflow:
To implement this system use the following scripts:

### Credit Request Creation:
For creating a credit request and collecting data about it, use:
  - **order_request_form.py**: Script to generate a form that collects the requester's personal information and details about the credit request.

### Credit Request Review: 
For evaluating the credit request, use:
  - **credit_engine.py**: Script to assign a grade to the request based on its details.
  - **automatic_review.py**: Script to approve the request if its score is sufficiently high.
  - **manual_review.py**: Script to generate a form that displays information about the credit request and asks the responsible team for approval or rejection.

### Credit Request Notification:
For notifing about the request approval/rejection:
  - **approval_email.py**: Script to notify the requester if the credit request has been approved.
  - **internal_notification.py**: Script to notify a Slack channel about the request rejection.

If you're interested in customizing this template to your team in under 30min, [book a customizing session here.](https://meet.abstra.app/demo?url=template-credit-onboarding)
