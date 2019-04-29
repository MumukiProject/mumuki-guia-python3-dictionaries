Unos ejercicios atrás te contamos la diferencia entre listas y registros. ¡Pero eso no significa que no podamos usar ambas estructuras a la vez! :wink:

Por ejemplo, una lista puede ser el campo de un registro. Mirá estos registros de postres, de los cuales sabemos cuántos minutos de cocción requieren y sus ingredientes:

```python
flanCasero = { "ingredientes": ["huevos", "leche", "azúcar", "vainilla"], "tiempoDeCoccion": 50 }
cheesecake = { "ingredientes": ["queso crema", "frambuesas"], "tiempoDeCoccion": 80 }
lemonPie = { "ingredientes": ["jugo de limón", "almidón de maíz", "leche", "huevos"], "tiempoDeCoccion": 65 }
```

> Creá una función `masDificilDeCocinar`, que recibe dos registros de postres por parámetros y devuelve el que tiene más ingredientes de los dos.

> ```python
ム masDificilDeCocinar(flanCasero, cheesecake)
=> { "ingredientes": ["huevos", "leche", "azúcar", "vainilla"], "tiempoDeCoccion": 50 }
```
