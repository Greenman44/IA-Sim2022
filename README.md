# IA-Sim2022
Repositorio para desarrollar el proyecto de IA-Simulación para la carrera de Ciencia de la Computación de la Universidad de la Habana

# Integrantes:
Ernesto Alfonso Hérnandez C312 \
Jorge Alejandro Soler González C312 \
Abraham González Rivero C312 

# Tema: Presa vs Depredador
Breve Descripción: \
  Una simulación por turnos de un ambiente hostil, habitado por una variedad de especies cuyo propósito es sobrevivir. \
  El entorno será un mapa dividido por casillas, cada casillas posee características q afectan a los habitantes de esta región( Su movilidad, visibilidad, si proveen de alimentos, entre otras).\
  Las especies tienen como principal objetivo sobrevivir, lo cual se traduce en alimentarse sin ser comidas, tienen conocimientos de aquellas especies que pueden devorar y de aquellas por las que pueden ser devoradas, así como sus caracterícticas. \
  Poseen, además, conocimiento de la disposición del mapa, pero no, de la disposición de las especies que lo habitan, a menos que se encuentren en su rango de visión.
  Toda especie posee: \
    - Movilidad: Cantidad de casillas que puede recorrer en un turno. \
    - Rango de visión: Conocimiento de lo que se encuentra en una vecindad de su posición. \
    - Hambre: Cantidad de turnos que puede estar sin comer. \
    . Devorar: Capacidad de regenerar hambre si en mi casilla actual hay una presa, y las características del terreno lo permiten. \
  Algunas especies pueden adquirir determinados rasgos tras devorar a otras, ejemplo: Si devoras a un mono, puedes usar la habilidad trepar en una casilla de tipo árbol. \
  Realmente nos interesa la modelación del proceso de la toma de decisiones de una especie para obtener alimentos. Unos primeros acercamientos pudieran ser, al no encontrar alimentos, evaluar la probabilidad de encontrar presas en determinadas casillas que proveen alimentos, dadas las características del mapa, las especies que lo habitan, sus hábitos alimenticios y la posición actual del  depredador en cuestión. 
