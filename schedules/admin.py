from django.contrib import admin

# Register your models here.
from .models import Tweet, LaligaTweetLike, Comment, LaligaCommentLike, Comment1    , Comment2    , Comment3    , LaligaCommentLike1, LaligaCommentLike2, LaligaCommentLike3


class TweetLikeAdmin(admin.TabularInline):
    model = LaligaTweetLike

class CommentLikeAdmin(admin.TabularInline):
    model = LaligaCommentLike

class TweetAdmin(admin.ModelAdmin):
    inlines = [TweetLikeAdmin]
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model = Tweet

class CommentAdmin(admin.ModelAdmin):
    inlines = [CommentLikeAdmin]
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model = Comment

class CommentLikeAdmin1(admin.TabularInline):
    model = LaligaCommentLike1

class CommentLikeAdmin2(admin.TabularInline):
    model = LaligaCommentLike2

class CommentLikeAdmin3(admin.TabularInline):
    model = LaligaCommentLike3

class CommentAdmin1(admin.ModelAdmin):
    inlines = [CommentLikeAdmin1]
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model = Comment1

class CommentAdmin2(admin.ModelAdmin):
    inlines = [CommentLikeAdmin2]
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model = Comment2

class CommentAdmin3(admin.ModelAdmin):
    inlines = [CommentLikeAdmin3]
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model = Comment3

admin.site.register(Comment1, CommentAdmin1)
admin.site.register(Comment2, CommentAdmin2)
admin.site.register(Comment3, CommentAdmin3)


admin.site.register(Tweet, TweetAdmin)
admin.site.register(Comment, CommentAdmin)


