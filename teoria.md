<img src="Captura de pantalla 2025-05-29 185207.png" width="500">

# 1. CLASES EN PYTHON


Lo primero que hay que saber a la hora de ver lo que representan las clases en Python, es su sintaxis.

~~~
class Student:
~~~  

Primero colocamos nuestra clase y automáticamente después siempre tenemos que poner en *mayúscula* la primera letra del nombre que queramos dar a nuestra clase. Despúes acabaremos siempre con *dos puntos*.

Siempre que haya dos puntos en Python la siguiente línea de código irá con sangría, es decir dos o cuatro espacios hacia dentro.  

Las clases pueden contener datos, funciones y hasta comportamiento. Son como plantillas que definen los atributos que tendrán los objetos. Estos objetos son instancias de las clases. Una clase es como un plano de un objeto. No ocurrirá nada en ella a menos que creemos un objeto dentro de ella.  

~~~
class Perro:
    mi_perro()
    print(mi_perro)

~~~

El proceso por el que se crea un objeto dentro de una clase se llama *instanciación*. Es decir, un objeto cualquiera se basa en la definición de una clase.  

Cada instancia de una clase es un objeto único que tiene sus propios valores. Aunque comparte con la clase la misma estructura y comportamiento definido por ella.  

Se crea un objeto concreto a partir de una clase y esto puede manipularse y utilizarse dentro de los programas.  

~~~
class Perro:
    mi_perro= Perro()
    print(mi_perro)

~~~

En el ejemplo de antes tenemos una clase llamada *perro*. Aqui hemos instanciado la clase y la almacenamos en una variable. Si imprimimos esto, nos va a dar un código donde nos dice que hemos creado una instancia de la clase perro y nos indica el lugar de la memoria del ordenador donde Python ha almacenado esa clase.

~~~
<user_code.Perro object at 0x7f92d316a050>
~~~  



~~~
class Perro:
    otro_perro= Perro()
    print(otro_perro)

~~~  

Si imprimimos esto nos da una nueva instancia pero conservando la anterior. Sigue siendo la misma clase de *perro* y el mismo plano. Pero al crear dos instancias, esta clase se almacenará en dos lugares distintos de la memoria. Así es como trabaja la instanciación.

~~~
<user_code.Perro object at 0x7f4b790262d0>
~~~  


 

En Python las clases se componen de datos y comportamiento que se gestiona mediante funciones. Tener comportameinto dentro de una clase se refiere a que eso es un conjunto de funciones.  

~~~
class Perro:
    def __init__
~~~  

Para definir una función dentro de una clase se utiliza este tipo de función (__init__) que está reservada especialmente dentro del lenguaje Python. Está disponible para utilizarse en clases. A init se llamará automáticamente al instanciar una clase. Al acceder a esta función init se procesará su contenido configurando lo necesario y agregando los datos a la clase.  

*<h2> Para qué se usan</h2>*   

<img src="Captura de pantalla 2025-05-31 003135.png" alt="clases" width="400">


Las clases se usan principalmente para definir plantillas que sirven para crear objetos.
Permiten organizar el código de manera clara y facilitan la reutilización y el mantenimiento del código dentro de un programa. 

Son importantes porque nos permiten agrupar datos dentro de una misma entidad. Ayudan a modelar los datos, evitan escribir código repetitivo y ayudan a escribir código más limpio y fácil de entender. Se usan para describir los objetos.  

~~~
class Perro:
    (dentro de esta clase vamos a poder describir un objeto)
    def __init__(self,nombre,raza): 
        self.nombre=nombre
        self.raza=raza

~~~  

Aquí tenemos una clase llamada 'perro', dentro de la cuál hemos añadido una función init. Siempre será asi la sintaxis def y luego dos guiones bajos, init y otra vez dos guiones bajos ( esto se llama "dunder"). Toda función dentro de una clase necesita pasar un primer argumento que siempre será *self*, luego podemos pasar otros argumentos (nombre, raza).  
Acabamos como toda función con dos puntos.

Debajo y siempre con sangría despues de los dos puntos, ponemos los datos directamente dentro de dos variables (self.nombre y self.raza).

Practicamente todo en Python es un objeto. Por eso al crear la clase *perro*  queremos asignar distintos datos al objeto. Los datos para nombre y raza se asignarán a este objeto recien creado (las dos variables). 

