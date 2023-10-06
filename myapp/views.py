from django.http import JsonResponse
from django.utils import timezone
#from .models import EndpointData


# Create your views here.

def get_info(request):
    slack_name = request.GET.get('slack_name', 'Millenium')
    current_day = timezone.now().strftime('%A')
    utc_time = timezone.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    track = request.GET.get('track', 'Backend')

    # We retrieve other data from the model or use default values
    #data, _ = EndpointData.objects.get_or_create(pk=1)

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": "https://github.com/millenium2023/endpoint/tree/main/endpoint",
        "github_repo_url": "https://github.com/millenium2023/endpoint/blob/main/endpoint/myapp/views.py",
        "status_code": 200
    }

    return JsonResponse(response_data)
