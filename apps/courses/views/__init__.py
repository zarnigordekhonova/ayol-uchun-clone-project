from .get_courses import GetCoursesView
from .get_webinars import GetWebinarsAPIView
from .get_single_course import GetSingleCourseAPIView
from .get_single_webinar import GetSingleWebinarAPIView
from .finish_webinar import FinishWebinarAPIView
from .course_update import UpdateCourseAPIView
from .webinar_update import UpdateWebinarAPIView
from .course_create import CreateCourseAPIView
from .webinar_create import CreateWebinarAPIView
from .course_delete import CourseDeleteAPIView
from .webinar_delete import WebinarDeleteAPIView

from .category_create import CreateCategoryAPIView
from .category_update import UpdateCategoryAPIView
from .category_list import GetCategoriesAPIView
from .category_delete import CategoryDeleteAPIView

from .module_create import ModuleCreateAPIView
from .modules_list import GetModulesListAPIView
from .module_update import ModuleUpdateAPIView
from .module_delete import ModuleDeleteAPIView

from .lesson_create import LessonCreateAPIView
from .lessons_list import GetLessonsListAPIView
from .lesson_update import LessonUpdateAPIView
from .lesson_delete import LessonDeleteAPIView

from .comment_create import CourseCreateCommentAPIView, WebinarCreateCommentAPIView

__all__ = [
    GetCoursesView,
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
    WebinarCreateCommentAPIView,
]