from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from website.models import Site
from .serializers import SiteSerializer, TaskSerializer
from workers.tasks import execute_task
from rest_framework.response import Response
from rest_framework import status


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

    @action(detail=True, methods=['post'])
    def execute_task(self, request, pk=None):
        site = self.get_object()
        serializer = TaskSerializer(data=request.data)
        
        if serializer.is_valid():
            task = execute_task.delay(site.id, serializer.validated_data['job_type'])
            return Response({
                'task_id': task.id,
                'status': 'Task submitted successfully'
            }, status=status.HTTP_202_ACCEPTED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)