from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class TaskItems(models.Model): 
    io_type = models.CharField(max_length = 255)
    task_name = models.TextField()
    deliverable = models.TextField()
    category = models.CharField(max_length = 255)
    duration = models.IntegerField(
        validators=[
            MaxValueValidator(120),
            MinValueValidator(1)
        ]
    )
    effort_level = models.SmallIntegerField()
    last_chosen_date = models.DateField()

