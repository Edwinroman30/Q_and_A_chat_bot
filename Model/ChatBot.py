import re
import random

class ChatBot():
    """
    Welcome to chatbot, this is a simple chatbot written by Juan L. Restituyo and improved by Edwin Roman. 
    More detail: https://github.com/Edwinroman30/Q_and_A_chat_bot
    """
    
    def __init__(self) -> None:
        self.list_of_QA = []
    
    
    def __repr__(self) -> str:
        return "Welcome to chatbot, this is a simple chatbot written by Juan L. Restituyo and improved by Edwin Roman. More detail: https://github.com/Edwinroman30/Q_and_A_chat_bot"
    
    
    def get_response(self, user_input) -> str:
        """Split the given user input string for analizing each word."""
        split_message = re.split(r'\s|[¡,¿,:;.?!-_]\s*', user_input.lower()) # \s -> Return a match at every white-space character:
        response = self.check_all_messages(split_message)
        return response


    def message_probability(self, user_message: list, recognized_words: list, single_response=False, required_word=[]) -> int:
        """Determinate the probability of the appearance of the user inputs regarding the list of recognized_words. """
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

        if has_required_words or single_response:                                             
            return int(percentage * 100)
        else:
            return 0


    def check_all_messages(self, user_message : list) -> str:
            """Create a new dict that contain the response string as the key & the probability as value. 
            Return the highest probability of the responses."""
                
            highest_prob = {}

            #instead of reciving multiple inputs recive a dict. Then pass each dict from the json list of dicts.

            def response(bot_response : str, posible_inputs : list, single_response = False, required_words = []) -> None:
                nonlocal highest_prob
                highest_prob[bot_response] = self.message_probability(user_message, posible_inputs, single_response, required_words)
            
            for ques_answ in self.list_of_QA:    
                response(ques_answ["bot_response"], ques_answ["bot_keywords"], single_response = ques_answ["is_single_response"], required_words = ques_answ["bot_required_words"] )

            best_match = max(highest_prob, key=highest_prob.get)
            #print(highest_prob)

            return self.unknown() if highest_prob[best_match] < 1 else best_match

    def unknown(self) -> str:
        response = ['¿Podría redactarlo de otra manera?', 'Lo siento, no estoy seguro de lo quieres.', 'Intente búscarlo en la web https://itla.edu.do, tal vez le ayude. :)'][random.randrange(3)]
        return response

    