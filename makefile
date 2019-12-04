resultado.png: eje17.dat Grafica.py
	python Grafica.py
	
eje17.dat:eje17.x
	./eje17.x

eje17.x:eje17.cpp
	c++ eje17.cpp -o eje17.x

solar.png : eje16.py
	python eje16.py

sigma.png : eje15.py
	python eje15.py
	
clean : 
	rm eje17.x resultado.png solar.ong sigma.png