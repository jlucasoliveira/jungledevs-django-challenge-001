from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, is_superuser=is_superuser, **kwargs)
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_user(self, email, password, **kwargs):
        return self._create_user(email, password, is_staff=False, is_superuser=False, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        return self._create_user(email, password, is_staff=True, is_superuser=True, **kwargs)
