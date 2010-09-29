from django.conf import settings

# path to inline_ordering.js
INLINE_ORDERING_JS = getattr(settings, 'INLINE_ORDERING_JS', settings.MEDIA_URL + 'inline_ordering.js')