Al crear las instancias de clase haríamos esto.  

~~~
 mi_perro= Perro('Zuri', 'Bichón Maltes')
 otro_perro= Perro('But', 'Pastor Alemán')

print(mi_perro)

~~~  

Si ejecutamos esto nos daría lo siguiente

~~~
<user_code.Perro object at 0x7f8036814f10>

~~~  

Esto nos dice que hemos creado una instancia de "perro". Nos indica el lugar de la memoria donde Python lo almacenará.
Si imprimimos la segunda opción  

~~~
print(otro_perro)
~~~  

~~~
<user_code.Perro object at 0x7f8036814910>
~~~  

Nos da una nueva instancia pero conserva la anterior.

~~~
<user_code.Perro object at 0x7f8036814f10>
<user_code.Perro object at 0x7f8036814910>
~~~  

Sigue usando la misma clase de *perro* y el mismo plano. Pero al crear dos instancias, la clase se almacena en dos lugares distintos de memoria.
Así es como trabaja la instanciación.  


Tambien podríamos declarar lo siguiente
~~~
print(f"{mi_perro.nombre} es un {mi_perro.raza}")
print(f"{otro_perro.nombre} es un {otro_perro.raza}")
~~~  

En este caso al formatear los argumentos el resultado será claro

~~~
Zuri es un Bichón Maltes
Bat es un Pastor Alemán
~~~  


# 2. CONSTRUCTOR

<h2> METODO QUE SE EJECUTA AUTOMATICAMENTE CUANDO SE CREA UNA INSTANCIA DE UNA CLASE </h2>  



Cuando un objeto se crea en Python, aparece automáticamente el Python constructor con la siguiente sintaxis:

def__init__(self)

Función dos guiones bajos (o dunder) init seguido de otros dos guiones bajos y entre paréntesis (self) porque siempre que creas una función dentro de una clase hay que pasar
*self*  como primer argumento.  

Esto es un método especial dentro de una clase que se invoca automáticamente en el momento en que crea un nuevo objeto (o instancia) de esa clase.
Su propósito principal es inicializar el estado del nuevo objeto con valores predeterminados o personalizados.  

En Python ya hemos dicho, el constructor se llama __init__.
Existe en muchos lenguajes de programación y el concepto siempre es el mismo.
Constructor es el punto de entrada para configurar un objeto justo depués de ser creado.  

~~~
"definición de una clase con constructor"

 class Persona:
    def __init__(self, nombre, edad):
        self.nombre= nombre
        self.edad= edad

"instancias después del constructor"

persona1= Persona ('Alba', 18)
persona2= Persona ('Ibai', 11)

print (persona1.nombre, persona1.edad)
print (persona2.nombre, persona2.edad)
~~~  

Esto nos da lo que estamos buscano  

~~~
Alba 18
Ibai 11

[Execution complete with exit code 0]
~~~  

En este ejemplo, __init__ (self, nombre, edad) es el constructor de la clase *Persona*. Cuando se crea una nueva instancia (persona1, persona2) Python automáticamente llama a __init__ () y pasa los argumentos nombre y edad que hemos proporcionado.  

El primer argumento del constructor (init) siempre es *self* que representa la instancia actual de la clase (antes de construir ningún código). Se utiliza para acceder a los atributos y métodos de la instancia dentro de la clase. Además de self, el constructor puede aceptar cualquier número de argumentos que queramos dar para inicializar la instancia.
Estos argumentos se pondrán al iniciar la instancia.  

~~~
class Coche:

    def__init__ (self, marca, modelo, color= "negro")
        self.marca= marca
        self.modelo= modelo
        self.color= color

coche1= Coche ("Seat", "Ibiza")
coche2= Coche ("Hyunday", "I38", "blanco")

print(coche1)
print(coche2)
~~~  

-Hemos creado una clase : Coche.  


-Creamos una función constructora : init( dunder, guiones bajos delante y detrás) con self que sirve para acceder a la instancia de la clase.  


-Pasamos tres argumentos, marca, modelo y color.  


-Asignamos esos argumentos al objeto, creando una variable dentro del objeto. Una para marca, otra para modelo y otra para color.  




