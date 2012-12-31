from django.db import models
from datetime import datetime
from taggit.managers import TaggableManager


class Article(models.Model):
    """
    An Article is a writing entry that is translated into markdown.
    """
    DRAFT_STATUS = 1
    PUBLISHED_STATUS = 2
    STATUS_CHOICES = (
        (DRAFT_STATUS, 'Draft'),
        (PUBLISHED_STATUS, 'Published'),
    )

    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=DRAFT_STATUS)
    timestamp_published = models.DateTimeField(null=True, blank=True)

    text_raw = models.TextField(null=True, blank=True)
    text_html = models.TextField(null=True, blank=True)

    tags = TaggableManager()

    def save(self, *args, **kwargs):
        if self.status == Article.PUBLISHED_STATUS and not self.timestamp_published:
            self.timestamp_published = datetime.now()

        super(Article, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'<Article: %s>' % self.title[:50]
