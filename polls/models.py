from django.db import models

# Create your models here.


# Create your models here.
class Dropbox(models.Model):
    title = models.CharField(max_length=30)
    document = models.FileField(upload_to='async-kv-table/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s %s %s" % (self.title, self.document, self.created_at, self.updated_at)