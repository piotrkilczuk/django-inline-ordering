from django.contrib.admin import StackedInline
from inline_ordering import settings

class OrderableStackedInline(StackedInline):
    
    """Adds necessary media files to regular Django StackedInline"""
    
    class Media:
        js = (
              settings.JQUERY_PREAMBLE_JS_URL,
              settings.JQUERY_UI_JS_URL,
              settings.INLINE_ORDERING_JS_URL,
        )