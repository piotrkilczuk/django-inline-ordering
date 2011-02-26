from django.conf import settings

# path to inline_ordering.js
INLINE_ORDERING_JS_URL = getattr(settings, 'INLINE_ORDERING_JS_URL', settings.MEDIA_URL + 'inline_ordering.js')


JQUERY_PREAMBLE_JS_URL = INLINE_ORDERING_JS_URL.replace('inline_ordering.js', 'inline_ordering_preamble.js')
JQUERY_UI_JS_URL = getattr(settings, 'JQUERY_UI_JS_URL', 'http://ajax.googleapis.com/ajax/libs/jqueryui/1/jquery-ui.min.js')
