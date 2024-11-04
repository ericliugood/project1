from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Author,Book,BookAuthor,Store,Order,OrderRetail
from .serializers import AuthorSerializer,BookSerializer,BookAuthorSerializer,StoreSerializer,OrderSerializer,OrderRetailSerializer

# Create your views here.

class AuthorModelViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()  # 使用過濾後的查詢集
    serializer_class = AuthorSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()  # 呼叫假刪除方法
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # 使用過濾後的查詢集
    serializer_class = BookSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()  # 呼叫假刪除方法
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class BookAuthorModelViewSet(viewsets.ModelViewSet):
    queryset = BookAuthor.objects.all()  # 使用過濾後的查詢集
    serializer_class = BookAuthorSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()  # 呼叫假刪除方法
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class StoreModelViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()  # 使用過濾後的查詢集
    serializer_class = StoreSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()  # 呼叫假刪除方法
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class OrderModelViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()  # 使用過濾後的查詢集
    serializer_class = OrderSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()  # 呼叫假刪除方法
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class OrderRetailModelViewSet(viewsets.ModelViewSet):
    queryset = OrderRetail.objects.all()  # 使用過濾後的查詢集
    serializer_class = OrderRetailSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()  # 呼叫假刪除方法
        return Response(status=status.HTTP_204_NO_CONTENT)