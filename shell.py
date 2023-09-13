from instagramm.models import *

posts = Post.objects.all()

posts_postman = Post.objects.filter(title='Postman')

posts_filter = posts_postman.filter(body='body')


posts_2023 = Post.objects.filter(date_posted__year=2023)

post_windows = Post.objects.filter(body__startswith='Windows', date_posted__year=2022)

posts = Post.objects.filter(date_posted__year=2023)

post = Post.objects.get(id=1)

post = Post.objects.get(date_updated__year=2023)


post = Post.objects.get(date_updated__year=2024)

posts = Post.objects.exclude(date_posted__year=2023).filter(title__startswith='Linux').exclude(date_posted__year=2022)


posts = Post.objects.all().order_by('-title')

posts = Post.objects.all().values('title', 'body')

posts = Post.objects.all().values_list('title', 'body')

posts = Post.objects.all().values_list('title', flat=True)

posts = Post.objects.all().none()


comments = Comment.objects.all()

comments = Comment.objects.all().select_related('post', 'user', 'post__user')


posts = Post.objects.all()[0:2]

post = Post.objects.all().order_by()('-id')[0]

post = Post.objects.filter(id=250)[0]

posts = Post.objects.all().only('title', 'body')



# filter lookup Type

posts = Post.objects.filter(date_posted__gt='2022-12-31')


post = Post.objects.filter(id__exact=1)


post = Post.objects.filter(title__iexact='Post about Postman program')


posts = Post.objects.filter(title__icontains='program')


posts = Post.objects.filter(id__in=[3, 4])

comments = Comment.objects.filter(post__title__icontains='postman')

comments = Comment.objects.filter(post__user__username__startswith='adm')


from django.db.models import Q

posts = Post.objects.filter(
    (Q(date_posted__year=2023) | Q(title__icontains='postman')) &
    (Q(body__icontains='gaiming'))
     )