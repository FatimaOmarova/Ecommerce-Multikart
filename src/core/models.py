from django.db import models


class Staff(models.Model):
    full_name =  models.CharField(
        max_length=128,
    )
    image = models.ImageField(upload_to="Staff_images", null=True)

    position = models.CharField(
        max_length=128,
    )
    description = models.TextField()
    def __str__(self):
        return self.full_name

class Faq(models.Model):
    title = models.TextField() 
    description = models.TextField() 
    def __str__(self):
        return self.title

class Contact(models.Model):
    first_name =  models.CharField(
        max_length=128,
    )
    last_name =  models.CharField(
        max_length=128,
    )
    email =  models.EmailField(
    )
    phone_number =   models.CharField(
        max_length=128,
    )
    description = models.TextField() 
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.first_name



class Subscribers(models.Model):
    email = models.EmailField(unique=True)

    def str(self):
        return self.email

    class Meta:
        verbose_name = 'Subscribers'
        verbose_name_plural = verbose_name



class Instagram(models.Model):
    image = models.ImageField(upload_to="Instagram_images", null=True)
    link = models.TextField()

    def __str__(self):
        return self.link



class Logo(models.Model):
    image =  models.ImageField(upload_to="Logo_images", null=True)




class Blog(models.Model):
    user_id = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.CASCADE)

    title =  models.CharField(
        max_length=250,
    )
    image = models.ImageField(upload_to="Blog_images", null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, null=True
    )

    def __str__(self):
        return self.title
    

class Comment(models.Model):

    blog = models.ForeignKey("core.Blog", null=True, blank=True, on_delete=models.CASCADE)

    full_name = models.CharField(
        max_length=128,
    )
    email = models.CharField(
        max_length=128,
    )

    date = models.DateTimeField(blank=True, null=True)

    comment = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True, null = True
    )
    def __str__(self):
        return self.full_name
