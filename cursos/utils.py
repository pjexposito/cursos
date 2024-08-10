import re
import uuid

def transformar_texto_oculto(texto):
    # Expresión regular para encontrar los bloques de texto oculto
    patron = re.compile(r'\*\* texto oculto \*\*\n(.*?)\n\*\* fin de texto oculto \*\*', re.DOTALL)
    texto = texto.replace('\r\n', '\n')
    # Función para reemplazar cada bloque encontrado
    def reemplazar_bloque(match):
        contenido = match.group(1).strip().split('\n', 1)
        if len(contenido) < 2:
            return ""  # Si no hay un titular y un texto, no se añade nada

        titular = contenido[0].strip()
        texto_oculto = contenido[1].strip()
        id_unico = uuid.uuid4().hex  # Generar un identificador único

        return f'<div class="expandible" id="section{id_unico}">\n<span>{titular}</span>\n<span class="simbolo" id="symbol{id_unico}"></span></div>\n<div class="contenido" id="content{id_unico}">\n<p>{texto_oculto}</p>\n</div>'

    # Reemplaza todos los bloques de texto oculto en el texto original
    texto_transformado = patron.sub(reemplazar_bloque, texto)
    return texto_transformado