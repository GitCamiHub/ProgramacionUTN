# Validamos que lo que ingresa el jugador es una letra.
def data_validation(letter):
    if letter<'a' or letter>'z' and letter!='ñ':
        print("Ingrese una letra de la A a la Z.")
        return False

# Analizamos si la letra está o no en la palbra
def contains_letter(has_letter,letter,word,secret_word,letter_counter):
    start = 0
    if has_letter == True:
        print("Bien!! La letra",letter,"está en la palabra.")
        # Si la letra está mas de una vez
        if letter_counter>1:
            # Se repite el ciclo for tantas veces como aparezca la letra
            for i in range(letter_counter):
                # Calcula la posicion de la letra
                position = word.find(letter,start)
                # Chequeamos que el lugar esté 'vacio'
                if secret_word[position]=="_":
                    # Escribimos en esa posicion la letra
                    secret_word[position]= letter
                    # Hacemos que start valga la posicion de la primera
                    # aparicion de la letra mas 1 para que en la proxima vuelta
                    # no vuelva a encontrar la primera letra, sino la segunda, tercera,etc.
                    start = position + 1
            print(secret_word,"\n")
        # Si la letra aparece solo una vez         
        else:
            position = word.find(letter)
            if secret_word[position]=="_":
                secret_word[position]= letter
                print(secret_word,"\n")
        return True
    # Si la letra no esta en la palabra se imprime un mensaje
    else:
        print("La letra",letter,"no está en la palabra.")
        print(secret_word,"\n")

        return False

# Controla si la palabra ya fue adivinada para imprimir un mensaje
def is_word_guess(secret_word,word):
    guess = 0
    for i in secret_word:
            if i != "_":
                guess +=1

    if guess == len(secret_word):
        print("ADIVINASTE!!\nLa palabra secreta es:",word)
        return True
    else:
        return False


