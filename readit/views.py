from django.db import models
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, Category
from .forms import PostForm, CategoryForm


def get_posts(request):
    posts = Post.objects.all()
    template = "readit/posts.html"
    context = {
        "posts": posts,
    }
    return render(request, template, context)


def view_post(request, id):
    post = get_object_or_404(Post, id=id)
    template = "readit/post_details.html"
    context = {
        "post": post,
    }
    return render(request, template, context)


@login_required
def add_post(request):
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, "Post added")
            return redirect(reverse("posts"))
        messages.error(request, "Error. Try again.")

    template = "readit/add_post.html"
    context = {
        "form": form,
    }
    return render(request, template, context)


@login_required
def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, "Post updated")
            return redirect(reverse("posts"))
        messages.error(request, "Error. Try again.")

    template = "readit/update_post.html"
    context = {
        "form": form,
        "post": post,
    }
    return render(request, template, context)


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    messages.success(request, "Post deleted")
    post.delete()
    return redirect(reverse("posts"))


@login_required
def add_category(request):
    if not request.user.is_superuser:
        messages.error(request, "Invalid user permission")
        return redirect(reverse("posts"))
    form = CategoryForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Category added")
            return redirect(reverse("categories"))
        messages.error(request, "Error. Try again.")

    template = "readit/add_category.html"
    context = {
        "form": form,
    }
    return render(request, template, context)


@login_required
def update_category(request, id):
    if not request.user.is_superuser:
        messages.error(request, "Invalid user permission")
        return redirect(reverse("posts"))
    category = get_object_or_404(Category, id=id)
    form = CategoryForm(request.POST or None, instance=category)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Category updated")
            return redirect(reverse("categories"))
        messages.error(request, "Error. Try again.")

    template = "readit/update_category.html"
    context = {
        "form": form, 
        "category": category,
    }
    return render(request, template, context)


@login_required
def delete_category(request, id):
    if not request.user.is_superuser:
        messages.error(request, "Invalid user permission")
        return redirect(reverse("posts"))
    category = get_object_or_404(Category, id=id)
    category.delete()
    messages.success(request, "Category deleted")
    return redirect(reverse("categories"))


@login_required
def categories(request):
    if not request.user.is_superuser:
        messages.error(request, "Invalid user permission")
        return redirect(reverse("posts")) 
    categories = Category.objects.all()
    template = "readit/categories.html"
    context = {
        "categories": categories,
    }
    return render(request, template, context)
