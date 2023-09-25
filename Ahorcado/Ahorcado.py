import funciones
import random

counter = 0
secret_word=[]
# Lista de posibles palabras
words_list = ['programacion','variable', 'python', 'lenguaje', 'bucle', 'computadora','funcion']

# El programa elije una palabra de la lista al azar
word = random.choice(words_list)

# Llenamos la lista 'secret_word' con tantos guiones como letras tenga la palabra
for i in word:
    secret_word += "_"

# Empieza el juego y le muestra al jugador la lista con los guiones correspondientes
print("\nEmpieza el juego del ahorcado. Tenés 5 intentos para adivinar una palabra relacionada a la programación.\nLa palabra es: ", end="")
print(secret_word)

# El while repite el proceso hasta que el jugador adivine o pierda los 5 intentos
while counter<5:
    letter_counter = 0
    has_letter=False
    # Le pedimos al jugador que ingrese una letra
    letter = input("\nLetra: ").lower()
    # Validamos que haya ingresado una letra, si no es asi, repite el proceso
    while funciones.data_validation(letter) == False:
        letter = input("\nLetra: ").lower()

    # Una vez que tenemos la letra, chequeamos que esté en la palabra.
    # Si está, la variable has_letter es igual a True y a la vez contamos cuantas
    # veces está esa letra en la palabra
    for i in word:
        if i == letter:
            letter_counter += 1
            has_letter=True

    # Si la funcion contains_letter devuelve falso, significa que la letra no
    # estaba en la palabra, entonces sumamos 1 al contador de intentos.
    if funciones.contains_letter(has_letter, letter,word,secret_word, letter_counter)==False:
        counter += 1
        if counter==5:
            print("Juego terminado. Te quedaste sin intentos :(\nLa palabra secreta es:",word)
        elif 5-counter == 1:
            print("Te queda solo 1 intento. Pensá bien.")
        else:
            print("Quedan", 5-counter,"intentos")
    
    # Si la funcion is_word_guess devuelve verdadero, significa que la palabra ya 
    # fue adivinada y corta el bucle.
    if funciones.is_word_guess(secret_word,word) == True:
        break

    
        


   






