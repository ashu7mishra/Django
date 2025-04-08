from django.urls import path
from .views import (
    health,
    add_student,
    get_students,
    get_student_by_id,
    update_student,
    delete_student,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("health/", health),
    path("add_student/", add_student, name="add_student"),
    path("get_students/", get_students, name="get_students"),
    path("get_student/<int:student_id>/", get_student_by_id, name="get_student_by_id"),
    path("update_student/<int:student_id>/", update_student, name="update_student"),
    path("delete_student/<int:student_id>/", delete_student, name="delete_student"),
]
