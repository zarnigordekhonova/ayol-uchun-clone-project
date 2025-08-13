from django.urls import path

from apps.courses.views import (GetCoursesView,
                                GetWebinarsAPIView,
                                GetSingleCourseAPIView,
                                GetSingleWebinarAPIView,
                                FinishWebinarAPIView,
                                UpdateCourseAPIView,
                                UpdateWebinarAPIView,
                                CreateCourseAPIView,
                                CreateWebinarAPIView,
                                CourseDeleteAPIView,
                                WebinarDeleteAPIView,

                                CreateCategoryAPIView,
                                UpdateCategoryAPIView,
                                GetCategoriesAPIView,
                                CategoryDeleteAPIView,

                                ModuleCreateAPIView,
                                GetModulesListAPIView,
                                ModuleUpdateAPIView,
                                ModuleDeleteAPIView,

                                LessonCreateAPIView,
                                GetLessonsListAPIView,
                                LessonUpdateAPIView,
                                LessonDeleteAPIView,

                                CourseCreateCommentAPIView,
                                WebinarCreateCommentAPIView
                                )

app_name = "courses"

urlpatterns = [
    path("get-courses/", GetCoursesView.as_view(), name="get-courses"),
    path("get-webinars/", GetWebinarsAPIView.as_view(), name="get-webinars"),
    path("get/<int:pk>/course/", GetSingleCourseAPIView.as_view(), name="get-single-course"),
    path("get/<int:pk>/webinar/", GetSingleWebinarAPIView.as_view(), name="get-single-webinar"),
    path("finish/<int:pk>/webinar/", FinishWebinarAPIView.as_view(), name="finish-webinar"),
    path("update/<int:pk>/course/", UpdateCourseAPIView.as_view(), name="update-course"),
    path("update/<int:pk>/webinar/", UpdateWebinarAPIView.as_view(), name="update-webinar"),
    path("create-course/", CreateCourseAPIView.as_view(), name="create-course"),
    path("create-webinar/", CreateWebinarAPIView.as_view(), name="create-webinar"),
    path("delete/<int:pk>/course/", CourseDeleteAPIView.as_view(), name="delete-course"),
    path("delete/<int:pk>/webinar/", WebinarDeleteAPIView.as_view(), name="delete-webinar"),

    path("create-category/", CreateCategoryAPIView.as_view(), name="create-category"),
    path("update/<int:pk>/category/", UpdateCategoryAPIView.as_view(), name="update-category"),
    path("category-list/", GetCategoriesAPIView.as_view(), name="category-list"),
    path("category/<int:pk>/delete/", CategoryDeleteAPIView.as_view(), name="category-delete"),

    path("module-create/", ModuleCreateAPIView.as_view(), name="module-create",),
    path("module-list/", GetModulesListAPIView.as_view(), name="module-list"),
    path("update/<int:pk>/module/", ModuleUpdateAPIView.as_view(), name="module-update"),
    path("delete/<int:pk>/module/", ModuleDeleteAPIView.as_view(), name="modul-delete"),

    path("lesson-create/", LessonCreateAPIView.as_view(), name="lesson-create"),
    path("lesson-list/", GetLessonsListAPIView.as_view(), name="lesson-list"),
    path("update/<int:pk>/lesson/", LessonUpdateAPIView.as_view(), name="lesson-update"),
    path("delete/<int:pk>/lesson/", LessonDeleteAPIView.as_view(), name="delete-lesson"),

    path("course-comment-create/", CourseCreateCommentAPIView.as_view(), name="course-comment-create"),
    path("webinar-comment-create/", WebinarCreateCommentAPIView.as_view(), name="webinar-comment-create"),

]