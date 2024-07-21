from django.shortcuts import render
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from datetime import date

navs = [
    'Politics',
    'Sports',
    'Business',
    'Tech',
    'Design',
    'Lifestyle',
    'Music',
    'Entertainment',
    'Entrepreneurship',
    'Culture',
    'Science',
    'More'
]

headlines = [
    {
        'topic': 'Design',
        'tag_title': 'Tags',
        'tag_1': 'Graphic Design',
        'tag_2': 'Illustration',
        'img': 'https://images.unsplash.com/photo-1518349619113-03114f06ac3a?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=619d961cdefa53c694595af8c409839e&auto=format&fit=crop&w=2250&q=80',
        'title': 'A Year Of UX, Straight Out Of College',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In eros ante, imperdiet efficitur venenatis eu, imperdiet non odio. Nunc ornare eu ipsum ac porta.',
        'author': 'Jane Doe',
        'read_time': '4 min read',
        'post_date': date(2024, 6, 22).strftime("%b %d, %Y")
    },
    {
        'topic': 'Entertainment',
        'tag_title': 'Tags',
        'tag_1': 'Christopher Pratt',
        'tag_2': 'Dinosaurs',
        'img': 'https://78.media.tumblr.com/2751ed3251b8727eafea857baffb8dbf/tumblr_nq3zattMun1u47gvjo1_1280.jpg',
        'title': 'Jurassic World, An Ending You Did not See Coming.',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In eros ante, imperdiet efficitur venenatis eu, imperdiet non odio. Nunc ornare eu ipsum ac porta.',
        'author': 'Dana Hayes',
        'read_time': '2 min read',
        'post_date': date(2024, 1, 12).strftime("%b %d, %Y")
    },
    {
        'topic': 'Tech',
        'tag_title': 'Tags',
        'tag_1': 'Arduino',
        'tag_2': 'DIY',
        'img': 'https://images.unsplash.com/photo-1517420704952-d9f39e95b43e?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=b2a93380e2d61894168230dfdb6e99f1&auto=format&fit=crop&w=2250&q=80',
        'title': 'Make Your Own Robot With This Simple Kit',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In eros ante, imperdiet efficitur venenatis eu, imperdiet non odio. Nunc ornare eu ipsum ac porta.',
        'author': 'Erik Voss',
        'read_time': '5 min read',
        'post_date': date(2024, 7, 14).strftime("%b %d, %Y")
    },
    {
        'topic': 'Music',
        'tag_title': 'Tags',
        'tag_1': 'Hip Hop',
        'tag_2': 'RB&B',
        'img': 'https://cdn.cnn.com/cnnnext/dam/assets/180617012056-beyonce-jayz-apes--t-screengrab.jpg',
        'title': 'Beyonce Is Back At It Again, Beehive Rejoice !!!',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In eros ante, imperdiet efficitur venenatis eu, imperdiet non odio. Nunc ornare eu ipsum ac porta.',
        'author': 'Carly Johanneson',
        'read_time': '2 min read',
        'post_date': date(2024, 4, 20).strftime("%b %d, %Y")
    }
]

posts = [
    {
        'title': 'Why You Should Start Playing Fortnite Right Now. It is Amazing.',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In eros ante, imperdiet efficitur venenatis eu, imperdiet non odio. Nunc ornare eu ipsum ac porta.',
        'author': 'Gibson Snipes',
        'read_time': '9 min read',
        'post_date': date(2024, 4, 21).strftime("%b %d, %Y")
    },
    {
        'title': 'Learning To Dance By Yourself And Why It is Important For Your Self Esteem',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In eros ante, imperdiet efficitur venenatis eu, imperdiet non odio. Nunc ornare eu ipsum ac porta.',
        'author': 'Milicent Lynn',
        'read_time': '5 min read',
        'post_date': date(2024, 7, 11).strftime("%b %d, %Y")
    }
]

bookmarks = [
    {
        'link': 'Entertainment',
        'title': 'From Draft to Full-time Novelist in 6 months',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In eros ante, imperdiet efficitur venenatis eu, imperdiet non odio. Nunc ornare eu ipsum ac porta.',
        'author': 'Vacys Mane',
        'read_time': '14 min read',
        'post_date': date(2024, 3, 19).strftime("%b %d, %Y")
    },
    {
        'link': 'Entertainment',
        'title': 'Thinking About Starting A T-Shirt Business? Here is What You Should Know.',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In eros ante, imperdiet efficitur venenatis eu, imperdiet non odio. Nunc ornare eu ipsum ac porta.',
        'author': 'JiJi Bernard',
        'read_time': '22 min read',
        'post_date': date(2024, 8, 1).strftime("%b %d, %Y")
    }
]

links = {
    'home': 'Home Page',
    'about': 'About Page'
}


def main(request):
    return render(request, 'starting_app/main.html', {'navs': navs, 'headlines': headlines, 'posts': posts, 'bookmarks': bookmarks})


def redirect(request, link):
    try:
        pages = list(links.keys())
        redirect_link = pages[link - 1]
        redirect_path = reverse('main-pages', args=[redirect_link])
        return HttpResponseRedirect(redirect_path)
    except:
        raise Http404()