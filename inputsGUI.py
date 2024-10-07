from customtkinter import *
import customtkinter as ctk

window = ctk.CTk()

# Get the screen dimensions of the unit
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set window dimensions as a percentage of the screen size, adopting to the screen of the user
width = int(screen_width * 0.9)   # 90% of screen width
height = int(screen_height * 0.9)  # 90% of screen height

x = (screen_width - width) // 2
y = (screen_height - height) // 2

window.geometry(f"{width}x{height}+{x}+{y}")

window.title("2nd GUI")

btnWidth = 250
btnHeight = 100
pad_x = 50
pad_y = 50

#frames for the table, entryboxes, and labels
left_frame = ctk.CTkFrame(window, width = 800, height = 600, fg_color = "#FF0000")
left_frame.place( x = 80, y = 170)

right_frame = ctk.CTkFrame(window, width = 800, height = 600, fg_color = "#0000FF")
right_frame.place( x = 850, y = 170)

#frame for the title of the 2nd Gui
frame_title = ctk.CTkFrame(window,width = 500, height = 100, fg_color = "#A020F0")
frame_title.place( x = 80 , y = 50)



#top buttons for sets of gui
topBtn = ["List", "Breakdown", "Budgeting"]
for i, topBtn_texts in enumerate(topBtn):
    
    topBtns = ctk.CTkButton(window, text = topBtn_texts, width = btnWidth, height = btnHeight, corner_radius = 40, font = ("Poppins", 20, "bold"), fg_color = "#808080", border_color ="#000000", border_width = 5 , hover_color = "#A020F0")
    topBtns.place( x = 840 + (btnWidth + 30) * i, y = 50)


left_bottomBtn = ["Log Out", "View Profile"]
for j, left_bottom_texts in enumerate(left_bottomBtn):
    
    bottom_leftBtns = ctk.CTkButton(window, text = left_bottom_texts, width = btnWidth, height = btnHeight, corner_radius = 40, font = ("Poppins", 20, "bold"), fg_color = "#808080", border_color ="#000000", border_width = 5 , hover_color = "#A020F0")
    bottom_leftBtns.place( x = 200 + (btnWidth + 30) * j, y = 800)


right_bottomBtn = [ "Add", "Delete"]
for k, right_buttom_texts in enumerate(right_bottomBtn):
    bottom_rightBtns = ctk.CTkButton(window, text = right_buttom_texts, width = btnWidth, height = btnHeight, corner_radius = 40, font = ("Poppins", 20, "bold"), fg_color = "#808080", border_color ="#000000", border_width = 5 , hover_color = "#A020F0")
    bottom_rightBtns.place( x = 1000 + (btnWidth + 30) * k, y = 800)


#left labels
left_frame_labels = ["Add Savings:", "Savings:", "Stipend:", "Month of Termination:"]

for l, labelsLf in enumerate(left_frame_labels):
    leftLbl = ctk.CTkLabel(left_frame, text = labelsLf, width = 200, height = 50, corner_radius = 40, font = ("Poppins", 20, "bold"), fg_color = "#000000")
    leftLbl.place( x = pad_x, y = pad_y + l * 100)
    
    entryBox = ctk.CTkEntry(left_frame, width = 400, height = 50)
    entryBox.place( x = pad_x + 300, y = pad_y + l * 100)

#right frame table
right_frame_tableLbl = ["Category", "Due Dates"]

for m, column in enumerate(right_frame_tableLbl):
    table_rightframeLbl = ctk.CTkLabel(right_frame, text=column, width=150, height=50, corner_radius = 40, font = ("Poppins", 20, "bold"), fg_color = "#000000")
    table_rightframeLbl.place( x = 170 + m * 300, y = 30)



window.mainloop()