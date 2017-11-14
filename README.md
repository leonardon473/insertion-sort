# insertion-sort
Ejemplo con funciones del algoritmo [Ordenamiento por inserción](https://es.wikipedia.org/wiki/Ordenamiento_por_inserci%C3%B3n) 

## Funciones
### insertion_sort_less_to_greater()
```python
def insertion_sort_less_to_greater(_lista):
    for i in range(1,len(_lista)):
	    #print("i:",i)
		for e in range(0,i):
			#print(e)
			if _lista[i] < _lista[e]:
				_lista = put_i_in_j(_lista,i,e)
		#print(_lista)
		#print()
	return _lista
```
### insertion_sort_greater_to_less()
```python
def insertion_sort_greater_to_less(_lista):
	for i in range(1,len(_lista)):
		#print("i:",i)
		for e in range(0,i):
			#print(e)  
			if _lista[i] > _lista[e]:
				_lista = put_i_in_j(_lista,i,e)
		#print(_lista)
		#print()
	return _lista
```
Estas dos funciones usan
### put_i_in_j()
```python
def put_i_in_j(_lista,i,j):
	t = _lista[i]
	if i>j:
		for e in range(i,j,-1):
			#print(e)
			_lista[e] = _lista[e-1]
		_lista[j] = t
		return _lista
	elif i<j:
		for e in range(i,j):
			#print(e)
			_lista[e] = _lista[e+1]
		_lista[j] = t
		return _lista
	else:
		return _lista
```
