from django.views import View
import json
from .ai.django_fn import _output
from django.http import JsonResponse
import os

# ai 함수 실행 View
class PredictView(View):
    def post(self, request):
        # body의 json값 받아와서 url 이라는 변수에 저장
        json_object = json.loads(request.body)

        # if spring이 접근할 때 
        url = json_object
        # if 장고만 쓸때
        # url = json_object['imageUrl']

        # 모델 위치 상대 경로
        file_path = os.path.abspath(__file__)
        folder_path = os.path.dirname(file_path)
        model_pth = os.path.join(folder_path, 'ai/model/best_model_dropout_0.1.pth')
        
        # 모델 돌리기
        emotion = _output(url, model_pth)

        # json으로 반환
        return JsonResponse(emotion, status=200)

