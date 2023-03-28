In the previous exercise, we modified the `path` of our file dictionaries, but we didn't use its `creation` date. Let's do that! We need to know if a file is from the past millennium, which is the case if its year is before 2000 :back: :

```python
ムis_from_past_millennium({ "path": "D:\photobirth.jpg", "creation": "1989-09-14" })
True
ムis_from_past_millennium({ "path": "D:\photomarriage.jpg", "creation": "2017-09-25" })
False
```

> Define the function `is_from_past_millennium`. We have created a `year` function for you, which works like this:
>
```python
ムyear("1993-11-04")
1993
```
