from django.contrib import admin
from .models import Detail, Contact, Book, Comments

admin.AdminSite.site_header ='Shivam Database'
admin.AdminSite.site_title = 'Shivam Database'
admin.AdminSite.index_title = "Data's"

class DetailAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'phone', 'message')
    list_display_links = ()
    list_filter = ('phone',)
    list_per_page = 1
    list_max_show_all = 20
    list_editable = ('message',)
    search_fields = ('name',)

    actions = []
    actions_on_top = False
    actions_on_bottom = True
    actions_selection_counter = True

class ContactAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'b', 'c', 'user', 'Images')
    list_display_links = ()
    list_filter = ('b',)
    list_select_related = False
    list_per_page = 2
    list_max_show_all = 20
    list_editable = ('c', )
    search_fields = ('b',)

    actions = []
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True

class BookAdmin(admin.ModelAdmin):
    def chng_status_p(modeladmin, request, data):
        data.update(statuses='p')
    chng_status_p.short_description = 'Change data in our Database in Published'
    def chng_status_d(modeladmin, request, data):
        data.update(statuses='d')
    chng_status_d.short_description = 'Change data in our Database in draft'
    def chng_status_w(modeladmin, request, data):
        data.update(statuses='w')
    chng_status_w.short_description = 'Change data in our Database in withdrawn'
    list_display = ('__str__', 'names', 'show_emails', 'addresses', 'fnames', 'mnames', 'category', 'fees', 'statuses')
    list_display_links = ()
    list_filter = ('names',)
    list_per_page = 5
    list_max_show_all = 10
    list_editable = ('mnames', 'statuses')
    search_fields = ('fnames',)
    actions = ['chng_status_p', 'chng_status_d', 'chng_status_w']
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'sno', 'timestamp')
    list_display_links = ()
    list_filter = ('comment',)
    list_per_page = 20
    list_max_show_all = 10
    list_editable = ()
    search_fields = ('user',)

    actions = []
    actions_on_top = False
    actions_on_bottom = True
    actions_selection_counter = True

admin.site.register(Detail, DetailAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Comments, CommentsAdmin)
