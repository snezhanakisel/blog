from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField('Заголовок', max_length=30)
    description = models.TextField('Текст')
    slug = models.SlugField('Title', max_length=35)
    data = models.DateField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('blog', kwargs={'post_slug':self.slug})

class Potfolio(models.Model):
    image = models.ImageField()
    description = models.TextField()


class Comment(models.Model):
    comment = models.TextField()
    post_id = models.Foreignkey()
