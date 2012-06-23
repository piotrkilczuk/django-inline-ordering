from django.contrib.admin import TabularInline, StackedInline
from django.conf import settings


class OrderableStackedInline(StackedInline):
    
    """Adds necessary media files to regular Django StackedInline"""
    
    class Media:
        js = (settings.INLINE_ORDERING_JS,)


class OrderableTabularInline(TabularInline):
    
    """Adds necessary media files to regular Django TabularInline"""
    
    class Media:
        js = (settings.INLINE_ORDERING_JS,)
