from rest_framework import generics
from rest_framework import permissions

from permissions import IsOwnerOrReadOnly

from bilgecode.apps.passage_planner.models import Passage
from serializers import PassageSerializer

from django.contrib.auth.models import User
from serializers import UserSerializer


class PassageList(generics.ListCreateAPIView):
    queryset = Passage.objects.all()
    serializer_class = PassageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PassageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Passage.objects.all()
    serializer_class = PassageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
