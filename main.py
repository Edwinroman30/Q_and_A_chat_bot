import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower()) # \s -> Return a match at every white-space character:
    response = check_all_messages(split_message)
    return response

def message_probability(user_message: list, recognized_words: list, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True
    
    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
        
    #Por defecto siempre van a ver dos opciones explicitas por el usurio que haran que esta condicion
    # se cumpla, la primera es que cuando no se quiere una palabra requerida, fijamente se coloca
    # el parametro single_response = True, cuando se quieren palabras requeridas estas solo se
    #asignan en el parametro required_words. Al final con esto siempre nos aseguraremos de que siempre
    #nos devuelva el valor de porcentaje encontrado, si es que hay.    
    
    if has_required_words or single_response:                                             
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(user_message : list) -> str:
        highest_prob = {}

        def response(bot_response : str, posible_inputs : list, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(user_message, posible_inputs, single_response, required_words)
            #posible_inputs = are posible questions inputs.
            
        response('Hola', ['hola', 'klk', 'saludos', 'buenas'], single_response = True)
        response('Estoy bien y tu?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])
        response('Estamos ubicados en la calle 23 numero 123', ['ubicados', 'direccion', 'donde', 'ubicacion'], single_response=True)
        response('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)

        best_match = max(highest_prob, key=highest_prob.get)
        print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match
        #para dar la response le vamos a pasar en formato json

def unknown():
    response = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'búscalo en google a ver que tal'][random.randrange(3)]
    return response

while True:
    print("Bot: " + get_response(input('You: ')))
    