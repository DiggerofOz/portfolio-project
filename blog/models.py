from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images')

    # The first def will change the admin page so instead of showing 'blog object' it will
    # show the blog title.
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_summary(self):
        return self.pub_date.strftime('%b %e %Y')

# Create a migration

# Migrate

# Add to the admin
