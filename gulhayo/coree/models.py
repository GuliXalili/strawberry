from django.db import models

class teacher(models.Model):
    NFP = models.CharField(max_length=30)
    job_title = models.TextField(max_length=500)
    salary = models.IntegerField(default=10000000)
    practice = models.CharField(max_length=30)

    def __str__(self):
        return f" NFP:{self.NFP} Job title:{self.job_title} Salarey:{self.salary} Practice:{self.practice}"

class doctor(models.Model):
    NFP = models.CharField(max_length=30)
    patient = models.IntegerField(default=1)
    location= models.CharField(max_length=30)
    type = models.CharField(max_length=20)

    def __str__(self):
        return f" NFP:{self.NFP} Patient:{self.patient} Location:{self.location} Type:{self.type}"

class student(models.Model):
    NFP = models.CharField(max_length=50)
    age = models.IntegerField(default=17)
    subject = models.CharField(max_length=30)
    ball = models.IntegerField(default=3)

    def __str__(self):
        return f"NFP:{self.NFP} Age:{self.age} Subject:{self.subject} Ball:{self.ball}"

class dentist(models.Model):
    NFP = models.CharField(max_length=50)
    medcenter = models.CharField(max_length=50)
    patients = models.IntegerField(default=1)

    def __str__(self):
        return f" NFP:{self.NFP} Medcenter:{self.medcenter} Patients:{self.patients}"

class stuardess(models.Model):
    NFP = models.CharField(max_length=50)
    Age = models.IntegerField(default=1)
    weight = models.IntegerField(default=50)
    height = models.FloatField(default=1.65)

    def __str__(self):
        return f" NEP:{self.NFP} Age:{self.Age} Weight:{self.weight} Height:{self.height}"

class policemen(models.Model):
    NFP = models.CharField(max_length=50)
    wtime = models.IntegerField(default=7)
    age = models.IntegerField(default=20)

    def __str__(self):
        return f" NFP:{self.NFP} Wtime:{self.wtime} Age:{self.age}"