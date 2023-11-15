from .models import Notes
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils import timezone


class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url = "/smart/notes/"
    template_name = "notes/notes_delete.html"
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all().order_by("-modified")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["note"] = get_object_or_404(Notes, pk=self.kwargs["pk"])
        context["notes"] = self.get_queryset()
        # context["user_timezone"] = timezone.get_current_timezone_name()
        # context["notes"] = Notes.objects.filter(user=self.request.user)
        return context


class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    success_url = "/smart/notes/"
    form_class = NotesForm
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all().order_by("-modified")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_object(self, queryset=None):
        note = super().get_object(queryset=queryset)
        if note.user != self.request.user:
            raise Http404("Note not found")
        return note

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["note"] = get_object_or_404(Notes, pk=self.kwargs["pk"])
        context["notes"] = self.get_queryset()
        # context["user_timezone"] = timezone.get_current_timezone_name()
        # context["notes"] = Notes.objects.filter(user=self.request.user)
        return context


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    success_url = "/smart/notes/"
    form_class = NotesForm
    login_url = "/login"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notes"] = self.get_queryset()
        # context["user_timezone"] = timezone.get_current_timezone_name()
        # context["notes"] = Notes.objects.filter(user=self.request.user)
        return context

    def get_queryset(self):
        return self.request.user.notes.all().order_by("-modified")


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all().order_by("-modified")


# class NotesDetailView(LoginRequiredMixin, DetailView):
#     model = Notes
#     context_object_name = "note"
#     login_url = "/login"
#     template_name = "notes/notes_detail.html"

#     def get_object(self, queryset=None):
#         note = super().get_object(queryset=queryset)
#         if note.user != self.request.user:
#             raise Http404("Note not found")
#         return note

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["notes"] = Notes.objects.filter(user=self.request.user)
#         return context