En este ejemplo además hemos creado un  atributo opcional que es el "color" y tiene un valor predeterminado de "negro". Pero se puede eleguir o no. Puedes proporcionar otro color al crear la instancia ( como hemos echo en el coche2).  

Si no definieramos un constructor (__init__(self)), Python proporcionaría uno por defecto que no inicializa ningún atributo.  


# 3. VERBOS PRINCIPALES DE LAS APIS  

Los tres verbos más importantes a la hora de trabajar con APIs son:  

Get que se utiliza para obtener o recuperar datos.
Post se utilza para crear o actualizar un nuevo recurso.
Delete sirve para eliminar un recurso.  

Estos verbos definen las acciones que se pueden realizar con lo que nos dá una API.
Comunican la intención del cliente al servidor, indicando que operación debe realizar.  

<h2> POST </h2>  

La solicitud "Post" nos dice que queremos crear algo nuevo dentro de nuestra aplicación.   Podemos querer crear una nueva guía en el programa y pasar los datos. En lugar de poner código complejo, utilizamos Postman para añadir los datos que queramos.  

~~~
@app.route('/gide',methods= ['POST'] )
~~~  

Aquí hemos creado un decorador y despúes ponemos lo que queremos que sea nuestro punto final. En este caso va a ser simplemente una guía y luego va a guiarse por el método Post (que tiene que ir siempre en mayúsculas dentro de cochetes y entre comillas).
Con este código creamos el primer punto final. Utilizamos el verbo "POST" cada vez que queremos crear algo nuevo en la base de datos.  

Si quieres crear una nueva guía vas a pulsar este punto final de guía de barra y usar Post que lo encontramos facilmente en Postman para poder utilizarlo.  

Las peticiones *post* como hemos dicho son para *crear* nuevos recursos, no para eliminarlos ni para modificarlos. Cada vez que utilizamos *post* debe producir un nuevo recurso. (El verbo nos dice qué haremos y la URL sobré que recurso).  

Post se puede usar para inicios de sesión, agregar cosas a un carrito de compras, procesar un pago nuevo...
Al iniciar sesión en algún programa no producimos un nuevo registro en la base de datos , pero usamos post porque estamos creando una sesión nueva.  

Post no es una herramienta segura porque puede alterar el estado del servidor.  

~~~
#Quiero añadir "manzanas" a mi lista de la compra

POST / lista-de-la-compra
{"nombre"= "manzanas"}

#La respuesta esperada es un mensaje de confirmación de que se añade algo a la lista y quiza la URL para consultarla {"status": "añadido", "id_artículo= "XYZ123"}
~~~  



<h2> GET </h2>  

Es el verbo más simple que vamos a utilizar con las APIS. Lo usamos para solicitar datos del servidor, para obtener un recurso.  

Las peticiones *get* no causan efectos secundarios en un servidor, no producen nuevos registros ni modifican los ya existentes. No importa cuántas veces llevemos a cabo una solicitud *get*, los resultados siempre serán los mismos.  

Permite a los clientes acceder a la información que deseen.
Get se considera una operación segura ya que no modifica nada en el servidor.  

Un ejemplo de la vida real es cuando abres una página web en el navegador. El navegador hace una petición get para obtener el contenido de esa página a la que quieres acceder.  

Ejemplo en la vida diaria. Vas a un restaurante y le pides la carta al camarero. Sólo quieres información. El camarero puede ser la API o el servidor que te puede dar esa información. Realizas una petición get al solicitar la carta. No vas a cambiar nada sólo quieres ver lo que hay.  

~~~
#Quiero ver que hay ahora mismo en mi lista de la compra. Esta es mi petición get. La respuesta será un listado con los artículos incluídos en la lista de la compra.

Get/lista-de-la-compra
["leche", "pan", "huevos"]
~~~

<img  

<h2> DELETE </h2>

Usaremos *delete* cuando queremos eliminar registros. Cuando alguien envía una solicitud delete, le indica al servidor que elimine el recurso especificado.  

Sirve para mantener las APIs limpias y bien organizadas.  

Al igual que el verbo *post*, *delete*, no es una herramienta segura, ya que puede alterar el estado del servidor.  

Sólo se puede eliminar un registro a la vez. Con esta solicitud vamos a una guía específica y luego la elimina de la base de datos.  

