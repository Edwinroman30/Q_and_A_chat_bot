import json
import os
from Model import ChatBot as ChatBot

# Where the term qa = QA = Questions & Answares

def load_qa(file_path : str) -> list:
    """Here load the json that contain an array of Q&A with an specific structure."""
    try:
        with open(file_path, encoding="utf-8") as the_file:    
            json_result = json.load(the_file)
            #print(json_result)
    except FileNotFoundError as e: #subclass of OSError
        with open(file_path, "w") as the_file:
                 the_file.write(json.dumps([]))
        print("This file is not found, let create it. Please run the app again.")
        exit()
    except OSError as e:
        print("Couldn't open file")
    except PermissionError as e:
        print("File is locked")
    except ValueError as e:
        print("Cannot parse data. Check file") 
    except Exception as e:
        print(type(e))
        print(e)
    finally:
        the_file.close()
        return json_result
         
def input_qa(file_path : str) -> None:
    """
    Allow us to insert the inputted data into a JSON file, having some interfaces to capture this values. 
    """
    ques_answ = dict()
    ques_answ["bot_keywords"] = input("Separed each one by a comma, type the posibles keywords to match (Practicaly the question without question mark): ") 
    ques_answ["bot_keywords"] = ques_answ["bot_keywords"].split(",")
    #
    ques_answ["bot_response"] = input("Type the posible boot answare: ")
    #
    ques_answ["is_single_response"] = input("Is going to be a single response?, (0 = NO, 1 = YES) ")
    ques_answ["is_single_response"] = ques_answ["is_single_response"] == "0" if False else True
    #
    ques_answ["bot_required_words"] = input("Type the required words each one separed by comma: ").split(",")

    print(json.dumps(ques_answ, indent = 4))
    
    try:
        with open(file_path, "r+", encoding="utf-8") as the_file:
            # First we load existing data into a list of dicts.
            json_result = json.load(the_file)
            
             # Join ques_answ the rest of the data.
            json_result.append(ques_answ)
            
            # Sets file's current position at offset.
            the_file.seek(0)
            
             # convert back to json.            
            the_file.write(json.dumps(json_result, indent = 4))
            
            print("Saved!")
    except FileNotFoundError as e: #subclass of OSError
        with open(file_path, "w") as the_file:
                 the_file.write(json.dumps([]))
        print("This file is not found, let create it. Please run the app again.")
        exit()
    except OSError as e:
        print("Couldn't open file")
    except PermissionError as e:
        print("File is locked")
    except ValueError as e:
        print("Cannot parse data. Check file") 
    except Exception as e:
        print(type(e))
        print(e)
    finally:
        the_file.close()
    
def main():
    
    bot = ChatBot.ChatBot()
    
    print("""
    1) Use the Bot.
    2) Input a new Q&A.
    3) Exit
    """)

    #Menu option
    opt = int(input("> "))
    
    #Where is my json file!
    _path = "QA.json"
    
    if(opt == 3):
        print("Thank for choose us!")
        exit()
    elif opt == 2:
        input_qa(_path)
        os.system("cls")
        main()
    elif opt == 1:
        #Loading the json.
        bot.list_of_QA = load_qa(_path)
        while True:
            print("Bot: " + bot.get_response(input('You: ')))
            
#Entry Point.
main()