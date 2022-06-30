# examen_extraordinaria
repositorio:https://github.com/Javifdz12/examen_extraordinaria.git
Ejercicio 1 (6 puntos) Tiempo estimado: 60 minutos.
Esta práctica tiene como objetivo principal la consolidación de los conocimientos relacionados con el
paradigma de Programación Orientada a Objetos, algoritmos de búsqueda y ordenación y con el
manejo de estructuras de datos. En ese sentido, se desarrollará como aplicación un hipotético juego
acerca de la próxima película del ™, utilizando el lenguaje de programación Python.
El Doctor Strange, como Maestro de las Artes Místicas, es uno de los encargados de proteger la Gema
del Tiempo. Esta piedra tiene la capacidad de controlar el tiempo y, con ello, la capacidad de crear
nuevos universos alternativos.
En este contexto, los creativos de StanLeeGames S.L. han pensado que ™ in the Multiverse
of Madness (The game), debido a los múltiples universos paralelos, podría presentar distintos escenarios
donde nuestros superhéroes, habitualmente amigos, estarían enemistados, crearían sus propias bandas
y lucharían para imponer su propio orden.
En resumen, el típico juego de lucha uno-contra-uno, donde cada jugador selecciona un equipo de
superhéroes y luchan entre ellos hasta que solo uno queda en pie (¡¡¡qué creativos más originales!!!).
Todo ello adaptándolo al tirón de marketing que la película tendrá.
Para ello, han definido el esquema general del juego que se describe a continuación.
Cada partida enfrenta a dos jugadores y se desarrolla en un escenario. Los escenarios se corresponden
con localizaciones famosas del universo Marvel. Un escenario simplemente es un elemento del juego
que establece, para cada jugador, un número de monedas iniciales con las que deberá formar su
equipo de superhéroes, restringiendo también el número de miembros que tendrá cada equipo. Por
otra parte, también restringirá el número de movimientos que cada superhéroe puede hacer en su
lucha.
Los combates se van a realizar secuencialmente. Además, un combate se entiende como aquel
llevado a cabo por un superhéroe de cada organización. Por lo tanto, en cada turno un superhéroe
de uno de los equipos va a atacar a otro superhéroe del otro equipo. Una vez que dos superhéroes
entran en combate, no se para este combate hasta que uno de los dos superhéroes es derrotado,
momento en el que el siguiente superhéroe del entrenador debe entrar al combate seleccionando un
superhéroe de aquellos que no estén derrotados. La función
get_Superheroe_in_a_list_of_Superheroes() tiene que ser implementada para ayudar a que el usuario
del juego pueda elegir algún superhéroe que todavía esté sin derrotar por parte de cada uno de los
entrenadores. Implementar también la función squad_is_undefeated() para que esta función nos
devuelva si todos los superhéroes de un entrenador han sido derrotados o queda alguno vivo.
Cuando una de las dos organizaciones tenga ya todos sus superhéroes derrotados al acabar el turno,
se acaba el juego, y se indica no solo quién es el ganador. En el caso de que los dos acaben sin
superhéroes en el mismo turno, el juego indicará un empate. En cada turno los dos Superhéroes se
atacan con independencia de si en ese mismo turno es derrotado.
En este ejercicio, vamos a hacer una versión programada en Python para que dos jugadores puedan
jugar a este juego. Los jugadores se encontrarán representados por los escenarios de cada una de las
organizaciones.
No es necesario implementar el docString correspondiente a las funciones y métodos desarrollados,
aunque se recomienda hacer el diagrama de flujo de los métodos en papel de forma previa a su
resolución.