~~~
#Quiero eliminar un recurso específico del servidor. En nuestro caso, quiero eliminar de mi lista de la compra los huevos, porque ya no los necesito.

DELETE/lista-de-la-compra/huevos
respuesta esperada {"status" : "eliminado"}  
~~~  

Los verbos le dan un significado a tus solicitudes. Al usar el verbo correcto, la API sabe que acción esperas que realice sobre los datos o recursos. Las aplicaciones buscan estas acciones (estos verbos) para realizar una acción u otra.
Esto hace que la comunicación entre distintos sistemas sea clara y predecible.
Porque podemos tener dos rutas idénticas, dos puntos finales idénticos pero tendrán un comportamiento diferente según el método(verbo) que se utilice.  

# 4. MONGODB ES UNA BASE DE DATOS SQL O NOSQL  

Mongo es una base de datos de código abierto NoSQL.
Las características principales de estas bases de datos son:  

Mongo es una base de datos orientada a documentos. Almacena los datos en documentos de tipo JSON. Usa una variedad de módelos de datos flexible (no es un módelo tabular como las bases de datos SQL).

- No suele utilizar esquemas y si los utiliza son muy flexibles. Los documentos dentro de una misma colección pueden tener estructuras diferentes. Esto es ideal para aplicaciones que evolucionan rapidamente.  

- Para lenguaje de consulta, MongoDB no utiliza SQL, utiliza MQL(MongoDB Query Lenguage).
Es un lenguaje de consulta basado en datos JSON. Funciona muy bien con operaciones CRUD(find,insert,delete..)

- Mongo es muy diferente a las bases de datos SQL.  Se diseñó para escalar horizontalmente. Esto significa que puede distribuir la carga entre muchos servidores, lo que permite crecer sin límites.  

- La flexibilidad y la escalabilidad horizontal son sus principales ventajas frente a las bases de datos SQL.  

Las bases de datos NoSQL como MOngoDB suelen ofrecer un alto rendimiento, especialmente para consultas en grandes volumenes de datos.
Están diseñadas para ofrecer alta disponibilidad y tolerancia a fallos.  

- Ofrece una amplia variedad de módulos de datos como clave-valor, documentos...y permite adaptarse a distintos tipos de aplicaciones y datos.  

- También MongoDB es adecuada para gestionar datos no estructurados como los que encuentran en redes sociales o aplicaciones móviles.  

La flexibilidad que tiene permite una mayor adaptación a los cambios en las aplicaciones.

Las bases de datos SQL conllevan el concepto de tablas y las tablas tienen columnas. No se usan los mismos términos en MongoDB, tenemos bases de datos y dentro de ellas tenemos colecciones.
Las colecciones son lo más parecido a las tablas y pueden almacenar muchos documentos y esos documentos son los elementos que vas a poner en la base de datos.  

~~~ 
db.createCollection('books')
~~~   

Al poner este código en MongoDB para añadir la colección libros,lo que el servidor nos va a devolver es algo importante en esta base de datos.  

~~~
{"ok" : 1}
~~~  

Esta sintaxis es importante para entender como funciona MongoDB porque nos muestra que todo es muy familiar y fácil de entender. Muy parecido a JavaScript.
Obtienes un objeto, un objeto clave-valor de tipo JSON en el cuál la clave es "ok" y el valor es 1.  

En MongoDB como no hay esquemas, puedes hacer que cada uno de tus documentos, nombres de columnas, nombres de las claves ... sea tan único como sea necesario.
A MongoDB no le importan tus datos, ni la estructura, es tan flexible que simplemente te permite almacenar los documentos tipo- objeto. Y el usuario se encarga de gestionar la creación y la capacidad de consultar las bases de datos. Al consultar algo hay que conocer los atributos presentes.  

<img src= "Captura de pantalla 2025-05-28 002547.png" alt="Mongo" width="500">

# 5. API 

<img src="Captura de pantalla 2025-05-28 002837.png" alt="api" width="400">

Interfaz de Programación de Aplicaciones.
Es una forma en la que podemos comunicarnos con una aplicación y podemos hacerlo sin más. Nos da un conjunto de comandos que podemos usar y hacer que una aplicación se comunique con otro servidor en otra aplicación. Lo que nos la API es un conjunto de puntos finales. Un punto final es sólo una URL( a lo que podemos acceder como si usaramos el navegador).  

