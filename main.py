from customtkinter import *
from customtitlebar import *
from pywinstyles import apply_style
from hPyT import all_stuffs,maximize_minimize_button,border_color
from CTkMenuBar import CTkTitleMenu as TitleMenu

from CTkMessagebox import CTkMessagebox as Messagebox
from DBManager import PasswordManager,ProductRecords,CSVManager
from CTkTableMini import CTkTableMini as CTkTable
from PIL import ImageTk
from os import _exit
from CTkCalender import CTkCalender
from PIL import Image
from excelCreater import ExcelTableCreator as Ecreater
from excelCreater import ExcelTableConcubines as Etc
from excelCreater import ExcelToPDFConverter as ExtPDF
from datetime import datetime
from pathlib import Path
from CTkPDFframe import PDFViewer
from time import sleep
from sys import argv
from sys import exit as superexit
from os import getenv

def get_desktop_path():
    # Kullanıcı profil dizinini al
    user_profile = os.getenv('USERPROFILE') or os.getenv('HOME')
    
    if not user_profile:
        raise EnvironmentError("Kullanıcı profil dizini bulunamadı.")
    
    # Masaüstü dizinini oluştur
    desktop_path = os.path.join(user_profile, 'Desktop')
    
    return desktop_path

MYFOLDER="Muhasebecin"
ICON="data\\assets\\icons\\"
ASSETS="data\\assets\\"
DATA="data\\"
DESKTOP_PATH = get_desktop_path()
MYFOLDER=DESKTOP_PATH+"\\"+MYFOLDER
print(MYFOLDER)
os.chdir(MYFOLDER)

try:

    LIBREOFFICE=open(DATA+'LibreOfficePath.txt').read().replace('"',"")
except:
    print("LibreOfficePath.txt\n\nwhere is it?")
class new_toplevel(CTkToplevel):
    def __init__(self,all_hide : bool = False,topmost : bool = False):
        super().__init__()
        set_default_color_theme(ASSETS+'extreme.json')
        self.configure(takefocus=False)
        self.attributes("-topmost", True)
        self.resizable(0,0)
        self.wm_iconbitmap()
        self.icon=ImageTk.PhotoImage(file=ICON+"transparent.ico")
        self.after(100,lambda:self.iconphoto(False,self.icon))
        self.after(200,lambda:self.iconphoto(False,self.icon))
        self.after(300,lambda:self.iconphoto(False,self.icon))
        if not topmost:
            self.attributes("-topmost", False)
        if all_hide:
            all_stuffs.hide(self)
        else:
            maximize_minimize_button.hide(self)
        apply_style(self,"acrylic")
#################### 


"""
ad
adres
telefon
ticaret sicil numarası
vergidairesi
verginumarası
"""





###################################
###################################
class passwords_window:
    def __init__(self,DataForAccess=None) :
        self.toplevel=CTkToplevel()
        if DataForAccess is not None:
            self.DataForAccess=DataForAccess
        else:
            self.DataForAccess=PasswordManager()
        self.toplevel.geometry("175x150+600+400")
        self.toplevel.resizable(0,0)
        self.toplevel.title("Erişim")
        maximize_minimize_button.hide(self.toplevel)
        self.toplevel.wm_iconbitmap()
        self.icon=ImageTk.PhotoImage(file=ICON+"transparent.ico")
        self.toplevel.after(100,lambda:self.toplevel.iconphoto(False,self.icon))
        self.toplevel.after(200,lambda:self.toplevel.iconphoto(False,self.icon))
        self.toplevel.after(300,lambda:self.toplevel.iconphoto(False,self.icon))

        border_color.set(self.toplevel,"#ff0000")
        apply_style(self.toplevel,"acrylic")
        self.toplevel.protocol("WM_DELETE_WINDOW",self.withdraw)
        self.font=CTkFont(size=12)
        self.name_list=[item for tup in self.DataForAccess.list_name() for item in tup]
        print(self.name_list)
        self.nameLabel=CTkLabel(self.toplevel,text="Adınız          :",font=self.font)
        self.nameLabel.place(rely=0.1,relx=0.01,relwidth=0.4,relheight=0.12)
        self.nameComboBox=CTkComboBox(self.toplevel,bg_color="black",values=self.name_list,font=self.font)
        self.nameComboBox.place(rely=0.1,relx=0.45,relwidth=0.5,relheight=0.12)
        self.passwordLabel=CTkLabel(self.toplevel,text="Şifreniz   :",font=self.font)
        self.passwordLabel.place(rely=0.4,relx=0.01,relwidth=0.4,relheight=0.12)
        self.passwordEnrty=CTkEntry(self.toplevel,bg_color="black",show="*",font=self.font)
        self.passwordEnrty.place(rely=0.4,relx=0.45,relwidth=0.5,relheight=0.12)
        self.forSave=CTkButton(self.toplevel,text="Kaydet",bg_color="black",command=self.save,font=self.font)
        self.forSave.place(rely=0.7,relx=0.1,relwidth=0.4,relheight=0.15)
        self.forDelete=CTkButton(self.toplevel,text="Sil",hover_color="#ff0000",bg_color="black",font=self.font,command=self.delete)
        self.forDelete.place(rely=0.7,relx=0.6,relwidth=0.3,relheight=0.15)
        self.toplevel.mainloop()####################
    def withdraw(self):
        self.toplevel.withdraw()
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
            Messagebox(title="Aynı bunlar",message="Zaten bu isim ve şifrede kayıtlılar")
        print(f"Name : {name}         PASSWORD: {password}")
    def delete(self):
        name=self.nameComboBox.get()
        self.DataForAccess.delete_data(name)
        self.updateNameBox()
    def updateNameBox(self):
        self.name_list=[item for tup in self.DataForAccess.list_name() for item in tup]
        self.nameComboBox.configure(values=self.name_list)
        self.nameComboBox.update()








