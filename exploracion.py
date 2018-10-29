"""
Vamos a hacer la exploración de los datos
Fecha: 16/10/2018
Autor: Luis Esteban
Proyecto: Google Analytics Cusomer Revenue Prediction
Python 3.6.4 - Anaconda.


El target se calcula como log(#Numero de veces que interviene cada usuario + 1)
"""

import pandas as pd

#Leemos los datos
train = pd.read_csv('data/train.csv')

#Vamos a ver el contenido del dataset
print(train.head())
#Vemos que tenemos diccionarios dentro de alguans variables

#Estadísticos básicos:
print(train.info())
#Tenemos 12 columnas y 903656 entradas y ningún missing
"""
De la dscripción de Kaggle:
fullVisitorId- A unique identifier for each user of the Google Merchandise Store.
channelGrouping - The channel via which the user came to the Store.
date - The date on which the user visited the Store.
device - The specifications for the device used to access the Store.
geoNetwork - This section contains information about the geography of the user.
sessionId - A unique identifier for this visit to the store.
socialEngagementType - Engagement type, either "Socially Engaged" or "Not Socially Engaged".
totals - This section contains aggregate values across the session.
trafficSource - This section contains information about the Traffic Source from which the session originated.
visitId - An identifier for this session. This is part of the value usually stored as the _utmb cookie.
    This is only unique to the user. For a completely unique ID, you should use a combination of fullVisitorId and visitId.
visitNumber - The session number for this user. If this is the first session, then this is set to 1.
visitStartTime - The timestamp (expressed as POSIX time)
"""
#Vamos a ver variable a variable que podemos sacar.
print('channelGrouping')
print(train.channelGrouping.value_counts())
#No parece que tengamos ningún tipo de relación ordinal entre las distintas variables.
#Aplicaremos un dummy

print('date')
print(train.date.value_counts())
#Se ordenan de forma natural debido al formato YYYYMMDD, podemos dejarla así

print('device')
print(train.device)
#Tenemos aquí la primera variable con diccionario
print(train.device.loc[0:3])
print(train.device.loc[0])
print(train.device.loc[1])
#Da la  impresión de que todos siguen el mismo formato.
#Vamos a coger las keys del primer registro y después generaremos una variable para cada una.
#false está sin comillas y da error lo sustituimos por comillas.
#La función eval, convierte un diccionario en "formato" string en un diccionario en formato dict
patron_device = eval(train.device.loc[0].replace('false','"false"'))
#Vamos a crearnos un dataframe a partir de cada uno de los valores de device. De índice vamos a utilizar el índice
#del problema. Así podremos sacar variables para cada registro real del problema final.
var_device = pd.DataFrame()
#Mapeamos la variable dentro del dataframe (versión bucle)
i=0
for elemento in train.device:
    tmp = eval(elemento.replace('false','"false"').replace('true','"true"')) #nos sale el error para true también.
    tmp_ser = pd.DataFrame(data=tmp, index=[train.fullVisitorId.iloc[i]], columns=patron_device.keys())
    var_device= pd.concat([var_device,tmp_ser],axis=0)
    if i % 1000 == 0:
        print('completado:'+str(i*1000.0/len(train))+'%')
    i+=1

#Vamos a guardar el dataframe generado porque el proceso ha sido un poco costoso,
#lo recuperaremos para generar variables

var_device.to_csv('data/info_device.csv',sep=';')
#Para ver si se ha escrito bien
info_device = pd.read_csv('data/info_device.csv',sep=';',index_col=0)

print('geoNetwork')
print(train.geoNetwork.iloc[0])
print(train.geoNetwork.iloc[1])
#Vemos que es un diccionario que parece que tiene los mismos campos en todos los registros. Aplicamos mismo método.
#Vamos a definir una clase que tenga un método que haga esto pero más adelante.
patron_geoNetwork = eval(train.geoNetwork.loc[0].replace('false','"false"'))
#Vamos a crearnos un dataframe a partir de cada uno de los valores de device. De índice vamos a utilizar el índice
#del problema. Así podremos sacar variables para cada registro real del problema final.
var_geoNetwork = pd.DataFrame()
#Mapeamos la variable dentro del dataframe (versión bucle)
i=0
for elemento in train.geoNetwork:
    tmp = eval(elemento)
    tmp_ser = pd.DataFrame(data=tmp, index=[train.fullVisitorId.iloc[i]], columns=patron_geoNetwork.keys())
    var_geoNetwork= pd.concat([var_geoNetwork,tmp_ser],axis=0)
    if i % 1000 == 0:
        print('completado:'+str(i*1000.0/len(train))+'%')
    i+=1
var_geoNetwork.to_csv('data/info_geoNetwork.csv',sep=';')
info_geoNetwork = pd.read_csv('data/info_geoNetwork.csv',sep=';',index_col=0)

