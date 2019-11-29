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

    title = blocks.CharBlock(required=True, help_text="Add your title")
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(requied=True)),
                ("title", blocks.CharBlock(requied=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False,
                                               help_text="If the buttton above selected, that will be used first."))
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
    Title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features=["bold", "italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default='Learn More', max_length=40)

    class Meta:
        template = "streams/cat_block.html"
        icon = "placeholder"
        label = "call to Action"