Si colocamos en el navegador una API nos da un código confuso y muy dificil de entender y de trabajar con él.  

<img src = "Captura de pantalla 2025-05-29 013607.png" alt="API" with="300">  

También podemos decir que es un conjunto de reglas que permite que dos o más programas informáticos se comuniquen entre si para intercambiar datos y funcionalidades. Es un intermediario, facilita el intercambio de información de manera sencilla y eficiente, sin que el usuario se de cuenta de como ocurre.  

El significado de *interfaz* es la conexión entre dos sistemas independientes o interación entre un sistema informático y su usuario. Es la forma en que un programa o una página web se presenta al usuario.  

Por lo tanto la API es una *interfaz* que define como se conectan las aplicaciones.  

Ejemplo de la vida real: Tenemos una aplicación de clima que va a usar la API de un servicio meteorológico para obtener información del tiempo.  

Un ejemplo más simple para definir lo que podría ser una API es un restaurante.  

- Yo voy a un restaurente (soy la aplicación y soy el cliente) y quiero comer.
- La cocina (es el sistema al que quiero acceder) es donde se prepara la comida y están los ingredientes y los utensilios. Yo no puedo ir directamente a la cocina a coger lo que quiera ni a cocinar.
- El camarero (en este caso va a ser la API). Yo le digo al camarero lo que quiero (una tortilla). Ël coge el pedido, lo lleva a la cocina, preparan la tortilla y me trae el plato ya preparado.  

En un cajero automático.
- Yo voy a sacar dinero. (Soy la aplicación y el cliente).
- El banco es el sistema al quiero acceder. Contiene mi cuenta corriente, mi saldo..
- El cajero en si es la interfaz( será la API). Yo interactúo con el banco através de botones y una pantalla.
Le digo que quiero sacar 20 euros (esto será mi solicitud). El cajero se comunica con el banco, comprueba mi saldo, procesa la transación y me entrega el dinero.  

<img src= "ali-mkumbwa-OnRPps1wPus-unsplash.jpg" alt="cajero" width="400">

La API me permite interactuar con el banco sin necesidad de saber como funciona por dentro, sus bases de datos, sus servidores,...  

Así, la API permite que diferentes programas se comuniquen entre sí. Recibe peticiones, instrucciones (funciones), los traduce al sistema y devuelve una respuesta sin que necesites saber los detalles de como funciona un sistema por dentro.  

<img src= "Captura de pantalla 2025-05-30 175737.png" alt="google maps" width="400">

La API de Google Maps es una de las más usadas actualmente a nivel mundial. 


  
# 6. POSTMAN  


Postman es muy útil porque permite comunicarte con APIs externas. La API es un servicio, algo así como un sitio web o servidor con el que puedes comunicarte y que en vez de devolverte una página web, te devuelve datos.
Método útil para desarrollar aplicaciones y pasar datos de un lado a otro.  

<img src= "Captura de pantalla 2025-05-29 185623.png" alt="postman" width= "400">

Postman no es algo específico de un lenguaje de programación. Lo único que le interesa a esta herramienta es la solicitud de datos.  

Con Postman los datos que vamos a manejar son datos JSON, por lo que devolverá algo que una aplicación externa realmente puede usar.  

Si ponemos en el navegador una API nos da todo el código confuso y es muy dificil trabajar con ello. Aqui es donde son importantes herramientas como Postman que se usa para simplificar la forma en la que podemos comunicarnos con las APIs.  

<img src="Captura de pantalla 2025-05-30 192205.png" alt="codigo API" width="400">

Con Postman el código es fácil de leer y se puede hacer cualquier tipo de ajuste en un programa sobre la marcha.  

También podemos decir que es una plataforma para diseño, prueba y documentación de APIs. Herramienta para los desarrolladores para interactuar con APIs de forma fácil y eficiente,desde la creación de peticiones hasta la realización de pruebas.  

Facilita la colaboración entre desarrolladores, permitiendo compartir colecciones,documentos...,esto facilita el trabajo en equipo.  

Esta plataforma es utilizada por más de 20 millones de usuarios. Su interfaz sencilla y fácil de usar ayuda mucho a la hora de documentar, diseñar y probar las APIs.  

