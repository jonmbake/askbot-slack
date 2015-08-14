import json
import requests
from askbot_slack_config import config
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.sites.models import Site
from askbot.models import Post


def get_url(model_instance):
    return "http://%s%s" % (Site.objects.get_current().domain, model_instance.get_absolute_url())


def post_msg(msg):
    payload = {"text": msg, "username": config.get('SLACK_POST_USERNAME'), "channel": config.get('SLACK_POST_CHANNEL')}
    requests.post(config.get('SLACK_WEBHOOK_URL'), data=json.dumps(payload))


@receiver(post_save, sender=Post)
def notify_question_posted(sender, instance, created, raw, using, **kwargs):
    if created:
        title = instance.thread.title
        if instance.is_question():
            action = "asked"
        elif instance.is_answer():
            action = "answered"
        elif instance.is_comment():
            action = "commented on"
        post_msg("%s  %s the question \"%s\": %s" % (instance.author,  action, title, get_url(instance)))


class SlackMiddleware(object):
    pass
