import osmnx as ox
import os

# 1. Definir la ubicación de interés
place_name = "Villavicencio, Colombia"

#Estetico
# 1.1 Dividir el string en partes utilizando la coma como separador
parts = place_name.split(',')
#1.2 Tomar la primera parte (antes de la coma)
city_name = parts[0].strip()

# 2. Crea una ruta con el nombre de la ciudad / Verifica si no existe el archivo
file_path = f"{city_name}_graph.graphml"
if not os.path.exists(file_path):
    # 3. Descargar el grafo de calles de la ubicación
    graph = ox.graph_from_place(place_name, network_type='all')

    # 4. Guardar el grafo en un archivo GraphML
    ox.save_graphml(graph, file_path)
    print(f"Grafo guardado en: {file_path}")
else: 
    print(f"El archivo {file_path} ya existe.")

