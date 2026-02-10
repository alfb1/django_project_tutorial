from django.contrib import admin
from .models import Choice, Question
# Register your models here.



"""
  Tutorial Part 7
  source code from :
  https://docs.djangoproject.com/en/6.0/intro/tutorial07/

  Customize the admin form
"""
"""
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
"""

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ["pub_date", "question_text"]
    fieldsets = [
        (None, {"fields" : ["question_text"]}),
        ("Date information", {"fields":["pub_date"]}),
    ]

    inlines = [ChoiceInline]
    
    list_display = ["question_text", "pub_date", "was_published_recently"]

    list_filter = ["pub_date"]

    search_fields = ["question_text"]

"""
Customizing the AdminSite class


class MyAdminSite(admin.AdminSite):
    site_header = "Polls Administration"

admin_site = MyAdminSite(name="admin")
admin_site.register(Question, QuestionAdmin)
"""    
admin.site.register(Question, QuestionAdmin)
