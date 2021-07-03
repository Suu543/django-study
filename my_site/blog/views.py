from datetime import date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.template.loader import render_to_string
from .models import Post


def get_date(post):
    return post['date']


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def post_detail(request, slug):
    try:
        identified_post = get_object_or_404(Post, slug=slug)
        return render(request, "blog/post-detail.html", {
            "post": identified_post,
            "post_tags": identified_post.tags.all()
        })

    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)

# Create your views here.
# def get_date(post):
#     return post['date']


# def starting_page(request):
#     sorted_posts = sorted(all_posts, key=get_date)
#     latest_posts = sorted_posts[-3:]
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })


# def post_detail(request, slug):
#     try:
#         identified_post = next(
#             post for post in all_posts if post['slug'] == slug)
#         return render(request, "blog/post-detail.html", {
#             "post": identified_post
#         })
#     except:
#         response_data = render_to_string("404.html")
#         return HttpResponseNotFound(response_data)


# all_posts = [
    #     {
    #         "slug": "hike-in-the-mountain",
    #         "image": "mountains.jpg",
    #         "author": "Yongsu",
    #         "date": date(2021, 7, 21),
    #         "title": "Mountain Hiking",
    #         "excerpt": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Minima exercitationem ut id voluptatem soluta cum cumque voluptatibus",
    #         "content": """
    #             Lorem, ipsum dolor sit amet consectetur adipisicing elit.
    #             Lorem, ipsum dolor sit amet consectetur adipisicing elit.
    #             Lorem, ipsum dolor sit amet consectetur adipisicing elit.
    #             Lorem, ipsum dolor sit amet consectetur adipisicing elit.
    #         """
    #     },
    #     {
    #         "slug": "coding-in-the-mountain",
    #         "image": "coding.jpg",
    #         "author": "Yongsu",
    #         "date": date(2020, 7, 21),
    #         "title": "Mountain Hiking",
    #         "excerpt": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Minima exercitationem ut id voluptatem soluta cum cumque voluptatibus",
    #         "content": """
    #             Lorem, ipsum dolor sit amet consectetur adipisicing elit.
    #             Lorem, ipsum dolor sit amet consectetur adipisicing elit.
    #             Lorem, ipsum dolor sit amet consectetur adipisicing elit.
    #             Lorem, ipsum dolor sit amet consectetur adipisicing elit.
    #         """
    #     },
    #     {
    #         "slug": "woods-in-the-mountain",
    #         "image": "woods.jpg",
    #         "author": "Yongsu",
    #         "date": date(2019, 7, 21),
    #         "title": "Mountain Hiking",
    #         "excerpt": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Minima exercitationem ut id voluptatem soluta cum cumque voluptatibus",
    #         "content": """
    #             Lorem, ipsum dolor sit amet consectetur adipisicing elit.
    #             Lorem, ipsum dolor sit amet consectetur adipisicing elit.
    #             Lorem, ipsum dolor sit amet consectetur adipisicing elit.
    #             Lorem, ipsum dolor sit amet consectetur adipisicing elit.
    #         """
    #     }
    # ]
