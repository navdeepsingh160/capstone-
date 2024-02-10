from tkinter import *
from tkinter import messagebox
root = Tk()
root.title(" Adviser")
root.geometry("600x600")

question1_Radiobutton = StringVar(value = "0")
question1 = Label(root, text = "you need to get your own ATM cart")
question1.pack()
question1_r1 = Radiobutton(root, text ="yes",  variable= question1_Radiobutton, value="yes")
question1_r1.pack()
question1_r2 = Radiobutton(root, text ="no",  variable= question1_Radiobutton, value="no")
question1_r2.pack()

question2_Radiobutton = StringVar(value = "0")
question2 = Label(root, text = "if you need to apply in game dvloper jop in future ")
question2.pack()
question2_r1 = Radiobutton(root, text ="yes",  variable= question2_Radiobutton, value="yes")
question2_r1.pack()
question2_r2 = Radiobutton(root, text ="no",  variable= question2_Radiobutton, value="no")
question2_r2.pack()

question3_Radiobutton = StringVar(value = "0")
question3 = Label(root, text = "how to increase you pc capasity")
question3.pack()
question3_r1 = Radiobutton(root, text ="yes",  variable= question3_Radiobutton, value="yes")
question3_r1.pack()
question3_r2 = Radiobutton(root, text ="no",  variable= question3_Radiobutton, value="no")
question3_r2.pack()

question4_Radiobutton = StringVar(value = "0")
question4 = Label(root, text = "softwares for game devlopers")
question4.pack()
question4_r1 = Radiobutton(root, text ="yes",  variable= question4_Radiobutton, value="yes")
question4_r1.pack()
question4_r2 = Radiobutton(root, text ="no",  variable= question4_Radiobutton, value="no")
question4_r2.pack()


def fever_score():
    score = 0
    if question1_Radiobutton.get() =="yes":
        score = score+10
        print(score)
    if question2_Radiobutton.get() =="yes":
        score = score+10
        print(score)
    if question3_Radiobutton.get() =="yes":
        score = score+10
        print(score)
    if question4_Radiobutton.get() =="yes":
        score = score+10
        print(score)    
        
        
        
    if score <= 10 :
        messagebox.showinfo("the adiviser ", "if you are 18 year ago you will apply in your near bank")
    elif score>10 and score<=20:
        messagebox.showinfo("the adiviser ", "these are the course you will master to become devloper, c++, python, java, ")
      
          
           
       
    else:
        messagebox.showinfo("the adiviser ", "you will change SSD of your computer and Ram of you computer ")
        messagebox.showinfo("the adiviser ", "unity engine, unreal engine 5")
btn = Button(root, text="click me", command = fever_score)
btn.pack()
root.mainloop()