from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField(db_index=True, unique=True)
    document = models.CharField("Document", max_length=20)
    phone = models.CharField(max_length=20)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)

    # TODO: models.ImageField(null=True, blank=True, upload_to=user_directory_path)
    photo = models.CharField("URL", max_length=512)

    def __str__(self):
        return self.name
