import tkinter as tk
import customtkinter
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from dbSQLite import RegDbSQLite

class appGUI(customtkinter.CTk):
    def __init__(self, dataBase=RegDbSQLite('appDB.db')):
        super().__init__()
        self.db = dataBase

        #App Parameters
        self.title('Vehicle Registration Record System')
        self.geometry('1325x650')
        self.config(bg='#73A5C6')
        self.resizable(False, False)

        #Fonts
        self.font1 = ('Arial', 18, 'bold')
        self.font2 = ('Arial', 12, 'bold')

        #Logo
        imgsrc = 'Logo.png'
        img = Image.open(imgsrc)
        imgres = img.resize((225,225),Image.Resampling(3))
        imgtk = ImageTk.PhotoImage(imgres)

        self.logo = Label(self,image=imgtk,bd=0)
        self.logo.photo = imgtk
        self.logo.place(x=5,y=5)

        #Label & Reset for Entry Fields
        self.reg_label = customtkinter.CTkLabel(self, 
                                            text='ENTRY \nFIELDS:',
                                            font=('Arial', 30, 'bold'),
                                            text_color='#000000',
                                            bg_color='#73A5C6')
        self.reg_label.place(x=280,y=30)
        self.clear_button = customtkinter.CTkButton(self,
                                        text='Clear Entry Fields',
                                        command=lambda:self.clear_form(True),
                                        font=self.font2,
                                        text_color='#FFFFFF',
                                        fg_color='#161C25',
                                        hover_color='#40526E',
                                        bg_color='#73A5C6',
                                        border_color='#FF0000',
                                        border_width=2,
                                        cursor='hand2',
                                        corner_radius=15,
                                        width=100)
        self.clear_button.place(x=275,y=120)

        # Registration Entry Field
        self.reg_label = self.newCtkLabel('Registration')
        self.reg_label.place(x=540, y=52)
        self.reg_entry = self.newCtkEntry()
        self.reg_entry.place(x=450, y=30)

        #Classification Entry Field
        self.clsf_label = self.newCtkLabel('Classification')
        self.clsf_label.place(x=835, y=52)
        self.clsf_entryVar = StringVar()
        self.clsf_entryOptions = ['Select Type','Private','Public/Commercial','Cargo/Logistics']
        self.clsf_entry = self.newCtkComboBox(options=self.clsf_entryOptions, 
                                    entryVariable=self.clsf_entryVar)
        self.clsf_entry.place(x=750, y=30)

        #VehicleType Entry Field
        self.type_label = self.newCtkLabel('Vehicle Type')
        self.type_label.place(x=1135, y=52)
        self.type_entryVar = StringVar()
        self.type_entryOptions = ['Select Type','Car/SUV/Van','Jeepney/PUV','Bus','Truck','Train','Aircraft','Watercraft']
        self.type_entry = self.newCtkComboBox(options=self.type_entryOptions, 
                                    entryVariable=self.type_entryVar)
        self.type_entry.place(x=1050, y=30)

        #Brand Entry Field
        self.brand_label = self.newCtkLabel('Brand')
        self.brand_label.place(x=555, y=122)
        self.brand_entry = self.newCtkEntry()
        self.brand_entry.place(x=450, y=100)

        #Model Entry Field
        self.model_label = self.newCtkLabel('Model')
        self.model_label.place(x=855, y=122)
        self.model_entry = self.newCtkEntry()
        self.model_entry.place(x=750, y=100)

        #Owner/Operator Entry Field
        self.op_label = self.newCtkLabel('Owner or Operator')
        self.op_label.place(x=1120, y=122)
        self.op_entry = self.newCtkEntry()
        self.op_entry.place(x=1050, y=100)

        #Label for Action Buttons
        self.act_label = customtkinter.CTkLabel(self, 
                                            text='ACTIONS:',
                                            font=('Arial', 30, 'bold'),
                                            text_color='#000000',
                                            bg_color='#73A5C6')
        self.act_label.place(x=50,y=260)

        #Add Button
        self.add_button = self.newCtkButton(text='Add Vehicle Info',
                                onClickHandler=self.add_entry,
                                fgColor='#05A312',
                                borderColor='#000000',
                                TextColor='#000000',
                                hoverColor='#C0C0C0')
        self.add_button.place(x=25,y=320)

        #Update Button
        self.update_button = self.newCtkButton(text='Update Vehicle Info',
                                    onClickHandler=self.update_entry,
                                    fgColor='#D5B60A',
                                    borderColor='#000000',
                                    TextColor='#000000',
                                    hoverColor='#C0C0C0')
        self.update_button.place(x=25,y=370)

        #Delete Button
        self.delete_button = self.newCtkButton(text='Delete Vehicle Info',
                                    onClickHandler=self.delete_entry,
                                    fgColor='#D0312D',
                                    borderColor='#000000',
                                    TextColor='#000000',
                                    hoverColor='#C0C0C0')
        self.delete_button.place(x=25,y=420)

        #Import Button
        self.import_button = self.newCtkButton(text='Import from CSV',
                                    onClickHandler=self.import_from_csv,
                                    borderColor='#FF0000')
        self.import_button.place(x=25,y=470)

        #Export CSV Button
        self.exportCSV_button = self.newCtkButton(text='Export to CSV',
                                    onClickHandler=self.export_to_csv,
                                    borderColor='#FF0000')
        self.exportCSV_button.place(x=25,y=520)
        
        #Export JSON Button
        self.exportJSON_button = self.newCtkButton(text='Export to JSON',
                                    onClickHandler=self.export_to_json,
                                    borderColor='#FF0000')
        self.exportJSON_button.place(x=25,y=570)

        #Tabular View
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('Treeview', 
                        font=self.font2, 
                        foreground='#000000',
                        background='#E8E8E8',
                        fieldlbackground='#313837')

        self.style.map('Treeview', background=[('selected', '#5A5A5A')])

        self.tree = ttk.Treeview(self, height=15)
        self.tree['columns'] = ('Registration', 'Classification','Vehicle Type', 'Brand', 'Model', 'Owner or Operator')
        self.tree.column('#0', width=0, stretch=tk.NO)
        self.tree.column('Registration', anchor=tk.CENTER, width=5)
        self.tree.column('Classification', anchor=tk.CENTER, width=30)
        self.tree.column('Vehicle Type', anchor=tk.CENTER, width=30)
        self.tree.column('Brand', anchor=tk.CENTER, width=50)
        self.tree.column('Model', anchor=tk.CENTER, width=50)
        self.tree.column('Owner or Operator', anchor=tk.CENTER, width=50)

        self.tree.heading('Registration', text='Registration')
        self.tree.heading('Vehicle Type', text='Vehicle Type')
        self.tree.heading('Classification', text='Classification')
        self.tree.heading('Brand', text='Brand')
        self.tree.heading('Model', text='Model')
        self.tree.heading('Owner or Operator', text='Owner or Operator')

        self.tree.place(x=250, y=175, width=1050, height=450)
        self.tree.bind('<ButtonRelease>', self.read_display_data)

        self.add_to_treeview()

    #Label Widget
    def newCtkLabel(self, text = 'CTK Label'):
        widget_Font=self.font2
        widget_TextColor='#000000'
        widget_BgColor='#73A5C6'
        widget = customtkinter.CTkLabel(self, 
                                    text=text,
                                    font=widget_Font, 
                                    text_color=widget_TextColor,
                                    bg_color=widget_BgColor)
        return widget

    #Entry Field Widget
    def newCtkEntry(self, text = 'CTK Label'):
        widget_Font=self.font1
        widget_TextColor='#000000'
        widget_FgColor='#FFFFFF'
        widget_BgColor='#73A5C6'
        widget_BorderColor='#5A5A5A'
        widget_BorderWidth=2
        widget_Width=250
        widget = customtkinter.CTkEntry(self,
                                    font=widget_Font,
                                    text_color=widget_TextColor,
                                    fg_color=widget_FgColor,
                                    bg_color=widget_BgColor,
                                    border_color=widget_BorderColor,
                                    border_width=widget_BorderWidth,
                                    width=widget_Width)
        return widget

    #Drop-Down Field Widget
    def newCtkComboBox(self, options=['DEFAULT', 'OTHER'], entryVariable=None):
        widget_Font=self.font1
        widget_TextColor='#000000'
        widget_FgColor='#FFFFFF'
        widget_BgColor='#73A5C6'
        widget_DropdownFgColor='#FFFFFF'
        widget_DropdownTextColor='#000000'
        widget_DropdownHoverColor='#C0C0C0'
        widget_ButtonColor='#5A5A5A'
        widget_ButtonHoverColor=''
        widget_BorderColor='#5A5A5A'
        widget_BorderWidth=2
        widget_Width=250
        widget_Options=options
        widget = customtkinter.CTkComboBox(self,
                                        font=widget_Font,
                                        text_color=widget_TextColor,
                                        fg_color=widget_FgColor,
                                        bg_color=widget_BgColor,
                                        dropdown_fg_color=widget_DropdownFgColor,
                                        dropdown_text_color=widget_DropdownTextColor,
                                        dropdown_hover_color=widget_DropdownHoverColor,
                                        button_color=widget_ButtonColor,
                                        border_color=widget_BorderColor,
                                        width=widget_Width,
                                        variable=entryVariable,
                                        values=options,
                                        state='readonly')
        widget.set(options[0]) #set default to 1st option
        return widget

    #Button Widget
    def newCtkButton(self, text = 'CTK Button', onClickHandler=None, fgColor='#161C25', hoverColor='#40526E', bgColor='#73A5C6', borderColor='#5A5A5A',TextColor='#FFFFFF'):
        widget_Font=self.font1
        widget_TextColor=TextColor
        widget_FgColor=fgColor
        widget_HoverColor=hoverColor
        widget_BackgroundColor=bgColor
        widget_BorderColor=borderColor
        widget_BorderWidth=2
        widget_Cursor='hand2'
        widget_CornerRadius=15
        widget_Width=200
        widget_Function=onClickHandler
        widget = customtkinter.CTkButton(self,
                                        text=text,
                                        command=widget_Function,
                                        font=widget_Font,
                                        text_color=widget_TextColor,
                                        fg_color=widget_FgColor,
                                        hover_color=widget_HoverColor,
                                        bg_color=widget_BackgroundColor,
                                        border_color=widget_BorderColor,
                                        border_width=widget_BorderWidth,
                                        cursor=widget_Cursor,
                                        corner_radius=widget_CornerRadius,
                                        width=widget_Width)
        return widget

    #Actions
    def add_to_treeview(self):
        vehicles = self.db.fetch_vehicles()
        self.tree.delete(*self.tree.get_children())
        for vehicle in vehicles:
            print(vehicle)
            self.tree.insert('', END, values=vehicle)

    def clear_form(self, *clicked):
        if clicked:
            self.tree.selection_remove(self.tree.focus())
            self.tree.focus('')
        self.reg_entry.delete(0, END)
        self.clsf_entryVar.set('Select Type')
        self.type_entryVar.set('Select Type')
        self.brand_entry.delete(0, END)
        self.model_entry.delete(0, END)
        self.op_entry.delete(0, END)

    def read_display_data(self, event):
        selected_item = self.tree.focus()
        if selected_item:
            row = self.tree.item(selected_item)['values']
            self.clear_form()
            self.reg_entry.insert(0, row[0])
            self.clsf_entry.set(row[1])
            self.type_entryVar.set(row[2])
            self.brand_entry.insert(0, row[3])
            self.model_entry.insert(0, row[4])
            self.op_entry.insert(0, row[5])
        else:
            pass

    def add_entry(self):
        reg=self.reg_entry.get()
        clsf=self.clsf_entry.get()
        type=self.type_entryVar.get()
        brand=self.brand_entry.get()
        model=self.model_entry.get()
        operator=self.op_entry.get()
        if not (reg and clsf and type and brand and model and operator):
            messagebox.showerror('Error', 'Please fill out all entry fields')
        elif clsf == 'Select Type':
            messagebox.showerror('Error', 'Please specify vehicle classification')
        elif type == 'Select Type':
            messagebox.showerror('Error', 'Please specify vehicle type')
        elif self.db.reg_exists(reg):
            messagebox.showerror('Error', 'Registration already exists')
        else:
            self.db.insert_vehicle(reg, clsf, type, brand, model, operator)
            self.add_to_treeview()
            self.clear_form()
            messagebox.showinfo('Success', 'Registration has been successfully added')

    def delete_entry(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror('Error', 'Select a registration to delete')
        else:
            reg = self.reg_entry.get()
            self.db.delete_vehicle(reg)
            self.add_to_treeview()
            self.clear_form()
            messagebox.showinfo('Success', 'Registration has been successfully deleted')

    def update_entry(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror('Error', 'Select a registration to update')
        else:
            reg=self.reg_entry.get()
            clsf=self.clsf_entry.get()
            type=self.type_entryVar.get()
            brand=self.brand_entry.get()
            model=self.model_entry.get()
            operator=self.op_entry.get()
            self.db.update_vehicle(reg, clsf, type, brand, model, operator)
            self.add_to_treeview()
            self.clear_form()
            messagebox.showinfo('Success', 'Registration has been successfully updated')

    def import_from_csv(self):
        csvFile = askopenfilename(filetypes=[('CSV Files','*.csv')])
        self.db.import_csv(csvFile)
        self.add_to_treeview()
        messagebox.showinfo('Success', f'Data from:\n \n{csvFile}\n \nhas been imported successfully')

    def export_to_csv(self):
        self.db.export_csv()
        messagebox.showinfo('Success', 'Data has been successfully exported to vehicles.csv')

    def export_to_json(self):
        self.db.export_json()
        messagebox.showinfo('Success', 'Data has been successfully exported to vehicles.json')