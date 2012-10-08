from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from models import Workshop

class WorkshopAdminForm(forms.ModelForm):
	content = forms.CharField(widget=CKEditorWidget())
	
	class Meta:
		model = Workshop

class WorkshopAdmin(admin.ModelAdmin):
	form = WorkshopAdminForm
	
admin.site.register(Workshop, WorkshopAdmin)
