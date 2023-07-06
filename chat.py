#this is simple chatbot with machine learning

#chatbot using python for beginners


def chat():

    users=['hai','how are you','I need help','what is your name','good morning','good afternoon','What are you doing','thank you']

    bot=['hai!','I am fine ! what about you','I am here to assist you','my name is chatBot','good morning','good afternoon','Im an ai model, here to assist you','welcome']

    user_input=input("You : ")

    i=0

    for user in users :

        if user_input==user:

            print("Bot : " +bot[i]) 
            
            return chat()

        i=i+1


chat()
