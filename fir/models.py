from django.conf import settings
from django.db import models
from django.utils import timezone
# from comments.models import comments
from django.contrib.contenttypes.models import ContentType


class Post(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.CharField(max_length = 200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    x = models.BooleanField(default = True)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class People(models.Model):
# 	# dp name aadhar email mobilemo address state pincode
	dp = models.ImageField(upload_to='fir/images', null = True, blank = True)
	name = models.CharField(max_length = 200)
	aadhar = models.CharField(max_length = 12)
	email = models.CharField(max_length = 100)
	mobile_no = models.CharField(max_length = 20)
	address = models.CharField(max_length = 200)
	pincode = models.CharField(max_length = 7)

	def __str__(self):
		return self.name
