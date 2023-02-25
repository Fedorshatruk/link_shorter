from django.contrib import admin

from shorter.models import Token, Owner


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    ...


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    ...
