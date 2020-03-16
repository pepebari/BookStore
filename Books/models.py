from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    register_date = models.DateField()
    phone_number = models.IntegerField()
    points = models.IntegerField()


class Genre(models.Model):
    name = models.CharField(max_length=100)


class Stock(models.Model):
    quantity = models.IntegerField()


class Book(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    quantity = models.ForeignKey(Stock, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    register_date = models.DateField()


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        purchaser = User.objects.get(id=self.user.id)
        purchaser.points = purchaser.points+1
        purchaser.save()

        super(Purchase, self).save(*args, **kwargs)
