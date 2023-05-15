from funzioni import Calcolo_perimetro_q 
from funzioni import Calcolo_circonferenza_cerchio
from funzioni import Calcolo_perimetro_rettangolo 
import math 

while True: 

	print ("seleziona il comando che vuoi utilizzare : ")
	print ("1. Perimetro Quadrato")
	print ("2. Cinconferenza cerchio")
	print ("3. Perimetro Rettangolo")
	print ("4. esci")	


	scelta = input ("inserisci la tua scenta :") 

	if scelta == '1':
		l= float(input("iserisci la lunghezza del lato del quadrato: "))
		perimetro = Calcolo_perimetro_q(l)
		print ("il perimetro del quadrato è : ",perimetro)
	
	elif scelta == '2':
		r= float(input("iserisci la lunghezza del raggio  del cerchio: "))
		cir = Calcolo_circonferenza_cerchio(r)
		print ("il perimetro del cerchio è : ",cir)
	elif scelta == '3':
		b= float(input("iserisci la base del rettangolo : "))
		h= float(input("iserisci l'altezza del rettangolo: "))
		perimetro = Calcolo_perimetro_rettangolo(b,h)
		print ("il perimetro del rettangolo è : ",perimetro)
	
	elif scelta == '4':
		print ("Sei uscito.")
		break
	
	else:
		print("scelta non valida. digita corretto")
 
