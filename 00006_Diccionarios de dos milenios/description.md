En el ejercicio anterior modificamos la ruta del diccionario, pero no utilizamos su fecha de creación. ¡Usémosla! Queremos saber si un archivo es del milenio pasado, lo que ocurre cuando su año es anterior al 2000 :back: :

```python
ム es_del_milenio_pasado({ "ruta": "D:\fotonacimiento.jpg", "creacion": "14/09/1989" })
True

ム es_del_milenio_pasado({ "ruta": "D:\fotocasamiento.jpg", "creacion": "25/09/2017" })
False
```

> Definí la función `es_del_milenio_pasado`. Te va a ser de ayuda la función `anio` que funciona así:
>
```python
ム anio("04/11/1993")
1993
``` 

