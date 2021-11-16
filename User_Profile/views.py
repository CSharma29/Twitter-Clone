from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from . models import Profile as ProfileModel
from twitter.models import Post


# Create your views here.
class Profile(LoginRequiredMixin, ListView):
    template_name = "User_Profile/profile.html"
    model = ProfileModel
    context_object_name = "follow"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['follow'] = ProfileModel.objects.all().exclude(user=self.request.user)
        context['posts'] = Post.objects.filter(author = self.request.user.profile)
        return context

class User_DetailView(LoginRequiredMixin, DetailView):
    model = ProfileModel
    template_name = 'User_Profile/detail.html'

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        view_profile = ProfileModel.objects.get(pk=pk)
        return view_profile
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        view_profile = self.get_object()
        my_profile = ProfileModel.objects.get(user=self.request.user)
        if view_profile.user in my_profile.following.all():
            follow = True
        else:
            follow = False
        context["follow"] = follow
        context["following"] = ProfileModel.objects.all().exclude(user=self.request.user)
        return context

@login_required
def follow_unfollow(request):
    if request.method == "POST":
        my_profile = ProfileModel.objects.get(user=request.user)
        pk = request.POST.get('profile_pk')
        obj = ProfileModel.objects.get(pk=pk)

        if obj.user in my_profile.following.all():
            my_profile.following.remove(obj.user)
        else:
            my_profile.following.add(obj.user)
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('User_Profile:user_name')

