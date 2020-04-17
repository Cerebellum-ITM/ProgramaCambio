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