Parte 1.1. (1 puntos) Corresponde a las diferentes organizaciones de superhéroes (Organizaciones.py)
Las organizaciones son agrupaciones de superhéroes que, con el objetivo de conseguir alguna o varias
misiones, se conformaron a lo largo del tiempo. Habitualmente, todos los superhéroes pertenecen (o
han pertenecido) a una o varias de ellas y siempre hay un líder.
Antes de seleccionar el escenario donde tendrá lugar la lucha, cada uno de los jugadores debe
afiliarse a una organización del juego. Esto le permitirá obtener ventajas a la hora de seleccionar, como
miembros de su equipo, a superhéroes afiliados a dicha organización.
Las organizaciones del juego se establecen a partir de los superhéroes protagonistas del juego, por
ejemplo: A-Force, Avengers, Mercs for Money, League of Realms, Strange Academy y X-Men.
i) Cada organización va a estar caracterizada por:
(1) Un nombre que lo identifique.
(2) La lista de superhéroes que forman su equipo. Al menos debería existir un superhéroe.
ii) Incluya los atributos de esta clase y establezca la visibilidad adecuada (público, privado,
protegido). Añada cualquier atributo y/o método que considere necesario.
iii) Programe un constructor que reciba los datos necesarios para crear una organización. El
método debe verificar el tipo y valor de cada uno de los parámetros y lanzar la excepción
correspondiente cuando no se cumplan los requisitos.
iv) No es un requisito necesario la programación de métodos para añadir/eliminar superhéroes
de una organización ya existente.
v) Programe los métodos setters y getters para la clase en función de lo que necesite. Si no
necesita algún o ningún getter y/o setter, argumente por qué en un comentario del módulo.
vi) Programe el método is_undefeated(self). Este método sirve para saber si la organización
está aún sin ser derrotada. Para ello evaluará que al menos uno de sus superhéroes esté
vivo.
vii) Programe el método surrender(self). Este método sirve para que la propia organización se
rinda. Para ello tiene que poner los puntos de vida de cada uno de sus superhéroes a 0.
viii) Programe los métodos str y repr para que cada uno muestre la información tal y como se
especifica a continuación.
 El método str debe mostrar la información:
(1) [SUPERHEROE_TYPE_NAME] with a [MOVE_TYPE_NAME] and health: [HEALTH_POINTS]
El método repr debe mostrar la información:
(2) [ID]\t[SUPERHEROE_TYPE_NAME]\t[MOVE_TYPE_NAME]
ix) Pruebe los objetos de la clase Organización con los casos de prueba que se le han pasado.
Modifíquelos si lo ve necesario, pero añada una justificación de cada uno de los cambios.
Este punto será evaluado inversamente proporcional al número de cambios realizados en
los casos de prueba.
Nota: Es obligatorio el uso de enumerados para el atributo del tipo de Organizaciones. Se recuerda
que el enumerado en Python tiene el formato "Clave / Valor".

Parte 1.2. (1 puntos) Corresponde a los diferentes escenarios (Escenarios.py)
Las partidas siempre se desarrollan en el ámbito de un escenario del juego. De esta manera, una vez
seleccionada la organización de cada uno de los participantes, el jugador que ha iniciado la partida
deberá seleccionar uno de los posibles escenarios del juego.
Cada escenario restringe las condiciones iniciales de ambos jugadores, estableciendo el número de
monedas disponible para la configuración de los equipos, el número de integrantes de cada equipo
y el número de movimientos que puede realizar cada superhéroe en la lucha. También establece la
energía vital que tendrá cada superhéroe cuando participe en dicho escenario.
La configuración básica del juego incluirá los siguientes escenarios:
Sanctum Sanctorum. Es un sitio pequeño y angosto, por lo tanto, cualquier batalla que tenga lugar
allí no puede tener muchos contrincantes. Así, este escenario establece una cantidad de 10000
monedas iniciales para cada jugador, un tamaño de 10 miembros por equipo y un número de 10
movimientos por cada miembro. La energía vital con la que contará cada superhéroe en este
escenario será de 100 unidades.
Eso sí, ¿quién no querría batallar allí para poder hacerse con el control de sus misterios ocultos?
Stark Tower. Sus inmensas plantas pueden ser el lugar perfecto para una batalla de grandes
superhéroes. Este escenario ofrecerá 20000 monedas iniciales a cada jugador para que desarrollen
una intrépida lucha, el número de miembros por equipo será de 20 y el número de movimientos
por superhéroe de 25. Los superhéroes contarán con 200 unidades de energía vital.
Xavier’s School for Gifted Youngsters. Si hay algún escenario propio de la más épica de las batallas
es esta escuela. Sumérgete en la lucha final, selecciona a tus mejores superhéroes y adéntrate en
sus recónditos pasillos y salas. Este escenario aportará, a cada jugador, 80000 monedas para que
puedan librar una batalla que se convertirá en leyenda. El número de superhéroes será de 30 y el
número de movimientos por superhéroe será de 40. En este gran escenario, los superhéroes
contarán con 300 unidades de energía vital.
A continuación, se describen los siguientes pasos a implementar:
o Enumeración de los 3 escenarios donde las organizaciones de superhéroes pueden jugar la
partida. Ayúdese del test de la función para conocer su valor.
o Creación de la función “from_str”: obtiene como parámetro de entrada un string, que deberá
de convertir en letras minúsculas y devolver el objeto Escenarios en función de cada entrada. En
caso de que no sea ningún tipo enumerado deberá devolver un TypeError. Ayúdese del test de
la función para conocer su valor.
Nota: Es obligatorio el uso de enumerados para el atributo del tipo de Escenarios. Se recuerda que el
enumerado en Python tiene el formato "Clave / Valor".

