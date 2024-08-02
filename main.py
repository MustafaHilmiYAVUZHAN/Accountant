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
            
        elif self.DataForAccess.find_data(name)[2]!=password:
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
        if self.DataForAccess.find_data("main")[2]=="main":
            Messagebox(title="Defualt Main access",message="name             : main\npassword     : main\n\nYou should change these")
            
        self.window.mainloop()####################
    def loginControl(self):
        password=self.passwordEnrty.get()
        name=self.nameEntry.get()
        print(f"Name : {name}         PASSWORD: {password}")
        if self.DataForAccess.find_data(name) is None:
            Messagebox(title="Wrong NAME",message="Your name is not on the list")
        elif self.DataForAccess.find_data(name)[2]!=password:
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
        self.window=CTk()
        
        #title_bar.hide(self.window)
        #self.window.mainloop()####################
        set_default_color_theme("assets\\extreme.json")
        self.window.geometry("360x900+20+20")
        self.window.resizable(0,0)
        self.window.title(f"User: {name}")
        maximize_minimize_button.hide(self.window)
        title_bar_text_color.set(self.window,"#aaaaaa")
        apply_style(self.window,"acrylic")
        self.window.protocol("WM_DELETE_WINDOW",lambda:Messagebox(title="Exit",message="Do you want exit",option_1="Exit",option_1_func=lambda:exit(),option_2="cancel",option_2_func=lambda:print("",end=""),option_3="Change user",option_3_func=lambda:(self.window.withdraw(),window_for_access())))
        self.TitleMenu=TitleMenu(master=self.window,x_offset=115)
        self.TitleMenu.add_cascade(text="Change user",hover_color="#3030dd",command=lambda:(self.window.withdraw(),self.TitleMenu.destroy(),window_for_access(),self.window.destroy()))#{"height":20,"width":15,"fg_color":"#505050","bg_color":"#000001"})
        if name=="main":
            self.TitleMenu.add_cascade(text="Change user's data",hover_color="#3030dd",command=lambda:(self.window.withdraw(),self.TitleMenu.destroy(),passwords_window(),self.window.destroy()))
        self.button_1=CTkButton(self.window,width=160,height=160,command=self.button_1_func,bg_color="black")
        self.button_1.grid(row=0,column=0,pady=10,padx=10)
        self.button_1=CTkButton(self.window,width=160,height=160,command=lambda:button_2_func(self.ProductRecords,name),bg_color="black")
        self.button_1.grid(row=0,column=1,pady=10,padx=10)
        self.button_1=CTkButton(self.window,width=160,height=160,bg_color="black")
        self.button_1.grid(row=1,column=0,pady=10,padx=10)
        self.button_1=CTkButton(self.window,width=160,height=160,bg_color="black")
        self.button_1.grid(row=1,column=1,pady=10,padx=10)
        self.button_1=CTkButton(self.window,width=160,height=160,bg_color="black")
        self.button_1.grid(row=2,column=0,pady=10,padx=10)
        self.button_1=CTkButton(self.window,width=160,height=160,bg_color="black")
        self.button_1.grid(row=2,column=1,pady=10,padx=10)
        self.button_1=CTkButton(self.window,width=160,height=160,bg_color="black")
        self.button_1.grid(row=3,column=0,pady=10,padx=10)
        self.button_1=CTkButton(self.window,width=160,height=160,bg_color="black")
        self.button_1.grid(row=3,column=1,pady=10,padx=10)
        self.button_1=CTkButton(self.window,width=160,height=160,bg_color="black")
        self.button_1.grid(row=4,column=0,pady=10,padx=10)
        self.button_1=CTkButton(self.window,width=160,height=160,bg_color="black")
        
        self.button_1.grid(row=4,column=1,pady=10,padx=10)
        self.ProductRecords=ProductRecords()
        self.window.mainloop()####################

    def button_3_func(self):
        toplevel = new_toplevel()
        toplevel.geometry("950x750")
        
    
        




    def button_1_func(self):
        toplevel=new_toplevel()
        toplevel.geometry("350x375")
        toplevel.title("button_1")
        ProductNameText = CTkLabel(toplevel, text="Product name :")
        ProductNameComboBox = CTkComboBox(toplevel, bg_color="black", width=220,values=self.ProductRecords.get_unique_product_names())
        BarCodeText = CTkLabel(toplevel, text="Barcode :")
        BarCodeEntry = CTkEntry(toplevel, bg_color="black", width=220)
        PurchasePriceText = CTkLabel(toplevel, text="Purchase Price :")
        PurchasePriceEntry = CTkEntry(toplevel, bg_color="black", width=220)
        SellingPriceText = CTkLabel(toplevel, text="Selling Price :")
        SellingPriceEntry = CTkEntry(toplevel, bg_color="black", width=220)
        UnitText = CTkLabel(toplevel, text="Unit :")
        UnitComboBox = CTkComboBox(toplevel, bg_color="black", width=220,values=self.ProductRecords.get_unique_product_units())
        PieceText = CTkLabel(toplevel, text="Piece :")
        PieceEntry = CTkEntry(toplevel, bg_color="black", width=70, font=CTkFont(size=18))

        ProductNameText.place(x=15, y=20)
        ProductNameComboBox.place(x=115, y=20)
        BarCodeText.place(x=15, y=60)
        BarCodeEntry.place(x=115, y=60)
        PurchasePriceText.place(x=15, y=100)
        PurchasePriceEntry.place(x=115, y=100)
        SellingPriceText.place(x=15, y=140)
        SellingPriceEntry.place(x=115, y=140)

        UnitText.place(x=15, y=180)
        UnitComboBox.place(x=115, y=180)

        PieceText.place(x=15, y=220)
        PieceEntry.place(x=190, y=220)
        #PieceEntry.insert(0,"0")
        def update_label(useless=None):
            if len(PieceEntry.get())<8:
                label_value.configure(text=PieceEntry.get())
            else:
                label_value.configure(text="Longgg")
        def add(value):
            current_value = int(PieceEntry.get()) if PieceEntry.get().isdigit() else 0
            PieceEntry.delete(0, 'end')
            PieceEntry.insert(0, str(current_value + value))
            update_label()

        def subtract(value):
            current_value = int(PieceEntry.get()) if PieceEntry.get().isdigit() else 0
            if current_value >= value:
                PieceEntry.delete(0, 'end')
                PieceEntry.insert(0, str(current_value - value))
                update_label()
        def update_combobox(last=None):
            new=ProductNameComboBox.get()
            if new in self.ProductRecords.get_unique_product_names() and (last is None or last != new):
                product_dict=self.ProductRecords.get_min_data(new)
                BarCodeEntry.delete(0,"end")
                PurchasePriceEntry.delete(0,"end")
                SellingPriceEntry.delete(0,"end")
                BarCodeEntry.insert(0,product_dict["barcode"])
                PurchasePriceEntry.insert(0,product_dict["purchase_price"])
                SellingPriceEntry.insert(0,product_dict["selling_price"])
                UnitComboBox.set(product_dict["unit"])

            toplevel.after(400,lambda:update_combobox(last=new))
        entry_add_10 = CTkButton(toplevel, text="<", fg_color="#003300", hover_color="#00cc00", width=15, command=lambda: add(10), font=CTkFont(size=10))
        entry_add_10.place(x=163, y=220)

        entry_add_100 = CTkButton(toplevel, text="<", fg_color="#003300", hover_color="#00cc00", width=15, command=lambda: add(100), font=CTkFont(size=10))
        entry_add_100.place(x=138, y=220)

        entry_add_1000 = CTkButton(toplevel, text="<", fg_color="#003300", hover_color="#00cc00", width=15, command=lambda: add(1000), font=CTkFont(size=10))
        entry_add_1000.place(x=113, y=220)

        entry_subtract_10 = CTkButton(toplevel, text=">", fg_color="#330000", hover_color="#cc0000", width=15, command=lambda: subtract(10), font=CTkFont(size=10))
        entry_subtract_10.place(x=265, y=220)

        entry_subtract_100 = CTkButton(toplevel, text=">", fg_color="#330000", hover_color="#cc0000", width=15, command=lambda: subtract(100), font=CTkFont(size=10))
        entry_subtract_100.place(x=290, y=220)

        entry_subtract_1000 = CTkButton(toplevel, text=">", fg_color="#330000", hover_color="#cc0000", width=15, command=lambda: subtract(1000), font=CTkFont(size=10))
        entry_subtract_1000.place(x=315, y=220)

        label_value = CTkLabel(toplevel, text="")
        label_value.place(x=60, y=220)
        toplevel.after(200,update_combobox)
        PieceEntry.bind("<Enter>",update_label)
        PieceEntry.bind("<KeyRelease>", update_label)

        toplevel.mainloop()
