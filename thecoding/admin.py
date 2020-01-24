from django.contrib import admin
from .models import Block,Address,Floorplan,Developer,People
# Register your models here.
admin.site.register(Block)
admin.site.register(Address)
admin.site.register(Floorplan)
admin.site.register(Developer)
admin.site.register(People)