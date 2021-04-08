from django.contrib.auth.models import User
from django.db import models


class Document(models.Model):
    file_name = models.CharField(max_length=100)
    public = models.BooleanField(default=False, blank=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='documents/%Y/%m/%d')

    def __repr__(self):
        return (f'{self.__class__.__name__} : '
                f'file_name: {self.file_name},'
                f'public: {self.public}, created_at : {self.created_at},'
                f'created_by: {self.created_by}')