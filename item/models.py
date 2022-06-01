from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        'auth.User', related_name='items', on_delete=models.CASCADE, null=True
    )

    class Meta:
        ordering = ('created_at', 'name')

    def __str__(self):
        return self.name