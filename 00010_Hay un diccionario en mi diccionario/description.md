¿Te acordás cuando vimos que una lista podía estar compuesta por otras listas? ¡Con los diccionarios aplica la misma idea! :hushed: Si tenemos alguna estructura de datos compleja, puede ocurrir que no alcance con representarla únicamente mediante strings, números, booleanos y listas, sino que necesitemos _otro_ diccionario dentro.

¡No se puede vivir a base de postres! Bueno, quizás sí, pero mantengamos una alimentación saludable :stuck_out_tongue_winking_eye:. Mediante un diccionario queremos modelar un menú completo: consiste en un plato principal :curry:, los vegetales de la ensalada que acompaña :tomato:, y un postre :custard: como lo veníamos trabajando, es decir, sigue siendo un diccionario.

Por ejemplo, el siguiente es un menú con bife de lomo como plato principal, una ensalada de lechuga, tomate y zanahoria como acompañamiento y un cheesecake de postre. Como el diccionario es un poco extenso, y para que sea más legible, lo vamos a escribir de la siguiente forma:

```python
menu_del_dia = {
  "plato_principal": "milanesas de berenjena",
  "ensalada": ["papa", "zanahoria", "arvejas"],
  "postre": { "ingredientes": ["queso crema", "frambuesas"], "tiempo_de_coccion": 80 }
}
```

> Averiguá los `ingredientes` del `postre` del `menu_infantil`. Es un diccionario dentro de otro, así que vamos a tener que acceder primero al campo `postre` y luego a su campo `ingredientes`. Si no se te ocurre cómo, podés mirar la pista. :mag: 

