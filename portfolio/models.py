from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.
class Technology(models.Model):
    tech_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.tech_name

    def get_absolute_url(self):
        return reverse('tech-detail', args=[str(self.id)])


class Project(models.Model):
    title = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=200, default="Placeholder")
    description = RichTextField(max_length=4000)
    tech_used = models.ManyToManyField(Technology)
    image = models.ImageField(upload_to='static/portfolio/images/')
    project_link = models.CharField(max_length=200, null=True, blank=True)
    github_link = models.CharField(max_length=200, null=True, blank=True)
    project_details_image_1 = models.ImageField(upload_to='static/portfolio/images/', null=True, blank=True)
    project_details_image_2 = models.ImageField(upload_to='static/portfolio/images/', null=True, blank=True)
    project_details_check_image = models.ImageField(upload_to='static/portfolio/images/', null=True, blank=True)
    project_details_github_image = models.ImageField(upload_to='static/portfolio/images/', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('portfolio:detail', args=[str(self.id)])
