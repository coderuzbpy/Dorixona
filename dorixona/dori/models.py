from django.db import models
# Create your models here.


class Dori(models.Model):
    make = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    date = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='car_images/', blank=True, null=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Dori'

    def __str__(self):
        return f'{self.make} {self.model} ({self.year})'

