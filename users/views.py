from django.contrib.auth import authenticate, logout,login
from django.shortcuts import render, redirect

from users.forms import UserLoginForm, UserRegistrationForm

#
from functools import wraps

class persist_session_vars(object):
    """
    Some views, such as login and logout, will reset all session state.
    (via a call to ``request.session.cycle_key()`` or ``session.flush()``).
    That is a security measure to mitigate session fixation vulnerabilities.

    By applying this decorator, some values are retained.
    Be very aware what find of variables you want to persist.
    """

    def __init__(self, vars):
        self.vars = vars

    def __call__(self, view_func):

        @wraps(view_func)
        def inner(request, *args, **kwargs):
            # Backup first
            session_backup = {}
            for var in self.vars:
                try:
                    session_backup[var] = request.session[var]
                except KeyError:
                    pass

            # Call the original view
            response = view_func(request, *args, **kwargs)

            # Restore variables in the new session
            for var, value in session_backup.items():
                request.session[var] = value

            return response

        return inner
#
@persist_session_vars(['cart'])
def login_view(request):
    form = UserLoginForm(request.POST or None)
    _next = request.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        _next = _next or '/'
        return redirect(_next)
    return render(request, 'users/login.html', {'form': form})

@persist_session_vars(['cart'])
def logout_view(request):
    logout(request)
    return redirect('/')

def registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'users/register_done.html', {'new_user': new_user})
        return render(request, 'users/register.html', {'form': form})
    else:
        form = UserRegistrationForm()
        return render(request, 'users/register.html', {'form': form})


