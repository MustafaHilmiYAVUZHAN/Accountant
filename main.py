from customtkinter import *
from customtitlebar import *
from pywinstyles import apply_style
from hPyT import all_stuffs,maximize_minimize_button,title_bar_text_color,rainbow_border,border_color
from CTkMenuBar import CTkTitleMenu as TitleMenu
from CTkMenuBar import CustomDropdownMenu as DropdownMenu
from CTkMessagebox import CTkMessagebox as Messagebox
from DBManager import PasswordManager,ProductRecords
from CTkTableMini import CTkTableMini as CTkTable
from CTkTable import CTkTableMini as CTkTablePro
from time import time
from os import path
from CTkCalender import CTkCalender
from PIL import Image
from excelCreater import excelCreater as ECreater

class new_toplevel(CTkToplevel):
    def __init__(self,all_hide : bool = False,topmost : bool = False):
        super().__init__()
        set_default_color_theme(path.join(path.dirname(path.realpath(__file__)), 'assets\\extreme.json'))
        self.configure(takefocus=False)
        self.attributes("-topmost", True)
        self.resizable(0,0)
        if not topmost:
            self.attributes("-topmost", False)
        if all_hide:
            all_stuffs.hide(self)
        else:
            maximize_minimize_button.hide(self)
        apply_style(self,"acrylic")
        print(self.winfo_name())
#################### 
class passwords_window:
    def __init__(self,DataForAccess=None) :
        self.toplevel=CTkToplevel()
        if DataForAccess is not None:
            self.DataForAccess=DataForAccess
        else:
            self.DataForAccess=PasswordManager()
        self.toplevel.geometry("175x150")
        self.toplevel.resizable(0,0)
        self.toplevel.title("Access")
        maximize_minimize_button.hide(self.toplevel)
        title_bar_text_color.set(self.toplevel,"#ff0000")

        border_color.set(self.toplevel,"#ff0000")
        apply_style(self.toplevel,"acrylic")
        self.toplevel.protocol("WM_DELETE_WINDOW",self.withdraw)
        self.font=CTkFont(size=12)
        self.name_list=[item for tup in self.DataForAccess.list_name() for item in tup]
        print(self.name_list)
        self.nameLabel=CTkLabel(self.toplevel,text="Name          :",font=self.font)
        self.nameLabel.place(rely=0.1,relx=0.01,relwidth=0.4,relheight=0.12)
        self.nameComboBox=CTkComboBox(self.toplevel,bg_color="black",values=self.name_list,font=self.font)
        self.nameComboBox.place(rely=0.1,relx=0.45,relwidth=0.5,relheight=0.12)
        self.passwordLabel=CTkLabel(self.toplevel,text="Password   :",font=self.font)
        self.passwordLabel.place(rely=0.4,relx=0.01,relwidth=0.4,relheight=0.12)
        self.passwordEnrty=CTkEntry(self.toplevel,bg_color="black",show="*",font=self.font)
        self.passwordEnrty.place(rely=0.4,relx=0.45,relwidth=0.5,relheight=0.12)
        self.forSave=CTkButton(self.toplevel,text="Save",bg_color="black",command=self.save,font=self.font)
        self.forSave.place(rely=0.7,relx=0.1,relwidth=0.4,relheight=0.15)
        self.forDelete=CTkButton(self.toplevel,text="delete",hover_color="#ff0000",bg_color="black",font=self.font,command=self.delete)
        self.forDelete.place(rely=0.7,relx=0.6,relwidth=0.3,relheight=0.15)
        self.toplevel.mainloop()####################
    def withdraw(self):
        print("doğru")
        self.toplevel.withdraw()
        print("heelllooo")
        market_window("main")
    def save(self):
        password=self.passwordEnrty.get()
        name=self.nameComboBox.get()
        if self.DataForAccess.find_data(name) is None:
            
            self.DataForAccess.insert_data(name,password)
            self.updateNameBox()
            
        elif self.DataForAccess.find_data(name)[1]!=password:
            self.DataForAccess.delete_data(name)
            self.DataForAccess.insert_data(name,password)
        else:
            Messagebox(title="This is same",message="These are same password and same name")
        print(f"Name : {name}         PASSWORD: {password}")
    def delete(self):
        name=self.nameComboBox.get()
        self.DataForAccess.delete_data(name)
        self.updateNameBox()
    def updateNameBox(self):
        self.name_list=[item for tup in self.DataForAccess.list_name() for item in tup]
        self.nameComboBox.configure(values=self.name_list)
        self.nameComboBox.update()
