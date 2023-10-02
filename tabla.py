import pandas as pd
from tabulate import tabulate

#Ruta del archivo.
archivo_excel = 'C:/Users/DELL/Documents/IDS/Estadistica/Python/Equipo6/datos.xlsx';
hoja_nombre = 'Hoja1';

#Carga los datos del archivo.
df = pd.read_excel(archivo_excel, sheet_name=hoja_nombre);

#Nombre de la columna de datos numéricos.
columna_nombre = 'Capital gain';

#Calcula las estadísticas necesarias;
media = df[columna_nombre].mean();
mediana = df[columna_nombre].median();
moda = df[columna_nombre].mode()[0];
varianza = df[columna_nombre].var();
desviacion_estandar = df[columna_nombre].std();

#Define los intervalos.
intervalos = pd.cut(df[columna_nombre], bins=32561);

#Calcula la tabla de frecuencias.
tabla_frecuencias = pd.DataFrame();
tabla_frecuencias['Limite Inferior'] = intervalos.apply(lambda x: x.left);
tabla_frecuencias['Limite Superior'] = intervalos.apply(lambda x: x.right);
tabla_frecuencias['Promedio de los Limites'] = tabla_frecuencias.mean(axis=1);
tabla_frecuencias['Frecuencia Absoluta'] = intervalos.groupby(intervalos, observed=False).count().values;
tabla_frecuencias['Frecuencia Relativa'] = tabla_frecuencias['Frecuencia Absoluta'] / len(df);
tabla_frecuencias['Frecuencia Absoluta Acumulativa'] = tabla_frecuencias['Frecuencia Absoluta'].cumsum();

#Tabla de frecuencias y las estadísticas en la consola.
print(tabulate(tabla_frecuencias, headers='keys', tablefmt='pretty', showindex=False));
print(f'Media: {media:.2f}, Mediana: {mediana:.2f}, Moda: {moda:.2f}');
print(f'Varianza: {varianza:.2f}, Desviación Estándar: {desviacion_estandar:.2f}');
