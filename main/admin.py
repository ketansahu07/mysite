from django.contrib import admin
from .models import Tutorial, TutorialCategory, TutorialSeries
# Register your models here.

class TutorialAdmin(admin.ModelAdmin):
	fieldsets = [
		("Title/date", {"fields": ["tutorial_title", "tutorial_published"]}),
		("URL", {"fields": ["tutorial_slug"]}),
		("Series", {"fields": ["tutorial_series"]}),
		("Content", {"fields": ["tutorial_content"]})
	]

admin.site.register(TutorialCategory)
admin.site.register(TutorialSeries)

admin.site.register(Tutorial, TutorialAdmin)