class window_for_access:
    def __init__(self):
        self.window=CTk()
        
        #title_bar.hide(self.window)
        #self.window.mainloop()####################
        set_default_color_theme("assets\\extreme.json")
        self.window.geometry("300x200")
        self.window.resizable(0,0)
        self.window.title("Access")
        all_stuffs.hide(self.window)
        
        apply_style(self.window,"acrylic")
        
        self.nameLabel=CTkLabel(self.window,text="Name          :")
        self.nameLabel.place(rely=0.2,relx=0.05,relwidth=0.252,relheight=0.15)
        self.nameEntry=CTkEntry(self.window,bg_color="black")
        self.nameEntry.place(rely=0.2,relx=0.45,relwidth=0.5,relheight=0.15)
        self.passwordLabel=CTkLabel(self.window,text="Password   :")
        self.passwordLabel.place(rely=0.4,relx=0.05,relwidth=0.252,relheight=0.15)
        self.passwordEnrty=CTkEntry(self.window,bg_color="black",show="*")
        self.passwordEnrty.place(rely=0.4,relx=0.45,relwidth=0.5,relheight=0.15)
        self.ButtonforAccess=CTkButton(self.window,text="Login",bg_color="black",command=self.loginControl)
        self.ButtonforAccess.place(rely=0.67,relx=0.3,relwidth=0.4,relheight=0.15)
        
        """
        Burada data okunur ve isim listesi ve şifreler çekilir
        eğer boş ise oluşturulur
        main : main
        """

        self.DataForAccess=PasswordManager()
        if self.DataForAccess.find_data("main")[1]=="main":
            Messagebox(title="Defualt Main access",message="name             : main\npassword     : main\n\nYou should change these")
            
        self.window.mainloop()####################
    def loginControl(self):
        password=self.passwordEnrty.get()
        name=self.nameEntry.get()
        print(f"Name : {name}         PASSWORD: {password}")
        if self.DataForAccess.find_data(name) is None:
            Messagebox(title="Wrong NAME",message="Your name is not on the list")
        elif self.DataForAccess.find_data(name)[1]!=password:
            Messagebox(title="Wrong PASSWORD",message="Your PASSWORD is not correct")
        else:
            if name=="main" and password=="main":
                self.window.withdraw()
                passwords_window(self.DataForAccess)
            else:
                #Messagebox(title="Succesfull your Access",message="Everythin is True")
                self.window.withdraw()
                market_window(name)
                self.window.destroy()
            

class market_window:
    def __init__(self,name):
        self.window=new_toplevel()
        self.window.iconify()
        
        self.window.geometry("360x360+20+20")#900

        self.name=name
        self.window.title(f"User: {name}")
        maximize_minimize_button.hide(self.window)
        title_bar_text_color.set(self.window,"#aaaaaa")
        apply_style(self.window,"acrylic")
        self.window.protocol("WM_DELETE_WINDOW",lambda:Messagebox(title="Exit",message="Do you want exit",option_1="Exit",option_1_func=lambda:exit(),option_2="cancel",option_2_func=lambda:print("",end=""),option_3="Change user",option_3_func=lambda:(self.window.withdraw(),window_for_access())))
        self.TitleMenu=TitleMenu(master=self.window,x_offset=115)
        self.TitleMenu.add_cascade(text="Change user",command=lambda:(self.window.withdraw(),self.TitleMenu.destroy(),window_for_access(),self.window.destroy()))#{"height":20,"width":15,"fg_color":"#505050","bg_color":"#000001"})
        if name=="main":
            self.TitleMenu.add_cascade(text="Change user's data",command=lambda:(self.window.withdraw(),self.TitleMenu.destroy(),passwords_window(),self.window.destroy()))
        self.add_image = CTkImage(Image.open("assets\\icons\\add_shopping_cart.png"), size=(70, 70))
        self.record_image = CTkImage(Image.open("assets\\icons\\description.png"), size=(70, 70))
        self.sell_image = CTkImage(Image.open("assets\\icons\\shopping.png"), size=(70, 70))
        self.Add_product = CTkButton(
            self.window,
            text="",
            width=160,
            height=160,
            command=lambda: (self.window.withdraw(), Add_product_screen(self.window, self.ProductRecords,name)),
            bg_color="black",
            fg_color="black",
            border_color="white",
            border_width=1,
            hover_color="#111111",
            image=self.add_image
        )
        self.Add_product.grid(row=0, column=0, pady=10, padx=10)

        self.Record = CTkButton(
            self.window,
            width=160,
            text="",
            height=160,
            command=lambda: (self.window.withdraw(), Record_screen(self.window, self.name, self.ProductRecords,main=True)),
            bg_color="black",
            fg_color="black",
            border_color="white",
            border_width=1,
            hover_color="#111111",
            image=self.record_image
        )
        self.Record.grid(row=0, column=1, pady=10, padx=10)

        self.Sell = CTkButton(
            self.window,
            width=160,
            text="",
            height=160,
            command=lambda: (self.window.withdraw(), Sell_screen(self.window, self.name, self.ProductRecords)),
            bg_color="black",
            fg_color="black",
            border_color="white",
            border_width=1,
            hover_color="#111111",
            image=self.sell_image
        )
        self.Sell.grid(row=1, column=0, pady=10, padx=10)

        self.ProductRecords=ProductRecords()
        self.window.deiconify()
        self.window.mainloop()####################

    
        
    
        



