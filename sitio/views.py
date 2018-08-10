from django.shortcuts import render, redirect
from .models import Question, Control, Dados, Contadores, Description
from django.conf import settings
from django.views import generic
from django.views.generic import View, TemplateView
from .forms import QuestionForm
from accounts.forms import UserAdminCreationForm
from accounts.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from diagnostico.models import Relatorio
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import EmailMessage
from reportlab.pdfbase import pdfmetrics
from django.http import HttpResponse
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import PCMYKColor
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
        BaseDocTemplate, 
        PageTemplate, 
        Frame, 
        Paragraph
    )
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.colors import (
    black,
    purple,
    white,
    yellow
)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def question(request):
        description = Description.objects.all().last()
        inputs = {}
        questoes = Question.objects.all()
        form = UserAdminCreationForm()
        
        context = {
        'questoes': questoes,
        'form': form,
        'description': description,
        }
        
        if request.method == "POST":
            form = UserAdminCreationForm(request.POST or None)

            if not Control.objects.filter(identificador=request.POST.get('email')).exists():
                if form.is_valid():
                    user = form.save()
                    dados = Dados()

                    #Capturando valores dos inputs (ID DA RESPOSTA: VALOR DA PERGUNTA)
                    for questao in questoes:
                        inputs[questao.id] = request.POST.get(str(questao.id))
                    #Funções para calculo das médias de respostas de cada segmento
                    media_financeiro_estrutural = form.media_financeiro_estrutural(inputs)
                    media_marketing = form.media_marketing(inputs)
                    media_pessoas = form.media_pessoas_processos(inputs)

                    #Calculos dos niveis (determinar em que nivel a empresa está em um segmento)
                    if(media_financeiro_estrutural<=3.0): 
                        nivelA = 1 
                    elif(media_financeiro_estrutural>3.0 and media_financeiro_estrutural<=7.0): 
                        nivelA = 2 
                    else: 
                        nivelA = 3 
                    if(media_marketing<=3.0): 
                        nivelB = 1 
                    elif(media_marketing>3.0 and media_marketing<=7.0): 
                        nivelB = 2 
                    else: 
                        nivelB = 3 
                    if(media_pessoas<=3.0): 
                        nivelC = 1 
                    elif(media_pessoas>3.0 and media_pessoas<=7.0): 
                        nivelC = 2
                    else: 
                        nivelC = 3

                    #Salvando médias e níveis necessários na tabela de Dados
                    form.atualizar_media_and_niveis(dados,media_financeiro_estrutural,media_marketing,media_pessoas,nivelA,nivelB,nivelC, user.pk, user.email, inputs)
                    dados.save()

                    
                    #Atualizando contadores na tabela de contadores
                    form.atualizar_contadores(nivelA, nivelB, nivelC, dados)

                    cont_usuarios = User.objects.all().count()

                    #Capturar os relatorios a partir do segmento e do nivel (3 relatórios sempre!)
                    rel1 = Relatorio.objects.filter(nivel=nivelA).filter(segmentos='Financeiro/Estrutural')
                    rel2 = Relatorio.objects.filter(nivel=nivelB).filter(segmentos='Marketing')
                    rel3 = Relatorio.objects.filter(nivel=nivelC).filter(segmentos='Pessoas/Processos')
                    
                    for i in rel1:
                        relatorioA = i.save()
                        print(i)

                    for j in rel2:
                        relatorioB = j.save()
                        print(j)

                    for k in rel3:
                        relatorioC = k.save()
                        print(k)

                    usuarios = User.objects.all()
                    num =  Contadores.objects.filter(pk=1).first()

                    
                    context = {
                        'relatorio1': rel1,
                        'relatorio2': rel2,
                        'relatorio3': rel3,
                        'nivelA': nivelA,
                        'nivelB': nivelB,
                        'nivelC': nivelC,
                        'mediaA': media_financeiro_estrutural,
                        'mediaB': media_marketing,
                        'mediaC': media_pessoas,
                        'usuario': usuarios,
                        'email': user.email,
                        'mediaAint': int(media_financeiro_estrutural),
                        'mediaBint': int(media_marketing),
                        'mediaCint': int(media_pessoas),
                        'inputs': inputs,
                        'cont_usuarios': cont_usuarios,
                        'num': num,
                    }
        
                    #Ao enviar uma resposta, pegamos o ID do usuário que a enviou
                    #controle = Control()
                    #controle.identificador = user.email
                    #controle.save()
                    #Enviar e-mail com relatório
                    #form.send_email(user.email)

                    #Logando o usuario recém-cadastrado, apenas para manter o template diagnostico privado
                    logger = authenticate(email=user.email)

                    if logger is not None:
                        if logger.is_active:
                            login(request, logger)        
                    form = UserAdminCreationForm()

                    return render(request, 'diagnostico/relatorio.html', context)
                else:
                    messages.error(request, 'Formulário inválido!')
                    form = UserAdminCreationForm()
                    return render(request, 'sitio/error.html', context)
            else:
                return render(request, 'sitio/error.html', context)
        return render(request, 'sitio/base.html', context)

    def get(self, request, format=None):
        labels = []
        data = {}
        return Response(data)

