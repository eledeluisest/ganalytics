"""
29/10/2018

Vamos a preparar los datos con la clase para que el método sea igual en el conjunto de train y en el de test
Autor: Luis Esteban
"""
import pandas as pd
from clases.prepara import ganalitycs

preparador = ganalitycs()
train_sample = pd.read_csv('data/train_sample.csv',sep=',',header=0)
train_sample.fullVisitorId = train_sample.fullVisitorId.apply(str)
preparador.carga_info(train_sample,
                      ['device','geoNetwork','totals','trafficSource'],'fullVisitorId')
preparador.dataset_de_columnadict('device',prefix='clase')
