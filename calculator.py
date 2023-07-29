from tkinter import *

first_number = second_number = operator = None

def get_digit(digit):
    current = result_label["text"]
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text="")

def get_operator(op):
    global first_number,operator
    first_number = int(result_label["text"])
    operator = op
    result_label.config(text="")

def get_result():
    global first_number,second_number,operator
    second_number = int(result_label["text"])

    if operator == "+":
        result_label.config(text=str(first_number+second_number))
    elif operator == "-":
        result_label.config(text=str(first_number - second_number))
    elif operator == "*":
        result_label.config(text=str(first_number * second_number))
    else:
        if second_number == 0:
            result_label.config(text="Error")
        else:
            result_label.config(text=str(round(first_number / second_number,2)))

root = Tk()

root.title("Calculator")

root.geometry("280x400")
root.resizable(0,0)
root.configure(background="#164B60")

result_label = Label(root,text="",bg="#164B60",fg="#A2FF86")
result_label.grid(row=0,column=0,columnspan=5,pady=(50,25),sticky="w")
result_label.config(font=("Times New Roaman",30,"bold"))

btn7 =Button(root,text="7",bg="#1B6B93",fg="#A2FF86",width=6,height=2,command=lambda : get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=("Times New Roman",14))

btn8 =Button(root,text="8",bg="#1B6B93",fg="#A2FF86",width=6,height=2,command=lambda : get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=("Times New Roman",14))

btn9 =Button(root,text="9",bg="#1B6B93",fg="#A2FF86",width=6,height=2,command=lambda : get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=("Times New Roman",14))

btn_add =Button(root,text="+",bg="#4FC0D0",fg="#164B60",width=6,height=2,command=lambda : get_operator("+"))
btn_add.grid(row=1,column=3)
btn_add.config(font=("Times New Roman",14))

btn4 =Button(root,text="4",bg="#1B6B93",fg="#A2FF86",width=6,height=2,command=lambda : get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=("Times New Roman",14))

btn5 =Button(root,text="5",bg="#1B6B93",fg="#A2FF86",width=6,height=2,command=lambda : get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=("Times New Roman",14))

btn6 =Button(root,text="9",bg="#1B6B93",fg="#A2FF86",width=6,height=2,command=lambda : get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=("Times New Roman",14))

btn_sub =Button(root,text="-",bg="#4FC0D0",fg="#164B60",width=6,height=2,command=lambda : get_operator("-"))
btn_sub.grid(row=2,column=3)
btn_sub.config(font=("Times New Roman",14))

btn1 =Button(root,text="1",bg="#1B6B93",fg="#A2FF86",width=6,height=2,command=lambda : get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=("Times New Roman",14))

btn2 =Button(root,text="2",bg="#1B6B93",fg="#A2FF86",width=6,height=2,command=lambda : get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=("Times New Roman",14))

btn3 =Button(root,text="3",bg="#1B6B93",fg="#A2FF86",width=6,height=2,command=lambda : get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=("Times New Roman",14))

btn_mul =Button(root,text="*",bg="#4FC0D0",fg="#164B60",width=6,height=2,command=lambda : get_operator("*"))
btn_mul.grid(row=3,column=3)
btn_mul.config(font=("Times New Roman",14))

btn_clr =Button(root,text="C",bg="#4FC0D0",fg="#164B60",width=6,height=2,command=lambda : clear())
btn_clr.grid(row=4,column=0)
btn_clr.config(font=("Times New Roman",14))

btn0 =Button(root,text="0",bg="#1B6B93",fg="#A2FF86",width=6,height=2,command=lambda : get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=("Times New Roman",14))

btn_equals =Button(root,text="=",bg="#4FC0D0",fg="#164B60",width=6,height=2,command=get_result)
btn_equals.grid(row=4,column=2)
btn_equals.config(font=("Times New Roman",14))

btn_div =Button(root,text="/",bg="#4FC0D0",fg="#164B60",width=6,height=2,command=lambda : get_operator("/"))
btn_div.grid(row=4,column=3)
btn_div.config(font=("Times New Roman",14))

credit_label = Label(root, text=" By Anushka Bhasme ",font=("Times New Roman", "10"), bg="#A2FF86", fg="black")
credit_label.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()

