import json
import requests
from askbot_slack_config import config
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.sites.models import Site
from askbot.models import Post


def get_url(model_instance):
    """
    Returns the URL for the model instance.  Dependent on Site Domain name being set.
    """
    return "http://%s%s" % (Site.objects.get_current().domain, model_instance.get_absolute_url())


def post_msg(msg):
    """
    Post message to specific slack channel defined in config.
    """
    payload = {"text": msg, "username": config.get('SLACK_POST_USERNAME'), "channel": config.get('SLACK_POST_CHANNEL')}
    requests.post(config.get('SLACK_WEBHOOK_URL'), data=json.dumps(payload))


@receiver(post_save, sender=Post)
def notify_post_created(sender, instance, created, raw, using, **kwargs):
    """
    Post message when Askbot Post is created.  A Post includes Questions, Comments and Answers.
    """
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
    """
    A NO-OP middleware class to ensure our receiver gets registered early on.
    From the django 1.5 docs on signals: 'make sure that the module it’s in gets imported early on so that the signal
    handling gets registered before any signals need to be sent'.  Registering as a no-op middleware class ensures that
    this is 'imported early on'.  In later versions of django we can use the App#register method.
    """
    pass
