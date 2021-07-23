from rest_framework.decorators import api_view
from rest_framework import filters
from rest_framework import generics
from rest_framework.views import APIView
from modu_forum_api.models import Post
from .serializers import PostSerializer, CommentSerializer
from django.http import JsonResponse
from rest_framework.response import Response


#질문 리스트
class PostList(APIView):
    def get(self, request):
        post = Post.objects.all()
        if len(post) > 0:
            serializer = PostSerializer(post, many=True)
            return Response(serializer.data, status=200)
        else:
            return JsonResponse({"message": "POST DOES NOT EXIST"}, status=404)


#질문 저장
@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(status=400)


#질문 수정
@api_view(['PUT'])
def update_post(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(status=400)


#질문 삭제
@api_view(['DELETE'])
def delete_post(request, pk):
    post = Post.objects.filter(id=pk)
    if post.exists():
        post.delete()
        return Response(status=200)
    else:
        return Response(status=400)


#질문에 달린 댓글 목록
def CommentList(request, pk):
    post = Post.objects.get(pk=pk)
    comments = post.comments.all()
    post_exist = Post.objects.filter(pk=pk)

    if post_exist.exists():
        if request.method == 'GET':
            serializer = CommentSerializer(comments, context={'request': request}, many=True)
            return JsonResponse(serializer.data, safe=False, status=200)
    else:
        return JsonResponse({"message": "COMMENT DOES NOT EXIST"}, status=400)


# 댓글 저장
@api_view(['POST'])
def create_comment(request, pk):
    serializer = CommentSerializer(data=request.data)
    post_exist = Post.objects.filter(pk=pk)
    if post_exist.exists():
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
    return JsonResponse({"message": "POST DOES NOT EXIST"}, status=400)


#키워드로 질문의 제목 또는 본문내용을 검색
class PostSearch(generics.ListAPIView):
    post = Post.objects.all()
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

