from django.db import models
import string
import random
from django.conf import settings

class URLLink(models.Model):
    original_url=models.URLField()
    shortened_url=models.URLField(blank=True,null=True)


    def shortener(self):
        while True:
            random_string = ''
            string_length = 6
            alpha_numerals = string.ascii_letters + string.digits
            # domain = self.original_url.split("//")[-1].split("/")[0]
            for _ in range(string_length):
                random_string = random_string + random.choice(alpha_numerals)

            new_link=settings.HOST_URL+'/' +random_string
    
            if not URLLink.objects.filter(shortened_url=new_link).exists():
                break

        return new_link

    def save(self,*args, **kwargs):
        #To check if entered URL is already present or not in the Database
        if URLLink.objects.filter(original_url = self.original_url).exists():
            self.shortened_url = URLLink.objects.filter(original_url = self.original_url).values('shortened_url')[0]['shortened_url']
            return self.shortened_url
        else:
            if not self.shortened_url:
                new_link=self.shortener()
                self.shortened_url=new_link
            return super().save(*args, **kwargs)