print('sessionId')
print(train.sessionId.iloc[0])
#Es un id total

print('socialEngagementType')
print(train.socialEngagementType.iloc[0])
print(train.socialEngagementType.value_counts())
#Todos tienen el mismo valor: Not Socially Engaged, esta variable no nos da información para el entrenamiento.

print('totals')
print(train.totals.iloc[0])
print(train.totals.iloc[1])
#Tenemos el diccionario, aplicamos la misma metodología que en los cass anteriores.

patron_totals = eval(train.totals.loc[0].replace('false','"false"'))
#Vamos a crearnos un dataframe a partir de cada uno de los valores de device. De índice vamos a utilizar el índice
#del problema. Así podremos sacar variables para cada registro real del problema final.
var_totals = pd.DataFrame()
#Mapeamos la variable dentro del dataframe (versión bucle)
i=0
for elemento in train.totals:
    tmp = eval(elemento)
    tmp_ser = pd.DataFrame(data=tmp, index=[train.fullVisitorId.iloc[i]], columns=patron_totals.keys())
    var_totals= pd.concat([var_totals,tmp_ser],axis=0)
    if i % 1000 == 0:
        print('completado:' + str(i) + '/' + str(len(train)))
    i+=1
var_totals.to_csv('data/info_totals.csv',sep=';')
info_totals = pd.read_csv('data/info_totals.csv',sep=';',index_col=0)

print('trafficSource')
print(train.trafficSource.iloc[0])
print(train.trafficSource.iloc[1])
#Tenemos un diccionario, hacemos como en los casos anteriores.

patron_trafficSource = eval(train.trafficSource.loc[0].replace('false','"false"').replace('true','"true"'))
#Vamos a crearnos un dataframe a partir de cada uno de los valores de device. De índice vamos a utilizar el índice
#del problema. Así podremos sacar variables para cada registro real del problema final.
var_trafficSource = pd.DataFrame()
#Mapeamos la variable dentro del dataframe (versión bucle)
i=0
for elemento in train.trafficSource:
    tmp = eval(elemento.replace('false','"false"').replace('true','"true"'))
    tmp_ser = pd.DataFrame(data=tmp, index=[train.fullVisitorId.iloc[i]], columns=patron_trafficSource.keys())
    var_trafficSource= pd.concat([var_trafficSource,tmp_ser],axis=0)
    if i % 1000 == 0:
        print('completado:' + str(i) + '/' + str(len(train)))
    i+=1

#Intentamos guardar pero no deja
var_trafficSource.to_csv('data/info_trafficSource.csv',sep=';')


#Vamos a ver si podemos encontrar el registro que da problemas
for col in patron_trafficSource.keys():
    print(col + '-------------\n')
    #var_trafficSource[col].to_csv('data/'+col+'info_trafficSource.csv')

#El problema nos lo da adwordsClickInfo
# Vamos a ver si podemos tratar esta variablea ahora

adwords = var_trafficSource['adwordsClickInfo']
print(adwords.value_counts())
#Es una variable vacia, la eliminamos y guardamos el dataset.

del var_trafficSource['adwordsClickInfo']
var_trafficSource.to_csv('data/info_trafficSource.csv',sep=';')
#Sigue dando problemas, el problema en verdad está en la variable keyword
#Hay caracteres japoneses o algo así. Justo está en el registro 564203
keyword = var_trafficSource['keyword']
var_trafficSource.drop(var_trafficSource.index[564203]).to_csv('data/info_trafficSource.csv',sep=';')
keyword.to_csv('data/keywordinfo_traffic_Source.csv')
info_trafficSource = pd.read_csv('data/info_trafficSource.csv',sep=';',index_col=0)

unapalabra = []
for palabra in keyword:
    unapalabra.append(str(palabra))

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
            's','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0',
            '(',')','A','B','C','D','E','F','G','H','I','J','K','L','M','N','R','O',
            'P','Q','R','S','T','U','V','W','X','Y','Z',',','.','/','',' ','-','+',
            '*','&','$','#','~','@']


unapalabra=''.join(unapalabra)
ha_salido = []
for x in unapalabra:
    if x not in alfabeto:
        print(x,'---->',unapalabra.count(x))

print(keyword.iloc[0])
#ESTE ÍNDICE ES EL QUE TIENE INFORMACIÓN QUE NO POEMOS LEER, DE MOMENTO LO ELIMINAMOS.
keyword = keyword.drop(keyword.index[564203])
keyword.to_csv('data/keywordinfo_traffic_Source.csv')

#Me creo una muestra del dataset para probar la clase con la que vamos a estandarizar la preparación del dataset y
# que no sea muy costoso.

train_sample = pd.read_csv('data/train.csv').iloc[:1000]
train_sample.to_csv('data/train_sample.csv',sep=',')
