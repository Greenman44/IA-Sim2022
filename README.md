# IA-Sim2022
Repositorio para desarrollar el proyecto de IA-Simulación para la carrera de Ciencia de la Computación de la Universidad de la Habana

# Integrantes:
Ernesto Alfonso Hérnandez C312(@ErnestoAlfonso) \
Jorge Alejandro Soler González C312(@jorgesolerrr) \
Abraham González Rivero C312(@Greenman44)

# Tema: Presa vs Depredador
### **Breve Descripción:** 
  Una simulación por turnos de un ecosistema, habitado por presas y depredadores cuyo propósito es sobrevivir la mayor cantidad de turnos. \
  El entorno será un mapa dividido por casillas, cada casillas posee características que afectan a los habitantes de esta región( Su movilidad, visibilidad, si proveen de alimentos, entre otras).\
  Las presas y los depredadores tienen como principal objetivo sobrevivir, cada presa y cada depredador tiene un estado interno de sentimientos que es el que dicta la accion a llevar a cabo en cada turno con cierta probabilidad. Los sentimientos que posee una presa son: 

* Miedo
* Hambre
* Satisfacción
* Molestia

Y las acciones a llevar a cabo son:

* Huir
* Buscar Comida
* Explorar
* Esperar
* Comer

El depredador posee lo mismo solo que el miedo y la accion de huir se cambia por persecución y cazar respectivamente.


Todo esto se hace a partir de un mapa cognitivo fuzzy, el cual se ve como un grafo ponderado donde cada nodo es un concepto(sensitivo, interno, motor) y a su vez un conjunto difuso, y cada arista con su peso nos dice el grado de implicación que puede tener un concepto con otro. Luego cada individuo de la simulación posee un grafo cognitivo, el cual se modela como una, matriz de adyacencia donde en la posición i,j se encuentra el peso de la arista que conecta a los nodos i,j. Dado que los pesos del mapa son valores que en principio son producto de nuestra propia apreciación, se decidió utilizar el algorita de IA simulated annealing para encontrar la mejor distribución de pesos que puede tener el mapa de un depredador y el de una presa en un entorno específico.\

### Para la ejecución:

* Crear un entorno virtual de python(> 3.9 preferiblemente)
* Dentro del archivo requirements.txt se almacenan las dependencias del proyecto, luego dentro del enviroment escribir el comando de consola  
  ``pip install -r requierements.txt``
* Luego ejecutar el proyecto mediante el comando de consola  
  ``python app_test``
* Los resultados de cada simulación del algoritmo, así como su estado final se almacenan en txt, en la carpeta *Result_Of_Plays* que se crea una vez que se ejecuta el proyecto
* El entorno se muestra en consola

PD: si se quieren cambiar los parametros de la simulación, en el archivo app_test están comentadas las líneas donde cambiar.
  
https://github.com/Greenman44/IA-Sim2022
