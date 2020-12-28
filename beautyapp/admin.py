from django.contrib import admin
from .models import *

admin.site.site_header = "Beauty salon Admin"
admin.site.site_title = "Beauty Salon admin Area"
admin.site.index_title = "Welcome to Beauty salon"

admin.site.register(Services)
admin.site.register(HairCare)
admin.site.register(MakeUpServices)
admin.site.register(FacialTreatment)
admin.site.register(NailArts)
admin.site.register(HairStyles)
admin.site.register(Pedicure)
admin.site.register(Manicure)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(BookingHaircare)
admin.site.register(BookingMakeUpServices)
admin.site.register(BookingFacialTreatment)
admin.site.register(BookingHairStyles)
admin.site.register(BookingNailArts)
admin.site.register(BookingPedicure)
admin.site.register(BookingManicure)
