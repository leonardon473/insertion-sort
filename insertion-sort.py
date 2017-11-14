lista = [6, 2, 4, 3, 1, 16, 14, 9, 8, 10]
print(lista)

def permuta(_lista, i, j):
	t = _lista[i]
	_lista[i] = _lista[j]
	_lista[j] = t
	return _lista
	
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
print(insertion_sort_less_to_greater(lista))

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
	
print(insertion_sort_greater_to_less(lista))