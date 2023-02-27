from slack_sdk.webhook import WebhookClient


def send_slack_notification(msg):
    url = "https://hooks.slack.com/services/T02A12FDSG/BFDAF12H6F3/JFDFAhjhhgFDSAFAK"

    webhook = WebhookClient(url)

    response = webhook.send(text=msg)
    try:
        assert response.status_code == 200
        assert response.body == "ok"
    except:
        print('Error Sending Slack Notification.')


send_slack_notification("Test Trigger Successful.")


# Notes:
# URL changed coz of privacy
# docs - https://api.slack.com/apps to create webhook url
# The Python document for this module is available at https://slack.dev/python-slack-sdk/api-docs/slack_sdk/