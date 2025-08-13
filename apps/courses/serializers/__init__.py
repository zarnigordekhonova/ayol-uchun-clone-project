from .get_courses import GetCoursesSerializer
from .get_webinars import GetWebinarsSerializer
from .get_single_course import GetSingleCourseSerializer
from .get_single_webinar import GetSingleWebinarSerializer
from .finish_webinar import FinishWebinarSerializer
from .course_update import CourseUpdateSerializer
from .webinar_update import WebinarUpdateSerializer
from .course_create import CourseCreateSerializer
from .webinar_create import WebinarCreateSerializer
# Category
from .category_create import CreateCategorySerializer
from .category_update import UpdateCategorySerializer
from .category_list import GetCategorySerializer
# Module
from .module_create import ModuleCreateSerializer
from .module_list import GetModulesListSerializer
from .module_update import ModuleUpdateSerializer
# Lesson
from .lesson_create import LessonCreateSerializer
from .lesson_list import GetLessonListSerializer
from .lesson_update import LessonUpdateSerializer
# Webinar
from .comment_create import CourseCommentCreateSerializer, WebinarCommentCreateSerializer


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
    # Category
    CreateCategorySerializer,
    UpdateCategorySerializer,
    GetCategorySerializer,
    # Module
    ModuleCreateSerializer,
    GetModulesListSerializer,
    ModuleUpdateSerializer,
    # Lesson
    LessonCreateSerializer,
    GetLessonListSerializer,
    LessonUpdateSerializer,
    # Comment
    CourseCommentCreateSerializer,
    WebinarCommentCreateSerializer,
]