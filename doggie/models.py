from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class DogCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'DogCategories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(DogCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Dog(models.Model):
    dogcategory = models.ForeignKey(DogCategory, on_delete=models.CASCADE)
    dog_name = models.CharField(max_length=128, unique=True)
    short_description = models.CharField(max_length=1280)
    long_description = models.CharField(max_length=1280)
    life_span = models.CharField(max_length=128)
    price = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    dogcategory_slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.dog_name)
        self.dogcategory_slug = slugify(self.dogcategory)
        super(Dog, self).save(*args, **kwargs)

    def __str__(self):
        return self.dog_name
