Por el momento estuvimos creando y consultando diccionarios. ¿No sería interesante poder... modificarlos? :smirk:

La sintaxis para modificar campos de diccionarios es muy similar a lo que hacemos para cambiar los valores de las variables. Por ejemplo, para cambiar la temperatura de un planeta:

```python
ム saturno["temperatura_promedio"] = -140
```
Ahora imaginá que tenemos un diccionario para representar un archivo, del que sabemos su ruta (dónde está guardado) y su fecha de creación. Si queremos cambiar su ruta podemos hacer...

```python
ム leeme
{ "ruta": "C:\leeme.txt", "creacion": "23/09/2004" }

ム mover_archivo(leeme, "C:\documentos\leeme.txt") }
```

Luego el diccionario `leeme` tendrá modificada su ruta:

```python
ム leeme
{ "ruta": "C:\documentos\leeme.txt", "creacion": "23/09/2004" }
```

> ¡Es tu turno! Definí el procedimiento `mover_archivo`, que recibe un diccionario y una nueva ruta y modifica el archivo con la nueva ruta.
