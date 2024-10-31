from django.db import models


class Category(models.Model):
    '''
    Represents a category for organizing blog posts.

    Attributes:
        title (str): The name of the category.
        slug (str): A URL-friendly version of the category name.
    '''
    title = models.CharField(max_length=255)
    slug = models.SlugField()


    class Meta:
        '''
        Meta options for the Category model.
        '''
        ordering = ('title',)
        verbose_name_plural = 'Categories'


    def __str__(self):
        '''
        Returns the string representation of the Category instance.

        Returns:
            str: The title of the category.
        '''
        return self.title


    def get_absolute_url(self):
        """
        Returns the absolute URL for the instance based on its category slug and instance slug.

        The URL is constructed in the format '/<category-slug>/<instance_slug>/'.

        Returns:
            str: The absolute URL for the instance.
        """
        return '/%s/' % self.slug


class Post(models.Model):
    '''
    Represents a blog post.

    Attributes:
        category (ForeignKey): The category to which the blog post belongs.
        title (str): The title of the blog post.
        slug (str): A URL-friendly version of the blog post title.
        intro (str): A brief introduction to the blog post.
        body (str): The main content of the blog post.
        content (str): Additional content for the blog post.
        created_at (DateTimeField): The date and time the blog post was created.
        updated_at (DateTimeField): The date and time the blog post was last updated.
        status: The status of the blog post (active or draft).
        image (img): The image of the blog post.
    '''
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft'),
    )

    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)


    class Meta:
        '''
        Meta options for the Post model.
        '''
        ordering = ('-created_at',)


    def __str__(self):
        '''
        Returns the string representation of the Post instance.

        Returns:
            str: The title of the blog post.
        '''
        return self.title


    def get_absolute_url(self):
        """
        Returns the absolute URL for the instance based on its category slug and instance slug.

        The URL is constructed in the format '/<category-slug>/<instance_slug>/'.

        Returns:
            str: The absolute URL for the instance.
        """
        return '/%s/%s/' % (self.category.slug, self.slug)


class Comment(models.Model):
    '''
    Represents a comment on a blog post.

    Attributes:
        post (ForeignKey): The post to which the comment belongs.
        name (str): The name of the commenter.
        email (str): The email address of the commenter.
        body (str): The content of the comment.
        created_at (DateTimeField): The date and time the comment was created.
    '''
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''
        Returns the string representation of the Comment instance.

        Returns:
            str: The name of the commenter.
        '''
        return self.name