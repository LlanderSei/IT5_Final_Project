import tkinter as tk
import customtkinter as ctk  
from tkinter import ttk
from PIL import Image
import os
class Breakdown:
	def __init__(self, parent, SP_MWF):
		self.__parent = parent
		self.SPMWF = SP_MWF
		self.__root = ctk.CTkToplevel(self.__parent.GET_TL_Root())
		self.__root.protocol("WM_DELETE_WINDOW", self.TL_PROTOCOL_Breakdown)
		self.__root.withdraw()
		self.__INSTANTIATE_VARS()
		self.Main_Window()

	def __INSTANTIATE_VARS(self):
		self.__BKDW_ProfileName = ctk.StringVar(value=0)
		self.__BKDW_Allowance = ctk.DoubleVar(value=0)
		self.__BKDW_TotalNeeds = ctk.DoubleVar(value=0)
		self.__BKDW_TotalWants = ctk.DoubleVar(value=0)
		self.__BKDW_BudgetNeeds = ctk.DoubleVar(value=0)
		self.__BKDW_BudgetWants = ctk.DoubleVar(value=0)
		self.__BKDW_NeedsRemaining = ctk.DoubleVar(value=0)
		self.__BKDW_WantsRemaining = ctk.DoubleVar(value=0)
		self.__BKDW_Savings = ctk.DoubleVar(value=0)
		self.__BKDW_TotalExpenses = ctk.DoubleVar(value=0)
		self.__BKDW_SavingsRemaining = ctk.DoubleVar(value=0)

	def CALL_BKDW_VARIABLES(self, VARIABLE):
		match VARIABLE:
			case 'PROFILENAME': return self.__BKDW_ProfileName
			case 'ALLOWANCE': return self.__BKDW_Allowance
			case 'TOTALNEEDS': return self.__BKDW_TotalNeeds
			case 'TOTALWANTS': return self.__BKDW_TotalWants
			case 'BUDGETNEEDS': return self.__BKDW_BudgetNeeds
			case 'BUDGETWANTS': return self.__BKDW_BudgetWants
			case 'SAVINGS': return self.__BKDW_Savings
	
	def CALL_BKDW_BUDGETCALCULATIONS(self):
		NEEDSREMAINING = self.__BKDW_BudgetNeeds.get() - self.__BKDW_TotalNeeds.get()
		WANTSREMAINING = self.__BKDW_BudgetWants.get() - self.__BKDW_TotalWants.get()
		TOTALEXPENSES = self.__BKDW_TotalNeeds.get() + self.__BKDW_TotalWants.get()
		ALLBUDGETREMAINING = self.__BKDW_Allowance.get() - TOTALEXPENSES

		self.__BKDW_NeedsRemaining.set(NEEDSREMAINING)
		self.__BKDW_WantsRemaining.set(WANTSREMAINING)
		self.__BKDW_TotalExpenses.set(TOTALEXPENSES)
		self.__BKDW_SavingsRemaining.set(ALLBUDGETREMAINING)
		
		self.UPDATE_TABLE_DETAILS()

	def UPDATE_TABLE_DETAILS(self):
		self.__category_table_display.item('cr1', values=('Needs', f'{self.__BKDW_TotalNeeds.get()}', f'{self.__BKDW_BudgetNeeds.get()}', f'{self.__BKDW_NeedsRemaining.get()}'))
		self.__category_table_display.item('cr2', values=('Wants', f'{self.__BKDW_TotalWants.get()}', f'{self.__BKDW_BudgetWants.get()}', f'{self.__BKDW_WantsRemaining.get()}'))

		self.__savings_table_display.item('sr1', values=('Savings:', f'{self.__BKDW_Savings.get()}'))
		self.__savings_table_display.item('sr2', values=('Total Expenses:', f'{self.__BKDW_TotalExpenses.get()}'))
		self.__savings_table_display.item('sr3', values=('Allowance Remaining:', f'{self.__BKDW_SavingsRemaining.get()}'))

	def TL_Breakdown_Show(self):
		self.SPMWF.UPDATE_Breakdown_Details()
		self.__root.deiconify()
		self.__root.after(50, lambda: self.__root.state('zoomed'))

	def TL_PROTOCOL_Breakdown(self):
		self.__root.withdraw()

	def TL_Get_Root_Breakdown(self):
		return self.__root

	def __get_root(self):
		return self.__root
	
	def __get_main_window_width(self):
		return self.__get_frame_width(0.8)
	
	def __get_main_window_height(self):
		return self.__get_frame_height(0.8)
	
	def __get_frame_width(self, percentage):
		return int(self.__root.winfo_screenwidth() * percentage)
	
	def __get_frame_height(self, percentage):
		return int(self.__root.winfo_screenheight() * percentage)
	
	def __get_mainframe_width(self, percentage):
		return int(self.__main_frame.winfo_screenwidth() * percentage)
	
	def __get_mainframe_height(self, percentage):
		return int(self.__main_frame.winfo_screenheight() * percentage)
	
	def __get_navigation_frame_width(self, percentage):
		return int(self.__navigation_header.winfo_screenheight() * percentage)
	
	def __on_close(self):
		self.__parent.quit()
		self.__parent.destroy()
		self.__root.destroy()
					
	def Main_Window(self):
		self.__root.title("Expense Tracker/Breakdown")
		# self.__root.after(50, lambda: self.__get_fullscreen())
		self.__root.configure(fg_color = "black")
		self.__root.minsize(self.__get_main_window_width(),self.__get_main_window_height())
		self.__main_frames()

	def __get_fullscreen(self):
		return self.__root.state("zoomed")

	def __main_frames(self):
		self.__set_main_frame()
		self.__navigation_frames()
		self.__category_table_frames()
		self.__savings_table_frames()
	
	def __get_main_frame_width(self):
		return self.__get_frame_width(0.8)
	
	def __get_main_frame_height(self):
		return self.__get_frame_height(0.8)
	
	def __set_main_frame(self):
		self.__main_frame = ctk.CTkFrame(self.__get_root(), width=self.__get_main_frame_width(), height= self.__get_main_frame_height(), fg_color="#696969")
		self.__main_frame.place(relx = 0.5, rely=0.5, anchor= "center")

	def __get_main_frame(self):
		return self.__main_frame
	
	def __get_navigation_frame(self):
		return self.__navigation_header
	
	def __get_category_table_frame(self):
		return self.__category_table
	
	def __get_savings_table_frame(self):
		return self.__saving_table
	
	def __navigation_width(self):
		return self.__get_mainframe_width(0.8)
	
	def __navigation_height(self):
		return self.__get_mainframe_height(0.1)
	
	def __category_width(self):
		return self.__get_mainframe_width(0.8)
	
	def __category_height(self):
		return self.__get_mainframe_height(0.3)
	
	def __saving_width(self):
		return self.__get_mainframe_width(0.8)
	
	def __saving_height(self):
		return self.__get_mainframe_height(0.3)
	
	def __username_button_width(self):
		return self.__get_navigation_frame_width(0.35)
	
	def __list_button_width(self):
		return self.__get_navigation_frame_width(0.275)
	
	def __breakdown_button_width(self):
		return self.__get_navigation_frame_width(0.275)
	
	def __navigation_frames(self):
		self.__navigation_header = ctk.CTkFrame(self.__get_main_frame(), width=self.__navigation_width(), height= self.__navigation_height(), fg_color="#696969")
		self.__navigation_header.place(relx = 0.5, rely = 0.025, anchor="n")
		self.__usernamebutton()
		self.__listbutton()
		self.__breakdownbutton()

	def __category_table_frames(self):
		self.__category_table = ctk.CTkFrame(self.__get_main_frame(), width=self.__category_width(), height= self.__category_height(), fg_color="#696969")
		self.__category_table.place(relx = 0.5, rely = 0.4, anchor="center")
		self.__category()

	def __savings_table_frames(self):
		self.__saving_table = ctk.CTkFrame(self.__get_main_frame(), width=self.__saving_width(), height= self.__saving_height(), fg_color="#696969")
		self.__saving_table.place(relx = 0.5, rely = 0.6, anchor="n")
		self.__savings()
	
	def __get_image_logo(self):
		return Image.open(self.GET_RELEVANT_PATHDIR('assets/logo.png')).convert("RGBA")
	
	def __usernamebutton(self):
		self.__name_pht = ctk.CTkImage(light_image = self.__get_name_logo(), dark_image = self.__get_name_logo(), size=(50,50))

		self.__username_button = ctk.CTkButton(self.__get_navigation_frame(),image = self.__name_pht, text="Name", textvariable=self.__BKDW_ProfileName, width= self.__username_button_width(), height= 60, font=("Poppins",23, "bold"),fg_color="#2c2c2c", corner_radius= 25)
		self.__username_button.place(relx=0.25, rely=0.5, anchor="center")
		self.__photo = ctk.CTkImage(light_image= self.__get_image_logo(),
									dark_image= self.__get_image_logo(),
									size=(70, 70))
		self.__photoplacement = ctk.CTkLabel(self.__get_navigation_frame(), image=self.__photo, text="", fg_color="#696969", corner_radius=10)
		self.__photoplacement.place(relx= 0.05, rely= 0.5, anchor="center")

	def __get_name_logo(self):
		return Image.open(self.GET_RELEVANT_PATHDIR('assets/profile2.png')).convert("RGBA")
	
	def __listbutton(self):
		self.__list_pht = ctk.CTkImage(light_image = self.__get_list_logo(), dark_image = self.__get_list_logo(), size=(40,40))

		self.__list_button = ctk.CTkButton(self.__get_navigation_frame(), text="List",image = self.__list_pht, width= self.__list_button_width(),  height= 50, font=("Poppins",23, "bold"), fg_color="#696969",border_width = 3,border_color = "#000000",  corner_radius = 25)
		self.__list_button.place(relx=0.6, rely=0.5, anchor="center")

	def __get_list_logo(self):
		return Image.open(self.GET_RELEVANT_PATHDIR('assets/list.png')).convert("RGBA")
	
	def __breakdownbutton(self):
		self.__breakdown_pht = ctk.CTkImage(light_image = self.__get_breakdown_logo(), dark_image = self.__get_breakdown_logo(), size=(40,40))

		self.__breakdown_button = ctk.CTkButton(self.__get_navigation_frame(), image = self.__breakdown_pht, text="Breakdown",width= self.__breakdown_button_width(),  height= 50, font=("Poppins",23, "bold"), fg_color="#696969",border_width = 3,border_color = "#000000",  corner_radius = 25)
		self.__breakdown_button.place(relx=0.85, rely=0.5, anchor="center")

	def __get_breakdown_logo(self):
		return Image.open(self.GET_RELEVANT_PATHDIR('assets/breakdown.png')).convert("RGBA")
	
	def __category(self):
		self.__style_category = ttk.Style()
		self.__style_category.configure("Category.Treeview", font=("Poppins", 20), bordercolor="Black", borderwidth=5, rowheight=130, background="#696969", fieldbackground="#696969", foreground="black")
		self.__style_category.configure("Category.Treeview.Heading", font=("Poppins", 25, "bold"),
																		padding=(5,10),
																		bordercolor="Black",
																		borderwidth=2,
																		foreground="black",
																		)
		self.__category_table_display = ttk.Treeview(self.__get_category_table_frame(), columns= ('Category', 'Total', 'Budget', 'Remaining'), show= 'headings', height=2, style="Category.Treeview")
		self.__category_table_display.heading('Category', text= 'Category')
		self.__category_table_display.heading('Total', text= 'Total')
		self.__category_table_display.heading('Budget', text= 'Budget')
		self.__category_table_display.heading('Remaining', text= 'Remaining')
		self.__category_table_display.column('Category', width= 100, stretch= True, anchor="center")
		self.__category_table_display.column('Total', width= 100, stretch= True, anchor="center")
		self.__category_table_display.column('Budget', width= 100, stretch= True, anchor="center")
		self.__category_table_display.column('Remaining', width= 100, stretch= True, anchor="center")
		self.__category_table_display.insert('','end', iid='cr1', values=('Needs',f'{self.__BKDW_TotalNeeds.get()}', f'{self.__BKDW_BudgetNeeds.get()}', f'{self.__BKDW_NeedsRemaining.get()}'))
		self.__category_table_display.insert('','end', iid='cr2', values=('Wants', f'{self.__BKDW_TotalWants.get()}', f'{self.__BKDW_BudgetWants.get()}', f'{self.__BKDW_WantsRemaining.get()}'))
		self.__category_table_display.place(relx=0.5, rely=0.5, relheight=1, relwidth= 1,anchor="center")
		self.__category_table_display.bind("<ButtonPress-1>", self.handle_click_category)


	def handle_click_category(self, event):
		"""Handle the click event for both preventing drag and clearing selection."""
		# Check if the click is on a separator (to prevent dragging)
		if self.__category_table_display.identify_region(event.x, event.y) == "separator":
			return "break"  # Prevent dragging if clicked on a separator

		# Handle clearing selection on double click
		selected_item = self.__category_table_display.selection()
		current_focus = self.__category_table_display.focus()

		if selected_item:
			if current_focus == selected_item[0]:
				# Deselect if the same item is clicked again
				self.__category_table_display.selection_remove(selected_item[0])
				self.__category_table_display.selection_clear()
				return "break"  # Prevent any further processing

		# Update the last clicked item
		self.last_clicked_item = current_focus  # Set this if needed for further logic
	def handle_click_save(self, event):
		"""Handle the click event for both preventing drag and clearing selection."""
		# Check if the click is on a separator (to prevent dragging)
		if self.__savings_table_display.identify_region(event.x, event.y) == "separator":
			return "break"  # Prevent dragging if clicked on a separator

		# Handle clearing selection on double click
		selected_item = self.__savings_table_display.selection()
		current_focus = self.__savings_table_display.focus()

		if selected_item:
			if current_focus == selected_item[0]:
				# Deselect if the same item is clicked again
				self.__savings_table_display.selection_remove(selected_item[0])
				self.__savings_table_display.selection_clear()
				return "break"  # Prevent any further processing

		# Update the last clicked item
		self.last_clicked_item = current_focus  # Set this if needed for further logic
	def __savings(self):
		self.__style_savings = ttk.Style()
		self.__style_savings.configure("Savings.Treeview", font=("Poppins", 20), rowheight=85, bordercolor="Black", borderwidth=2,background="black", fieldbackground="black", foreground="white")
		self.__style_savings.configure("Savings.Treeview.Heading", font=("Poppins", 25, "bold"),bordercolor="Black", borderwidth=2, padding=(5,10))
		self.__savings_table_display = ttk.Treeview(self.__get_savings_table_frame(), columns= ('Savings', 'Amount'), show= 'headings', height=3, style="Savings.Treeview")
		self.__savings_table_display.heading('Savings', text= 'Savings')
		self.__savings_table_display.heading('Amount', text= 'Amount')
		self.__savings_table_display.column('Savings', width= 100, stretch= True,anchor="center")
		self.__savings_table_display.column('Amount', width= 100, stretch= True, anchor="center")
		self.__savings_table_display.place(relx=0.5, rely=0.5, relheight=1, relwidth= 1,anchor="center")
		self.__savings_table_display.insert('','end', iid='sr1', values=('Savings:', f'{self.__BKDW_Savings.get()}'))
		self.__savings_table_display.insert('','end', iid='sr2', values=('Total Expenses:', f'{self.__BKDW_TotalExpenses.get()}'))
		self.__savings_table_display.insert('','end', iid='sr3', values=('Allowance Remaining:', f'{self.__BKDW_SavingsRemaining.get()}'))
		self.__savings_table_display.bind("<ButtonPress-1>", self.handle_click_save)

	def GET_RELEVANT_PATHDIR(self, IMAGENAME):
		path = os.path.dirname(os.path.abspath(__file__))
		return os.path.join(path, IMAGENAME)