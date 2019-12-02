"""
StreamFileds live in here
"""
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='add you title')
    text = blocks.TextBlock(required=True, help_text='Add your additional')

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class CardBlock(blocks.StructBlock):
    """ Cards with image and text and button(s)"""

    # title = blocks.CharBlock(required=True, help_text="Add your title")
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(requied=True)),
                ("title", blocks.CharBlock(requied=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_value1", blocks.CharBlock(required=False, max_length=30)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False,
                                               help_text="If the buttton above selected, that will be used first.")),
                ("button_value2", blocks.CharBlock(required=False, max_length=30)),
                ("button_page2", blocks.PageChooserBlock(required=False)),
                ("button_url2", blocks.URLBlock(required=False,
                                                help_text="If the buttton above selected, that will be used first.")),
                ("button_value3", blocks.CharBlock(required=False, max_length=30)),
                ("button_page3", blocks.PageChooserBlock(required=False)),
                ("button_url3", blocks.URLBlock(required=False,
                                                help_text="If the buttton above selected, that will be used first.")),
            ]

        )
    )

    class Meta:
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Staff Cards"


class RichTextBlock(blocks.RichTextBlock):
    """ RichTextBlock with all the features (全部的richtext功能都在)"""

    class Meta:
        template = "streams/rich_text_block.html"
        icon = "doc-full"
        label = "Full RichText"


class SimpleRichTextBlock(blocks.RichTextBlock):
    """ RichTextBlock without limited the features (部分的richtext功能)"""

    def __init__(self, required=True, help_text=None, editor='default',
                 features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = [
            "blod",
            "italic",
            "link",
        ]

    class Meta:
        template = "streams/rich_text_block.html"
        icon = "edit"
        label = "Simple RichText"


class CtaBlock(blocks.StructBlock):
    """
    A Simple call to action section
    """
    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features=["bold", "italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(
        required=True, default='Learn More', max_length=40)

    class Meta:
        template = "streams/cat_block.html"
        icon = "placeholder"
        label = "call to Action"


class LinkStructValue(blocks.StructBlock):

    def url(self):
        button_page = self.get('button_page')
        button_url = self.get('button_url')
        if button_page:
            return button_url
        else:
            return button_page

        return None


# class ButtonBlock(blocks.StructBlock):
#     button_page = blocks.PageChooserBlock(
#         required=False, help_text="If selected, this url will be used first")
#     button_url = blocks.URLBlock(
#         required=False, help_text="If added, this url will be used secondarily to the button page")

#     def get_context(self, request, *args, **kwargs):
#         context = super().get_context(request, *args, **kwargs)
#         context['latest_posts'] = BlogDetailPage.objects.live().public()[:3]
#         return context

#     class Meta:
#         template = "streams/button_block.html"
#         icon = "placeholder"
#         label = "Simple Button"
#         value_class = LinkStructValue