from django.db import models


class CategoryManager(models.Manager):
    def enabled(self):
        """Возвращает категории enabled=True."""
        return (
            super().get_queryset().filter(
                enabled=True
            )
        )
