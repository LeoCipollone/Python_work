print("Hola")
print("\tHola") #Sangría
print("Saludos:\nHola\nBuenos días\n¿Cómo andamos?") #Nueva linea
print("Números:\n\t1\n\t\t2\n\t\t\t3") #Nueva linea con sangría

hola = "¿Cómo estás? "
hola #Sale con espacios
hola.rstrip() #Elimina temporalmente los espacios de la derecha en Strings

favorite_language = " python "
favorite_language = favorite_language.rstrip() #Elimina permanentemente los espacios derecha
favorite_language = favorite_language.lstrip() #Elimina permanentemente los espacios izquierda 
favorite_language = favorite_language.strip()  #Elimina permanentemente ambos espacios
