# askbot-slack

A basic [Askbot](https://github.com/ASKBOT/askbot-devel) integration with Slack.  When a question, comment or answer is posted to Askbot, a specific Slack channel is sent a message that looks like this:

![Askbot Slack Hook](https://raw.githubusercontent.com/jonmbake/screenshots/master/askbot-slack/hook.png)

## Up and Running In Three Easy Steps

### Step 1 - Install Using Pip

```
pip install askbot_slack
```

### Step 2 - Alter Askbot's settings.py

Add 'askbot_slack.SlackMiddleware' to MIDDLEWARE_CLASSES of settings.py in the Askbot install directory.

### Step 3 - Configure Slack integration parameters

Parameters are available in Askbot's settings -> external services -> Slack integration

Alternatively, specify the following settings in the `settings.py`, with the corresponding values:

   ASKBOT_SLACK_ENABLED = True
   ASKBOT_SLACK_USERNAME = '...'
   ASKBOT_SLACK_CHANNEL = '#...'
   ASKBOT_SLACK_WEBHOOK_URL = '...'

