from django.contrib import admin
from .models import Post, Category, Comment


class CommentItemInline(admin.TabularInline):
    '''
    Inline admin interface for managing comments related to a post.

    Attributes:
        model (Comment): The Comment model to be displayed inline.
        raw_id_fields (list): Field to be displayed as raw IDs for better performance.
    '''
    model = Comment
    raw_id_fields = ['post']


class PostAdmin(admin.ModelAdmin):
    '''
    Admin interface for managing blog posts.

    Attributes:
        search_fields (list): Fields that can be searched in the admin interface.
        list_display (list): Fields displayed in the list view of posts.
        list_filter (list): Fields that can be used to filter the list of posts.
        inlines (list): Inline models to be displayed within the post admin.
    '''
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'created_at']
    list_filter = ['category', 'created_at']
    inlines = [CommentItemInline]


class CategoryAdmin(admin.ModelAdmin):
    '''
    Admin interface for managing categories.

    Attributes:
        search_fields (list): Fields that can be searched in the admin interface.
        list_display (list): Fields displayed in the list view of categories.
    '''
    search_fields = ['title']
    list_display = ['title']


class CommentAdmin(admin.ModelAdmin):
    '''
    Admin interface for managing comments.

    Attributes:
        list_display (list): Fields displayed in the list view of comments.
    '''
    list_display = ['name', 'post', 'created_at']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
