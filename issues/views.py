from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
)
from .models import Post, Status
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)


class PostListView(ListView):
    template_name = "issues/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        published = Status.objects.get(name="published")
        context["title"] = "Published"
        context["issue_list"] = (
            Post.objects
            .filter(status=published)
            .order_by("created_on").reverse()
        )
        return context

class ToDoPostListView(LoginRequiredMixin, ListView):
    template_name = "issues/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        to_do = Status.objects.get(name="to_do")
        context["title"] = "To_Do"
        context["issue_list"] = (
            Post.objects
            .filter(status=to_do)
            .filter(author=self.request.user)
            .order_by("created_on").reverse()
        )
        return context

class InProgressPostListView(LoginRequiredMixin, ListView):
    template_name = "issues/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        in_progress = Status.objects.get(name="in_progress")
        context["title"] = "in_progress"
        context["issue_list"] = (
            Post.objects
            .filter(status=in_progress)
            .order_by("created_on").reverse()
        )
        return context  
    
class DonePostListView(LoginRequiredMixin, ListView):
    template_name = "issues/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        done = Status.objects.get(name="done")
        context["title"] = "done"
        context["issue_list"] = (
            Post.objects
            .filter(status=done)
            .order_by("created_on").reverse()
        )
        return context

class PostDetailView(UserPassesTestMixin, DetailView):
    template_name = "issues/detail.html"
    model = Post

    def test_func(self):
        issue = self.get_object()
        if issue.status.name == "published":
            return True
        elif issue.status.name == "to_do":
            if (self.request.user.is_authenticated
                    and self.request.user == issue.author):
                return True
        elif (issue.status.name == "in_progress"
                and self.request.user == issue.author):
            return True
        elif (issue.status.name == "done"
                and self.request.user == issue.author):
            return True
        else:
            return False

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "issues/new.html"
    model = Post
    fields = ["title", "body", "status", "priority"]    # temp

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "issues/edit.html"
    model = Post
    fields = ["title", "body", "status", "priority"]

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user