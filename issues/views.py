from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.urls import reverse_lazy
from .models import Issue, Status
from accounts.models import CustomUser, Role, Team

class IssueListView(LoginRequiredMixin, ListView):
    template_name = "issues/list.html"
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        role = Role.objects.get(name="product owner")
        team_po = (
            CustomUser.objects
            .filter(team=user.team)
            .filter(role=role)
        )
        to_do = Status.objects.get(name="to do")
        context["to_do_list"] = (
            Issue.objects
            .filter(Status=to_do)
            .filter(reporter=team_po[0])
            .order_by("create_on").reverse()
        )
        in_progress = Status.objects.get(name="in_progress")
        context["in_progress_list"] = (
            Issue.objects
            .filter(Status=in_progress)
            .filter(reporter=team_po[0])
            .order_by("create_on").reverse()
        )
        done = Status.objects.get(name="done")
        context["done_list"] = (
            Issue.objects
            .filter(Status=done)
            .filter(reporter=team_po[0])
            .order_by("create_on").reverse()
        )
        return context

class IssueDetailView(UserPassesTestMixin, DetailView):
    template_name = "issues/detail.html"
    model = Issue


class IssueCreateView(LoginRequiredMixin, CreateView):
    template_name = "issues/new.html"
    model = Issue
    fields = ["name", "summary", "description", "status", "prioritry"]    # temp

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "issues/edit.html"
    model = Issue
    fields = ["name", "summary", "description", "status", "prioritry"]

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class IssueDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    template_name = "issues/delete.html"
    model = Issue
    success_url = reverse_lazy("list")

    def test_func(self):
        issue = self.get_object()
        return issue.author == self.request.user