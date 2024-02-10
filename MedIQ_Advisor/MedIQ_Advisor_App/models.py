from django.db import models

# makemigrations(meaning) => create changes and store in a file
# migrate(meaning) => apply the pending chamges created by makemigrations

# # Create your models here.
class Contact(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Sign_up(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    security_question = models.CharField(max_length=100)
    security_question_answer = models.CharField(max_length=255)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

class Mental_Health_Survey(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    self_employed = models.CharField(max_length=5)
    family_history = models.CharField(max_length=5)
    mental_health_interference = models.CharField(max_length=10)
    company_size = models.CharField(max_length=20)
    remote_work = models.CharField(max_length=5)
    tech_company = models.CharField(max_length=5)
    mental_health_benefits = models.CharField(max_length=5)
    know_mental_health_care = models.CharField(max_length=10)
    discussed_mental_health = models.CharField(max_length=10)
    resources_learn_mental_health = models.CharField(max_length=10)
    anonymity_protected = models.CharField(max_length=10)
    medical_leave = models.CharField(max_length=20)
    negative_consequences_mental_health = models.CharField(max_length=10)
    negative_consequences_physical_health = models.CharField(max_length=10)
    discuss_with_coworkers = models.CharField(max_length=10)
    discuss_with_supervisors = models.CharField(max_length=10)
    bring_up_in_interview_mental_health = models.CharField(max_length=10)
    bring_up_in_interview_physical_health = models.CharField(max_length=10)
    employer_takes_mental_health_seriously = models.CharField(max_length=10)
    observed_negative_consequences = models.CharField(max_length=5)

    def __str__(self):
        return self.id