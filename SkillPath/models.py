from django.db import models


class Skill(models.Model):
    """
    Skills you know
    """

    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return str(self.name)


class Course(models.Model):
    """
    The courses information
    """

    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, unique=True)

    description = models.TextField(blank=True)

    DIFFICULTY_CHOICES = [
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    ]

    difficulty = models.CharField(max_length=200, choices=DIFFICULTY_CHOICES)

    workload = models.CharField(max_length=50)

    assessment_type = models.CharField(max_length=50)

    peer = models.FloatField(default=0.0)

    skills = models.ManyToManyField(Skill, blank=True, related_name="courses")

    prerequisites = models.ManyToManyField(
        "self", blank=True, symmetrical=False, related_name="required_by"
    )

    def __str__(self):
        return f"{self.code} - {self.name}"


class Career(models.Model):
    name = models.CharField(max_length=100)

    description = models.TextField()

    skills = models.ManyToManyField(Skill, blank=True, related_name="career")

    courses = models.ManyToManyField(Course, blank=True, related_name="career")

    def __str__(self):
        return str(self.name)