<img src="Captura de pantalla 2025-05-30 233210.png" alt="postman" width="600">







# 7. POLIMORFISMO  

"Poli" = muchos
"Morfismo" = cambiar.  

Puede tener muchos cambios o que un elemento puede tener muchas formas.  

El polimorfismo va muchas veces asociado a la herencia en las clases de Python.
Podemos tener una clase en la que dentro de ella hay varias subclases y tienen un mismo método para compartir su comportamiento.
Pero las subclases aunque usen el mismo método que la clase principal pueden cambiar su comportamiento. Esto es lo que hace el *polimorfismo*. Una clase hija hereda los métodos de la clase principal y luego puede anular el comportamiento.
Es la capacidad de objetos de diferentes clases de ser tratados como objetos de un tipo común y de responder de manera diferente a la misma llamada de método.

Tienes varias clases y todas tienen llamada al mismo código (método), pero luego pueden utilizarlo de diferente forma ejecutando su propia versión.  

Ejemplo cotidiano:

    Un reproductor de DVD.
    Un reproductor de MP3.  


Los dos aparatos tienen la función de *reproducir*. Cuando damos al play los dos aparatos van a funcionar pero de diferente manera. Este botón de play actúa como polimorfismo. Es igual para los dos pero cada uno va a hacer con él algo distinto. Y no necesitamos saber el mecanismo interno de los aparatos para iniciar la reproducción, sólo tenemos que saber que los dos tienen un botón de reproducir.

El primero, DVD, al dar al play va a mostrar una película.
El segundo,MP3, cuando presionamos ese botón de play va a saber como empezar a sonar una canción.

Ejemplo en Python.  


~~~
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        raise NotImplementedError
        
class Perro (Animal):
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Guau guau!"

class Gato (Animal):
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Miau miau!"


mi_perro= Perro('Zuri')
mi_gato= Gato('Lucas')

print(mi_perro.hacer_sonido())
print(mi_gato.hacer_sonido())
~~~

Solución  

~~~
Zuri dice: ¡Guau guau!
Lucas dice: ¡Miau miau!
~~~  

La función "hacer_sonido" crea el polimorfismo. Es la misma para los dos animales pero el comportamiento de estos animales es distinto al utilizar esa función.  

<img src= "Captura de pantalla 2025-05-29 011117.png" alt="perro" width="300"><img src="Captura de pantalla 2025-05-29 011221.png" alt="gato" width="247">

Si una clase tiene muchas funciones y hay mucho comportamiento compartido entre ellas es mejor usar la herencia.
Pero si no comparten mucho comportamiento pero quieres usar la misma función entonces es mejor usar el polimorfismo. Usas menos código y consigues el mismo resultado.(Todas las clases deben de llevar la misma función)  








# 8. METODOS DUNDER  

Son métodos que se utilizan en las clases de Python dentro de sus funciones. Comienzan siempre con dos guiones bajos seguido del nombre de función y terminado tambén por otros dos guiones bajos.  

Estos guiones bajos hacen que Python trabaje con métodos privados y protegidos dentro de sus clases.  

Cada vez que veas estos dunder en Python significa que es método privado que se proporciona directa y automáticamente desde el lenguaje Python.
Cualquiera lo puede usar pero no se debe anular ni cambiar de ninguna manera. Sólo debes usarlo en tus programas si quieres.  

Vamos a crear un método dunder de *cuerda* (dunder str) y vamos a insertarlo dentro de nuestra clase anterior llamada *Perro*.  

~~~
class Perro:

    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def __str__(self):
        return f" {self.nombre} es un {self.raza} de {self.edad} años."
mi_perro = Perro("Zuri", "Bichón Maltes", 6)
otro_perro = Perro("But", "Pastor Alemán", 15)

print(str(mi_perro))
print(otro_perro)
~~~  

Este método nos va a devolver una cadena de texto. Podemos imprimir de las dos maneras.

~~~
 Zuri es un Bichón Maltes de 6 años.
 But es un Pastor Alemán de 15 años.
~~~  

Lo que hace este método str es que busca que Python defina el método y si está definido en una clase busca lo que se devuelve. El objetivo de este método siempre que se use en una clase es ayudarnos a obtener algo de visibilidad en cada cosa de lo que se haya instanciado en la clase. Hacemos que sea dinámico.  
El método __str__ hace que la información de tus objetos sea mucho más clara y útil cuando los imprimes. Siempre que quieras una representación de cadena amigable para el usuario de un objeto se puede utilizar.

