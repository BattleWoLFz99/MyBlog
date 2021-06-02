from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "BattleWoLFz",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains!",
        "content": """
          Test Test Test Test Test Test Test Test Test Test Test Test Test Test 
          Test Test Test Test Test Test Test Test Test Test Test Test Test Test 
          Test Test Test Test Test Test Test Test Test Test Test Test Test Test 
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.png",
        "author": "BattleWoLFz",
        "date": date(2021, 6, 3),
        "title": "Programming is Great",
        "excerpt": "WSL2 for the win",
        "content": """
          Test Test Test Test Test Test Test Test Test Test Test Test Test Test 
          Test Test Test Test Test Test Test Test Test Test Test Test Test Test 
          Test Test Test Test Test Test Test Test Test Test Test Test Test Test 
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "BattleWoLFz",
        "date": date(2016, 1, 1),
        "title": "Yosemite",
        "excerpt": "Yosemite!",
        "content": """
          Test Test Test Test Test Test Test Test Test Test Test Test Test Test 
          Test Test Test Test Test Test Test Test Test Test Test Test Test Test 
          Test Test Test Test Test Test Test Test Test Test Test Test Test Test 
        """
    }
]

def get_date(post):
  return post['date']

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
      "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
      "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
      "post": identified_post
    })