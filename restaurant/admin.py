from django.contrib import admin
from restaurant.models import Contact,User,BookTable,Product,Orders,OrderUpdate

# Register your models here.
admin.site.register(Contact)
admin.site.register(BookTable)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)