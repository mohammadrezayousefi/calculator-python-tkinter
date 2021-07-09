from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
# ************************ settings **********************************
windows = Tk()
windows.title('calculater')
windows.geometry('350x450')
windows.resizable(width= False , height= False)
my_label_str = ''
#************************** frams **********************************
f_1 = Frame(windows,width=350 , height= 122 , bg = 'gray')
f_1.pack(side = TOP)
f_2 = Frame(windows,width=350 , height= 83 , bg = 'gray')
f_2.pack(side = TOP)
f_3 = Frame(windows,width=350 , height= 83 , bg = 'gray')
f_3.pack(side = TOP)
f_4 = Frame(windows,width=350 , height= 83 , bg = 'gray')
f_4.pack(side = TOP)
f_5 = Frame(windows,width=350 , height= 83 , bg = 'gray')
f_5.pack(side = TOP)
# ****************************** functions ******************************
def press(n):
    global my_label_str 
    my_label_str = my_label_str + n
    label.config(text=my_label_str)

def equal():
    try :
        label.config(text='')
        global my_label_str
        equal = str(eval(my_label_str))
        my_label_str = equal
        label.config(text= equal)
    except :
        messagebox.showerror(title='error', message='something went wrong')
        label.config(text='0')
        my_label_str = ''


def clear():
    label.config(text='0')
    global my_label_str
    my_label_str = ''

#************************** buttons and entries **********************************
label = Label(f_1 ,text = '0',width=40 , height=5 )
label.pack(side= LEFT , padx= 1 , pady= 1)

btn_c = Button(f_1 , text= 'c' , width=6 , height= 5, command = lambda : clear())
btn_c.pack(side=RIGHT , padx= 1 , pady= 1)

b_7 = Button(f_2 , text= '7' , width= 11 , height=5 ,command= lambda : press('7') )
b_7.pack(side=LEFT , padx= 1 , pady= 1 )

b_8 = Button(f_2 , text= '8' , width= 11 , height=5 ,command= lambda : press('8') )
b_8.pack(side=LEFT , padx= 1 , pady= 1 )

b_9 = Button(f_2 , text= '9' , width= 11 , height=5 ,command= lambda : press('9') )
b_9.pack(side=LEFT , padx= 1 , pady= 1 )

b_zarb = Button(f_2 , text= 'X' , width= 11 , height=5,command= lambda : press('*') )
b_zarb.pack(side=LEFT , padx= 1 , pady= 1 )

b_4 = Button(f_3 , text= '4' , width= 11 , height=5 ,command= lambda : press('4') )
b_4.pack(side=LEFT , padx= 1 , pady= 1 )

b_5 = Button(f_3 , text= '5' , width= 11 , height=5,command= lambda : press('5') )
b_5.pack(side=LEFT , padx= 1 , pady= 1 )

b_6 = Button(f_3 , text= '6' , width= 11 , height=5 ,command= lambda : press('6') )
b_6.pack(side=LEFT , padx= 1 , pady= 1 )

b_taghsim = Button(f_3 , text= '/' , width= 11 , height=5 ,command= lambda : press('/') )
b_taghsim.pack(side=LEFT , padx= 1 , pady= 1 )

b_1 = Button(f_4 , text= '1' , width= 11 , height=5 ,command= lambda : press('1') )
b_1.pack(side=LEFT , padx= 1 , pady= 1 )


b_2 = Button(f_4 , text= '2' , width= 11 , height=5 ,command= lambda : press('2') )
b_2.pack(side=LEFT , padx= 1 , pady= 1 )

b_3 = Button(f_4 , text= '3' , width= 11 , height=5 ,command= lambda : press('3') )
b_3.pack(side=LEFT , padx= 1 , pady= 1 )




b_jam = Button(f_4 , text= '+' , width= 11 , height=5 ,command= lambda : press('+') )
b_jam.pack(side=LEFT , padx= 1 , pady= 1 )


b_zero = Button(f_5 , text= '0' , width= 11 , height=5 ,command= lambda : press('0') )
b_zero.pack(side=LEFT , padx= 1 , pady= 1 )

b_poin = Button(f_5 , text= '.' , width= 11 , height=5 ,command= lambda : press('.') )
b_poin.pack(side=LEFT , padx= 1 , pady= 1 )

b_tafrigh = Button(f_5 , text= '-' , width= 11 , height=5 ,command= lambda : press('-') )
b_tafrigh.pack(side=LEFT , padx= 1 , pady= 1 )

b_mosavi = Button(f_5 , text= '=' , width= 11 , height=5 , command= lambda : equal())
b_mosavi.pack(side=LEFT , padx= 1 , pady= 1 )

windows.mainloop()