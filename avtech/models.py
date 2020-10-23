from django.db import models

# Create your models here.
class  Think(models.Model):
	title = models.CharField(max_length=100) 
	author = models.CharField(max_length=500,) 
	summary = models.TextField(blank=True , null=True)
	pdf = models.FileField(upload_to='think/ideas/')

	def _str_(self):
		return self.title


class Video(models.Model):
    name = models.CharField(max_length=500)
    videofile = models.FileField(upload_to='upload/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)
       