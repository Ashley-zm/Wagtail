from django.db import models
# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from streams import blocks


# Create your models here.


class QueryPage(Page):
    template = "query/query_page.html"
    # content = StreamField(
    #     [
    #         ("title_and_text", blocks.TitleAndTextBlock()),
    #         ("full_rich_text", blocks.RichTextBlock()),
    #         ("simple_rich_text", blocks.SimpleRichTextBlock()),
    #         ("cards", blocks.CardBlock()),
    #         ("cta", blocks.CtaBlock()),
    #         # ("button", blocks.ButtonBlock()),
    #     ],
    #     null=True,
    #     blank=True,
    # )

    # subtitle = models.CharField(max_length=100, null=True, blank=True)

    # content_panels = Page.content_panels + [
    #     FieldPanel("subtitle"),
    #     StreamFieldPanel("content"),
    # ]

    class Meta:
        verbose_name = "Query Page"
        verbose_name_plural = "Query Pages"
