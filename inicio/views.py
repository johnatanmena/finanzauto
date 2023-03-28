from django.shortcuts import render,redirect
from .form import MyForm, carga
import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from django.views.generic import ListView,CreateView,UpdateView,View
from .models import chatbots, cargar

def index(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        print((request.POST))
        if form.is_valid():
            chatbot = chatbots(
            nombres = form.cleaned_data['nombres'],
            selecc = form.cleaned_data['selecc'],
            Skill = form.cleaned_data['Skill'],
            estado = form.cleaned_data['estado']
            )
            chatbot.save()
            return redirect('/watson')
    else:
        form = MyForm()
    return render(request, 'inicio/index.html', {'form': form})
class cargue(View):
    def get(self,request):
        cargo = carga
        return render(request, 'inicio/cargue.html',{'cargo': cargo})
    def post(self,request):
        if request.method == 'POST':
            cargue = carga(request.POST)
            if cargue.is_valid():
                cargado = cargar(
                    nombre = cargue.cleaned_data['nombre'],
                    chatbot = cargue.cleaned_data['chatbot'],
                    cantidad_intentos = cargue.cleaned_data['cantidad_intentos']
                    )
                cargado.save()
                return redirect('/watson')
class lista(ListView):
    template_name="inicio/watson_assistant.html"
    model = chatbots
    def post(self,request):
        if request.method == 'POST':
            seleccion = request.POST.get('seleccion')
        authenticator = IAMAuthenticator('oamwPPzKWlS9EOImbL1fyctNQDiPr8JxxdHACD0qTjgs')
        assistant = AssistantV2(
            version='2021-06-14',
            authenticator=authenticator)
        assistant.set_service_url('https://api.us-south.assistant.watson.cloud.ibm.com')
        assistant_id=seleccion
        session_id = assistant.create_session(assistant_id).get_result()['session_id']
        response = assistant.message(
            assistant_id= assistant_id,
            session_id = session_id,
            input= {
                'message_type': 'text',
                'text': 'Hola'}).get_result()
        output = response['output']['generic'][0]['text']
        return render(request, 'inicio/chat.html', {'out': output})