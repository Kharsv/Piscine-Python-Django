from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import DatabaseError
from django.forms import BaseForm
from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, RedirectView, DetailView

from .forms import LoginForm, FavouriteForm, PublishForm, RegisterForm
from .models import Article, UserFavouriteArticle


class Home(RedirectView):
    url = reverse_lazy('articles')


class Articles(ListView):
    template_name = 'articles.html'
    queryset = Article.objects.filter().order_by('-created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    def get(self, request: HttpRequest, *args, **kwargs):
        if self.request.user.is_authenticated:
            messages.error(self.request, 'You already logined!')
            return redirect('index')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form: LoginForm):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is None:
            messages.error(self.request, "Invalid username or password.")
            return
        login(self.request, user)
        messages.info(self.request, f"You are now logged in as {username}.")
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class Publications(ListView):
    model = Article
    template_name = 'publications.html'

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)


class Detail(DetailView):
    template_name = "detail.html"
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = context['object']
        context["favouriteForm"] = FavouriteForm(article.id)
        return context


class Logout(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('index')
    login_url = reverse_lazy('index')

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super().get_redirect_url(*args, **kwargs)



class Favourite(LoginRequiredMixin, ListView, FormView):
    template_name = "favourite.html"
    form_class = FavouriteForm
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('index')
    model: UserFavouriteArticle = UserFavouriteArticle

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def form_valid(self, form: AuthenticationForm):
        article_id = form.cleaned_data['article']
        try:
            UserFavouriteArticle.objects.get(
                article=article_id, user=self.request.user).delete()
            messages.success(
                self.request, "successful Remove to favourite.")
        except UserFavouriteArticle.DoesNotExist as e:
            try:
                UserFavouriteArticle.objects.create(
                    user=self.request.user,
                    article=Article.objects.get(id=article_id),
                )
                messages.success(
                    self.request, "successful Add to favourite.")
            except DatabaseError as e:
                messages.error(
                    self.request, "Unsuccessful Add to favourite. Database error.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Unsuccessful Add to favourite. Invalid information.")
        return redirect('favourite')

    def get_form(self, form_class=None) -> BaseForm:
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(None, **self.get_form_kwargs())


class Publish(LoginRequiredMixin, FormView):
    template_name = "publish.html"
    form_class = PublishForm
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('index')

    def form_valid(self, form: PublishForm):
        title = form.cleaned_data['title']
        synopsis = form.cleaned_data['synopsis']
        content = form.cleaned_data['content']
        try:
            Article.objects.create(
                title=title,
                author=self.request.user,
                synopsis=synopsis,
                content=content
            )
        except DatabaseError as e:
            messages.success(
                self.request, "Unsuccessful publish. DatabaseError")
            return redirect('index')
        messages.success(self.request, "Successful publish.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Unsuccessful publish. Invalid information.")
        return super().form_invalid(form)


class Register(FormView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('index')

    def get(self, request: HttpRequest, *args: str, **kwargs):
        if self.request.user.is_authenticated:
            messages.error(self.request, 'You already logined!')
            return redirect('index')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form: RegisterForm):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Registration successful.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Unsuccessful registration. Invalid information.")
        return super().form_invalid(form)