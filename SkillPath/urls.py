from django.urls import path
from . import views

urlpatterns = [
    path(
        "", views.index, name="index"
    ),  # when someone visit /, call the index function in views.py
    path(
        "courses/", views.course_list, name="course_list"
    ),  # /courses/ calls course_list
    path(
        "courses/<int:pk>/", views.course_detail, name="course_detail"
    ),  # calls course_detail and passes primary key = 3 to it
    path("careers/", views.career_list, name="career_list"),
    path("compare/", views.compare, name="compare"),
    path("compare/add/<int:pk>/", views.compare_add, name="comapre_add"),
    path("compare/remove/<int:pk>/", views.compare_remove, name="compare_remove"),
    path("plan/", views.plan, name="plan"),
    path("plan/add/<int:pk>/", views.plan_add, name="plan_add"),
    path("plan/remove/<int:pk>/", views.plan_remove, name="plan_remove"),
    path("validate/", views.validate, name="validate"),
    path("skill-tracker/", views.skill_tracker, name="skill_tracker"),
    path("advisor/", views.ai_advisor, name="ai_advisor"),
]
