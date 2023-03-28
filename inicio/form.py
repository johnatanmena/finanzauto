from django import forms
from .models import chatbots, cargar
class MyForm(forms.Form):
    
    nombres = forms.CharField (
        widget = forms.TextInput (
            attrs = {
                "class":"form-control",
                "autocomplete":"off",
                "placeholder":"Ingrese el nobmre del Chatbot",
                "id":"nombre"
            }
        )
    )
    selecc = forms.ChoiceField(choices=[('0', ''), ('Chatbot morosos', 'Chatbot morosos'), ('Chatbot cobro simple', 'Chatbot cobro simple'),('Chatbot de ventas','Chatbot de ventas')])
    Skill = forms.CharField (
        widget = forms.TextInput (
            attrs = {
                "class":"form-control",
                "autocomplete":"off",
                "placeholder":"Ingrese el skill-ID",
                "id":"Skill-ID"
            }
        )
    )
    estado = forms.ChoiceField(choices=[('0', ''), ('Activo', 'Activo'), ('Inactivo', 'Inactivo'),('Revisión','Revisión'),('Eliminado','Eliminado')])

class carga (forms.ModelForm):
    nombre = forms.CharField(
        widget = forms.TextInput(
            attrs= {
                "class":"form-control",
                "autocomplete":"off",
                "placeholder":"Ingrese nombre de la campaña",
                "id":"nombre"
            }

        )
    )

    chatbot = forms.ModelChoiceField(
        queryset=chatbots.objects.all(),widget=forms.Select(attrs={"class":"form-control"}), empty_label="Selecionar ChatBot"
    )

    cantidad_intentos = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class":"form-label",
                "name":"prueba1",
                "id":"prueba1",
                "type":"number",
                "onkeydown":"javascript: return ['Backspace','Delete','ArrowLeft','ArrowRight'].includes(event.code) ? true : !isNaN(Number(event.key)) && event.code!=='Space'",
                "value":"1"
            }
        )
    )
    class Meta:
        model= cargar
        fields= "__all__"

