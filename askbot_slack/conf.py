from askbot.conf.super_groups import EXTERNAL_SERVICES
from askbot.conf import settings as askbot_settings
from askbot.deps import livesettings
from django.utils.translation import ugettext_lazy as _

SLACK_SETTINGS = livesettings.ConfigurationGroup(
    'SLACK',
    _('Slack integration'),
    super_group=EXTERNAL_SERVICES
)

askbot_settings.register(
    livesettings.BooleanValue(
        SLACK_SETTINGS,
        'SLACK_ENABLED',
        default=False,
        description=_('Enable posting to Slack')
    )
)

askbot_settings.register(
    livesettings.StringValue(
        SLACK_SETTINGS,
        'SLACK_USERNAME',
        default='',
        description=_('Slack user name'),
    )
)

askbot_settings.register(
    livesettings.StringValue(
        SLACK_SETTINGS,
        'SLACK_CHANNEL',
        default='',
        description=_('Slack channel')
    )
)

askbot_settings.register(
    livesettings.StringValue(
        SLACK_SETTINGS,
        'SLACK_WEBHOOK_URL',
        default='',
        description=_('Slack webhook url')
    )
)
