from datetime import datetime
from django.http import HttpResponse
from django.template import loader

def home (self):
    return HttpResponse('Hola soy pagina Home')

    
        
        
    def familia(self):
        data= {'nombre': 'Albert','apellido':'Pg','edad':63,'Fecha de Nacimiento':' 59-09-09'}
        planilla = loader.get_template('familia.html')
        documento= planilla.render(data)
        return HttpResponse (documento) 
