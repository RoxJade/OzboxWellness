from django.db import models


class Category(models.Model):
    '''return category model'''

    class Meta:
        '''return category as plural'''
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        '''return category name'''
        return str(self.name)

    def get_friendly_name(self):
        '''return friendly category name'''
        return self.friendly_name


class Programmes(models.Model):
    '''return product model'''
    class Meta:
        '''return programmess correctly'''
        verbose_name_plural = 'Programmes'

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=250)
    description = models.TextField()
    programme_length = models.CharField(max_length=250)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    programme_cost = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        '''return programme model'''
        return str(self.name)
