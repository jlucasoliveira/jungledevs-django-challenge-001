from rest_framework.routers import SimpleRouter

from posts.api import views

router = SimpleRouter()
router.register("admin/authors", views.AuthorViewSet, basename="author")
router.register("admin/categories", views.CategoryViewSet, basename="category")
router.register("admin/articles", views.ArticleViewSet, basename="article")
router.register("articles", views.ArticleReadOnlyViewSet, basename="public-article")
