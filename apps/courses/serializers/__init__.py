# Course
from .course_create import CourseCreateSerializer
from .course_list import GetCoursesSerializer
from .course_get_single import GetSingleCourseSerializer
from .course_update import CourseUpdateSerializer
# Webinar
from .webinar_list import GetWebinarsSerializer
from .webinar_get_single import GetSingleWebinarSerializer
from .webinar_finish import FinishWebinarSerializer
from .webinar_update import WebinarUpdateSerializer
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
    # Course
    GetCoursesSerializer,
    GetSingleCourseSerializer,
    CourseUpdateSerializer,
    CourseCreateSerializer,
    # Webinar
    GetWebinarsSerializer,
    GetSingleWebinarSerializer,
    FinishWebinarSerializer,
    WebinarUpdateSerializer,
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