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

### Step 3 - Add askbot_slack_config.py

Add askbot_slack_config.py to the directory where Askbot is installed.  Fill in the configuration values for your instance.

