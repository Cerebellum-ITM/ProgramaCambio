

# ProgramaCambio 
Programa realizado para el canal de  :video_camera: youtube [Cerebellum](https://www.youtube.com/channel/UCngKMVEN9mc94vOvS8SFEGA?view_as=subscriber)
 en Python.
 
 ## Pseudocódigo
 ```python
Funcion Cambio(importe, DinRecibido, ListadeDenom)
		Cambio = DinRecibido - importe
		Repetir hata i = NumdeDenom
			Escribir Cambio
			Billetesx = Camio/Denominacion (Eliminar fracciones)
			Cambio = Cambio%Denominacion
			Esccribir Billetesx, Denominacion
		Escribir Cambio  
	Fin de la funcion Cambio.
``` 
 ## Código en Python
 ```python
Cantidades = [500, 200, 100,50,10,5,1,0.5]
Importe = 2143.5
DinRecibido = 4000
Cambio = DinRecibido - Importe

for Denominacion in Cantidades:
	print(Cambio)
	Billetesx = int(Cambio/Denominacion)
	Cambio = Cambio%Denominacion
	print(Billetesx, Denominacion)
print(Cambio)
```
## Resultado
 ```python
1856.5
	3 500
	356.5
	1 200
	156.5
	1 100
	56.5
	1 50
	6.5
	0 10
	6.5
	1 5
	1.5
	1 1
	0.5
	1 0.5
	0.0
```


Autor: M.C. Pascual Neftalí Chávez Campos.

![](https://github.com/Cerebellum-ITM/ProgramaCambio/blob/master/Cere60PCC.jpg)



