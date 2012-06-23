from django.contrib.admin import TabularInline, StackedInline
from django.conf import settings

INLINE_ORDERING_JS = getattr(settings,
                             'INLINE_ORDERING_JS', 'inline_ordering.js')


class OrderableStackedInline(StackedInline):
    
    """Adds necessary media files to regular Django StackedInline"""
    
    class Media:
        js = (INLINE_ORDERING_JS,)


class OrderableTabularInline(TabularInline):
    
    """Adds necessary media files to regular Django TabularInline"""
    
    class Media:
        js = (INLINE_ORDERING_JS,)