class Add_product_screen(new_toplevel):
    def __init__(self, master, ProductRecords,user):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", lambda: (master.deiconify(), self.withdraw(), self.title_menu.withdraw(), self.title_menu.destroy()))
        self.geometry("350x435")
        self.title("Add_product")
        self.user=user
        self.ProductRecords = ProductRecords
        
        self.ProductNameText = CTkLabel(self, text="Product name :")
        self.ProductNameComboBox = CTkComboBox(self, bg_color="black", width=220, values=self.ProductRecords.get_unique_product_names())
        self.BarCodeText = CTkLabel(self, text="Barcode :")
        self.BarCodeEntry = CTkEntry(self, bg_color="black", width=220)
        self.BarCodeEntryFake = CTkLabel(self, text_color="#888888", text=" ", anchor="w", fg_color=ThemeManager.theme["CTkEntry"]["fg_color"], corner_radius=ThemeManager.theme["CTkComboBox"]["corner_radius"], width=220)
        self.PurchasePriceText = CTkLabel(self, text="Purchase Price :")
        self.PurchasePriceEntry = CTkEntry(self, bg_color="black", width=220)
        self.UnitText = CTkLabel(self, text="Unit :")
        self.UnitComboBox = CTkComboBox(self, bg_color="black", width=220, values=self.ProductRecords.get_unique_product_units())
        self.UnitComboBoxFake = CTkLabel(self, text="", text_color="#888888", anchor="w", fg_color=ThemeManager.theme["CTkComboBox"]["fg_color"], corner_radius=ThemeManager.theme["CTkComboBox"]["corner_radius"], width=218)
        self.PieceText = CTkLabel(self, text="Piece :")
        self.PieceEntry = CTkEntry(self, bg_color="black", width=70, font=CTkFont(size=18))
        self.CustomerText = CTkLabel(self, text="Seller :")
        self.CustomerComboBox = CTkComboBox(self, bg_color="black", values=self.ProductRecords.get_unique_customers_by_process_type("Buy"), width=220)
        self.SellingPriceText = CTkLabel(self, text="Selling price :", font=CTkFont(size=12))
        self.SellingPriceEntry = CTkEntry(self, bg_color="black", font=CTkFont(size=12), width=70, fg_color="black", border_color="#aa3333", border_width=1)
        self.PaymentStatusText = CTkLabel(self, text="Payment status :")
        self.PaymentStatusComboBox = CTkComboBox(self, bg_color="black", values=self.ProductRecords.get_unique_payment_status(), width=220)

        self.DescritionText = CTkLabel(self,text="Description :")
        self.DescriptionEntry = CTkEntry(self, bg_color="black", width=220)

        self.DescritionText.place(x=15,y=340)        
        self.DescriptionEntry.place(x=115,y=340)

        self.ProductNameText.place(x=15, y=20)
        self.ProductNameComboBox.place(x=115, y=20)
        self.BarCodeText.place(x=15, y=60)
        self.PurchasePriceText.place(x=15, y=220)
        self.PurchasePriceEntry.place(x=115, y=220)
        self.UnitText.place(x=15, y=180)
        self.CustomerText.place(x=15, y=100)
        self.CustomerComboBox.place(x=115, y=100)
        self.PaymentStatusText.place(x=15, y=140)
        self.PaymentStatusComboBox.place(x=115, y=140)
        self.PieceText.place(x=15, y=260)
        self.PieceEntry.place(x=190, y=260)
        self.PieceEntry.insert(0, "0")
        self.SellingPriceText.place(x=15, y=300)
        self.SellingPriceEntry.place(x=190, y=300)
        
        self.label_value = CTkLabel(self, text="")
        self.label_value.place(x=60, y=260)
        
        self.entry_add_10 = CTkButton(self, text="<", fg_color="#003300", hover_color="#00cc00", width=15, command=lambda: self.add(10), font=CTkFont(size=10))
        self.entry_add_10.place(x=163, y=260)
        self.entry_add_100 = CTkButton(self, text="<", fg_color="#003300", hover_color="#00cc00", width=15, command=lambda: self.add(100), font=CTkFont(size=10))
        self.entry_add_100.place(x=138, y=260)
        self.entry_add_1000 = CTkButton(self, text="<", fg_color="#003300", hover_color="#00cc00", width=15, command=lambda: self.add(1000), font=CTkFont(size=10))
        self.entry_add_1000.place(x=113, y=260)
        self.entry_subtract_10 = CTkButton(self, text=">", fg_color="#330000", hover_color="#cc0000", width=15, command=lambda: self.subtract(10), font=CTkFont(size=10))
        self.entry_subtract_10.place(x=265, y=260)
        self.entry_subtract_100 = CTkButton(self, text=">", fg_color="#330000", hover_color="#cc0000", width=15, command=lambda: self.subtract(100), font=CTkFont(size=10))
        self.entry_subtract_100.place(x=290, y=260)
        self.entry_subtract_1000 = CTkButton(self, text=">", fg_color="#330000", hover_color="#cc0000", width=15, command=lambda: self.subtract(1000), font=CTkFont(size=10))
        self.entry_subtract_1000.place(x=315, y=260)

        self.after(200, self.update_combobox)
        self.PieceEntry.bind("<Enter>", self.update_label)
        self.PieceEntry.bind("<KeyRelease>", self.update_label)
        self.SaveButton = CTkButton(self,text="",fg_color="black",hover=False,height=0,width=0,bg_color="red",command=self.save,image=CTkImage(Image.open("assets\\icons\\save.png"),size=(30,30)))
        self.SaveButton.place(x=305,y=380)
        self.mainloop()
    
    def update_label(self, useless=None):
        if len(self.PieceEntry.get()) < 8:
            self.label_value.configure(text=self.PieceEntry.get())
        else:
            self.label_value.configure(text="Longgg")
    
    def add(self, value):
        current_value = int(self.PieceEntry.get()) if self.PieceEntry.get().isdigit() else 0
        self.PieceEntry.delete(0, 'end')
        self.PieceEntry.insert(0, str(current_value + value))
        self.update_label()

    def subtract(self, value):
        current_value = int(self.PieceEntry.get()) if self.PieceEntry.get().isdigit() else 0
        if current_value >= value:
            self.PieceEntry.delete(0, 'end')
            self.PieceEntry.insert(0, str(current_value - value))
            self.update_label()
    
    def update_combobox(self, last=None):
        new = self.ProductNameComboBox.get()
        if last is None or last != new:
            if new in self.ProductRecords.get_unique_product_names():
                product_dict = self.ProductRecords.get_first_data(new)
                self.BarCodeEntry.delete(0, "end")
                self.PurchasePriceEntry.delete(0, "end")
                self.SellingPriceEntry.delete(0, "end")
                self.DescriptionEntry.delete(0,"end")
                self.BarCodeEntry.insert(0, product_dict["barcode"])
                self.PurchasePriceEntry.insert(0, product_dict["purchase_price"])
                self.SellingPriceEntry.insert(0, product_dict["selling_price"])
                self.CustomerComboBox.set(product_dict["customer"])
                self.PaymentStatusComboBox.set(product_dict["payment_status"])
                self.DescriptionEntry.insert(0,product_dict["description"])

                self.BarCodeEntry.place_forget()
                self.BarCodeEntryFake.configure(text=product_dict["barcode"])
                self.BarCodeEntryFake.place(x=115, y=60)
                self.UnitComboBox.place_forget()
                self.UnitComboBoxFake.configure(text=product_dict["unit"])
                self.UnitComboBoxFake.place(x=116, y=180)
                self.fake=True
            else:
                self.fake=False
                self.UnitComboBoxFake.place_forget()
                self.UnitComboBox.place(x=115, y=180)
                self.BarCodeEntryFake.place_forget()
                self.BarCodeEntry.place(x=115, y=60)
                self.PurchasePriceEntry.delete(0, "end")
                self.SellingPriceEntry.delete(0, "end")
                self.DescriptionEntry.delete(0,"end")
                self.BarCodeEntry.delete(0,"end")
                self.PurchasePriceEntry.insert(0, "0")
                self.SellingPriceEntry.insert(0, "0")



        self.after(400, lambda: self.update_combobox(last=new))
    def save(self):
        self.SaveButton.configure(command=None)

        if self.fake:
            self.ProductRecords.add(self.ProductNameComboBox.get(),self.BarCodeEntryFake.cget("text"),self.PurchasePriceEntry.get(),self.SellingPriceEntry.get(),self.PieceEntry.get(),self.UnitComboBoxFake.cget("text"),self.user,"Buy",self.CustomerComboBox.get(),self.PaymentStatusComboBox.get(),self.DescriptionEntry.get())
        else:
            self.ProductRecords.add(self.ProductNameComboBox.get(),self.BarCodeEntry.get(),self.PurchasePriceEntry.get(),self.SellingPriceEntry.get(),self.PieceEntry.get(),self.UnitComboBox.get(),self.user,"Buy",self.CustomerComboBox.get(),self.PaymentStatusComboBox.get(),self.DescriptionEntry.get())
        self.after(1020,lambda:self.SaveButton.configure(command=self.save))
        """self.master.deiconify()
        self.withdraw()"""
        
