from django.db import models
from django.shortcuts import render

# Create your models here.
from wagtail.core.models import Page
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks

# RoutablePageMixin混合为页面提供了一种方便的方式来响应具有不同视图的多个子URL
# 默认情况下，存在r'^ $'的路由，该路由完全像常规Page那样提供内容。
# 可以通过在继承类的任何其他方法上使用@route（r'^ $'）来覆盖它。


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
        context["posts"] = BlogDetailPage.objects.live().public()
        # context["regular_context_var"] = "I like the page"
        # context["a_special_link"] = self.reverse_subpage('latest_posts')
        return context
# 添加路径
    @route(r'^latest/$', name="latest_posts")
    def latest_blog_posts_only_shows_last_5(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        context["latest_posts"] = BlogDetailPage.objects.live().public()
        context["name"] = "Kalaob Tauline"
        context["website"] = "Learn Kalaob Tauline"
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
