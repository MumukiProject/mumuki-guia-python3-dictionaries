Awesome! In this exercise, we dealt with another common problem in programming: _dates_. 🐍 In real life Python programming, we would probably never use string to _encode_ a date, but use a specific data-type instead. 📅 Let's meet `date`:

```python
ムdate(2014, 11, 20)
datetime.date(2014, 11, 20)
```

`date`s can be nicely operated in order to query their parts, compare them o even extract the duration of a interval between two of them: 

```python
ムanother_date = date(1985, 10, 25)
ムanother_date.year
1989
ムanother_date.month
1989
ムanother_date > date(1955, 11, 5)
True
ムdate(1985, 10, 26) - another_date
datetime.timedelta(days=1)
```
