from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CarPhotos)
admin.site.register(Favorite)
admin.site.register(Basket)