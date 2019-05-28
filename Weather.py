import tkinter as tk
import json
import requests

HEIGHT = 500
WIDTH = 600

root = tk.Tk()

#7b4946cd71a7aafacc31c5c62a7d930e
#api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
def test_function():
    print("This is the entry")


#For window size
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

##background_image = tk.PhotoImage(file="F:\\Programming\\Python\\My Python Projects\\GUI\\P1.png")
##background_label = tk.Label(root,image=background_image)
##background_label.place(relwidth=1, relheight=1)

#Frame in uper side
frame = tk.Frame(root, bg='#80c1ff', bd='5')
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

#Enter the city name
entry = tk.Entry(frame,font=40)
entry.place(relwidth=0.65, relheight=1)

#button for clicking to give Musam ka haal ;)
button = tk.Button(frame, text='Get Weather',font=40, command= test_function())
button.place(relx=0.7, relwidth=0.3, relheight=1)


#frame in lower side
lower_frame = tk.Frame(root,bg='#80c1ff', bd='10')
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame,text='Vandana Pandey')
label.place(relwidth=1, relheight=1)

root.mainloop()