Se suele utilizar este método cuerda para tener la capacidad de deshacerme de todos los diferentes valores que son específicos de un objeto. Es decir, se usa para depurar.  

Hay otro método similar a *str*,*dunder repr*. Normalmente este se utiliza más para la salida en bruto del código. La forma de usarlo es igual y puedes utilizar o no ambos métodos en una clase.
No hay diferencia en cuanto a la implementación. Sólo cambia lo que representa.
Str se usa para tener una salida de código agradable, fácil de leer y repr nos da los valores en bruto. Envuelve todos los atributos, cualquier dato que vaya a necesitar utilizar cuando realiza la depuración y también se utiliza para arreglar errores en un programa.  

~~~
class Perro:

    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad= edad

    def __str__(self):
        return f" {self.nombre} es un {self.raza} de {self.edad} años."

    def __repr__ (self):
        return f" Perro ({self.nombre}, {self.raza})"
mi_perro = Perro("Zuri", "Bichón Maltes",6)
otro_perro = Perro("But", "Pastor Alemán", 15)

print(repr(mi_perro))
print(otro_perro)
~~~  

Si ejecutamos esto  

~~~
 Perro (Zuri, Bichón Maltes)
 But es un Pastor Alemán de 15 años.
~~~ 

# 9. DECORADOR EN PYTHON  

<img src="Captura de pantalla 2025-05-30 194535.png" alt="decorador" width="400">

Un decorador en Python es una función que recibe otra función como parámetro, le añade cosas y retorna una función diferente. Son herramientas muy útiles. Nos permiten envolver una función dentro de otra y modificar el comportamiento de esta última sin modificarla permanentemente.  

La  sintaxis de "@" le indica a Python que decore la función. Básicamente, un decorador es una función que modifica el comportamiento de otra función.  Los decoradores permiten añadir funcionalidad dinámicamente antes o después de la ejecución de funciones.  

Al trabajar con Python se utilizan mucho los decoradores. A través de los decoradores somos capaces de reducir las líneas de código duplicadas, hacemos que nuestro código sea legible, fácil de entender, fácil de mantener.  

Un decorador no es más que una función la cual toma como principio una función y a su vez retorna otra función.
Al momento de usar un decorador estamos trabajando, con por lo menos, 3 funciones. El input, el output y la función principal. Para que sea más claro, se puede nombrar a las funciones como: a, b y c.

"A" recibe como parámetro a "b" para dar como salida a "c".
Con la herramienta *decorar* estamos indicando que queremos modificar el comportamiento de una función ya existente, pero sin tener que modificar su código.
Para decorar una función basta con colocar, en la parte superior de dicha función, el decorador con el prefijo @.

Un decorador se puede ajustar a los métodos o a las clases. 


~~~
def make_upper(func):
    def wrapper():
        return func().upper()
    
    return wrapper

@make_upper
def python_greeting():
    return 'hi, i\'m a Python developer!'

print(python_greeting())  
~~~  

Esto es lo que nos devuelve la función decoradora al imprimirla.  


~~~
HI, I´M A PYTHON DEVELOPER!
~~~

Haces más legible el código para que otra persona pueda entenderlo.

Usamos el operador @ para decorar la función y obtener una salida clara y limpia.  


Podemos decorar varias veces una sola función. Esto siempre va a ser posible en el orden en que llamas a los decoradores. Ahora, además del decorador anterior, aplicamos uno que invierta el orden de las letras que le pasamos.  

~~~
def make_upper(func):
    def wrapper():
        return func().upper()
    
    return wrapper

def reverse_str(func):
    def wrapper():
        return func()[::-1] 
    
    return wrapper   

@make_upper
@reverse_str
def python_greeting():
    return 'hi, i\'m a Python developer!'
print(python_greeting())
~~~  


Primero se aplica @make_upper para convertir todo el string en mayúsculas y luego @reverse_str para invertir el orden de la misma. Por lo tanto, en la terminal veremos.  


~~~
HI, I´M A PYTHON DEVELOPER!
!REPOLEVED NOHTYP A M'I ,IH
~~~










