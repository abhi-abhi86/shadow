from django.db import models

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('FRONTEND', 'Frontend'),
        ('BACKEND', 'Backend'),
        ('TOOLS', 'Tools & DevOps'),
        ('OTHER', 'Other'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='OTHER')
    proficiency = models.IntegerField(help_text="Proficiency percentage (0-100)", default=50)
    icon_class = models.CharField(max_length=50, blank=True, help_text="FontAwesome class (e.g. fa-brands fa-python)")

    def __str__(self):
        return self.name
