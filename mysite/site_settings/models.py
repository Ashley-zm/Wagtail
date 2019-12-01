from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

# Create your models here.

@register_setting
class SocialMediaSettings(BaseSetting):
    """Social Media Settings for our custom website"""

    facebook = models.URLField(blank=True, null=True, help_text="facebook URL")
    twitter = models.URLField(blank=True, null=True, help_text="Twitter URL")
    youtube = models.URLField(blank=True, null=True, help_text="YouTube URL")

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("youtube"),
        ], heading="Social Media Settings")
    ]
