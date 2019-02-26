

app_name = 'login'
urlpatterns = [
    url('^$', views.home, name='home'),
    url('^do_login/$', views.do_login, name='do_login')
]

@login_required(login_url='/login/do_login')
def home(request):
    return render(request,
                  'home.html',
                  {'username': request.user.username})
