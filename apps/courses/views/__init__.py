# Course
from .course_create import CreateCourseAPIView
from .course_list import GetCoursesView
from .course_get_single import GetSingleCourseAPIView
from .course_update import UpdateCourseAPIView
from .course_delete import CourseDeleteAPIView
# Webinar
from .webinar_list import GetWebinarsAPIView
from .webinar_get_single import GetSingleWebinarAPIView
from .webinar_finish import FinishWebinarAPIView
from .webinar_update import UpdateWebinarAPIView
from .webinar_create import CreateWebinarAPIView
from .webinar_delete import WebinarDeleteAPIView
# Category
from .category_create import CreateCategoryAPIView
from .category_update import UpdateCategoryAPIView
from .category_list import GetCategoriesAPIView
from .category_delete import CategoryDeleteAPIView
# Module
from .module_create import ModuleCreateAPIView
from .module_list import GetModulesListAPIView
from .module_update import ModuleUpdateAPIView
from .module_delete import ModuleDeleteAPIView
# Lesson
from .lesson_create import LessonCreateAPIView
from .lesson_list import GetLessonsListAPIView
from .lesson_update import LessonUpdateAPIView
from .lesson_delete import LessonDeleteAPIView
# Comment
from .comment_create import CourseCreateCommentAPIView, WebinarCreateCommentAPIView

__all__ = [
    # Course
    CreateCourseAPIView,
    GetCoursesView,
    GetSingleCourseAPIView,
    UpdateCourseAPIView,
    CourseDeleteAPIView,
    # Webinar
    CreateWebinarAPIView,
    GetWebinarsAPIView,
    GetSingleWebinarAPIView,
    FinishWebinarAPIView,
    UpdateWebinarAPIView,
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
    WebinarCreateCommentAPIView,
]