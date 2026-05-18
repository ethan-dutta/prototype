from django.db import models

class college (models.Model):
    college_id = models.CharField(max_length=4, primary_key=True)
    namer = models.CharField(max_length= 25)

    def __str__(self):
        return self.namer


class teacher (models.Model):
    name = models.CharField(max_length=25)
    area = models.CharField(max_length=30)
    college = models.ForeignKey(college, on_delete=models.CASCADE)

class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    pdf = models.FileField(upload_to='books/pdfs')

    def __str__(self):
        return self.title