Parte 1.3. (4 puntos) corresponde a los Superhéroes (Superheores.py).
Los equipos de cada uno de los jugadores están formados por superhéroes. Antes de comenzar la
lucha, los jugadores, mediante el uso de las monedas iniciales que les asigna el escenario
seleccionado, configuran su equipo, seleccionando aquellos superhéroes que creen más interesantes.
El número de superhéroes que se deben seleccionar también viene determinado por el escenario.
De esta manera, cada superhéroe tiene las siguientes características:
1. Identificador: Es un número único que identificará a cada superhéroe dentro del juego. Puede
ser un número auto-incrementado.
2. Alias. ¿Todos los superhéroes poderosos tienen un nombre molón, no?
3. IdentidadSecreta: Se corresponde con el nombre real de cada uno de los héroes, por seguridad
no debería ser revelada.
4. Conjunto de movimientos. Cada superhéroe tiene un conjunto de movimientos de defensa o
ataque. El tipo de movimiento y su orden los elige el jugador. Lo hace justo después de
seleccionar al superhéroe para su equipo.
5. Tipo de Superhéroe. Por lo tanto, podríamos clasificar a nuestros superhéroes y sus poderes en
función de su origen. Así, todos los superhéroes se pueden clasificar en función de si tienen un
origen humano (homo sapiens), o no humano (extraterrestre). El origen del superhéroe es muy
importante puesto que determina la configuración que pueden tener las distintas
características que conforman la parrilla de poderes.
La parrilla de Poderes: Es un conjunto de características que se definen a la hora de
seleccionar el superhéroe y que determinan los poderes y habilidades que tiene cada
uno. Sirven para modular los movimientos de ataque y defensa. Estas características son
las siguientes: inteligencia, fuerza, velocidad, resistencia, proyección de energía y
habilidades de lucha. Los valores establecidos serán números aleatorios entre los valores
facilitados a continuación.
En esta primera versión del juego, solamente tenemos 2 tipos de superhéroes:
1. Humanos. Debido a su naturaleza como Homo Sapiens, la configuración de
la parrilla de poderes de estos superhéroes está limitada a los siguientes
parámetros (Estos márgenes se pueden calcular utilizando el módulo
random.):
a. Inteligencia: Poseen una inteligencia entre 3 y 7 unidades.
b. Fuerza: Establecida entre 1 y 6 unidades.
c. Velocidad: Comprendida entre 2 y 5 unidades.
d. Resistencia: De 2 y 5 unidades.
e. Proyección de energía: Puede estar entre 1 y 6 unidades.
f. Habilidades de lucha: Varía entre 1 y 7 unidades.
2. No Humano. Los no humanos son aquellos seres a los que, habitualmente, nos
referimos como extraterrestres. Es decir, han venido desde otras dimensiones 
o planetas. Desde S.H.I.E.L.D. llevan un control de los conocidos y, en base a
esa clasificación, podemos establecer los siguientes parámetros en su parrilla
de poderes(Estos márgenes se pueden calcular utilizando el módulo
random.):
a. Inteligencia: Poseen una inteligencia entre 4 y 6 unidades.
b. Fuerza: Establecida entre 1 y 7 unidades.
c. Velocidad: Comprendida entre 1 y 7 unidades.
d. Resistencia: De 3 y 7 unidades.
e. Proyección de energía: Puede estar entre 1 y 7 unidad.
f. Habilidades de lucha: Varía entre 3 y 6 unidades.
1. Coste. Son las monedas que debe invertir un jugador para incorporar un superhéroe de ese tipo
a su equipo. Se calcula en base a las monedas iniciales proporcionadas por el escenario, el
número de miembros del equipo y los valores de las características de la parrilla de poderes del
jugador. El valor será:
(monedas_iniciales/numero_miebros)*(suma_valores_parrilla/30)
Nota: Es obligatorio el uso de enumerados para los atributos del tipo de guerrero y tipo de arma.
El índice de ataque del guerrero se recomienda que contenga el valor del tipo de arma. Se
recuerda que el enumerado en Python tiene el formato "Clave / Valor".
7. Energía. Cada superhéroe tiene una cantidad de energía concreta: La energía vital que
depende del escenario en que transcurra la acción. Este campo de energía vital se inicializará
como la energía proporcionada por el escenario multiplicada por el valor del campo
resistencia de la parrilla de poderes.
En base a estas especificaciones se solicita que:
i) Incluya los atributos de esta clase y establezca la visibilidad adecuada (público, privado,
protegido). Añada cualquier atributo y/o método que considere necesario.
ii) Programe un constructor que reciba los datos necesarios para crear un guerrero. El método
debe verificar el tipo y valor de cada uno de los parámetros y lanzar la excepción
correspondiente cuando no se cumplan los requisitos.
iii) Programe los métodos setters y getters para la clase en función de lo que necesite. Si no
necesita algún o ningún getter y/o setter, argumente por qué en un comentario del módulo.
iv) Programe el método is_alive(self) de la clase Superhéroe. Este método sirve para saber si el
superhéroe está vivo.
(1) Constructor que identifica mediante la variable booleana vivo si está vivo o muerto.
(2) Función “is_vivo” que devuelve True si está vivo y False si está muerto.
(3) Función “die” que cambia el estado del superhéroe en cuestión.
Ayúdese del test de la función para implementar la clase.

