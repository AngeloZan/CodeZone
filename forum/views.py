from django.shortcuts import render, redirect

from forum.forms import NewForumPostForm
from forum.models import ForumPost

def new_post_view(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect('login')
    if request.POST:
        form = NewForumPostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            text = form.cleaned_data.get('text')
            author = request.user
            post = ForumPost(title=title, text=text, author=author)
            post.save()
            return redirect('home')
        else:
            context['new_post_form'] = form
    else:
        form = NewForumPostForm()
        context['new_post_form'] = form
    return render(request, 'forum/new-post.html', context)

