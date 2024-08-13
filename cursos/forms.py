from django import forms
from .models import Pregunta

class PreguntaForm(forms.Form):
    def __init__(self, *args, **kwargs):
        preguntas = kwargs.pop('preguntas', None)
        super().__init__(*args, **kwargs)
        
        if preguntas:
            for pregunta in preguntas:
                opciones = pregunta.opciones_lista()
                campo_nombre = f'pregunta_{pregunta.id}'
                
                if len(pregunta.respuestas_lista()) > 1:
                    # Pregunta con múltiples respuestas (checkboxes)
                    self.fields[campo_nombre] = forms.MultipleChoiceField(
                        choices=[(opcion, opcion) for opcion in opciones],
                        widget=forms.CheckboxSelectMultiple,
                        label=pregunta.pregunta_texto,
                        required=False
                    )
                else:
                    # Pregunta con una sola respuesta (radio buttons)
                    self.fields[campo_nombre] = forms.ChoiceField(
                        choices=[(opcion, opcion) for opcion in opciones],
                        widget=forms.RadioSelect,
                        label=pregunta.pregunta_texto,
                        required=False
                    )