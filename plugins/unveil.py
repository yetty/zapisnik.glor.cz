import re
from pelican import signals


REGEX_IMAGE = re.compile(ur'<img(.*)src="([^"]*)"', re.UNICODE | re.IGNORECASE)


def images_to_unveil(article_generator):
    for article in article_generator.articles:
        article._content = REGEX_IMAGE.sub(ur'<img\1src="http://zapisnik.glor.cz/theme/img/loader.gif" data-src="\2"', article._content)


def register():
    signals.article_generator_finalized.connect(images_to_unveil)