def generatePDF(request):

    #Cadastrando fontes para utilizar no corpo do documento em PDF
    pdfmetrics.registerFont(TTFont('Hind-Light', 'static/fonts/Hind-Light.ttf'))
    pdfmetrics.registerFont(TTFont('Hind-Medium', 'static/fonts/Hind-Medium.ttf'))
    
    #Verificando se o usuário que respondeu o formulário está logado
    if request.user.is_authenticated() and not request.user.is_superuser:
        usuario = User.objects.all().filter(email=request.user.email).last()
        def stylesheet():
            #Definindo diferentes estilos para utilizar no PDF
            styles= {
                'default': ParagraphStyle(
                    'default',
                    fontName='Hind-Light',
                    fontSize=10,
                    leading=12,
                    leftIndent=0,
                    rightIndent=0,
                    firstLineIndent=0,
                    alignment=TA_LEFT,
                    spaceBefore=0,
                    spaceAfter=5,
                    bulletFontName='Hind-Light',
                    bulletFontSize=10,
                    bulletIndent=0,
                    textColor= black,
                    backColor=None,
                    wordWrap=None,
                    borderWidth= 0,
                    borderPadding= 0,
                    borderColor= None,
                    borderRadius= None,
                    allowWidows= 1,
                    allowOrphans= 0,
                    textTransform=None,  # 'uppercase' | 'lowercase' | None
                    endDots=None,         
                    splitLongWords=1,
                ),
            }
            styles['title'] = ParagraphStyle(
                'title',
                parent=styles['default'],
                fontName='Hind-Medium',
                fontSize=24,
                leading=26,
                alignment=TA_LEFT,
                textColor=black,
                spaceAfter=0,
            )
            styles['title2'] = ParagraphStyle(
                'title',
                parent=styles['default'],
                fontName='Hind-Light',
                fontSize=8,
                alignment=TA_LEFT,
                textColor=black,
                spaceBefore=0,
                spaceAfter=10,
            )
            styles['subtitle'] = ParagraphStyle(
                'subtitle',
                parent=styles['default'],
                fontName='Hind-Medium',
                alignment=TA_LEFT,
                textColor=black,
                spaceBefore=10,
            )
            styles['alert'] = ParagraphStyle(
                'alert',
                parent=styles['default'],
                leading=14,
                fontName='Hind-Medium',
                bulletFontName='Hind-Medium',
                backColor=HexColor('#178089'),
                textColor=white,
                borderColor=HexColor('#178089'),
                alignment=TA_CENTER,
                textTransform='uppercase', 
                borderWidth=1,
                borderPadding=5,
                borderRadius=2,
                spaceBefore=30,
                spaceAfter=30,
            )
            return styles


        empresa = Dados.objects.get(id_usuario=usuario.id)

        nivelA = empresa.nivel_Financeiro_Estrutural
        nivelB = empresa.nivel_Marketing
        nivelC = empresa.nivel_Pessoas_Processos

        relA = Relatorio.objects.filter(nivel=nivelA).filter(segmentos='Financeiro/Estrutural').first()
        relB = Relatorio.objects.filter(nivel=nivelB).filter(segmentos='Marketing').first()
        relC = Relatorio.objects.filter(nivel=nivelC).filter(segmentos='Pessoas/Processos').first()



        def build_flowables(stylesheet):
            return [
                Paragraph('JRS - Consultoria', stylesheet['title']),
                Paragraph(' Empresa Júnior da Consultoria Empresarial da UFAL', stylesheet['title2']),
                Paragraph("Relatório realizado para a empresa: " + str(usuario.empresa), stylesheet['alert']),

                Paragraph('Média do Segmento Financeiro Estrutural: ' + str(empresa.media_Financeiro_Estrutural), stylesheet['default']),
                Paragraph('Média do Segmento de Marketing: ' + str(empresa.media_Marketing), stylesheet['default']),
                Paragraph('Média do Segmento Pessoas e Processos: ' + str(empresa.media_Pessoas_Processos), stylesheet['default']),
                Paragraph('-------------------------------------------------------------------------------', stylesheet['default']),

                Paragraph('Nível do Segmento Financeiro Estrutural: ' + str(empresa.nivel_Financeiro_Estrutural), stylesheet['default']),
                Paragraph('Nível do Segmento de Marketing: ' + str(empresa.nivel_Marketing), stylesheet['default']),
                Paragraph('Nível do Segmento Pessoas e Processos: ' + str(empresa.nivel_Pessoas_Processos), stylesheet['default']),

                Paragraph('RELATÓRIO DE DIAGNÓSTICOS', stylesheet['alert']),

                Paragraph(str(relA.titulo) + ":", stylesheet['subtitle']),
                Paragraph(str(relA.texto), stylesheet['default']),
                Paragraph('-------------------------------------------------------------------------------', stylesheet['default']),

                Paragraph(str(relB.titulo) + ":", stylesheet['subtitle']),
                Paragraph(str(relB.texto), stylesheet['default']),
                Paragraph('-------------------------------------------------------------------------------', stylesheet['default']),

                Paragraph(str(relC.titulo) + ":", stylesheet['subtitle']),
                Paragraph(str(relC.texto), stylesheet['default']),
            ]
        
        
        def create_bar_graph():

            e = Drawing(280, 250)
            bar = VerticalBarChart()
            bar.x = 60
            bar.y = 85
            data = [[empresa.media_Financeiro_Estrutural, empresa.media_Marketing, empresa.media_Pessoas_Processos]]
            bar.data = data
            bar.categoryAxis.categoryNames = ['Financeiro/Estrutural', 'Marketing', 'Pessoas/Processos']
            
            bar.categoryAxis.labels.fontName = 'Hind-Light'
            bar.categoryAxis.labels.fontSize = 5
            
            bar.bars[0].fillColor = PCMYKColor(100,0,90,50,alpha=85)
            
            e.add(bar, '')

            #e.save(formats=['pdf'], outDir='.', fnRoot=str(usuario.email) + ' - Gráficos de Diagnósticos')


        def build_pdf(filename, flowables):
            doc = BaseDocTemplate(filename)
            doc.addPageTemplates(
                [
                    PageTemplate(
                        frames=[
                            Frame(
                                doc.leftMargin,
                                doc.bottomMargin,
                                doc.width,
                                doc.height,
                                id=None
                            ),
                        ]
                    ),
                ]
            )
            doc.build(flowables)

        create_bar_graph()

        logout(request)
        build_pdf(usuario.email + ' - Relatório de Diagnósticos.pdf', build_flowables(stylesheet()))
        email = EmailMessage('[JRS - Consultoria] Relatórios de Diagnóstico', 'Olá! Segue em anexo o relatório do diagnóstico gerado a partir do formulário submetido. Agradecemos sua participação.', settings.DEFAULT_FROM_EMAIL, [usuario.email])
        email.attach_file(usuario.email + ' - Relatório de Diagnósticos.pdf')
#        email.attach_file(usuario.email + ' - Gráficos de Diagnósticos.pdf')
        email.send()
        if(email.send()):
            return render(request, 'sitio/success.html')
        else:
            return render(request, 'sitio/error2.html')

    else:
        return render(request, 'diagnostico/relatorio.html')
        
    


