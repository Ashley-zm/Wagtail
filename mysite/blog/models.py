from django.db import models
from django.shortcuts import render

# Create your models here.

# from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks


class BlogListPage(RoutablePageMixin, Page):
    template = "blog/blog_list_page.html"
    custom_title = models.CharField(
        max_length=100,
        blank=False,  # 针对表单，若为true，表示你的表单填写该字段的时候可以不填
        null=False,  # 针对数据库而言，为True，表示数据库的该字段可以以为空
        help_text='Overwrites the default title',
    )
    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context"""
        context = super().get_context(request, *args, **kwargs)
        context['posts] = BlogDetailPage.object.live().public()
        return context

    @route(r'^latest/$')
    def latest_blog_posts(self, request, *args, ***kwargs):
        context = self.get_context(request, & args, **kwargs)

        return render(request, "blog/latest_posts.html", context)


class BlogDetailPage(Page):

    template = "blog/blog_detail_page.html"
    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        help_text='Overwrites the default title',
    )
    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_rich_text", blocks.RichTextBlock()),
            ("simple_rich_text", blocks.SimpleRichTextBlock()),
            ("cards", blocks.CardBlock()),
            ("cta", blocks.CtaBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        ImageChooserPanel("blog_image"),
        StreamFieldPanel("content"),
    ]
