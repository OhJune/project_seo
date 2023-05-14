from django.db import models
<<<<<<< HEAD
=======
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수 입력 사항입니다.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='이메일', unique=True)
    name = models.CharField(verbose_name='이름', max_length=30)
    is_active = models.BooleanField(verbose_name='활성화 여부', default=True)
    is_staff = models.BooleanField(verbose_name='스태프 여부', default=False)
    date_joined = models.DateTimeField(verbose_name='가입일', auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.name

class RollingPaper(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rolling_papers')
    title = models.CharField(verbose_name='제목', max_length=50)
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='수정일', auto_now=True)

    def __str__(self):
        return self.title
>>>>>>> 0846c43897bbe12644ec604bf785140197af2dcd
