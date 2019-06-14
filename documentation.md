# Description of the Monty's CAD Language

## 3 dimensional primitives

### Cube

```python
cube(size, center = False)
```

Where:
+ `size` is the list `[lenght, wide, height]`. If `size` is simply a number, `n`, then it is `[n, n, n]`.
+ `center` can be `True` or `False`. If it is `True` it's centered at the origin, if it's `False` it rests at the first octant touching a vertex the origin.

__Fisrst octant cube__

```python
cube(20)
```

![alt text](https://github.com/RubenRubens/Montys-CAD/blob/master/Images/3D%20primitives/cube%20first%20octant.PNG)

__Centered cube__

```python
cube(20, center = True)
```

![alt text](https://github.com/RubenRubens/Montys-CAD/blob/master/Images/3D%20primitives/cube%20center.PNG)

__Cube with sides of diferent lenght__

```python
cube([65, 30, 10])
```

![alt text]()