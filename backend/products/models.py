from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=300)
    des = models.TextField()
    code = models.CharField(blank=True,max_length=12)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(upload_to='img')
    upload_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.title)
def save(self,*args,**kwargs):
    if not self.code:
        self.code = str(uuid.uuid4).replace("-","").upper() [:12]
    super().save(*args,**kwargs)
