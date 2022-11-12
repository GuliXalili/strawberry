from django.db import models

class math(models.Model):
    theme = models.TextField(max_length=300)
    time = models.IntegerField(default=1)
    teacher = models.CharField(max_length=30)

    def __str__(self):
        return f" Theme:{self.theme} Time:{self.time} Teacher:{self.teacher}"

class history(models.Model):
    theme = models.TextField(max_length=300)
    time = models.IntegerField(default=1)
    teacher = models.CharField(max_length=30)

    def __str__(self):
        return f" Theme:{self.theme} Time:{self.time} Teacher:{self.teacher}"

class biology(models.Model):
    theme = models.TextField(max_length=300)
    time = models.IntegerField(default=1)
    teacher = models.CharField(max_length=30)

    def __str__(self):
        return f" Theme:{self.theme} Time:{self.time} Teacher:{self.teacher}"

class phisics(models.Model):
    theme = models.TextField(max_length=300)
    time = models.IntegerField(default=1)
    teacher = models.CharField(max_length=30)

    def __str__(self):
        return f" Theme:{self.theme} Time:{self.time} Teacher:{self.teacher}"

class FT(models.Model):
    theme = models.TextField(max_length=300)
    time = models.IntegerField(default=1)
    teacher = models.CharField(max_length=30)

    def __str__(self):
        return f" Theme:{self.theme} Time:{self.time} Teacher:{self.teacher}"

class english(models.Model):
    theme = models.TextField(max_length=300)
    time = models.IntegerField(default=1)
    teacher = models.CharField(max_length=30)

    def __str__(self):
        return f" Theme:{self.theme} Time:{self.time} Teacher:{self.teacher}"
