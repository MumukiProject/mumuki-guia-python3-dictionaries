 Unos ejercicios atrás te contamos la diferencia entre listas y diccionarios. ¡Pero eso no significa que no podamos usar ambas estructuras a la vez! :wink:

Por ejemplo, una lista puede ser el campo de un diccionario. Mirá estos diccionarios de postres, de los cuales sabemos cuántos minutos de cocción requieren y sus ingredientes:

```python
ム flan_casero = { "ingredientes": ["huevos", "leche", "azúcar", "vainilla"], "tiempo_de_coccion": 50 }
ム cheesecake = { "ingredientes": ["queso crema", "frambuesas"], "tiempo_de_coccion": 80 }
ム lemon_pie = { "ingredientes": ["jugo de limón", "almidón de maíz", "leche", "huevos"], "tiempo_de_coccion": 65 }
```

> Definí la función `mas_dificil_de_cocinar`, que recibe dos diccionarios de postres como argumento y retorna el que tiene más ingredientes de los dos:

> ```python
ム mas_dificil_de_cocinar(flan_casero, cheesecake)
{ "ingredientes": ["huevos", "leche", "azúcar", "vainilla"], "tiempo_de_coccion": 50 }
```
