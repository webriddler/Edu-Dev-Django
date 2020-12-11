from django.contrib import admin
from django.contrib.auth.models import Group
from .models import	headlines,events,subscription
 ##here '.' segnifies the class on the same app
from django.utils import timezone

class headlinesAdmin(admin.ModelAdmin):
	list_display=('id','title','concern','active','day','created','author','last_modified','ago')
	list_filter=('concern','created')
	search_fields=('title','concern','id')
	actions=('activate_articles','unactivate_articles')
	date_hierarchy=('created')


	def activate_articles(self,request,queryset):
		count=queryset.update(active=True)
		self.message_user(request,'Selected {} Article has now Active in user panels'.format(count))
	activate_articles.short_description="Make Article Active"

	def unactivate_articles(self,request,queryset):
		count2=queryset.update(active=False)
		self.message_user(request,'Selected {} Article has now Unactivated in user panels'.format(count2))
	unactivate_articles.short_description="Make Article Unactive"

class eventsAdmin(admin.ModelAdmin):
	list_display=('event_name','date','created','last_modified','active')
	list_filter=('active',)
	actions=('activate_events','unactivate_events') #REquires Two or more values else give error
	search_fields=('event_name','date')

	def activate_events(self,request,queryset):
		count3=queryset.update(active=True,last_modified=timezone.now())
		self.message_user(request,'Selected {} events has been active now'.format(count3))
	activate_events.short_description="Make Event Active"

	def unactivate_events(self,request,queryset):
		count4=queryset.update(active=False)
		self.message_user(request,'Selected {} events has been deactive now'.format(count4))
	activate_events.short_description="Make Event Deactive"


class subsAdmin(admin.ModelAdmin):
	list_display=('name','email','created','active')
	search_fields=('name',)


admin.site.register(events,eventsAdmin)
admin.site.register(headlines,headlinesAdmin)
admin.site.register(subscription,subsAdmin)

admin.site.unregister(Group)
admin.site.site_header='Edu Dev a Learning Platform of SHCSD'
admin.site.index_title='Edu Dev Admin Panel'	