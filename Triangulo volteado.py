def triangulo_de_cabeza(n):
	x=" "
	z=1
	t="T"
	u=n
	while (n>0):
		p=(n-1)*x
		n=n-1
		w=z*t
		z=z+1
		print(p+w)
	
	while (n<z):
		p=(n+1)*x
		n=n+1
		w=t*(u-1)
		u=u-1
		print (p + w)
		
		
	
n=int(input("Ingrese el tamano del triangulo: "))
tri=triangulo_de_cabeza(n)


