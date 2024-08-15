from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Title', max_length=550)
    owner = models.CharField('Owner', max_length=250)
    datenow = models.DateField("Published")
    c_name = models.CharField('Enter certificate name', max_length=2048)
    file_name = models.CharField("File name", max_length=550)
    articlesnumber = models.CharField("Articles number", max_length=1024)
    certificate_file = models.FileField("Certificate", upload_to='certificates/')
    file = models.FileField("File", upload_to='')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'