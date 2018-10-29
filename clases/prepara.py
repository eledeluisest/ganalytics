"""
Modulo para solucionar el problema de ganalitycs

"""
import pandas as pd
class ganalitycs:
    def carga_info(self, datos, columnas_diccionario,indice):
        """
        Vamos a cargar los datos y a tener información de las claves que existen en cada una de las coumnas.
        :param datos: Son los datos que vamos a utilizar
        :param columnas_diccionario: Son las columnas que son diccionarios
        :param indice: Columna que sirve de index del dataset
        :return:
        """
        self.datos = datos
        self.columnas_diccionario = columnas_diccionario
        self.keys_columnas = {}
        for columna in self.columnas_diccionario:
            self.keys_columnas[columna] = eval(self.datos[columna].iloc[0].replace('false','"false"').replace('true','"true"')).keys()
        self.indice = indice
        self.datos = self.datos.set_index(keys=self.indice,drop=True)
    def dataset_de_columnadict(self,columna,guardar=True,prefix=''):
        var = pd.DataFrame()
        # Mapeamos la variable dentro del dataframe (versión bucle)
        i = 0
        for elemento in self.datos[columna]:
            tmp = eval(
                elemento.replace('false', '"false"').replace('true', '"true"'))  # nos sale el error para true también.
            tmp_ser = pd.DataFrame(data=tmp, index=[self.datos.index[i]],
                                   columns=self.keys_columnas[columna])
            var = pd.concat([var, tmp_ser], axis=0)
            if i % 10000 == 0:
                print('completado:' + str(i)+'/' +str(len(self.datos)))
            i += 1
        if guardar:
            var.to_csv('data/'+'info_'+columna+prefix+'.csv',sep=';')


