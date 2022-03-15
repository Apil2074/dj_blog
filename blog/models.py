
from django.db import models
# from django.utils.html import formathtml
from tinymce.models import HTMLField
from django.utils.timezone import now


# Create your models here.

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title= models.CharField(max_length=100)
    description= models.TextField()
    url=models.CharField(max_length=100)
    image=models.ImageField(upload_to='category/')
    add_date= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self): 
        # return self.title
        return self.add_date.strftime("Y")

class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=HTMLField()
    url=models.CharField(max_length=100)
    cat=models.ForeignKey(Category, on_delete= models.CASCADE)
    image=models.ImageField(upload_to='post/')
    add_date= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self): 
        return self.title 




# class PostComment(models.Model):
#     comment_id=models.AutoField(primary_key=True)
#     comment=models.TextField()
#     # user=models.ForeignKey(User, on_delete=models.CASCADE)
#     post=models.ForeignKey(Post, on_delete=models.CASCADE)
#     parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
#     timestamp= models.DateTimeField(default=now)

      
        

