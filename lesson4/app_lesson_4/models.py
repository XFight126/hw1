from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

# Описываем поля для будущей модели (объявления)
# --------------------------------------------------------------
# Заголовок
# Описание
# Дата создания
# Дата обновления
# Цена
# Уместен ли торг (Булевое поле)
# --------------------------------------------------------------

User = get_user_model()

class Adverisement(models.Model):
    # поле заголовка
    title = models.CharField(("Заголовок"), max_length=128)
    # описание
    description = models.TextField(("Описанние"), max_length=1000)
    # цена
    price = models.DecimalField(("Цена"), max_digits=10, decimal_places=2 )
    # торг
    auction = models.BooleanField(("Торг"), help_text='Отметьте, если торг уместен')
    # поле создания объявления
    created_add = models.DateTimeField(('Было создано'),auto_now_add=True)
    # поле обновления объявления
    updated_add = models.DateTimeField(('Было обновлено'),auto_now=True)
    # пользователь
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True)
    # поле для изображения объявления
    image = models.ImageField('Изображение', upload_to='lesson4/')
    
    
    def __str__(self):
        return f"<Advertisement: Advertisement(title={self.title},price={self.price})>"
