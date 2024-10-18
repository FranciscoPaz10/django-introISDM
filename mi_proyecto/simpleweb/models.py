from django.db import models

# Create your models here.
class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=100)
    is_deleted = models.IntegerField()

    class Meta:
        db_table = 'tb_category'
        managed = False  # Para indicar que Django no gestionará la creación de esta tabla

    def __str__(self):
        return self.category_name