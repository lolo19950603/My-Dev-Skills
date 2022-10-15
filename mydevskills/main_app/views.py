from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Skill
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')

class SkillList(ListView):
  model = Skill

class SkillCreate(CreateView):
  model = Skill
  fields = ['description', 'skill_level']

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class SkillUpdate(UpdateView):
  model = Skill
  fields = ['description', 'skill_level']

class SkillDelete(DeleteView):
  model = Skill
  success_url = '/skills/'
