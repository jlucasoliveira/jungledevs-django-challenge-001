from rest_framework.routers import SimpleRouter

from posts.api import views

router = SimpleRouter()
router.register("admin/authors", views.AuthorViewSet, basename="author")
router.register("admin/categories", views.CategoryViewSet, basename="category")
