import re
from django.utils.html import strip_spaces_between_tags
from django.conf import settings

RE_SPACE = re.compile(r"\s{2,}")
RE_NEWLINE = re.compile(r"\n")

class MinifyHTMLMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):

        response = self.get_response(request)

	if 'text/html' in response['Content-Type'] and settings.COMPRESS_HTML:
		response.content = strip_spaces_between_tags(response.content.strip())
		response.content = RE_SPACE.sub(" ", response.content)
		response.content = RE_NEWLINE.sub("", response.content)
	return response
