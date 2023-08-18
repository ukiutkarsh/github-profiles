from testapp.models import Repository, UserProfile
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from testapp.forms import UserForm
from testapp.models import user_name, repos
import datetime

# Create your views here
def update_profile(p, m):
    p.followers = m['followers']
    temp_var = m['updated_at']
    p.date = temp_var[0:10]
    p.time = temp_var[11:19]
    p.save()
    return 1

def convert(d, t):
    year, month, day = d.split("-")
    hour, minute, second = t.split(":")
    m = int(minute)
    h = int(hour)
    d = int(day)
    m = m+30
    if m>60:
        h=h+1
        m = m%60
    h = h+5
    if h>24:
        d = d+1
        h = h%24
    final = datetime.datetime(int(year), int(month), int(day), h, m, int(second))
    final_date = final.strftime("%b. %d, %Y")
    final_time = final.strftime("%I:%M %p")
    return final_date, final_time

def update_repo(p, m):
    js_number = len(m)
    repo_old_set = Repository.objects.filter(owner = p).order_by('-stars')
    repo_old_list = list(repo_old_set)
    repo_old_names = []
    for i in repo_old_list:
        repo_old_names.append(i.repo_name)
    repo_new_names = []
    for i in range(0,js_number):
        repo_new_names.append(m[i]['name'])
    matches = list(set(repo_old_names).intersection(repo_new_names))
    deleted = list(set(repo_old_names).difference(matches))
    added = list(set(repo_new_names).difference(matches))
    indices = []
    for i in range(0, js_number):
        for j in added:
            if m[i]['name']==j:
                indices.append(i)
    for k in range(0,len(indices)):
        temp = Repository.objects.create(owner=p, repo_name=m[indices[k]]['name'], stars=m[indices[k]]['stargazers_count'])
    return 1

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts/login/')
    else:
        form = UserForm()
        args = {'form': form}
        return render(request, 'reg_form.html', args)

def home(request):
    current = request.user.id
    t = UserProfile.objects.get(user=current).id
    o = UserProfile.objects.all()
    o = list(o)
    context = {'o': o, 'current': t}
    return render(request, 'home.html', context)

def index(request, userprofile_id):
    curr = request.user.id
    t = UserProfile.objects.get(user=curr).id
    n = userprofile_id
    p = UserProfile.objects.get(id=n).user.id #Id of User = 49
    o = UserProfile.objects.get(user=p) # UserProfile = 38
    temp1 = user_name(o.user.username) #js
    temp2 = repos(o.user.username) # js_repo
    if curr==p:
        result = update_profile(o, temp1)
        result2 = update_repo(o, temp2)
        date, time = convert(o.date, o.time)
    else:
        date = o.date
        time = o.time
    repo_set = Repository.objects.filter(owner = o).order_by('-stars')
    repo_list = list(repo_set)
    return render(request, 'profile.html', {'repo_list': repo_list, 'o': o, 'date': date, 'time': time, 'curr': curr, 't': t})

def homepage(request):
    return render(request, 'homepage.html')