###################################
###################################
class window_for_access:
    def __init__(self):
         
        
        self.window=CTk()
        
        #title_bar.hide(self.window)
        #self.window.mainloop()####################
        set_default_color_theme(ASSETS+"extreme.json")
        self.window.geometry("300x200+600+250")
        self.window.resizable(0,0)
        self.window.title("Erişim")
        all_stuffs.hide(self.window)
        
        apply_style(self.window,"acrylic")
        self.window.wm_iconbitmap()
        self.icon=ImageTk.PhotoImage(file=ICON+"transparent.ico")
        self.window.iconphoto(False,self.icon)
        self.window.after(50,lambda:self.window.iconphoto(False,self.icon))
        self.window.after(100,lambda:self.window.iconphoto(False,self.icon))
        self.window.after(200,lambda:self.window.iconphoto(False,self.icon))
        self.nameLabel=CTkLabel(self.window,text="İsminiz          :")
        self.nameLabel.place(rely=0.2,relx=0.05,relwidth=0.252,relheight=0.15)
        self.nameEntry=CTkEntry(self.window,bg_color="black")
        self.nameEntry.place(rely=0.2,relx=0.45,relwidth=0.5,relheight=0.15)
        self.passwordLabel=CTkLabel(self.window,text="Şifreniz   :")
        self.passwordLabel.place(rely=0.4,relx=0.05,relwidth=0.252,relheight=0.15)
        self.passwordEnrty=CTkEntry(self.window,bg_color="black",show="*")
        self.passwordEnrty.place(rely=0.4,relx=0.45,relwidth=0.5,relheight=0.15)
        self.ButtonforAccess=CTkButton(self.window,text="Giriş",bg_color="black",command=self.loginControl)
        self.ButtonforAccess.place(rely=0.67,relx=0.3,relwidth=0.4,relheight=0.15)
        
        self.nameEntry.bind("<Return>",lambda event:self.passwordEnrty.focus())
        self.passwordEnrty.bind("<Return>",self.loginControl)
        """
        Burada data okunur ve isim listesi ve şifreler çekilir
        eğer boş ise oluşturulur
        main : main
        """

        self.DataForAccess=PasswordManager()
        if self.DataForAccess.find_data("main")[1]=="main":
            Messagebox(title="Defualt Main access",message="name             : main\npassword     : main\n\nYou should change these")
            
        self.window.mainloop()####################
    def loginControl(self,useless=None):
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
            









###################################
###################################
class market_window:
    def __init__(self,name):
        self.window=new_toplevel()
        
        
        self.window.geometry("360x540+600+100")#900

        self.name=name
        self.window.title(f"User: {name}")
        maximize_minimize_button.hide(self.window)
        apply_style(self.window,"acrylic")
        self.window.protocol("WM_DELETE_WINDOW",lambda:Messagebox(title="Exit",message="Do you want exit",option_1="Exit",option_1_func=lambda:(superexit(),exit(),_exit()),option_2="cancel",option_2_func=lambda:print("",end=""),option_3="Change user",option_3_func=lambda:(self.window.withdraw(),window_for_access())))
        self.add_image = CTkImage(Image.open(ICON+"add_shopping_cart.png"), size=(70, 70))
        self.record_image = CTkImage(Image.open(ICON+"description.png"), size=(70, 70))
        self.sell_image = CTkImage(Image.open(ICON+"shopping.png"), size=(70, 70))

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

        self.logout = CTkButton(
            self.window,
            width=160,
            text="",
            height=160,
            command=lambda:(self.window.withdraw(),window_for_access(),self.window.destroy()),
            bg_color="black",
            fg_color="black",
            border_color="white",
            border_width=1,
            hover_color="#111111",
            image=CTkImage(Image.open(ICON+"logout.png"),size=(70,70))
        )
        self.logout.grid(row=1, column=1, pady=10, padx=10)
        if name=="main":

            self.pin = CTkButton(
                self.window,
                width=160,
                text="",
                height=160,
                command=lambda:(self.window.withdraw(),passwords_window(),self.window.destroy()),
                bg_color="black",
                fg_color="black",
                border_color="white",
                border_width=1,
                hover_color="#111111",
                image=CTkImage(Image.open(ICON+"pin.png"),size=(70,70))
            )
        else:
            self.pin = CTkButton(
                self.window,
                width=160,
                text="",
                height=160,
                hover=False,
                bg_color="black",
                fg_color="black",
                command=lambda:Messagebox(title="You are not main",message="You can't this"),
                border_color="white",
                border_width=1,
                hover_color="#111111",
                image=CTkImage(Image.open(ICON+"pin.png"),size=(70,70))
            )


        self.pin.grid(row=2, column=0, pady=10, padx=10)
        self.ProductRecords=ProductRecords()
        self.ProductRecords.refresh_for_time()

        
        self.window.mainloop()####################

    
        
    
        











