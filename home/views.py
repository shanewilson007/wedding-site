# from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, FormView
from django.shortcuts import render, redirect
from .forms import PostForm, ReceptionForm, ExtrasForm
from .models import RSVP, Post
from django import forms
from django.contrib.auth.decorators import login_required

# --------------- Home / GET View ---------------------

class HomeView(TemplateView):
    template_name = 'home/content.html'

    def get(self,request,*args, **kwargs):
        if request.user.is_active:
            receptionform = ReceptionForm(self.request.GET or None)
            extrasform = ExtrasForm(self.request.GET or None)
            rsvps = RSVP.objects.filter(user=request.user)
            postform = PostForm(self.request.GET or None)
            posts = Post.objects.all().order_by('-date')

            args = {
                    'receptionform': receptionform, 
                    'extrasform': extrasform, 
                    'rsvps':rsvps,
                    'postform':postform, 'posts':posts
            }
            return render(request, self.template_name, args)

        else:
            posts = Post.objects.all().order_by('-date')
            return render(request, self.template_name, {'posts':posts})

# ------------------ POST / Update Views ---------------------------------

class ReceptionView(FormView):
    template_name = 'home/rsvp.html'

    def post(self, request):
        if request.method == 'POST':

            if len(RSVP.objects.filter(user=request.user)) == 0:
                form1 = ReceptionForm(request.POST)
                if form1.is_valid():
                    post = form1.save(commit=False) 
                    post.user = request.user
                    post.save()

                    guest = RSVP.objects.get(user=request.user)
                    form2 = ExtrasForm(data=request.POST, instance=guest)
                    if form2.is_valid():
                        post = form2.save(commit=False)
                        post.save()
                        return redirect('/home/#rsvp')

            else:
                guest = RSVP.objects.get(user=request.user)
                form1 = ReceptionForm(data=request.POST, instance=guest)
                form2 = ExtrasForm(data=request.POST, instance=guest)
                if form1.is_valid() or form2.is_valid():
                    post1 = form1.save(commit=False)
                    post2 = form2.save(commit=False)
                    post1.save()
                    post2.save()
                    return redirect('/home/#rsvp')
        else:
            form1 = ReceptionForm()
            form2 = ExtrasForm()

        args = {'form1':form1,
                'form2':form2,
                }
        return render(request, self.template_name, args)


class PostView(FormView):
    template_name = 'home/comments.html'

    def post(self, request):
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['post']
            form = PostForm()
            return redirect('/home/#comments')

        args = {'form':form, 'text':text}
        return render(request, self.template_name, args)


# def register(request):
#     if request.method =='POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect('/home')
#     else:
#         form = UserCreationForm()
# 
#         args = {'form':form}
#         return render(request, 'home/register.html', args)
