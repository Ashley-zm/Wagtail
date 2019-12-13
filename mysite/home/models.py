from django.db import models
from django.shortcuts import render


from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable

from wagtail.admin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
    MultiFieldPanel,
    InlinePanel,
    PageChooserPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.fields import RichTextField, StreamField

from streams import blocks


class HomePageCarouselImages(Orderable):
    """ between 1 and 5 images for home page carousel轮播"""

    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_images = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    panels = [
        ImageChooserPanel("carousel_images"),
    ]


class HomePage(RoutablePageMixin, Page):
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
        MultiFieldPanel([
            FieldPanel('banner_title'),
            FieldPanel('banner_subtitle'),
            ImageChooserPanel('banner_image'),
            PageChooserPanel('banner_cta'),
            FieldPanel('body', classname="full"),
        ], heading="Banner Options"),
        # InlinePanel("carousel_images"),这样没有框架，如下所示写入到
        # 设置Images最少一个最多5个，添加的标签名为 Image
        MultiFieldPanel([
            InlinePanel("carousel_images", max_num=5,
                        min_num=1, label="Image"),
        ], heading="Carousel Panel"
        ),
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

    @route(r'^subscribe/$')
    def the_subscribe_page(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        context['a_special_test'] = "Hello World 123"
        return render(request, "home/subscribe.html", context)
