from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from models import News

class NewsAdminForm(forms.ModelForm):
	content = forms.CharField(widget=CKEditorWidget())
	
	class Meta:
		model = News

class NewsAdmin(admin.ModelAdmin):
	form = NewsAdminForm
	
admin.site.register(News, NewsAdmin)
