# from django.conf import settings
# from django.db import models
# from django.utils import timezone
#
#
# class Post(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#


from django.conf import settings
from django.db import models
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def comm_count(self):
        return Comment.objects.filter(answer_massage=self).count()

    def comments(self):
        return Comment.objects.filter(answer_massage=self)


class Comment(MPTTModel):
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text_massage = models.TextField()
    answer_massage = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return str(self.id)

    class MPTTMeta:
        order_insertion_by = ['date']
