import os
from kaggle.api.kaggle_api_extended import KaggleApi

location = "C:/Users/FABIAN/Documents/DevOps/proyecto_parcial/python/dataset"

###Validar que la carpeta exista###
if not os.path.exists(location):
    ##En caso mi carpeta no exista, voy a crear una nueva##
    os.mkdir(location) ##mkdir -> make directory
else:
    ##Si la carpeta ya existe, entonces borramos el contenido##
    for root, dirs, files in os.walk(location, topdown=False):
        for name in files:
            os.remove(os.path.join(root,name)) ##elimino todos los archivos
        for name in dirs:
            os.rmdir(os.path.join(root,name)) ##rmdir -> remove directory / elimino todas mis carpetas

api = KaggleApi()
api.authenticate()

#print(api.dataset_list(search='henryshan'))
api.dataset_download_file('henryshan/tesla-stock-price','TSLA.csv',path=location,quiet = False)