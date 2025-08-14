from django.urls import path

from apps.courses.views import (
                                # Course
                                CreateCourseAPIView,
                                GetCoursesView,
                                GetSingleCourseAPIView,
                                UpdateCourseAPIView,
                                CourseDeleteAPIView,
                                # Webinar
                                CreateWebinarAPIView,
                                FinishWebinarAPIView,
                                UpdateWebinarAPIView,
                                GetSingleWebinarAPIView,
                                GetWebinarsAPIView,
                                WebinarDeleteAPIView,
                                # Category
                                CreateCategoryAPIView,
                                UpdateCategoryAPIView,
                                GetCategoriesAPIView,
                                CategoryDeleteAPIView,
                                # Module
                                ModuleCreateAPIView,
                                GetModulesListAPIView,
                                ModuleUpdateAPIView,
                                ModuleDeleteAPIView,
                                # Lesson
                                LessonCreateAPIView,
                                GetLessonsListAPIView,
                                LessonUpdateAPIView,
                                LessonDeleteAPIView,
                                # Comment
                                CourseCreateCommentAPIView,
                                WebinarCreateCommentAPIView
                                )

app_name = "courses"

urlpatterns = [
    # Course
    path("create-course/", CreateCourseAPIView.as_view(), name="create-course"),
    path("get-courses/", GetCoursesView.as_view(), name="get-courses"),
    path("get/<int:pk>/course/", GetSingleCourseAPIView.as_view(), name="get-single-course"),
    path("update/<int:pk>/course/", UpdateCourseAPIView.as_view(), name="update-course"),
    path("delete/<int:pk>/course/", CourseDeleteAPIView.as_view(), name="delete-course"),
    # Webinar
    path("create-webinar/", CreateWebinarAPIView.as_view(), name="create-webinar"),
    path("get-webinars/", GetWebinarsAPIView.as_view(), name="get-webinars"),
    path("get/<int:pk>/webinar/", GetSingleWebinarAPIView.as_view(), name="get-single-webinar"),
    path("update/<int:pk>/webinar/", UpdateWebinarAPIView.as_view(), name="update-webinar"),
    path("finish/<int:pk>/webinar/", FinishWebinarAPIView.as_view(), name="finish-webinar"),
    path("delete/<int:pk>/webinar/", WebinarDeleteAPIView.as_view(), name="delete-webinar"),
    # Category
    path("create-category/", CreateCategoryAPIView.as_view(), name="create-category"),
    path("update/<int:pk>/category/", UpdateCategoryAPIView.as_view(), name="update-category"),
    path("category-list/", GetCategoriesAPIView.as_view(), name="category-list"),
    path("category/<int:pk>/delete/", CategoryDeleteAPIView.as_view(), name="category-delete"),
    # Module
    path("module-create/", ModuleCreateAPIView.as_view(), name="module-create",),
    path("module-list/", GetModulesListAPIView.as_view(), name="module-list"),
    path("update/<int:pk>/module/", ModuleUpdateAPIView.as_view(), name="module-update"),
    path("delete/<int:pk>/module/", ModuleDeleteAPIView.as_view(), name="modul-delete"),
    # Lesson
    path("lesson-create/", LessonCreateAPIView.as_view(), name="lesson-create"),
    path("lesson-list/", GetLessonsListAPIView.as_view(), name="lesson-list"),
    path("update/<int:pk>/lesson/", LessonUpdateAPIView.as_view(), name="lesson-update"),
    path("delete/<int:pk>/lesson/", LessonDeleteAPIView.as_view(), name="delete-lesson"),
    # Comment
    path("course-comment-create/", CourseCreateCommentAPIView.as_view(), name="course-comment-create"),
    path("webinar-comment-create/", WebinarCreateCommentAPIView.as_view(), name="webinar-comment-create"),
]