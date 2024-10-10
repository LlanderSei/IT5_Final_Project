import customtkinter as ctk

# Create a customTkinter application
app = ctk.CTk()

# Set the title and size of the window
app.title("Dropdown Example")
app.geometry("400x300")

# Define a function to be called when the dropdown value changes
def dropdown_callback(choice):
    print("Selected:", choice)

# Create a dropdown variable
dropdown_var = ctk.StringVar(value="Select an option")  # Default value

# Create a dropdown menu (combobox)
dropdown = ctk.CTkOptionMenu(
    app,
    variable=dropdown_var,  # Use the variable parameter correctly
    values=["Option 1", "Option 2", "Option 3"],  # Pass options as a list
    command=dropdown_callback
)
dropdown.pack(pady=20)

# Run the application
app.mainloop()
