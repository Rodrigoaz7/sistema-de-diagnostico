from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import logout, authenticate, login
from accounts.models import User
from sitio.models import Contadores
from reportlab.pdfgen import canvas
from django.http import HttpResponse


class HomeView(View):
    def get(self, request, *args, **kwargs):
        contador = Contadores.objects.first()
        usuarios = User.objects.all().count()
        
        media_p1_r1 = contador.num_pergunta_1_resposta_1/usuarios*100
        media_p1_r2 = contador.num_pergunta_1_resposta_2/usuarios*100
        media_p1_r3 = contador.num_pergunta_1_resposta_3/usuarios*100
        media_p1_r4 = contador.num_pergunta_1_resposta_4/usuarios*100
        media_p1_r5 = contador.num_pergunta_1_resposta_5/usuarios*100
        media_p1_r6 = contador.num_pergunta_1_resposta_6/usuarios*100
        media_p1_r7 = contador.num_pergunta_1_resposta_7/usuarios*100
        media_p1_r8 = contador.num_pergunta_1_resposta_8/usuarios*100
        media_p1_r9 = contador.num_pergunta_1_resposta_9/usuarios*100
        media_p1_r10 = contador.num_pergunta_1_resposta_10/usuarios*100
        
        media_p2_r1 = contador.num_pergunta_2_resposta_1/usuarios*100
        media_p2_r2 = contador.num_pergunta_2_resposta_2/usuarios*100
        media_p2_r3 = contador.num_pergunta_2_resposta_3/usuarios*100
        media_p2_r4 = contador.num_pergunta_2_resposta_4/usuarios*100
        media_p2_r5 = contador.num_pergunta_2_resposta_5/usuarios*100
        media_p2_r6 = contador.num_pergunta_2_resposta_6/usuarios*100
        media_p2_r7 = contador.num_pergunta_2_resposta_7/usuarios*100
        media_p2_r8 = contador.num_pergunta_2_resposta_8/usuarios*100
        media_p2_r9 = contador.num_pergunta_2_resposta_9/usuarios*100
        media_p2_r10 = contador.num_pergunta_2_resposta_10/usuarios*100
        
        media_p3_r1 = contador.num_pergunta_3_resposta_1/usuarios*100
        media_p3_r2 = contador.num_pergunta_3_resposta_2/usuarios*100
        media_p3_r3 = contador.num_pergunta_3_resposta_3/usuarios*100
        media_p3_r4 = contador.num_pergunta_3_resposta_4/usuarios*100
        media_p3_r5 = contador.num_pergunta_3_resposta_5/usuarios*100
        media_p3_r6 = contador.num_pergunta_3_resposta_6/usuarios*100
        media_p3_r7 = contador.num_pergunta_3_resposta_7/usuarios*100
        media_p3_r8 = contador.num_pergunta_3_resposta_8/usuarios*100
        media_p3_r9 = contador.num_pergunta_3_resposta_9/usuarios*100
        media_p3_r10 = contador.num_pergunta_3_resposta_10/usuarios*100
        
        media_p4_r1 = contador.num_pergunta_4_resposta_1/usuarios*100
        media_p4_r2 = contador.num_pergunta_4_resposta_2/usuarios*100
        media_p4_r3 = contador.num_pergunta_4_resposta_3/usuarios*100
        media_p4_r4 = contador.num_pergunta_4_resposta_4/usuarios*100
        media_p4_r5 = contador.num_pergunta_4_resposta_5/usuarios*100
        media_p4_r6 = contador.num_pergunta_4_resposta_6/usuarios*100
        media_p4_r7 = contador.num_pergunta_4_resposta_7/usuarios*100
        media_p4_r8 = contador.num_pergunta_4_resposta_8/usuarios*100
        media_p4_r9 = contador.num_pergunta_4_resposta_9/usuarios*100
        media_p4_r10 = contador.num_pergunta_4_resposta_10/usuarios*100
        
        media_p5_r1 = contador.num_pergunta_5_resposta_1/usuarios*100
        media_p5_r2 = contador.num_pergunta_5_resposta_2/usuarios*100
        media_p5_r3 = contador.num_pergunta_5_resposta_3/usuarios*100
        media_p5_r4 = contador.num_pergunta_5_resposta_4/usuarios*100
        media_p5_r5 = contador.num_pergunta_5_resposta_5/usuarios*100
        media_p5_r6 = contador.num_pergunta_5_resposta_6/usuarios*100
        media_p5_r7 = contador.num_pergunta_5_resposta_7/usuarios*100
        media_p5_r8 = contador.num_pergunta_5_resposta_8/usuarios*100
        media_p5_r9 = contador.num_pergunta_5_resposta_9/usuarios*100
        media_p5_r10 = contador.num_pergunta_5_resposta_10/usuarios*100
        
        media_p6_r1 = contador.num_pergunta_6_resposta_1/usuarios*100
        media_p6_r2 = contador.num_pergunta_6_resposta_2/usuarios*100
        media_p6_r3 = contador.num_pergunta_6_resposta_3/usuarios*100
        media_p6_r4 = contador.num_pergunta_6_resposta_4/usuarios*100
        media_p6_r5 = contador.num_pergunta_6_resposta_5/usuarios*100
        media_p6_r6 = contador.num_pergunta_6_resposta_6/usuarios*100
        media_p6_r7 = contador.num_pergunta_6_resposta_7/usuarios*100
        media_p6_r8 = contador.num_pergunta_6_resposta_8/usuarios*100
        media_p6_r9 = contador.num_pergunta_6_resposta_9/usuarios*100
        media_p6_r10 = contador.num_pergunta_6_resposta_10/usuarios*100
        
        media_p7_r1 = contador.num_pergunta_7_resposta_1/usuarios*100
        media_p7_r2 = contador.num_pergunta_7_resposta_2/usuarios*100
        media_p7_r3 = contador.num_pergunta_7_resposta_3/usuarios*100
        media_p7_r4 = contador.num_pergunta_7_resposta_4/usuarios*100
        media_p7_r5 = contador.num_pergunta_7_resposta_5/usuarios*100
        media_p7_r6 = contador.num_pergunta_7_resposta_6/usuarios*100
        media_p7_r7 = contador.num_pergunta_7_resposta_7/usuarios*100
        media_p7_r8 = contador.num_pergunta_7_resposta_8/usuarios*100
        media_p7_r9 = contador.num_pergunta_7_resposta_9/usuarios*100
        media_p7_r10 = contador.num_pergunta_7_resposta_10/usuarios*100
        
        media_p8_r1 = contador.num_pergunta_8_resposta_1/usuarios*100
        media_p8_r2 = contador.num_pergunta_8_resposta_2/usuarios*100
        media_p8_r3 = contador.num_pergunta_8_resposta_3/usuarios*100
        media_p8_r4 = contador.num_pergunta_8_resposta_4/usuarios*100
        media_p8_r5 = contador.num_pergunta_8_resposta_5/usuarios*100
        media_p8_r6 = contador.num_pergunta_8_resposta_6/usuarios*100
        media_p8_r7 = contador.num_pergunta_8_resposta_7/usuarios*100
        media_p8_r8 = contador.num_pergunta_8_resposta_8/usuarios*100
        media_p8_r9 = contador.num_pergunta_8_resposta_9/usuarios*100
        media_p8_r10 = contador.num_pergunta_8_resposta_10/usuarios*100
        
        media_p9_r1 = contador.num_pergunta_9_resposta_1/usuarios*100
        media_p9_r2 = contador.num_pergunta_9_resposta_2/usuarios*100
        media_p9_r3 = contador.num_pergunta_9_resposta_3/usuarios*100
        media_p9_r4 = contador.num_pergunta_9_resposta_4/usuarios*100
        media_p9_r5 = contador.num_pergunta_9_resposta_5/usuarios*100
        media_p9_r6 = contador.num_pergunta_9_resposta_6/usuarios*100
        media_p9_r7 = contador.num_pergunta_9_resposta_7/usuarios*100
        media_p9_r8 = contador.num_pergunta_9_resposta_8/usuarios*100
        media_p9_r9 = contador.num_pergunta_9_resposta_9/usuarios*100
        media_p9_r10 = contador.num_pergunta_9_resposta_10/usuarios*100
        
        media_p10_r1 = contador.num_pergunta_10_resposta_1/usuarios*100
        media_p10_r2 = contador.num_pergunta_10_resposta_2/usuarios*100
        media_p10_r3 = contador.num_pergunta_10_resposta_3/usuarios*100
        media_p10_r4 = contador.num_pergunta_10_resposta_4/usuarios*100
        media_p10_r5 = contador.num_pergunta_10_resposta_5/usuarios*100
        media_p10_r6 = contador.num_pergunta_10_resposta_6/usuarios*100
        media_p10_r7 = contador.num_pergunta_10_resposta_7/usuarios*100
        media_p10_r8 = contador.num_pergunta_10_resposta_8/usuarios*100
        media_p10_r9 = contador.num_pergunta_10_resposta_9/usuarios*100
        media_p10_r10 = contador.num_pergunta_10_resposta_10/usuarios*100
        
        media_p11_r1 = contador.num_pergunta_11_resposta_1/usuarios*100
        media_p11_r2 = contador.num_pergunta_11_resposta_2/usuarios*100
        media_p11_r3 = contador.num_pergunta_11_resposta_3/usuarios*100
        media_p11_r4 = contador.num_pergunta_11_resposta_4/usuarios*100
        media_p11_r5 = contador.num_pergunta_11_resposta_5/usuarios*100
        media_p11_r6 = contador.num_pergunta_11_resposta_6/usuarios*100
        media_p11_r7 = contador.num_pergunta_11_resposta_7/usuarios*100
        media_p11_r8 = contador.num_pergunta_11_resposta_8/usuarios*100
        media_p11_r9 = contador.num_pergunta_11_resposta_9/usuarios*100
        media_p11_r10 = contador.num_pergunta_11_resposta_10/usuarios*100
        
        media_p12_r1 = contador.num_pergunta_12_resposta_1/usuarios*100
        media_p12_r2 = contador.num_pergunta_12_resposta_2/usuarios*100
        media_p12_r3 = contador.num_pergunta_12_resposta_3/usuarios*100
        media_p12_r4 = contador.num_pergunta_12_resposta_4/usuarios*100
        media_p12_r5 = contador.num_pergunta_12_resposta_5/usuarios*100
        media_p12_r6 = contador.num_pergunta_12_resposta_6/usuarios*100
        media_p12_r7 = contador.num_pergunta_12_resposta_7/usuarios*100
        media_p12_r8 = contador.num_pergunta_12_resposta_8/usuarios*100
        media_p12_r9 = contador.num_pergunta_12_resposta_9/usuarios*100
        media_p12_r10 = contador.num_pergunta_12_resposta_10/usuarios*100
        
        
        
        
        context = {
            'contador': contador,
            'usuarios': usuarios,
            
            'media_p1_r1': media_p1_r1,
            'media_p1_r2': media_p1_r2,
            'media_p1_r3': media_p1_r3,
            'media_p1_r4': media_p1_r4,
            'media_p1_r5': media_p1_r5,
            'media_p1_r6': media_p1_r6,
            'media_p1_r7': media_p1_r7,
            'media_p1_r8': media_p1_r8,
            'media_p1_r9': media_p1_r9,
            'media_p1_r10': media_p1_r10,
            
            'media_p2_r1': media_p2_r1,
            'media_p2_r2': media_p2_r2,
            'media_p2_r3': media_p2_r3,
            'media_p2_r4': media_p2_r4,
            'media_p2_r5': media_p2_r5,
            'media_p2_r6': media_p2_r6,
            'media_p2_r7': media_p2_r7,
            'media_p2_r8': media_p2_r8,
            'media_p2_r9': media_p2_r9,
            'media_p2_r10': media_p2_r10,
            
            'media_p3_r1': media_p3_r1,
            'media_p3_r2': media_p3_r2,
            'media_p3_r3': media_p3_r3,
            'media_p3_r4': media_p3_r4,
            'media_p3_r5': media_p3_r5,
            'media_p3_r6': media_p3_r6,
            'media_p3_r7': media_p3_r7,
            'media_p3_r8': media_p3_r8,
            'media_p3_r9': media_p3_r9,
            'media_p3_r10': media_p3_r10,
            
            'media_p4_r1': media_p4_r1,
            'media_p4_r2': media_p4_r2,
            'media_p4_r3': media_p4_r3,
            'media_p4_r4': media_p4_r4,
            'media_p4_r5': media_p4_r5,
            'media_p4_r6': media_p4_r6,
            'media_p4_r7': media_p4_r7,
            'media_p4_r8': media_p4_r8,
            'media_p4_r9': media_p4_r9,
            'media_p4_r10': media_p4_r10,
            
            'media_p5_r1': media_p5_r1,
            'media_p5_r2': media_p5_r2,
            'media_p5_r3': media_p5_r3,
            'media_p5_r4': media_p5_r4,
            'media_p5_r5': media_p5_r5,
            'media_p5_r6': media_p5_r6,
            'media_p5_r7': media_p5_r7,
            'media_p5_r8': media_p5_r8,
            'media_p5_r9': media_p5_r9,
            'media_p5_r10': media_p5_r10,
            
            'media_p6_r1': media_p6_r1,
            'media_p6_r2': media_p6_r2,
            'media_p6_r3': media_p6_r3,
            'media_p6_r4': media_p6_r4,
            'media_p6_r5': media_p6_r5,
            'media_p6_r6': media_p6_r6,
            'media_p6_r7': media_p6_r7,
            'media_p6_r8': media_p6_r8,
            'media_p6_r9': media_p6_r9,
            'media_p6_r10': media_p6_r10,
            
            'media_p7_r1': media_p7_r1,
            'media_p7_r2': media_p7_r2,
            'media_p7_r3': media_p7_r3,
            'media_p7_r4': media_p7_r4,
            'media_p7_r5': media_p7_r5,
            'media_p7_r6': media_p7_r6,
            'media_p7_r7': media_p7_r7,
            'media_p7_r8': media_p7_r8,
            'media_p7_r9': media_p7_r9,
            'media_p7_r10': media_p7_r10,
            
            'media_p8_r1': media_p8_r1,
            'media_p8_r2': media_p8_r2,
            'media_p8_r3': media_p8_r3,
            'media_p8_r4': media_p8_r4,
            'media_p8_r5': media_p8_r5,
            'media_p8_r6': media_p8_r6,
            'media_p8_r7': media_p8_r7,
            'media_p8_r8': media_p8_r8,
            'media_p8_r9': media_p8_r9,
            'media_p8_r10': media_p8_r10,
            
            'media_p9_r1': media_p9_r1,
            'media_p9_r2': media_p9_r2,
            'media_p9_r3': media_p9_r3,
            'media_p9_r4': media_p9_r4,
            'media_p9_r5': media_p9_r5,
            'media_p9_r6': media_p9_r6,
            'media_p9_r7': media_p9_r7,
            'media_p9_r8': media_p9_r8,
            'media_p9_r9': media_p9_r9,
            'media_p9_r10': media_p9_r10,
            
            'media_p10_r1': media_p10_r1,
            'media_p10_r2': media_p10_r2,
            'media_p10_r3': media_p10_r3,
            'media_p10_r4': media_p10_r4,
            'media_p10_r5': media_p10_r5,
            'media_p10_r6': media_p10_r6,
            'media_p10_r7': media_p10_r7,
            'media_p10_r8': media_p10_r8,
            'media_p10_r9': media_p10_r9,
            'media_p10_r10': media_p10_r10,
            
            'media_p11_r1': media_p11_r1,
            'media_p11_r2': media_p11_r2,
            'media_p11_r3': media_p11_r3,
            'media_p11_r4': media_p11_r4,
            'media_p11_r5': media_p11_r5,
            'media_p11_r6': media_p11_r6,
            'media_p11_r7': media_p11_r7,
            'media_p11_r8': media_p11_r8,
            'media_p11_r9': media_p11_r9,
            'media_p11_r10': media_p11_r10,
            
            'media_p12_r1': media_p12_r1,
            'media_p12_r2': media_p12_r2,
            'media_p12_r3': media_p12_r3,
            'media_p12_r4': media_p12_r4,
            'media_p12_r5': media_p12_r5,
            'media_p12_r6': media_p12_r6,
            'media_p12_r7': media_p12_r7,
            'media_p12_r8': media_p12_r8,
            'media_p12_r9': media_p12_r9,
            'media_p12_r10': media_p12_r10,
            
            
        }
        return render(request, 'diagnostico/relatorio.html', context)

def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response

class ChartDataAdmin(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = ["A","B", "C", "D", "E"]
        default_items = [5, 23, 2, 3, 12]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

def login_view(request):

    if request.method == 'GET':
        return render(request, 'home/login.html')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')