###################################
###################################
class Add_product_screen(new_toplevel):
    def __init__(self, master, ProductRecords,user):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", lambda: (master.deiconify(), self.withdraw()))
        self.geometry("350x435+600+100")
        self.title("Add_product")
        self.user=user
        self.ProductRecords = ProductRecords
        self.fake =False
        self.master=master
        self.ProductNameText = CTkLabel(self, text="Product name :")
        self.ProductNameComboBox = CTkComboBox(self, bg_color="black", width=220, values=self.ProductRecords.get_unique_product_names())
        self.BarCodeText = CTkLabel(self, text="Barcode :")
        self.BarCodeEntry = CTkEntry(self, bg_color="black", width=220)
        self.BarCodeEntryFake = CTkLabel(self, text_color="#888888", text=" ", anchor="w", fg_color=ThemeManager.theme["CTkEntry"]["fg_color"], corner_radius=ThemeManager.theme["CTkComboBox"]["corner_radius"], width=220)
        self.CustomerText = CTkLabel(self, text="Seller :")
        self.CustomerComboBox = CTkComboBox(self, bg_color="black", values=self.ProductRecords.get_unique_customers_by_process_type("Buy"), width=220)
        self.PaymentStatusText = CTkLabel(self, text="Payment status :")
        self.PaymentStatusComboBox = CTkComboBox(self, bg_color="black", values=self.ProductRecords.get_unique_payment_status(), width=220)
        self.UnitText = CTkLabel(self, text="Unit :")
        self.UnitComboBox = CTkComboBox(self, bg_color="black", width=220, values=self.ProductRecords.get_unique_product_units())
        self.PurchasePriceText = CTkLabel(self, text="Purchase Price :")
        self.PurchasePriceEntry = CTkEntry(self, bg_color="black", width=220)
        self.UnitComboBoxFake = CTkLabel(self, text="", text_color="#888888", anchor="w", fg_color=ThemeManager.theme["CTkComboBox"]["fg_color"], corner_radius=ThemeManager.theme["CTkComboBox"]["corner_radius"], width=218)
        self.PieceText = CTkLabel(self, text="Piece :")
        self.PieceEntry = CTkEntry(self, bg_color="black", width=70, font=CTkFont(size=18))

        self.SellingPriceText = CTkLabel(self, text="Selling price\nof a unit :", font=CTkFont(size=12))
        self.SellingPriceEntry = CTkEntry(self, bg_color="black", font=CTkFont(size=12), width=70, fg_color="black", border_color="#aa3333", border_width=1)


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
        self.UnitComboBox.set("")
        self.CustomerComboBox.set("")
        self.ProductNameComboBox.set("")
        self.PaymentStatusComboBox.set("")
        self.after(200, self.update_combobox)
        self.PieceEntry.bind("<Enter>", self.update_label)
        self.PieceEntry.bind("<KeyRelease>", self.update_label)
        self.SaveButton = CTkButton(self,text="",fg_color="black",hover=False,height=0,width=0,bg_color="red",command=self.save,image=CTkImage(Image.open(ICON+"save.png"),size=(30,30)))
        self.SaveButton.place(x=305,y=380)
        self.mainloop()
    
    def update_label(self, useless=None):
        if len(self.PieceEntry.get()) < 8:
            try:
                self.label_value.configure(text=str(int(self.PurchasePriceEntry.get())/int(self.PieceEntry.get())))
            except:
                pass
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
                product_dict = self.ProductRecords.get_first_data_with_process_type(new,"Buy")
                self.BarCodeEntry.delete(0, "end")
                self.PurchasePriceEntry.delete(0, "end")
                self.SellingPriceEntry.delete(0, "end")
                self.DescriptionEntry.delete(0,"end")
                self.PieceEntry.delete(0,"end")

                self.BarCodeEntry.insert(0, product_dict["barcode"])
                #self.PurchasePriceEntry.insert(0, product_dict["amount"])
                self.SellingPriceEntry.insert(0, product_dict["selling_price"])
                self.CustomerComboBox.set(product_dict["customer"])
                self.PaymentStatusComboBox.set(product_dict["payment_status"])
                self.DescriptionEntry.insert(0,product_dict["description"])
                self.PieceEntry.insert(0,"0")

                self.BarCodeEntry.place_forget()
                self.BarCodeEntryFake.configure(text=product_dict["barcode"])
                self.BarCodeEntryFake.place(x=115, y=60)
                self.UnitComboBox.place_forget()
                self.UnitComboBoxFake.configure(text=product_dict["unit"])
                self.UnitComboBoxFake.place(x=116, y=180)
                
                self.fake=True
            else:
                if self.fake:
                    self.PurchasePriceEntry.delete(0, "end")
                    self.SellingPriceEntry.delete(0, "end")
                    self.DescriptionEntry.delete(0,"end")
                    self.BarCodeEntry.delete(0,"end")
                    self.PurchasePriceEntry.insert(0, "0")
                    self.SellingPriceEntry.insert(0, "0")
                    self.CustomerComboBox.set("")
                    self.PaymentStatusComboBox.set("")
                self.fake=False
                self.UnitComboBoxFake.place_forget()
                self.UnitComboBox.place(x=115, y=180)
                self.BarCodeEntryFake.place_forget()
                self.BarCodeEntry.place(x=115, y=60)
                



        self.after(400, lambda: self.update_combobox(last=new))
    def convert_str(self,s):
        try:
            # Önce integer'a dönüştürmeyi dene
            int_value = int(s)
            return int_value if int_value != 0 else False
        except ValueError:
            # Eğer integer'a dönüştürme başarısız olursa, float'a dönüştürmeyi dene
            try:
                float_value = float(s)
                return float_value if float_value != 0.0 else False
            except ValueError:
                # Her iki dönüşüm de başarısız olursa False döndür
                return False

    def save(self):
        self.SaveButton.configure(command=None)
        print(self.PieceEntry.get())
        
        if self.CustomerComboBox.get() not in CSVManager().read_column() and self.CustomerComboBox.get()!="unknown" :
            self.after(10,lambda:self.SaveButton.configure(command=self.save))
            self.withdraw()
            self.after(20,lambda:Concubines_screen(customer=self.CustomerComboBox.get(),master=self,end_func=self.save))  
                

        elif self.ProductNameComboBox.get()=="":
            Messagebox(self,title="Product Name ComboBox",message="should not be empty")
        elif self.DescriptionEntry.get()=="":
            Messagebox(self,title="Description Entry",message="should not be empty")
        elif self.CustomerComboBox.get()=="":
            Messagebox(self,title="Seller ComboBox",message="should not be empty")
        
        elif self.PaymentStatusComboBox.get()=="":
            Messagebox(self,title="Payment Status ComboBox",message="should not be empty")
        elif not self.convert_str(self.PieceEntry.get()):
            Messagebox(self,title="Piece Entry",message="should not be empty or 0")
        elif not self.convert_str(self.PurchasePriceEntry.get()):
            Messagebox(self,title="Purchase Price Entry",message="should not be empty or 0")
        elif not self.convert_str(self.SellingPriceEntry.get()):
            Messagebox(self,title="Selling Price Entry",message="should not be empty or 0")

        elif self.fake:
            self.ProductRecords.add(self.ProductNameComboBox.get(),self.BarCodeEntryFake.cget("text"),"-"+self.PurchasePriceEntry.get(),self.SellingPriceEntry.get(),self.PieceEntry.get(),self.UnitComboBoxFake.cget("text"),self.user,"Buy",self.CustomerComboBox.get(),self.PaymentStatusComboBox.get(),self.DescriptionEntry.get())
            Messagebox(title="Succesfull",message="Your record is succesfull",icon="check",text_color="green")
            self.ProductNameComboBox.set("")

            self.update_combobox()
        elif self.BarCodeEntry.get()=="":
            Messagebox(self,title="Barcode Entry",message="should not be empty")
        elif self.UnitComboBox.get()=="":
            Messagebox(self,title="Unit ComboBox",message="should not be empty")
        else:
            self.ProductRecords.add(self.ProductNameComboBox.get(),self.BarCodeEntry.get(),"-"+self.PurchasePriceEntry.get(),self.SellingPriceEntry.get(),self.PieceEntry.get(),self.UnitComboBox.get(),self.user,"Buy",self.CustomerComboBox.get(),self.PaymentStatusComboBox.get(),self.DescriptionEntry.get())
            self.ProductNameComboBox.set("")
            Messagebox(title="Succesfull",message="Your record is succesfull",icon="check",text_color="green")
            self.update_combobox()
        self.after(1020,lambda:self.SaveButton.configure(command=self.save))
          
        
        
        """self.master.deiconify()
        self.withdraw()"""
        








