from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    preview_image = models.ImageField(
        upload_to='projects/previews/', 
        blank=True, 
        null=True, 
        verbose_name="Превью изображения"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE, 
        related_name='project_images',
        verbose_name="Проект"
    )
    image = models.ImageField(
        upload_to='projects/images/', 
        verbose_name="Изображение"
    )
    # Можно добавить порядок отображения
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Изображение проекта"
        verbose_name_plural = "Изображения проекта"
        ordering = ['order']

    def __str__(self):
        return f"Изображение для {self.project.title}"