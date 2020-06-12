from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=20)
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='static.kadrisite/', null=True, blank=True)

    class Meta:
        ordering = ["title"]

    # def getImage(self):
    #     if not self.image:
    #         # depending on your template
    #         return "article_imag.png"

    def __str__(self):
        return self.title
