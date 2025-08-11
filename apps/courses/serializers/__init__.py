from .get_courses import GetCoursesSerializer
from .get_webinars import GetWebinarsSerializer
from .get_single_course import GetSingleCourseSerializer
from .get_single_webinar import GetSingleWebinarSerializer
from .finish_webinar import FinishWebinarSerializer
from .course_update import CourseUpdateSerializer
from .webinar_update import WebinarUpdateSerializer
from .course_create import CourseCreateSerializer
from .webinar_create import WebinarCreateSerializer

from .category_create import CreateCategorySerializer
from .category_update import UpdateCategorySerializer
from .category_list import GetCategorySerializer

__all__ = [
    GetCoursesSerializer,
    GetWebinarsSerializer,
    GetSingleCourseSerializer,
    GetSingleWebinarSerializer,
    FinishWebinarSerializer,
    CourseUpdateSerializer,
    WebinarUpdateSerializer,
    CourseCreateSerializer,
    WebinarCreateSerializer,

    CreateCategorySerializer,
    UpdateCategorySerializer,
    GetCategorySerializer,
]