class Record_screen(new_toplevel):

    def __init__(self,master,user,ProductRecords,list_=None,main=False):
        super().__init__()
        self.calender=None
        self.list_=list_
        self.master=master
        self.main = self.master if main else master.main
        self.ProductRecords=ProductRecords
        self.ProductRecords.refresh_for_time()
        self.geometry("1260x850")
        self.protocol("WM_DELETE_WINDOW",lambda:(master.deiconify(),self.withdraw(),self.title_menu.withdraw(),self.title_menu.destroy()))
        self.user=user
        self.header=["no","Product Name","Barcode","Purchase","Selling","Piece","Unit","Time","Date","User","Process Type","Customer","Payment status","Description"]
        self.title_menu=TitleMenu(master=self,x_offset=215)
        self.master.withdraw()
        
        self.title_menu.add_cascade(text="◀",command=self.backstep)
        self.title_menu.add_cascade(text="re",hover_color="transparentcolor")
        self.title_menu.add_entry(width=25)
        self.title_menu.menu_button.bind("<FocusIn>",lambda event: self.title_menu.menu_buttons[2].delete(0,"end"))
        self.title_menu.menu_button.bind("<FocusOut>",self.entry_delete)
        self.title_menu.menu_button.bind("<KeyRelease>", self.go_page)
        self.title_menu.add_cascade(text="▶",command=self.nobackstep)
        self.title_menu.add_cascade(text="Search within date",command=self.search_in_date)
        self.title_menu.add_cascade(text="Export Only this page")
        self.title_menu.add_cascade(text="Export this page")
        self.title_menu.add_cascade(text="",image=CTkImage(Image.open("assets\\icons\\menu.png")),command=lambda:(self.main.deiconify(),self.withdraw()))
        self.bind("<Motion>",self.get_mouse_position)
        self.title_menu.bind("<Motion>",self.get_mouse_position)
        if list_ is None:
            self.ProductList=self.ProductRecords.get_numerate_table()
            
        else:
            self.ProductList=self.ProductRecords.get_numerate(list_)
        ProductList=self.ProductList
        self.title_menu.menu_buttons[1].configure(text=str(int((len(self.ProductList)/25+0.999)))+"      /")
        if len(ProductList)>25:
            self.SelectedProductList=self.ProductList[0:25]
            
        else:
            self.SelectedProductList=ProductList[0:len(ProductList)]
        if self.check_customer(self.ProductList):
            self.title(f"Customer : {self.ProductList[0][11]}")
        self.title_menu.menu_buttons[5].configure(command=lambda:Ecreater(self.SelectedProductList[1:]))
        self.title_menu.menu_buttons[6].configure(command=lambda:Ecreater(self.ProductList))


        self.SelectedProductList.insert(0,self.header)
        SelectedProductList=self.SelectedProductList
        self.table = CTkTable(self,
                                       command=lambda a:self.table_command(a),
                                       column_widths=[10,100,100,40,40,50,50,40,85,100,80,120,120,100],
                                       header_color="#4444dd",values=SelectedProductList,
                                       colors=["#1f1f1f","#303030"],
                                       command_2=lambda a:self.table_command_2(a),
                                       corner_radius=5)
            
        """self.table.mainframe.configure(border_width=1,border_color="#ff0000")"""

        
        self.after(100,lambda t=self.table:(t.grid(sticky="new",padx=30,pady=10)))
    def check_customer(self,nested_list):
        if not nested_list or not all(len(sublist) > 11 for sublist in nested_list):
            return False
        
        elements = [sublist[11] for sublist in nested_list]
        return all(element == elements[0] for element in elements)
    def get_mouse_position(self,event):
        x, y = event.x_root, event.y_root
        self.x=x
        self.y=y
    def date_func(self,date):
        selection=self.ProductRecords.get_by_date(self.calender.selection)
        if len(selection)!= 0 and selection!=self.list_:
            
            Record_screen(master=self,ProductRecords=self.ProductRecords,user=self.user,list_=selection)
        
        
    def search_in_date(self):
        self.calender=CTkCalender(all_hide=None,command=self.date_func,position=f"{self.x}+{self.y+20}")

    def get_page(self):
        self.entry_delete()
        return int(self.title_menu.menu_buttons[2].get())
    def go_page(self,useless=None):
        try:
            step=self.get_page()
            print(step)
        except Exception as e:
            if self.title_menu.menu_buttons[2].get()!="":
                self.entry_delete()
            #self.title_menu.menu_buttons[2].delete(0,"end")
         
        if 0<step*25:

            if step<=int((len(self.ProductList)/25+0.999)):
                self.SelectedProductList=self.ProductList[(step-1)*25:step*25]
                print(str(self.SelectedProductList[1]))
                
                self.SelectedProductList.insert(0,self.header)
                self.table.update_values(self.SelectedProductList)


    def nobackstep(self):
        step=step=self.get_page()
        step+=1
        if step*25<len(self.ProductList):
            self.SelectedProductList=self.ProductList[(step-1)*25:step*25]
            self.SelectedProductList.insert(0,self.header)
            self.table.update_values(self.SelectedProductList)
        elif (step-1)*25<len(self.ProductList) and step*25>len(self.ProductList):
            self.SelectedProductList=self.ProductList[(step-1)*25:len(self.ProductList)]
            self.SelectedProductList.insert(0,self.header)
            self.table.update_values(self.SelectedProductList)
        else:
            step-=1
        self.number_of(step)
    def backstep(self):
        step=self.get_page()
        step-=1
        if step>0:
            self.SelectedProductList=self.ProductList[(step-1)*25:step*25]
            self.SelectedProductList.insert(0,self.header)
            self.table.update_values(self.SelectedProductList)
        else:
            step+=1
        self.number_of(step)
    def number_of(self,step):
        
        self.title_menu.menu_buttons[2].delete(0,"end")
        self.title_menu.menu_buttons[2].insert(0,step)
    def table_command(self,dict_,list_=None):
        if dict_["value"]!="" and dict_["row"]!=0:
            print(dict_)
            if dict_["column"]==12:
                list_new=self.ProductRecords.get_customer(dict_["value"])
            if dict_["column"]==2:
                list_new=self.ProductRecords.get_product(dict_["value"])
            if dict_["column"]==3:
                list_new=self.ProductRecords.get_barcode(dict_["value"])
            if  "list_new" in list(locals().keys()) :
                if list_new!=self.list_:
                    Record_screen(master=self,ProductRecords=self.ProductRecords,user=self.user,list_=list_new)
    def table_command_2(self,dict_,list_=None):
        if dict_["value"]!="":
            data=list(self.SelectedProductList[int(dict_["row"])])
            #data=[["Name","Purchase","Selling","Piece","Unit","Type","Customer","Status"],data]
            #data=data.insert(0,)
            del data[0]

            data_row=self.ProductRecords.find_row_id(*data)
            self.withdraw()
            Repair_row_screen(data_row,self.ProductRecords,self.user,self.main)

    def entry_delete(self,useless=None):
        

        self.title_menu.menu_buttons[2].delete(0,"end")
 
        self.title_menu.menu_buttons[2].insert(0,str((self.ProductList.index(self.SelectedProductList[1])+1)//25+1))
class Repair_row_screen:
    def __init__(self, data_row, ProductRecords, user, master):
        self.toplevel = new_toplevel()
        self.row = data_row
        self.ProductRecords = ProductRecords
        self.repair_data()
        self.toplevel.geometry("360x440")
        self.toplevel.title(f"Repair row : {data_row}    Date : {self.data[7]}    Time : {self.data[6]}")
        self.toplevel.protocol("WM_DELETE_WINDOW", lambda: (master.deiconify(), self.toplevel.withdraw()))
        self.master = master
        self.user = user
        

        self.delete_button = CTkButton(self.toplevel,command=self.delete_row, width=30, height=30, text="", bg_color="black", fg_color="black", hover=False,image=CTkImage(Image.open("assets\\icons\\Trash.png"), size=(20,20)))
        self.delete_button.place(x=300, y=380)

        self.update_button = CTkButton(self.toplevel,command=self.update_data ,width=30,height=30,text="",bg_color="black",fg_color="black", image=CTkImage(Image.open("assets\\icons\\Cached.png"), size=(20,20)))
        self.update_button.place(x=250,y=380)

        self.ProductNameText = CTkLabel(self.toplevel, text="Product name :")
        self.ProductNameComboBox = CTkComboBox(self.toplevel, bg_color="black", width=220, values=self.ProductRecords.get_unique_product_names())
        self.ProductNameComboBox.set(self.data[0])
        self.BarCodeText = CTkLabel(self.toplevel, text="Barcode :")
        self.BarCodeEntryFake = CTkLabel(self.toplevel, fg_color="black", text=" ", anchor="w", corner_radius=ThemeManager.theme["CTkComboBox"]["corner_radius"], width=220)
        self.PurchasePriceText = CTkLabel(self.toplevel, text="Purchase Price :")
        self.PurchasePriceEntry = CTkEntry(self.toplevel, bg_color="black", width=220)
        
        self.UnitText = CTkLabel(self.toplevel, text="Unit :")
        self.UnitComboBoxFake = CTkLabel(self.toplevel,fg_color="black" ,text="", anchor="w",corner_radius=ThemeManager.theme["CTkComboBox"]["corner_radius"], width=218)
        self.PieceText = CTkLabel(self.toplevel, text="Piece :")
        self.PieceEntry = CTkEntry(self.toplevel, bg_color="black", width=70, font=CTkFont(size=18))
        self.CustomerText = CTkLabel(self.toplevel, text="Seller :")
        self.CustomerComboBox = CTkComboBox(self.toplevel, bg_color="black", values=self.ProductRecords.get_unique_customers(), width=220)
        self.SellingPriceText = CTkLabel(self.toplevel, text="Selling price :", font=CTkFont(size=12))
        self.SellingPriceEntry = CTkEntry(self.toplevel, bg_color="black", font=CTkFont(size=12), width=70, fg_color="black", border_color="#aa3333", border_width=1)
        
        self.DescritionText = CTkLabel(self.toplevel,text="Description :")
        self.DescriptionEntry = CTkEntry(self.toplevel, bg_color="black", width=220)

        self.DescritionText.place(x=15,y=340)        
        self.DescriptionEntry.place(x=115,y=340)
        
        self.ProductNameText.place(x=15, y=20)
        self.ProductNameComboBox.place(x=115, y=20)
        self.BarCodeText.place(x=15, y=60)
        self.BarCodeEntryFake.place(x=115,y=60)
        
        self.PurchasePriceText.place(x=15, y=220)
        self.PurchasePriceEntry.place(x=115, y=220)
        self.PaymentStatusText = CTkLabel(self.toplevel, text="Payment status :")
        self.PaymentStatusComboBox = CTkComboBox(self.toplevel, bg_color="black", values=self.ProductRecords.get_unique_payment_status(), width=220)

        self.UnitText.place(x=15, y=180)
        self.UnitComboBoxFake.place(x=115,y=180)
        
        self.CustomerText.place(x=15, y=100)
        self.CustomerComboBox.place(x=115, y=100)

        self.PaymentStatusText.place(x=15, y=140)
        self.PaymentStatusComboBox.place(x=115, y=140)

        self.PieceText.place(x=15, y=260)
        self.PieceEntry.place(x=190, y=260)
        self.PieceEntry.insert(0, self.data[4])

        self.SellingPriceText.place(x=15, y=300)
        self.SellingPriceEntry.place(x=190, y=300)

        self.label_value = CTkLabel(self.toplevel, text="")
        self.label_value.place(x=60, y=260)

        self.PieceEntry.bind("<Enter>", self.update_label)
        self.PieceEntry.bind("<KeyRelease>", self.update_label)
        
        self.entry_add_10 = CTkButton(self.toplevel, text="<", fg_color="#003300", hover_color="#00cc00", width=15, command=lambda: self.add(10), font=CTkFont(size=10))
        self.entry_add_10.place(x=163, y=260)

        self.entry_add_100 = CTkButton(self.toplevel, text="<", fg_color="#003300", hover_color="#00cc00", width=15, command=lambda: self.add(100), font=CTkFont(size=10))
        self.entry_add_100.place(x=138, y=260)

        self.entry_add_1000 = CTkButton(self.toplevel, text="<", fg_color="#003300", hover_color="#00cc00", width=15, command=lambda: self.add(1000), font=CTkFont(size=10))
        self.entry_add_1000.place(x=113, y=260)

        self.entry_subtract_10 = CTkButton(self.toplevel, text=">", fg_color="#330000", hover_color="#cc0000", width=15, command=lambda: self.subtract(10), font=CTkFont(size=10))
        self.entry_subtract_10.place(x=265, y=260)

        self.entry_subtract_100 = CTkButton(self.toplevel, text=">", fg_color="#330000", hover_color="#cc0000", width=15, command=lambda: self.subtract(100), font=CTkFont(size=10))
        self.entry_subtract_100.place(x=290, y=260)

        self.entry_subtract_1000 = CTkButton(self.toplevel, text=">", fg_color="#330000", hover_color="#cc0000", width=15, command=lambda: self.subtract(1000), font=CTkFont(size=10))
        self.entry_subtract_1000.place(x=315, y=260)

        self.write_row()

        self.toplevel.mainloop()

    def repair_data(self):
        self.data = self.ProductRecords.get_by_row_id(self.row)
        self.data = list(self.data)

    
    def update_label(self, useless=None):
        if len(self.PieceEntry.get()) < 8:
            self.label_value.configure(text=self.PieceEntry.get())
        else:
            self.label_value.configure(text="Longgg")

    def add(self, value):
        current_value = int(self.PieceEntry.get()) if self.PieceEntry.get().isdigit() else 0
        self.PieceEntry.delete(0, 'end')
        self.PieceEntry.insert(0, str(current_value + value))
        self.update_label()

    def subtract(self, value):
        current_value = int(self.PieceEntry.get()) if self.PieceEntry.get().isdigit() else 0
        if current_value >= value:
            self.PieceEntry.delete(0, 'end')
            self.PieceEntry.insert(0, str(current_value - value))
            self.update_label()

    def write_row(self):
        self.ProductNameComboBox.set(self.data[0])
        
        self.CustomerComboBox.set(self.data[10])
        self.PurchasePriceEntry.insert(0,self.data[2])
        self.SellingPriceEntry.insert(0,self.data[3])
        self.PaymentStatusComboBox.set(self.data[11])
        self.DescriptionEntry.insert(0,self.data[12] if "Edited/" not in self.data[12] else self.data[12][:-7])

        self.update_labels()
    def update_labels(self):
        product_dict=self.ProductRecords.get_first_data(self.ProductNameComboBox.get())
        self.BarCodeEntryFake.configure(text=product_dict["barcode"])
        self.UnitComboBoxFake.configure(text=product_dict["unit"])
        self.toplevel.after(500,self.update_labels)
        self.update_label()
    def delete_row(self):
        
        self.ProductRecords.delete_row(self.row)
        if self.user!="main":
            self.ProductRecords.add(self.data[0],self.data[1],0.0,self.data[3],0,self.data[5],self.user,"Deleted","","",self.data[9]+"/"+self.DescriptionEntry.get(),self.data[6],self.data[7])
        self.close_window()
    def update_data(self):
        self.ProductRecords.delete_row(self.row)
        self.ProductRecords.add(self.ProductNameComboBox.get(),self.BarCodeEntryFake.cget("text"),self.PurchasePriceEntry.get(),self.SellingPriceEntry.get(),self.PieceEntry.get(),self.UnitComboBoxFake.cget("text"),self.user,self.data[9],self.CustomerComboBox.get(),self.PaymentStatusComboBox.get(),self.DescriptionEntry.get()+"/Edited")
        self.close_window()
    def close_window(self):
        Record_screen(self.master,self.user,self.ProductRecords,main=True)
        self.toplevel.withdraw()
class Sell_screen(new_toplevel):
    def __init__(self, master,user, ProductRecords):
        super().__init__()
        self.geometry("700x700")
        self.user=user
        self.ProductRecords=ProductRecords
        self.master = master
        self.ProcessStatus = 1
        self.protocol("WM_DELETE_WINDOW",lambda:(master.deiconify(),self.withdraw()))
        self.title("Shop     User : "+self.user)

        self.options_frame = CTkFrame(self,fg_color="black",border_color="#cccccc",border_width=1,width=650,height=90)
        self.options_frame.place(x=25,y=5)
        
        self.CustomerText = CTkLabel(self.options_frame,height=30,text="Customer :")
        self.CustomerComboBox = CTkComboBox(self.options_frame,height=30,values=self.ProductRecords.get_unique_customers_by_process_type("sell"))

        self.ReturnButton = CTkButton(self.options_frame,height=30,width=120,text="change Return",command=self.ProcessStatusReturn)
        self.SellButton = CTkButton(self.options_frame,height=30,width=120,text="change Sell",command=self.ProcessStatusSell)
        


        self.CustomerText.place(x=30,y=30)
        self.CustomerComboBox.place(x=140,y=30)

        self.Status_positon = {"x":460,"y":30}
        self.ReturnButton.place(**self.Status_positon)
        self.mainloop()
    def ProcessStatusReturn(self):
        self.ProcessStatus=-1
        print("a")
        self.ReturnButton.place_forget()
        self.SellButton.place(**self.Status_positon)
    def ProcessStatusSell(self):
        print("b")
        self.ProcessStatus=1
        self.SellButton.place_forget()
        self.ReturnButton.place(**self.Status_positon)


if __name__=="__main__":
    market_window("main")
    #win=window_for_access()