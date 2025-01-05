from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from website.models import Site
from .serializers import SiteSerializer, TaskSerializer
from workers.tasks import execute_task
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from website.models import TaskLog

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

class TaskStatusAPIView(APIView):
    def get(self, request, task_id, *args, **kwargs):
        try:
            # Fetch the TaskLog entry by task_id
            task_log = TaskLog.objects.get(task_id=task_id)

            # Return task status and result
            return Response({
                'task_id': task_log.task_id,
                'status': task_log.status,
                'result': task_log.result,
                'started_at': task_log.started_at,
                'finished_at': task_log.finished_at,
            }, status=status.HTTP_200_OK)

        except TaskLog.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)