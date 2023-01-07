from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Post, Category, About, PostComment
from .forms import PostForms, EditForms
from django.urls import reverse_lazy
from .forms import ContactForms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .templatetags import tag


def search(request):
    if request.method == "POST":
        searched= request.POST['query']
        search = Post.objects.filter(Q(title__contains=searched))
        #search = Post.objects.filter(Q(title__icontains= searched)| Q(category__icontains= searched ))

        context = {
            "searches": search,
        }
        return render(request, "app/search.html", context)
    else:
        return render(request, "app/search.html")

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'app/index.html'

    def get_context_data(self, *args, **kwargs):
        catManu =Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['catManu'] = catManu
        return context

def categoryView(request, cats):
    categoryPost = Post.objects.filter(category= cats.replace('-', ''))
    contex = {
        'cats': cats,
        'categoryPost': categoryPost,
    }
    return render(request, 'app/categores.html', contex)


class DetailsView(DetailView):
    model = Post
    template_name = 'app/details.html'

    def get_context_data(self, *args, **kwargs):
        liked= False
        if self.object.liked.filter(id= self.request.user.id).exists():
            liked= True
        context = super().get_context_data(*args, **kwargs)
        post =context.get('object')
        comments = PostComment.objects.filter(post=post.id, parent=None)
        replies = PostComment.objects.filter(post=post.id).exclude(parent=None)
        comReply = {}
        for reply in replies:
            if reply.parent.id not in comReply.keys():
                comReply[reply.parent.id]=[reply]
            else:
                comReply[reply.parent.id].append(reply)
        context['post'] = context.get('object')
        context['comments'] = comments
        context['comReply'] = comReply
        context['liked'] = liked
        return context

def likesPost(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(id= pk)
        if post.liked.filter(id= request.user.id).exists():
            post.liked.remove(request.user)
        else:
            post.liked.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class AddPostView(CreateView):
    model = Post
    form_class = PostForms
    template_name = 'app/addPost.html'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForms
    template_name = 'app/updatePost.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'app/deletePost.html'
    success_url = reverse_lazy('index')

def about(request):
    abouts = About.objects.all()
    context ={
        'abouts': abouts,
    }
    return render(request,'app/about.html',context)

def contact(request):
    if request.method == "POST":
        form = ContactForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            comment = form.cleaned_data['comment']
            html = render_to_string('gmail/contactForm.html',
                                    {
                                        'name': name,
                                        'phone': phone,
                                        'email': email,
                                        'comment': comment,
                                    })
            send_mail('The contact form TackBook', 'This is the message', 'sayeedamin02@gmail.com',
                      ['ammin.eu@gmail.com'], html_message=html)
            return redirect('index')

    else:
        form =ContactForms()

    context ={
        'form': form,
    }
    return render(request, 'app/contact.html',context)


def postComment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        postid = request.POST['postid']
        parentid = request.POST['parentid']
        post = Post.objects.get(id=postid)
        if parentid:
            parent = PostComment.objects.get(id=parentid)
            new_comment = PostComment(comment=comment, user=request.user, post=post, parent=parent)
            new_comment.save()
        else:
            new_comment = PostComment(comment=comment, user=request.user, post=post)
            new_comment.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))