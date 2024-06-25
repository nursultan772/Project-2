from django.db import models


class UserProfile(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    date_registered = models.DateField(auto_now=True)
    email = models.EmailField()
    phone_number = models.IntegerField()
    statuss = (
        ('Simple', 'Simple'),
        ('VIP', 'VIP'),
    )

    status = models.CharField(max_length=10, choices=statuss, default='simple')

    def __str__(self):
        return self.first_name

class Category(models.Model):
    name = models.CharField(max_length=32,)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название машины', default='')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    rudder_choices = (
        ('левый руль', 'левый руль'),
        ('правый руль', 'правый руль')
    )
    rudder = models.CharField(max_length=50, choices=rudder_choices, default='левый руль', verbose_name='Расположение рулья')
    volume = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='Обьём двигателя')
    drive_choices = (
        ('передний привод', 'передний привод'),
        ('задний привод', 'задний привод'),
        ('полный привод', 'полный привод'),
    )

    drive_unit = models.CharField(max_length=100, choices=drive_choices, default='передний привод', verbose_name='Привод')
    type_of_fuel_choices = (
        ('бензин', 'бензин'),
        ('дизель', "дизель"),
        ('газ', "газ"),
        ('электро', "электро"),

    )
    type_of_fuel = models.CharField(max_length=15, choices=type_of_fuel_choices, default='бензин',verbose_name='Вид топлива')

    checkpoint_choices = (
        ('автомат','автомат'),
        ('механика','механика'),
    )

    checkpoint = models.CharField(max_length=15, choices=checkpoint_choices, default='автомат', verbose_name='КПП')
    mileage = models.PositiveIntegerField('Пробег машины',)
    horse_power = models.PositiveIntegerField(default=0, verbose_name='Лошадиные силы')
    max_speed = models.PositiveIntegerField(default=0, verbose_name='Максимальная скорость')
    country = models.TextField('Город,регион нахождения')
    post_time = models.DateTimeField('Время поста')
    car_year = models.PositiveIntegerField("Год машины",default='')
    price = models.PositiveIntegerField('Цена автомобиля',default=0)
    description = models.TextField('Описание владельца',blank=True, null=True)

    def __str__(self):
       return self.name

class CarPhotos(models.Model):
    car_photo = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')


class Basket(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Favorite(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
