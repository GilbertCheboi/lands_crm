from django.contrib import admin

# Register your models here.
from .models import Tweet, NFLTweetLike, Comment, NFLCommentLike, Comment1, Comment2, Comment3, NFLCommentLike1, NFLCommentLike2, NFLCommentLike3


class TweetLikeAdmin(admin.TabularInline):
    model = NFLTweetLike

class CommentLikeAdmin(admin.TabularInline):
    model = NFLCommentLike

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
    model = NFLCommentLike1

class CommentLikeAdmin2(admin.TabularInline):
    model = NFLCommentLike2

class CommentLikeAdmin3(admin.TabularInline):
    model = NFLCommentLike3

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


from django.contrib import admin

# Register your models here.
