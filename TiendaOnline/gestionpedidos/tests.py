from TiendaOnline.wsgi import *
from gestionpedidos.models import *

data = ['Leche y derivados', 'Carnes, pescados y huevos', 'Patatas, legumbres, frutos secos',
        'Verduras y Hortalizas', 'Frutas', 'Cereales y derivados, azúcar y dulces',
        'Grasas, aceite y mantequilla']

# for i in data:
#     cat = Category(names=i)
#     cat.save()
#     print('Guardado registro N°{}'.format(cat.id))
