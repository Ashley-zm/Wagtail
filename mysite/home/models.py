from django.db import models

from wagtail.core.models import Page

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.admin.edit_handlers import PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.fields import RichTextField, StreamField

from streams import blocks


class HomePage(Page):
    template = "home/home_page.html"
    # max_count=1

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["blod", "italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content = StreamField(
        [
            ("cta", blocks.CtaBlock()),
        ],
        null=True,
        blank=True,
    )

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [

        FieldPanel('banner_title'),
        FieldPanel('banner_subtitle'),
        ImageChooserPanel('banner_image'),
        PageChooserPanel('banner_cta'),
        FieldPanel('body', classname="full"),
        StreamFieldPanel("content"),

    ]

    class Meta:
        """
        增加创建页面的名字
        """
        db_table = ''
        managed = True
        verbose_name = 'Home Page'
        verbose_name_plural = 'Home Page'
