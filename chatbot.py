from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *

bot = ChatBot("My Bot")

convo = [
    'hello',
    'hi there !',
    'what is your name ?',
    'My name is Bot , i am created by Niraj',
    'how are you',
    'I am fine',
    'what is today weather ?',
    '30',
    'what is yesterday weather ?',
    '40'
]

trainer = ListTrainer(bot)
# now training the bot with the help of trainers
trainer.train(convo)
# answer = bot.get_response("what is your name ?")

# print("Talk to bot")
# while True:
#    query = input()
#    if query == ' exit':
#        break
#
#    else:
#        answer = bot.get_response(query)
#        print("bot :", answer)
main= Tk()
main.geometry('500x650')
main.title("my chat bot")
img = PhotoImage(file='bot.png')
photoL = Label(main, image=img)
photoL.pack(pady=5)

def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    msgs.insert(END, "bot : " + str(answer_from_bot))
    textF.delete(0, END)


frame = Frame(main)
#sc = Scrollbar(frame)
msgs = Listbox(width=80, height=20)
#sc.pack(side=LEFT, fill=Y)
msgs.pack( pady=10)
frame.pack()
# creating text filed
textF = Entry(main, font=("verdana", 20))
textF.pack(fill=X, pady=10)
btn = Button(main, text='Ask from bot', font=("verdana", 10), command=ask_from_bot)
btn.pack()


main.mainloop()