class button_2_func:

    def __init__(self,ProductRecords,user,list_=None):

        self.ProductRecords=ProductRecords
        toplevel = new_toplevel()
        toplevel.geometry("1100x850")
        self.user=user
        self.title_menu=TitleMenu(master=toplevel,x_offset=115)
        toplevel.protocol("WM_DELETE_WINDOW",lambda:(toplevel.withdraw(),self.title_menu.withdraw()))
        self.title_menu.add_cascade(text="◀",command=self.backstep)
        self.title_menu.add_cascade(text="re",hover_color="transparentcolor")
        self.title_menu.add_entry(width=25)
        self.title_menu.menu_button.bind("<FocusIn>",lambda event: self.title_menu.menu_buttons[2].delete(0,"end"))
        self.title_menu.menu_button.bind("<FocusOut>",self.entry_delete)
        self.title_menu.menu_button.bind("<KeyRelease>", self.go_page)
        self.title_menu.add_cascade(text="▶",command=self.nobackstep)
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

        self.SelectedProductList.insert(0,["no","Product Name","Barcode","Purchase","Selling","Piece","Unit","Time","Date","User","Process Type","Customer","Payment status"])
        SelectedProductList=self.SelectedProductList
        self.table = CTkTable(toplevel,
                                       command=lambda a:self.table_command(a),
                                       column_widths=[10,100,100,40,40,50,50,40,85,100,80,80,80],
                                       header_color="#4444dd",values=SelectedProductList,
                                       colors=["#1f1f1f","#303030"],
                                       command_2=lambda a:self.table_command_2(a),
                                       corner_radius=5,border_width=1)
            
        """self.table.mainframe.configure(border_width=1,border_color="#ff0000")"""
        
        toplevel.after(20,lambda t=self.table:(t.grid(sticky="new",padx=30,pady=10)))
    
    def get_page(self):
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
                
                self.SelectedProductList.insert(0,["no","Product Name","Barcode","Purchase","Selling","Piece","Unit","Time","Date","User","Process Type","Customer","Payment status"])
                self.table.update_values(self.SelectedProductList)


    def nobackstep(self):
        step=step=self.get_page()
        step+=1
        if step*25<len(self.ProductList):
            self.SelectedProductList=self.ProductList[(step-1)*25:step*25]
            self.SelectedProductList.insert(0,["no","Product Name","Barcode","Purchase","Selling","Piece","Unit","Time","Date","User","Process Type","Customer","Payment status"])
            self.table.update_values(self.SelectedProductList)
        elif (step-1)*25<len(self.ProductList) and step*25>len(self.ProductList):
            self.SelectedProductList=self.ProductList[(step-1)*25:len(self.ProductList)]
            self.SelectedProductList.insert(0,["no","Product Name","Barcode","Purchase","Selling","Piece","Unit","Time","Date","User","Process Type","Customer","Payment status"])
            self.table.update_values(self.SelectedProductList)
        else:
            step-=1
        self.number_of(step)
    def backstep(self):
        step=self.get_page()
        step-=1
        if step>0:
            self.SelectedProductList=self.ProductList[(step-1)*25:step*25]
            self.SelectedProductList.insert(0,["no","Product Name","Barcode","Purchase","Selling","Piece","Unit","Time","Date","User","Process Type","Customer","Payment status"])
            self.table.update_values(self.SelectedProductList)
        else:
            step+=1
        self.number_of(step)
    def number_of(self,step):
        
        self.title_menu.menu_buttons[2].delete(0,"end")
        self.title_menu.menu_buttons[2].insert(0,step)
    def table_command(self,dict_,list_=None):
        if dict_["value"]!="":
            print(dict_)
            if dict_["column"]==12:
                list_new=self.ProductRecords.get_customer(dict_["value"])
            if dict_["column"]==2:
                list_new=self.ProductRecords.get_product(dict_["value"])
            if dict_["column"]==3:
                list_new=self.ProductRecords.get_barcode(dict_["value"])
            if  "list_new" in list(locals().keys()):
                button_2_func(self.ProductRecords,user=self.user,list_=list_new)
    def table_command_2(self,dict_,list_=None):
        if dict_["value"]!="":
            print(self.SelectedProductList[int(dict_["row"])])

    def entry_delete(self,useless=None):
        

        self.title_menu.menu_buttons[2].delete(0,"end")
 
        self.title_menu.menu_buttons[2].insert(0,str((self.ProductList.index(self.SelectedProductList[1])+1)//25+1))
    def Repair(self,data):
        self.Repair_page=new_toplevel()
        self.Repair_page.geometry("1000x60")
        """a soon as posible"""
class new_toplevel(CTkToplevel):
    def __init__(self,all_hide : bool = False):
        super().__init__()
        set_default_color_theme(path.join(path.dirname(path.realpath(__file__)), 'assets\\extreme.json'))
        self.configure(takefocus=False)
        #new_toplevel.attributes("-topmost", True)
        if all_hide:
            all_stuffs.hide(self)
        else:
            maximize_minimize_button.hide(self)
        apply_style(self,"acrylic")
        print(self.winfo_name())
####################
if __name__=="__main__":
    market_window("main")
    #win=window_for_access()