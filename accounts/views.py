from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm
from order.models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponseRedirect


# Create your views here.
def register(request):
    '''
    Render the register page
    '''
    form = RegisterForm()
    if request.method == "POST":
        # Retrieve form values
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password_confirm = request.POST["password_confirm"]
        # Check if both passwords match
        if password == password_confirm:
            # Check username hasn't already been used in DB
            if User.objects.filter(username=username).exists():
                messages.error(request, "That username already exists")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "That email already exists")
                    return redirect("register")
                else:
                    user = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=password,
                    )
                    # Login user in after successful registration
                    auth.login(request, user)
                    messages.success(
                        request, "You have succesfully registered and are now logged in"
                    )
                    return redirect("index")
        else:
            messages.error(request, "passwords do not match")
            return redirect("register")
    else:
        return render(request, "accounts/register.html", {"form": form})


def login(request):
    '''
    Return a login page and logs in user
    '''
    form = LoginForm()
    if request.method == "POST":
        # If form is valid we get both the username and password
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        # If details are valid, log user in and display message
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect("index")
        else:
            # If details don't match display error message
            messages.error(request, "Invalid username or password")
            return redirect("login")
    else:
        return render(request, "accounts/login.html", {"form": form})


def logout(request):
    '''
    Log the user out
    '''
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!")
    return redirect("index")


@login_required()
def profile(request):
    '''
    the user's profile page
    Allows the user to update their password and view order history
    '''
    if request.user.is_authenticated:
        email = str(request.user.email)
        order_details = Order.objects.filter(emailAddress=email).order_by("-created")
        paginator = Paginator(order_details, 4)
        page = request.GET.get("page")
        paged_history = paginator.get_page(page)

    context = {"order_details": paged_history, "order_details_all": order_details}
    return render(request, "accounts/profile.html", context)
