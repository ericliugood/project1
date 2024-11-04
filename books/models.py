from django.db import models

# Create your models here.

class MyModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class Author(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = MyModelManager()  # 自定義的過濾管理器
    all_objects = models.Manager()  # 包含所有記錄的管理器

    def delete(self, *args, **kwargs):
        # 假刪除：將 is_deleted 設為 True，而不是實際刪除記錄
        self.is_deleted = True
        self.save()



    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, through='BookAuthor')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = MyModelManager()  # 自定義的過濾管理器
    all_objects = models.Manager()  # 包含所有記錄的管理器

    def delete(self, *args, **kwargs):
        # 假刪除：將 is_deleted 設為 True，而不是實際刪除記錄
        self.is_deleted = True
        self.save()

    def __str__(self):
        return self.title
    
class BookAuthor(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    collaboration_year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = MyModelManager()  # 自定義的過濾管理器
    all_objects = models.Manager()  # 包含所有記錄的管理器

    def delete(self, *args, **kwargs):
        # 假刪除：將 is_deleted 設為 True，而不是實際刪除記錄
        self.is_deleted = True
        self.save()

class Store(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = MyModelManager()  # 自定義的過濾管理器
    all_objects = models.Manager()  # 包含所有記錄的管理器

    def delete(self, *args, **kwargs):
        # 假刪除：將 is_deleted 設為 True，而不是實際刪除記錄
        self.is_deleted = True
        self.save()

class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="orders")
    books = models.ManyToManyField(Book, through='OrderRetail')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = MyModelManager()  # 自定義的過濾管理器
    all_objects = models.Manager()  # 包含所有記錄的管理器

    def delete(self, *args, **kwargs):
        # 假刪除：將 is_deleted 設為 True，而不是實際刪除記錄
        self.is_deleted = True
        self.save()

class OrderRetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)  # 只能為正數或零
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = MyModelManager()  # 自定義的過濾管理器
    all_objects = models.Manager()  # 包含所有記錄的管理器

    def delete(self, *args, **kwargs):
        # 假刪除：將 is_deleted 設為 True，而不是實際刪除記錄
        self.is_deleted = True
        self.save()

    