Parte 1.4. (1 puntos) corresponde a la programación de los métodos de los diferentes Movimientos
(ataque y defensa)
Como hemos descrito hasta el momento, cada superhéroe posee un conjunto de movimientos que va
a utilizar a lo largo de la lucha.
El jugador deberá configurar tantos movimientos como establezca el escenario. Para cada
movimiento, el jugador elegirá el tipo y la cantidad de energía de lucha que desea asignarle.
Los movimientos se clasifican en dos categorías: movimientos de ataque y movimientos de defensa.
Sin embargo, todos ellos tienen las mismas características:
1. Todos los movimientos son realizados por un superhéroe. Todos los movimientos van dirigidos a
otro superhéroe.
2. Todos los movimientos llevan asociada una determinada energía inicial que el jugador
especifica al configurarlo.
3. Sin embargo, la energía real del movimiento dependerá de ciertas características de la parrilla
de poderes del superhéroe que lo ejecuta.
¿Cómo alteran los movimientos la energía de los superhéroes?
Una vez definidos los movimientos, podemos establecer su relación con la energía que poseen los
superhéroes.
En primer lugar, se debe calcular la energía real de cada uno de los movimientos, ya sean de ataque
o defensa. La energía real de un movimiento se ve ampliada por las características de la parrilla de
poderes que tenga el superhéroe.
1. En un movimiento de ataque influyen la fuerza (80 %), la velocidad (25 % ), las habilidades de
lucha (75 % ) y la proyección de energía (100 % ) que tenga un superhéroe.
2. En un movimiento de defensa influyen la inteligencia (100 %), la velocidad (75 % ), las las
habilidades de lucha (25 % ) y la fuerza (20 % ) que tenga un superhéroe.
Una vez obtenidos todos los factores, para calcular la contribución de cada característica en el
movimiento, se multiplica cada factor por la energía inicial del movimiento y se divide entre 10.
En base a estas especificaciones se solicita que:
i) Programe el método fight_attack(self, SuperHeroe superheroe_to_attack). Método que
implementa el ataque del superhéroe usando un golpe sobre otro superhéroe. Este método
se basa en el método fight_defense(self, int points_of_damage) del superhéroe atacado. Se
aplicará tanto a la energía vital del superheroe atacante como a la energía de lucha.
ii) Programe el método fight_defense(self, int points_of_damage). Este método implementa la
defensa del superhéroe de un golpe de otro superhéroe. Este método actualiza el atributo
de puntos de energía vital que tiene el superhéroe en base a lo anteriormente desarrollado.
iii) Pruebe los objetos de la clase superhéroe con los casos de prueba que se le han pasado.
Modifíquelos si lo ve necesario, pero añada una justificación de cada uno de los cambios.
Se penalizarán los cambios realizados en los casos de prueba proporcionados.