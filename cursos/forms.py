# forms.py
from django import forms
from .models import Pregunta, Cuestionario

class CuestionarioForm(forms.Form):
    def __init__(self, *args, **kwargs):
        cuestionario = kwargs.pop('cuestionario')
        super(CuestionarioForm, self).__init__(*args, **kwargs)
        preguntas = cuestionario.pregunta_set.all()
        
        for pregunta in preguntas:
            opciones = pregunta.opciones_lista()
            if len(pregunta.respuestas_lista()) > 1:
                self.fields[f'pregunta_{pregunta.id}'] = forms.MultipleChoiceField(
                    choices=[(opcion, opcion) for opcion in opciones],
                    widget=forms.CheckboxSelectMultiple,
                    label=pregunta.pregunta_texto,
                    required=True
                )
            else:
                self.fields[f'pregunta_{pregunta.id}'] = forms.ChoiceField(
                    choices=[(opcion, opcion) for opcion in opciones],
                    widget=forms.RadioSelect,
                    label=pregunta.pregunta_texto,
                    required=True
                )
