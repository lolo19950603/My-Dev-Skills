from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

SKILLS = (
    (1, '1 - Fundamental Awareness'),
    (2, '2 - Novice'),
    (3, '3 - Intermediate'),
    (4, '4 - Advanced'),
    (5, '5 - Expert')
)

# Create your models here.
class Skill(models.Model):
    description = models.TextField(max_length=250)
    skill_level = models.IntegerField(
        max_length=1,
	    choices=SKILLS,
	    default=SKILLS[0][0]
  )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('skills_index')

    def get_skill_display(self):
        return SKILLS[self.skill_level-1][1]