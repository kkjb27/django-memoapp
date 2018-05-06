from django.db import models


class Memo(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'memos'