###################################
###################################
class Record_screen(new_toplevel):

    def __init__(self,master,user,ProductRecords,list_=None,main=False,customer=None):
        super().__init__()
        self.calender=None
        self.list_=list_
        self.master=master
        self.title("Records")
        self.user=user
        self.master=master
        self.customer = customer
        self.list_=list_
        self.main = self.master if main else master.main
        self.ProductRecords=ProductRecords
        if len(self.ProductRecords.get_numerate_table())==0:
            self.withdraw()
            self.master.deiconify()
            self.destroy()
            Messagebox(icon="warning",title="Empyt",message="No record")

        else:
            self.after(100,self.wigdet())
    def wigdet(self):

        self.ProductRecords.refresh_for_time()
        self.geometry("1260x850+300+100")
        self.protocol("WM_DELETE_WINDOW",lambda:(self.master.deiconify(),self.withdraw(),self.title_menu.withdraw(),self.title_menu.destroy()))
        
        self.all_customer = True
        self.header=["no","Product Name","Barcode","Amount","Selling","Piece","Unit","Time","Date","User","Process Type","Customer","Payment status","Description","Regulation"]
        self.title_menu=TitleMenu(master=self,x_offset=315)
        self.master.withdraw()
        self.after(250,lambda:self.title_menu.add_cascade(text=f"user : {self.user}",hover=False))
        self.after(250,lambda:self.title_menu.add_cascade(text="◀",command=self.backstep))
        self.after(250,lambda:self.title_menu.add_cascade(text="re",hover_color="transparentcolor"))
        self.after(250,lambda:self.title_menu.add_entry(width=25))
        self.after(250,lambda:self.title_menu.menu_button.bind("<FocusIn>",lambda event: self.title_menu.menu_buttons[3].delete(0,"end")))
        self.after(250,lambda:self.title_menu.menu_button.bind("<FocusOut>",self.entry_delete))
        self.after(250,lambda:self.title_menu.menu_button.bind("<KeyRelease>", self.go_page))
        self.after(250,lambda:self.title_menu.add_cascade(text="▶",command=self.nobackstep))
        self.after(250,lambda:self.title_menu.add_cascade(text="Search within date",command=self.search_in_date))
        self.after(250,lambda:self.title_menu.add_cascade(text="Export Only this page"))
        self.after(250,lambda:self.title_menu.add_cascade(text="Export this page"))
        self.after(250,lambda:self.title_menu.add_cascade(text="",image=CTkImage(Image.open(ICON+"menu.png")),command=lambda:(self.main.deiconify(),self.withdraw())))
        self.bind("<Motion>",self.get_mouse_position)
        self.after(250,lambda:self.title_menu.bind("<Motion>",self.get_mouse_position))
        self.bottomFrame = CTkFrame(self)
        self.AmountLabel = CTkLabel(self.bottomFrame,text="Amount : ")
        self.AmountText = CTkLabel(self.bottomFrame,text=".")
        self.after(1200,lambda:self.bottomFrame.place(x=30,y=800))
        self.AmountLabel.place(x=10,y=30)
        self.AmountText.place(x=67,y=30)
        
        if self.list_ is None:
            self.ProductList=self.ProductRecords.get_numerate_table()
            self.list_=self.ProductList
            
        else:
            self.ProductList=self.ProductRecords.get_numerate(self.list_)
        ProductList=self.ProductList
        
        self.after(250,lambda:self.title_menu.menu_buttons[2].configure(text=str(int((len(self.ProductList)/25+0.999)))+"      /"))
        if len(ProductList)>25:
            self.SelectedProductList=self.ProductList[0:25]
            
        else:
            self.SelectedProductList=ProductList[0:len(ProductList)]
        
        if self.check_customer(self.ProductList) and self.ProductList[0][11]!="unknown":
            try:
                self.title(f"Customer : {self.ProductList[0][11]}")
                self.csvm=CSVManager()
                self.customer_info=self.csvm.get_row_by_name(self.ProductList[0][11])
                print(self.customer_info)
                for i,a in enumerate(list(self.customer_info)):
                    if a!="name":
                        CTkLabel(self.bottomFrame,text=f"{a}\n\n{self.customer_info[a]}").place(x=i*180+200,y=20)
            except:
                pass
            self.all_customer = False
        ################################THREADING##########################################"main"

        #export_command()
        if self.all_customer:
            thread_export_only = lambda: (
                self.withdraw(),
                Ecreater(self.SelectedProductList[1:]),
                ExtPDF("main",LIBREOFFICE),
                sleep(0.3),
                PDFviewerToplevel(master=self,name="Table.pdf"),
                print("bitti")
            )

        else:
            thread_export_only = lambda: (
                self.withdraw(),
                Ecreater(self.SelectedProductList[1:],filename="Data\\STable.xlsx"),
                ExtPDF("special",LIBREOFFICE,excel_file="Data\\STable.xlsx"),
                sleep(0.3),
                PDFviewerToplevel(master=self,name="STable.pdf"),
                print("bitti")
                )
            
        ####################################################################################

        if self.all_customer:
            thread_export = lambda: (
                self.withdraw(),
                Ecreater(self.ProductList),
                ExtPDF("main",LIBREOFFICE),
                
                sleep(0.3),
                PDFviewerToplevel(master=self,name="Table.pdf"),
                print("bitti")
                )
            
        else:
            thread_export = lambda: (
                self.withdraw(),
                Ecreater(self.ProductList,filename="Data\\STable.xlsx"),
                ExtPDF("special",LIBREOFFICE,excel_file="Data\\STable.xlsx"),
                
                sleep(0.3),
                PDFviewerToplevel(master=self,name="STable.pdf"),
                print("bitti")
                )
            

        ###################################################################################
        self.after(250,lambda:self.title_menu.menu_buttons[6].configure(command=lambda:thread_export_only()))
        self.after(250,lambda:self.title_menu.menu_buttons[7].configure(command=lambda:thread_export()))


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
        self.after(420,lambda:(
            self.geometry(f"{self.table.mainframe.winfo_width()+60}x900+300+100"),
            print(f"{self.table.mainframe.winfo_width()+50}x850")
        )
                   )
        self.after(120,self.AmountUpdate)
        self.after(500,self.pieceC)
    def pieceC(self):
        if self.check_product(self.ProductList):
            self.PieceText = CTkLabel(self.bottomFrame,text=".")
            self.PieceText.place(x=177,y=30)
            self.after(9,self.PieceUpdate())
    def check_customer(self,nested_list):
        if not nested_list or not all(len(sublist) > 11 for sublist in nested_list):
            return False
        
        elements = [sublist[11] for sublist in nested_list]
        return all(element == elements[0] for element in elements)
    def check_product(self,nested_list):
        if not nested_list or not all(len(sublist) > 1 for sublist in nested_list):
            return False
        
        elements = [sublist[1] for sublist in nested_list]
        return all(element == elements[0] for element in elements)
    def AmountUpdate(self):
        Amount=0
        for a in [r[3] for r in self.table.values]:
            try:
                Amount+=float(a)
            except:
                pass
        self.AmountText.configure(text=Amount)
        self.after(400,lambda:self.bottomFrame.configure(width=self.table.mainframe.winfo_width()))
        self.after(200000,self.AmountUpdate)
    def PieceUpdate(self):
        Piece=0
        for a in [r[5] for r in self.table.values]:
            try:
                Piece+=float(a)
            except:
                pass
        self.PieceText.configure(text=f"stok : {int(Piece)}")
        self.bottomFrame.configure(width=self.table.mainframe.winfo_width())
        self.after(200000,self.PieceUpdate)
    def get_mouse_position(self,event):
        x, y = event.x_root, event.y_root
        self.x=x
        self.y=y
    def date_func(self,date):
        selection=self.ProductRecords.get_by_date(self.calender.selection)
        if len(selection)!= 0 and selection!=self.list_:
            
            Record_screen(master=self,ProductRecords=self.ProductRecords,user=self.user,list_=selection)
        else:
            self.title_menu.menu_buttons[5].configure(command=self.search_in_date)
        
    def search_in_date(self):

        self.title_menu.menu_buttons[5].configure(command=None)

        print(self.title_menu.menu_buttons[5].cget("command"))

        self.calender=CTkCalender(all_hide=None,command=self.date_func,position=f"{self.x}+{self.y+20}")
        

        self.after(1000,lambda:self.title_menu.menu_buttons[5].configure(command=self.search_in_date))
            
    def get_page(self):
        self.entry_delete()
        return int(self.title_menu.menu_buttons[3].get())
    def go_page(self,useless=None):
        try:
            step=int(self.title_menu.menu_buttons[3].get())
        
            if 0<step*25:

                if step*25<len(self.ProductList):
                    self.SelectedProductList=self.ProductList[(step-1)*25:step*25]
                    self.SelectedProductList.insert(0,self.header)
                    self.table.update_values(self.SelectedProductList)
                elif (step-1)*25<len(self.ProductList) and step*25>len(self.ProductList):
                    self.SelectedProductList=self.ProductList[(step-1)*25:len(self.ProductList)]
                    self.SelectedProductList.insert(0,self.header)
                    self.table.update_values(self.SelectedProductList)
                else:
                    self.entry_delete()
                self.number_of(step)
        except:
            if self.title_menu.menu_buttons[3].get()=="":
                pass
            else:
                self.entry_delete()


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
        
        self.title_menu.menu_buttons[3].delete(0,"end")
        self.title_menu.menu_buttons[3].insert(0,step)
    def table_command(self,dict_,list_=None):
        if dict_["value"]!="" and dict_["row"]!=0:
            print(dict_)
            if dict_["column"]==11:
                list_new=self.ProductRecords.get_customer(dict_["value"])
            if dict_["column"]==1:
                list_new=self.ProductRecords.get_product(dict_["value"])
            if dict_["column"]==2:
                list_new=self.ProductRecords.get_barcode(dict_["value"])
            if dict_["column"]==6:
                list_new=self.ProductRecords.get_unit(dict_["value"])
            if dict_["column"]==10:
                list_new=self.ProductRecords.get_process_type(dict_["value"])
            if dict_["column"]==12:
                list_new=self.ProductRecords.get_payment_status(dict_["value"])
            if dict_["column"]==9:
                list_new=self.ProductRecords.get_user(dict_["value"])
            if  "list_new" in list(locals().keys()) :
                if list_new!=self.list_:
                    Record_screen(master=self,ProductRecords=self.ProductRecords,user=self.user,list_=list_new)
    def table_command_2(self,dict_,list_=None):
        if dict_["value"]!="" and dict_["value"] not in self.header:
            data=list(self.SelectedProductList[int(dict_["row"])])
            del data[0]
            
            print(".................................")
            data_row=self.ProductRecords.find_row_id(*data)
            print(data_row)
            self.withdraw()
            Repair_row_screen(data_row,self.ProductRecords,self.user,self)
            

    def entry_delete(self,useless=None):
        

        self.title_menu.menu_buttons[3].delete(0,"end")
        try:
            self.title_menu.menu_buttons[3].insert(0,str((self.ProductList.index(self.SelectedProductList[0])+1)//25+1))
        except:
            self.title_menu.menu_buttons[3].insert(0,str((self.ProductList.index(self.SelectedProductList[1])+1)//25+1))








###################################
###################################
class Repair_row_screen:
    def __init__(self, data_row, ProductRecords, user, master):
        self.toplevel = new_toplevel(all_hide=True)
        self.row = data_row
        self.ProductRecords = ProductRecords
        self.repair_data()
        self.toplevel.geometry("360x450+600+100")
        self.toplevel.title(f"Repair row : {data_row}        Date : {self.data[7]}        Time : {self.data[6]}")
        self.master = master
        self.user = user
        
        self.undo_button = CTkButton(self.toplevel,command=lambda: (Record_screen(self.master,self.user,self.ProductRecords,main=True), self.toplevel.withdraw()), width=30, height=30, text="", bg_color="black", fg_color="black",image=CTkImage(Image.open(ICON+"undo_24.png"), size=(20,20)))
        self.undo_button.place(x=200, y=400)

        self.delete_button = CTkButton(self.toplevel,command=self.delete_row, width=30, height=30, text="", bg_color="black", fg_color="black",image=CTkImage(Image.open(ICON+"Trash.png"), size=(20,20)))
        self.delete_button.place(x=300, y=400)

        self.update_button = CTkButton(self.toplevel,command=self.update_data ,width=30,height=30,text="",bg_color="black",fg_color="black", image=CTkImage(Image.open(ICON+"Cached.png"), size=(20,20)))
        self.update_button.place(x=250,y=400)

        self.ProductNameText = CTkLabel(self.toplevel, text="Product name :")
        self.ProductNameComboBox = CTkComboBox(self.toplevel, bg_color="black", width=220, values=self.ProductRecords.get_unique_product_names())
        self.ProductNameComboBox.set(self.data[0])
        self.CustomerText = CTkLabel(self.toplevel, text="Seller :")
        self.CustomerComboBox = CTkComboBox(self.toplevel, bg_color="black", values=self.ProductRecords.get_unique_customers(), width=220)
        self.PaymentStatusText = CTkLabel(self.toplevel, text="Payment status :")
        self.PaymentStatusComboBox = CTkComboBox(self.toplevel, bg_color="black", values=self.ProductRecords.get_unique_payment_status(), width=220)
        self.BarCodeText = CTkLabel(self.toplevel, text="Barcode :")
        self.BarCodeEntryFake = CTkLabel(self.toplevel, fg_color="black", text=" ", anchor="w", corner_radius=ThemeManager.theme["CTkComboBox"]["corner_radius"], width=220)
        self.PurchasePriceText = CTkLabel(self.toplevel, text="Amount Price :")
        self.PurchasePriceEntry = CTkEntry(self.toplevel, bg_color="black", width=220)
        
        self.UnitText = CTkLabel(self.toplevel, text="Unit :")
        self.UnitComboBoxFake = CTkLabel(self.toplevel,fg_color="black" ,text="", anchor="w",corner_radius=ThemeManager.theme["CTkComboBox"]["corner_radius"], width=218)
        self.PieceText = CTkLabel(self.toplevel, text="Piece :")
        self.PieceEntry = CTkEntry(self.toplevel, bg_color="black", width=70, font=CTkFont(size=18))

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
        if current_value >= value or self.data[9]!="Buy":
            self.PieceEntry.delete(0, 'end')
            self.PieceEntry.insert(0, str(current_value - value))
            self.update_label()

    def write_row(self):
        self.ProductNameComboBox.set(self.data[0])
        
        self.CustomerComboBox.set(self.data[10])
        self.PurchasePriceEntry.insert(0,self.data[2])
        self.SellingPriceEntry.insert(0,self.data[3])
        self.PaymentStatusComboBox.set(self.data[11])
        self.DescriptionEntry.insert(0,self.data[12])
        if self.data[9]=="Buy":
            self.DisposeButton = CTkButton(self.toplevel,text="Dispose",bg_color="black",fg_color="black",border_color="red",border_width=1,command=lambda:(self.toplevel.withdraw(),Dispose_screen(self.master,self.ProductRecords,self.row,self.user)))
            self.DisposeButton.place(y=400,x=40)
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
            self.ProductRecords.add(self.data[0],self.data[1],0.0,self.data[3],0,self.data[5],self.user,"Deleted","","",self.DescriptionEntry.get(),time=self.data[6],date=self.data[7],regulation=str(self.user+">"+self.data[8]+":"+self.data[13]))
        self.ProductRecords.refresh_for_time()
        self.close_window()
    def update_data(self):
        self.ProductRecords.delete_row(self.row)
        self.ProductRecords.add(self.ProductNameComboBox.get(),self.BarCodeEntryFake.cget("text"),self.PurchasePriceEntry.get(),self.SellingPriceEntry.get(),self.PieceEntry.get(),self.UnitComboBoxFake.cget("text"),self.user,self.data[9],self.CustomerComboBox.get(),self.PaymentStatusComboBox.get(),self.DescriptionEntry.get(),regulation=self.data[8]+">"+self.user+":"+self.data[13])

        self.close_window()
    def close_window(self):
        Record_screen(self.master,self.user,self.ProductRecords,main=True)
        self.toplevel.withdraw()









###################################
###################################
class Sell_screen(new_toplevel):
    def __init__(self, master,user, ProductRecords):
        super().__init__()
        self.geometry("1000x900+400+100")
        self.user=user
        self.ProductRecords=ProductRecords
        self.master = master
        self.EntryToplevelBool = False
        self.ProcessStatus = 1
        self.protocol("WM_DELETE_WINDOW",lambda:(master.deiconify(),self.withdraw()))
        self.title("     Shop"+120*" "+"User : "+self.user)

        self.options_frame = CTkFrame(self,fg_color="black",border_color="#cccccc",border_width=1,width=950,height=90)
        self.options_frame.place(x=25,y=5)
        self.ResultFrame = CTkFrame(self,fg_color="black",border_color="#cccccc",border_width=1,width=950,height=90)
        self.ResultFrame.place(x=30,y=800)

        self.BarcodeText = CTkLabel(self.options_frame,width=100,height=30,text="Barcode :")
        self.BarcodeEntry = CTkEntry(self.options_frame,height=30,width=140,fg_color="black",border_width=1,border_color="white")

        self.BarcodeText.place(x=560,y=30)
        self.BarcodeEntry.place(x=650,y=30)

        self.BarcodeEntry.bind("<KeyRelease>",self.ControlProduct)

        self.NameText = CTkLabel(self.options_frame,text="Product Name : ")
        self.NameOptionMenu = CTkOptionMenu(self.options_frame,values=self.ProductRecords.get_unique_product_names(),fg_color="#0f0f0f",button_color="#0f0f0f")
        self.NameOptionMenu.set("")
        
        self.NameOptionMenu.bind("<Button-1>",
                                 lambda event :self.after(50,  
                                                          self.ControlProduct))

        self.NameText.place(x=300,y=30)
        self.NameOptionMenu.place(x=410,y=30)

        self.CustomerText = CTkLabel(self.options_frame,height=30,text="Customer :")
        self.CustomerComboBox = CTkComboBox(self.options_frame,width=140,height=30,values=["unknown",*self.ProductRecords.get_unique_customers()] if "unknown" not in self.ProductRecords.get_unique_customers() else self.ProductRecords.get_unique_customers() )
        self.CustomerComboBox.set("unknown")
        self.CustomerText.place(x=30,y=30)
        self.CustomerComboBox.place(x=120,y=30)

        self.Status_positon = {"x":800,"y":30}



        self.ReturnButton = CTkButton(self.options_frame,height=30,width=140,text="change Return",command=self.ProcessStatusReturn,image=CTkImage(Image.open(ICON+"assignment_return_24.png")))
        self.SellButton = CTkButton(self.options_frame,height=30,width=140,text="change Sell",command=self.ProcessStatusSell)

        
        self.SaveButton = CTkButton(self.ResultFrame,height=30,fg_color="black",border_width=1,border_color="green",width=140,text="Sell",command=self.saveReceipt)
        
        
        self.SumLabel = CTkLabel(self.ResultFrame,text="Sum price : ")
        self.SumText = CTkLabel(self.ResultFrame,text="0",width=100,fg_color="#404040",corner_radius=5)

        self.SumLabel.place(x=20,y=30)
        self.SumText.place(x=100,y=30)

        self.PaymentStatusLabel = CTkLabel(self.ResultFrame,text="Select Payment \n Status :")
        self.PaymentStatusComboBox = CTkComboBox(self.ResultFrame,bg_color="black", values=self.ProductRecords.get_unique_payment_status(), width=120)

        self.PaymentStatusLabel.place(x=300,y=30)
        self.PaymentStatusComboBox.place(x=400,y=30)
        self.PaymentStatusComboBox.set("")

        self.DescriptionLabel = CTkLabel(self.ResultFrame,text="Description : ")
        self.DescriptionEntry = CTkEntry(self.ResultFrame)

        self.DescriptionLabel.place(x=550,y=30)
        self.DescriptionEntry.place(x=630,y=30)

        self.barcpode_column=1
        self.selling_price=2
        self.unit_column=3
        self.sum_column=4
        self.piece_column=6
        self.add_column=5
        self.subtract_column=self.piece_column+1
        self.trash_column=self.piece_column+2
        
        
        self.ReturnButton.place(**self.Status_positon)
        self.SaveButton.place(**self.Status_positon)

        self.ProductTable = CTkTable(self,
                                     values=[[]],
                                     colors=["#101010","#202020"],
                                     column_widths=[200,200,70,70,100,30,50,30,20,20],
                                     defualt_colums={self.piece_column:"1",
                                                     self.add_column:"+",
                                                     self.subtract_column:"-",
                                                     self.trash_column:ICON+"delete_forever_24.png***",
                                                     
                                                     },
                                     command=print,
                                     command_2=print,
                                     row_height=30,
                                     corner_radius=15)
        self.after(100,self.tableCommands)
        

        self.mainloop()
    def saveReceipt(self):
        now = datetime.now()
        
        time = now.strftime("%H:%M:%S")
        
        date = now.strftime("%d/%m/%Y")

        for row in self.ProductTable.values:
            self.ProductRecords.add(row[0],
                                    row[1],
                                    self.ProcessStatus*float(row[self.sum_column]),
                                    float(row[self.selling_price]),
                                    -int(row[self.piece_column])*self.ProcessStatus,
                                    row[self.unit_column],
                                    self.user,
                                    "Sell" if self.ProcessStatus==1 else "Return",
                                    self.CustomerComboBox.get() if self.CustomerComboBox.get()!="" else "unknown",
                                    self.PaymentStatusComboBox.get() if self.PaymentStatusComboBox.get()!="" else "?",
                                    description=self.DescriptionEntry.get() if self.DescriptionEntry.get()!="" else "no explanation",
                                    time=time,
                                    date=date
            )
        Messagebox(icon="check",title="",message="Succesfull",text_color="green")
        
        for i in range(self.ProductTable.rows):
            self.ProductTable.remove_row(0)
        if self.CustomerComboBox.get() not in CSVManager().read_column() and self.CustomerComboBox.get()!="unknown" :
            self.withdraw()
            Concubines_screen(customer=self.CustomerComboBox.get(),master=self)

    def SumPriceUpdate(self):
        price=0.0
        for p in [row[self.sum_column] for row in self.ProductTable.values]:
            price+=float(p)
        self.SumText.configure(text=str(price))
        self.after(100,self.SumPriceUpdate)
    def tableCommands(self):
        self.ProductTable.place(x=25,y=110)
        self.ProductTable.remove_row(0)
        self.ProductTable.column_special_command(
            self.add_column,
            lambda index :(
                index.update({"column":self.piece_column}),
                self.ProductTable.update_one_value(str(int(self.ProductTable.values[index["row"]][index["column"]])+1),index),
                self.ProductTable.update_one_value(float(self.ProductTable.values[index["row"]][self.piece_column])*float(self.ProductTable.values[index["row"]][self.selling_price]),row=index["row"],column=self.sum_column)
            )
        )
        self.ProductTable.column_special_command(
            self.subtract_column,
            lambda index :(
                index.update({"column":self.piece_column}),
                self.ProductTable.update_one_value(str(int(self.ProductTable.values[index["row"]][index["column"]])-1) if int(self.ProductTable.values[index["row"]][index["column"]])>0 else 0,index),
                self.ProductTable.remove_row(index["row"]) if self.ProductTable.values[index["row"]][index["column"]]==0 else None,
                self.ProductTable.update_one_value(float(self.ProductTable.values[index["row"]][self.piece_column])*float(self.ProductTable.values[index["row"]][self.selling_price]),row=index["row"],column=self.sum_column)
            )
        )
        self.ProductTable.column_special_command(
            self.trash_column,
            lambda index:(
                self.ProductTable.remove_row(index["row"])
            )
        )
        self.ProductTable.column_special_command(
            self.piece_column,
            self.Entry_piece
        )
        self.SumPriceUpdate()
    def ProcessStatusReturn(self):
        self.ProcessStatus=-1
        print("a")
        self.ReturnButton.place_forget()
        self.SaveButton.configure(border_color="red",text="Return")
        self.SellButton.place(**self.Status_positon)
    def ProcessStatusSell(self):
        print("b")
        self.ProcessStatus=1
        self.SellButton.place_forget()
        self.SaveButton.configure(border_color="green",text="Sell")
        self.ReturnButton.place(**self.Status_positon)
    def ControlProduct(self,useless=None):
        if useless is not None:
            ProductLastList = self.ProductRecords.get_barcode(self.BarcodeEntry.get())
            
        else:
            
            ProductLastList = self.ProductRecords.get_product(self.NameOptionMenu.get())
            print(self.NameOptionMenu.get())
            self.NameOptionMenu.set("")
        ProductLastList = ProductLastList if len(ProductLastList)!=0 else "empty"
        if ProductLastList!="empty":
            for i,a in enumerate([row[9] for row in ProductLastList]):
                if a=="Buy":
                    ProductLastList=ProductLastList[i]
                    break
            if ProductLastList[0] in [row[0] for row in self.ProductTable.values]:
                for i,a in enumerate([row[0] for row in self.ProductTable.values]):
                    if a==ProductLastList[0]:
                        row=i
                        break
                self.ProductTable.update_one_value(int(self.ProductTable.values[row][self.piece_column])+1,row=row,column=self.piece_column)
                self.ProductTable.update_one_value(float(self.ProductTable.values[row][self.piece_column])*float(self.ProductTable.values[row][self.selling_price]),row=row,column=self.sum_column)
            else:
                print(ProductLastList)
                self.ProductTable.add_row([ProductLastList[0],ProductLastList[1],ProductLastList[3],ProductLastList[5],ProductLastList[3]])
            if useless is not None:
                self.BarcodeEntry.delete(0,"end")
        print(ProductLastList)
    def Entry_piece(self,index=None,**kwargs):
        def ToplevelBool(self):
            self.EntryToplevelBool = False
        if self.EntryToplevelBool:
            pass
        else:
            self.EntryToplevelBool = True
            
            if index is None:
                index=kwargs
            Toplevel = new_toplevel(topmost=True)
            Toplevel.protocol("WM_DELETE_WINDOW",lambda:(ToplevelBool(self),Toplevel.destroy()))
            Toplevel.geometry(f"{self.winfo_pointerx()}+{self.winfo_pointery()}")
            index["column"]=self.piece_column
            Toplevel.title("     Piece")
            Entry = CTkEntry(Toplevel,width=100)
            Entry.pack()
            Entry.bind("<Return>",
                    lambda event, entry=Entry:(
                        self.ProductTable.update_one_value(entry.get(),index) if entry.get().isdigit() else None,
                        self.ProductTable.update_one_value(float(self.ProductTable.values[index["row"]][self.piece_column])*float(self.ProductTable.values[index["row"]][self.selling_price]),row=index["row"],column=self.sum_column),
                        ToplevelBool(self),
                        Toplevel.destroy()

                    ))
            
            Toplevel.after(299,Toplevel.focus)
            Toplevel.after(300,Entry.focus)
            print(Entry.focus_displayof())
    
            Toplevel.mainloop()

class PDFviewerToplevel:
    def __init__(self,master=None,name="STable.pdf",path=DATA):

        self.toplevel = new_toplevel()
        self.toplevel.resizable(1,1)
        if master is not None:
            self.toplevel.protocol("WM_DELETE_WINDOW", lambda: (master.deiconify(), self.toplevel.withdraw()))
        PDFViewer(self.toplevel,pdf_path=path+name)
        self.toplevel.mainloop()












###################################
###################################
class Concubines_screen:
    def __init__(self, master=None,user=None,customer=None,end_func=None):
        self.master=master
        if end_func is None:
            end_func=lambda:print("skip")
        self.toplevel=new_toplevel()
        self.end_func = end_func
        if master is not None:
            self.toplevel.protocol("WM_DELETE_WINDOW", lambda: (master.deiconify(),end_func(), self.toplevel.destroy()))
        else:
            self.toplevel.protocol("WM_DELETE_WINDOW", lambda:  self.toplevel.destroy())
        self.toplevel.geometry("320x305+600+100")
        self.master=master
        self.toplevel.title("Concubines")
        self.csvm=CSVManager()
        self.customer=customer
        self.user_is_main = True if user=="main" else False
        self.add_wigdet()
        self.toplevel.mainloop()
    def add_wigdet(self):
        wigdet={}
        for i,a in enumerate(self.csvm.get_column_names()):
            wigdet[a]=[CTkLabel(self.toplevel,text=f"{a} : ",width=150),CTkEntry(self.toplevel,width=150,bg_color="black")]
            wigdet[a][0].grid(row=i,column=0,pady=5,padx=5)
            wigdet[a][1].grid(row=i,column=1,pady=5,padx=5)
        if self.customer is not None:
            wigdet["name"][1].grid_forget()
            
            wigdet["name"][1]=CTkLabel(self.toplevel,text=self.customer,width=150 ,text_color="#cccccc", anchor="w", fg_color=ThemeManager.theme["CTkEntry"]["fg_color"],bg_color="black", corner_radius=ThemeManager.theme["CTkComboBox"]["corner_radius"])
            wigdet["name"][1].grid(row=0,column=1)
        self.wigdet=wigdet
        self.saveButton=CTkButton(self.toplevel,width=310,text="save",bg_color="black",command=self.save)
        self.saveButton.grid(columnspan=2,row=10,column=0,pady=10,padx=5)
    def save(self):
        savedict={}
        empty=False
        for i,a in enumerate(self.csvm.get_column_names()):
            try:
                savedict[a]=self.wigdet[a][1].get()
            except:
                savedict[a]=self.customer
        for i,a in enumerate(self.csvm.get_column_names()):
            if savedict[a]=="":
                empty=True
                Messagebox(title="Empty entry",message=f"Look at {a}")
        if not empty:
            self.toplevel.withdraw()
            self.csvm.add_row(savedict)
            self.csvm.save()
            self.end_func()
            Etc(self.csvm.to_2d_list(),)
            if self.master is not None:
                self.master.deiconify()
                
                self.toplevel.withdraw()
            self.toplevel.destroy()
        print(savedict)
class Dispose_screen:
    def __init__(self,master,ProductRecords,row,user):
        self.user=user
        self.toplevel=new_toplevel()
        self.toplevel.protocol("WM_DELETE_WINDOW", lambda:  (master.deiconify(),self.toplevel.destroy()))
        self.toplevel.geometry("320x420+600+200")
        self.ProductRecords=ProductRecords
        self.master=master
        self.row=row
        self.row_data=self.ProductRecords.get_by_row_id_as_dict(row)
        print(self.row_data)
        self.NameLabel = CTkLabel(self.toplevel,text="Product Name : ",width=150)
        self.NameText =  CTkLabel(self.toplevel, text_color="#dddddd", text=self.row_data["product_name"], anchor="w", fg_color=ThemeManager.theme["CTkEntry"]["fg_color"], corner_radius=ThemeManager.theme["CTkComboBox"]["corner_radius"], width=150)
        
        self.PieceLabel = CTkLabel(self.toplevel,text="Dispose Piece : ")
        self.PieceEntry = CTkEntry(self.toplevel,bg_color="black",width=150)

        self.DescriptionLabel = CTkLabel(self.toplevel,text="Description :")
        self.DescriptionEntry = CTkEntry(self.toplevel,bg_color="black",width=150)

        self.PaymentStatusLabel = CTkLabel(self.toplevel,text="Payment Status :")
        self.PaymentStatusCombobox = CTkComboBox(self.toplevel,values=self.ProductRecords.get_unique_payment_status(),width=150)
        self.PaymentStatusCombobox.set("")
        self.AddButton = CTkButton(self.toplevel,text="Add",command=self.save,width=310)


        self.NameLabel.grid(column=0,row=0,pady=5,padx=5)
        self.NameText.grid(column=1,row=0,pady=5,padx=5)
        self.PieceLabel.grid(row=1,column=0,pady=5,padx=5)
        self.PieceEntry.grid(column=1,row=1,pady=5,padx=5)
        self.DescriptionLabel.grid(column=0,row=2,pady=5,padx=5)
        self.DescriptionEntry.grid(column=1,row=2,pady=5,padx=5)
        self.PaymentStatusCombobox.grid(column=1,row=3,pady=5,padx=5)
        self.PaymentStatusLabel.grid(column=0,row=3,pady=5,padx=5)
        self.AddButton.grid(columnspan=2,row=4,column=0,pady=5,padx=5)
    def save(self):
        if self.PaymentStatusCombobox.get()!="" and self.PieceEntry.get().isdigit() and self.DescriptionEntry.get()!="":
            self.ProductRecords.add(self.row_data["product_name"],
                                    self.row_data["barcode"],
                                    float(self.row_data["selling_price"])*float(self.PieceEntry.get()),
                                    self.ProductRecords.get_first_data(self.row_data["product_name"])["selling_price"],
                                    -1*int(self.PieceEntry.get()),
                                    self.row_data["unit"],
                                    self.user,
                                    "Dispose",
                                    self.row_data["customer"],
                                    self.PaymentStatusCombobox.get(),
                                    self.DescriptionEntry.get()

                                    )
            self.toplevel.withdraw()
            self.master.deiconify()
        else:
            Messagebox(title="Look like something is empty",message="Something is empty.")
if __name__=="__main__":
    if Path(LIBREOFFICE).is_file():
        #PDFviewerToplevel()
        window_for_access()
        if False:
            if len(argv)==1:
                print("You have not access")
            elif argv[1]==datetime.now().strftime("%d/%m/%Y"):
                window_for_access()
            elif argv[1]=="3.1415926535897":
                if len(argv)==3:
                    if argv[2]==datetime.now().strftime("%d/%m/%Y"):
                        market_window("main")
            elif argv[1]=="eval":
                while 1:
                    try:
                        print(str(eval(input(">>>"))))
                    except Exception as e:
                        print(f"Error: {e}")
            else:
                print("You have not access\n\nWhat are you doing\n\n   ◌  #/#/#\n\n#/#/#")
            #Concubines_screen(customer="hilmi")
    else:
        Messagebox(message="Requirement is not installed, please download or check the file path \nLook LibreOfficePath.txt",title="Requirement",icon="warning").mainloop()
        