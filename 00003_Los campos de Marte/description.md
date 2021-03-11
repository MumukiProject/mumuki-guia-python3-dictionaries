Cuando consultaste los diccionarios existentes, se veía algo parecido a lo siguiente:

```python
ム taj_mahal
{ "nombre": "Taj Mahal", "locacion": "Agra, India", "anio_de_construccion": 1653 }
```

Esa consulta era porque estábamos viendo al diccionario `taj_mahal` completo, incluyendo todos sus campos. ¡Pero también se puede consultar por un campo particular! Mirá :eyes::

```python
ム taj_mahal["locacion"]
"Agra, India"
ム taj_mahal["anio_de_construccion"]
1653
```

> Inicializamos los planetas `mercurio`, `marte` y `saturno` como diccionarios con los campos `nombre`, `temperatura_promedio` y si `tiene_anillos`. 

> Miralos en la consola y cuando termines escribí `listo()`.
