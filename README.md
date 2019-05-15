# L-SYSTEMS
### Trabajo realizado para la asignatura Lenguajes Formales (UC)

## Funcionamiento
Ejecutar con Python 3 el fichero main_gui.py.
El botón "Guardar regla" guarda los campos "Variables" y "Reglas" ya que se aceptan varias reglas, pero solo una por variable.
El botón JSON abre un filechooser para cargar directamente l-systems sin tener que utilizar los campos.

## Explicación de cada campo
### Estado inicial
Estado en el que empieza el l-sistema

### Variables 
Cada letra que encontramos en el alfabeto del lenguaje

### Avance
Checkbox que determina si una variable es representada o no gráficamente

### Reglas 
Estados a los que llegas con cada variable

### Iteraciones
Número de iteraciones que va a procesarse el l-sistema

### Ángulo
Cada vez que el l-sistema gira, se mueve tantos grados como el ángulo que indiquemos

### Linea 
Tamaño que se le pone a cada representación de las variables, para poder representar así un mayor número de iteraciones en un espacio más reducido

### Orientación
Lista con las orientaciones posibles, en grados
