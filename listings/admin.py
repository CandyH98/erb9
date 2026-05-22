from django.contrib import admin
from django import forms
from .models import Listing
from taggit.forms import TagWidget
# Register your models here.
class ListingAdminForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
        widgets = {
            'services' : TagWidget(attrs={
                "style":"width:700px"
            }),
        }

class ListingAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'is_published', 'tag_list', 'list_date', 'doctor'
    list_display_links = ('id', 'title')
    list_filter = ( 'doctor', 'services')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', "services__slug", 'doctor__name',)
    list_per_page = 25

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("services")
    
    def tag_list(self,obj):
        return ", ".join([tag.name for tag in obj.services.all()]) or "No tags"

    tag_list.short_description = "Services"

admin.site.register(Listing, ListingAdmin)