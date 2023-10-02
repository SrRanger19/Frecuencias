import pandas as pd
import matplotlib.pyplot as plt

#Ruta del archivo.
archivo_excel = 'C:/Users/DELL/Documents/IDS/Estadistica/Python/Equipo6/datos.xlsx';
hoja_nombre = 'Hoja1';

#Carga de datos del archivo.
df = pd.read_excel(archivo_excel, sheet_name=hoja_nombre);

#Para la gráfica de pastel
columna_nombre_pie = 'Sex';
columna_datos_pie = df[columna_nombre_pie];
datos_agrupados_pie = columna_datos_pie.value_counts();

#Para la gráfica de barras
columna_nombre_bar = 'Capital gain';
columna_datos_bar = df[columna_nombre_bar];

#Crea una figura con 2 subgráficas (una fila, dos columnas)
fig, axs = plt.subplots(1, 2, figsize=(12, 6));

#Gráfica de pastel
axs[0].pie(datos_agrupados_pie, labels=datos_agrupados_pie.index, autopct='%1.1f%%', startangle=140);
axs[0].set_title('Gráfica de Pastel (Sex)');

#Gráfica de barras
axs[1].bar(columna_datos_bar.index, columna_datos_bar.values);
axs[1].set_xlabel('Numero de personas');
axs[1].set_ylabel('Capitales');
axs[1].set_title('Gráfica de Barras (Capital gain)');

#Ajusta el espacio entre las gráficas para evitar superposiciones
plt.tight_layout();

#Muestra las gráficas
plt.show();
