from django.contrib import admin

from app.models import Haircut, Contestant, Donation

# Register your models here.
admin.site.register(Haircut)
admin.site.register(Contestant)
admin.site.register(Donation)
