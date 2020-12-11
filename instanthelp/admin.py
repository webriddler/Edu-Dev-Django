from django.contrib import admin
from .models import help

class helpAdmin(admin.ModelAdmin):
	list_display=('subscriber','user','name','description','date','solved')
	list_filter=('date',)
	search_fields=('subscriber','user','name')
	date_hierarchy=('date')
	actions=('solved',)

	def solved(self,request,queryset):
		ncount=queryset.update(solved=True)
		self.message_user(request,'Selected {} Issues has now solved'.format(ncount))
	solved.short_description="Has Solved"

admin.site.register(help,helpAdmin)


# Register your models here.
