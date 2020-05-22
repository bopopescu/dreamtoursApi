from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, blank=False)
    objects = models.Manager()

    def __str__(self):
        return "%s" % self.name

class User(models.Model):
    username = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=50, blank=False)
    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=False)
    birthdate = models.CharField(max_length=70, blank=False)
    objects = models.Manager()

    def __str__(self):
        return "%s" % self.username

class Particular(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    dni = models.CharField(max_length=9, blank=False)
    objects = models.Manager()

    def __str__(self):
        return "%s" % self.user

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    cif = models.CharField(max_length=9, blank=False)
    phone_number = models.CharField(max_length=9, blank=False)
    objects = models.Manager()

class LocalType(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return "%s" % self.name

class Local(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=False)
    type = models.ForeignKey(LocalType, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return "%s" % self.company

class Rating(models.Model):
    particular = models.ForeignKey(Particular, on_delete=models.CASCADE, blank=False)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, blank=False)
    rate = models.IntegerField(blank=False)

class Comment(models.Model):
    particular = models.ForeignKey(Particular, on_delete=models.CASCADE, blank=False)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, blank=False)
    comment = models.CharField(max_length=150, blank=False)