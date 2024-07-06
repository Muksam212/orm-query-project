from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    date_created = models.DateField() 

    def __str__(self):
        return f"{self.name}"

class Language(models.Model):
    name = models.CharField(max_length=20)
    creator = models.CharField(max_length=20)
    paradigm = models.CharField(max_length=20)
    date_created = models.DateField()

    def __str__(self):
        return f"{self.name}"

class Programmer(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="programmer", blank=True, null=False)
    languages = models.ManyToManyField(Language, related_name="programmers", null=False, blank=True)

    def __str__(self):
        return f"{self.name}"



#QUERY TO FETCH ALL THE PROGRAMMERS WHO KNOW PYTHON