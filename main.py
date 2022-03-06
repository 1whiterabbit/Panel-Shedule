import tkinter as tk
from tkinter.ttk import *

from openpyxl import Workbook,load_workbook

program=tk.Tk()
program.title("Data Entry Page")
program.geometry("260x450+110+200")
program.resizable(False,False)
program.config(bg="white")
program.iconbitmap("molecule.ico")
program.attributes("-topmost",1)

program2=tk.Tk()
program2.title("Panel Schedule Page")
program2.geometry("1100x450+390+200")
program2.resizable(False,True)
program2.minsize(1000,200)
program2.config(bg="white")
program2.iconbitmap("molecule.ico")
#program2.attributes("-topmost",1) #

#

linyeno=tk.Label(program,text="Linye Numarası:",fg="black",bg="white", font="arial 8 bold")
linyeno.place(x=10,y=10)

linyenumaralari= ["Linye 1","Linye 2","Linye 3","Linye 4","Linye 5","Linye 6","Linye 7","Linye 8","Linye 9","Linye 10","Linye 11","Linye 12",
                  "Linye 13","Linye 14","Linye 15","Linye 16","Linye 17","Linye 18","Linye 19","Linye 20","Linye 21","Linye 22","Linye 23",
                  "Linye 24","Linye 25"]

y1=tk.StringVar()

box=Combobox(program,values=linyenumaralari,width=8,height=5,textvariable=y1)
box.pack()
box.place(x=110,y=10)

#

linyeno=tk.Label(program,text="Linye Türü:",fg="black",bg="white", font="arial 8 bold")
linyeno.place(x=10,y=38)

linyecesidi= ["Priz","Aydınlatma","Yedek"]

y2=tk.StringVar()

box2=Combobox(program,values=linyecesidi,height=5,textvariable=y2,width=10)
box2.pack()
box2.place(x=110,y=38)

faz = tk.IntVar()
faz.set(1)

faz2 = tk.IntVar()
faz2.set(1)

kablo = tk.IntVar()
kablo.set(1)

kesitbox =[1.5,2.5,4,6,10,16,25,35,50,70,95,120,150]

turbox=["NHXMH","N2XH","NYY","NYM"]

gerilimsev=[220,230,380,400]

exceldosyasi=load_workbook("panel.xlsx")

excelsayfasi=exceldosyasi.active

class excelgiris:

    def __init__(self,satir,linyeno,linyeturu,faz,iletkencinsi,kablokesiti,metraj,guc,akim,sigorta,gerilimdusumu):
        self.satir = satir
        self.linyeno = linyeno
        self.linyeturu = linyeturu
        self.faz = faz
        self.iletkencinsi = iletkencinsi
        self.kablokesiti = kablokesiti
        self.metraj = metraj
        self.guc = guc
        self.akim = akim
        self.sigorta = sigorta
        self.gerilimdusumu = gerilimdusumu

    def giris(self):
        excelsayfasi["A{}".format(self.satir)].value = self.linyeno
        excelsayfasi["B{}".format(self.satir)].value = self.linyeturu
        excelsayfasi["C{}".format(self.satir)].value = self.faz
        excelsayfasi["D{}".format(self.satir)].value = self.iletkencinsi
        excelsayfasi["E{}".format(self.satir)].value = self.kablokesiti
        excelsayfasi["F{}".format(self.satir)].value = self.metraj
        excelsayfasi["G{}".format(self.satir)].value = self.guc
        excelsayfasi["H{}".format(self.satir)].value = self.akim
        excelsayfasi["I{}".format(self.satir)].value = self.sigorta
        excelsayfasi["J{}".format(self.satir)].value = self.gerilimdusumu

ilksatir=excelgiris(1,"Linye No","Linye Türü","Faz","İletken Cinsi","Kablo Kesiti","Metraj","Güç","Akım","Sigorta","Gerilim Düşümü")
ilksatir.giris()

class sigortasecimi:

    def __init__(self,akim):
        self.akim=akim

    def secim(self):

        if 0 < self.akim < 16:
            return "MCB C 16 A"
        elif 16 <= self.akim < 20:
            return "MCB C 20 A"
        elif 20 <= self.akim < 25:
            return "MCB C 25 A"
        elif 25 <= self.akim < 40:
            return "MCB C 40 A"
        elif 40 <= self.akim < 50:
            return "MCB C 50 A"
        elif 50 <= self.akim:
            return "MCB C 100 A"
        elif self.akim == 0:
            return "-----"
        else:
            pass

#

def ilerle():

 def islem():
     
    if box2.get() == "Priz":

      p1=spinbox1.get()
      p2=spinbox2.get()
      p3=spinbox3.get()
      p4=spinbox4.get()

      teklipriz_guc=300
      ikilipriz_guc=600
      klemens_guc=1000
      kombinepriz_guc=1500

      toplam_prizguc=int(p1)*teklipriz_guc+int(p2)*ikilipriz_guc+int(p3)*klemens_guc+int(p4)*kombinepriz_guc

      u1 = int(boxx1.get())
      akım1=float(toplam_prizguc/u1)
      akım1 = round(akım1, 2)

      prizsigortasec = sigortasecimi(akım1) # obje tanımlama #
      sigorta1 = prizsigortasec.secim()

      if (faz.get() == 1):
          f = 200
      elif (faz.get() == 2):
          f = 100
      else:
          pass

      if (kablo.get() == 1):
          k = 56
      elif (kablo.get() == 2):
          k = 35
      else:
          pass

      if box2.get() == "Priz":
          n = toplam_prizguc
      elif box2.get() == "Aydınlatma":
          n = toplam_aydguc
      else:
          pass

      if faz2.get()==1:
          sisfaz="R"
      elif faz2.get()==2:
          sisfaz="S"
      elif faz2.get()==3:
          sisfaz="T"
      elif faz2.get()==4:
          sisfaz="R-S-T"
      else:
          pass

      lx = int(metraj_giris.get())

      s = float(box1.get())
      yuzde_e1 = (f * lx * n) / (k * s * u1 * u1)  # l=uzunluk, n=güç, k=iletkenlik katsayısı, s=kablo kesiti
      yuzde_e1 = round(yuzde_e1, 2)

      l1 = box.get()
      xx = []
      xx = l1.split()
      l0 = int (xx[1])

      l2=l0+1

      prizgiris = excelgiris(l2, l0, box2.get(), sisfaz, boxx.get(), box1.get(), lx, toplam_prizguc, akım1, sigorta1, yuzde_e1) # obje tanımlama #
      prizgiris.giris()
      exceldosyasi.save("panel.xlsx")

      gerilim_dusumu_cikti1 = tk.Label(program2, text="\nLinye {} (Priz) :  Faz = {}  --  Kablo Türü = {}  --  Kesit = {} mm2  --  Metraj = {} Metre  --  Güç = {} Watt  --  Akım = {} Amper "
                                                      " --  Sigorta : {}  --  Gerilim Düşümü %e = {}".format(l0,sisfaz,boxx.get(),box1.get(),lx,toplam_prizguc,akım1, sigorta1,yuzde_e1)
                                                      ,bg="white", font="arial 8 bold")
      gerilim_dusumu_cikti1.pack()

    elif box2.get() == "Aydınlatma":

      a1=spinbox5.get()
      a2=spinbox6.get()
      a3=spinbox7.get()
      a4=spinbox8.get()

      sl1_guc=22
      sl2_guc=38
      ul1_guc=33
      ul2_guc=31

      toplam_aydguc=int(a1)*sl1_guc+int(a2)*sl2_guc+int(a3)*ul1_guc+int(a4)*ul2_guc

      u1 = int(boxx1.get())
      akım2=float(toplam_aydguc/u1)
      akım2 = round(akım2, 2)

      aydsigortasec = sigortasecimi(akım2)
      sigorta2 = aydsigortasec.secim()

      if (faz.get() == 1):
          f = 200
      elif (faz.get() == 2):
          f = 100
      else:
          pass

      if (kablo.get() == 1):
          k = 56
      elif (kablo.get() == 2):
          k = 35
      else:
          pass

      if box2.get() == "Priz":
          n = toplam_prizguc
      elif box2.get() == "Aydınlatma":
          n = toplam_aydguc
      else:
          pass

      if faz2.get()==1:
          sisfaz="R"
      elif faz2.get()==2:
          sisfaz="S"
      elif faz2.get()==3:
          sisfaz="T"
      elif faz2.get()==4:
          sisfaz="R-S-T"
      else:
          pass

      lx = int(metraj_giris.get())
      s = float(box1.get())
      yuzde_e2 = (f * lx * n) / (k * s * u1 * u1)  # l=uzunluk, n=güç, k=iletkenlik katsayısı, s=kablo kesiti
      yuzde_e2 = round(yuzde_e2, 2)

      l1 = box.get()
      xx = []
      xx = l1.split()
      l0 = int(xx[1])

      l2 = l0 + 1

      aydgiris = excelgiris(l2, l0, box2.get(), sisfaz, boxx.get(), box1.get(), lx, toplam_aydguc, akım2, sigorta2, yuzde_e2)
      aydgiris.giris()
      exceldosyasi.save("panel.xlsx")

      gerilim_dusumu_cikti2 = tk.Label(program2, text="\nLinye {} (Aydınlatma) :  Faz = {}  --  Kablo Türü = {}  --  Kesit = {} mm2  --  Metraj = {} Metre  --  Güç = {} Watt  --  Akım = {} Amper "
                                                      " --  Sigorta : {}  --  Gerilim Düşümü %e = {}".format(l0,sisfaz,boxx.get(),box1.get(),lx,toplam_aydguc,akım2,sigorta2,yuzde_e2),
                                                      bg="white", font="arial 8 bold")
      gerilim_dusumu_cikti2.pack()

    elif box2.get() == "Yedek":

        if faz2.get() == 1:
            sisfaz = "R"
        elif faz2.get() == 2:
            sisfaz = "S"
        elif faz2.get() == 3:
            sisfaz = "T"
        elif faz2.get() == 4:
            sisfaz = "R-S-T"
        else:
            pass

        l1 = box.get()
        xx = []
        xx = l1.split()
        l0 = int(xx[1])

        l2 = l0 + 1

        aydgiris = excelgiris(l2, l0, box2.get(), sisfaz, "(null)", "(null)", "(null)", "(null)", "(null)", "(null)","(null)")
        aydgiris.giris()
        exceldosyasi.save("panel.xlsx")

        gerilim_dusumu_cikti2 = tk.Label(program2,text="\nLinye {} (Yedek) :  Faz = {}  --  Kablo Türü = {} --  Kesit = {} mm2  --  Metraj = {} --  Güç = {} -- Akım = {} "
                                            "-- Sigorta : {} -- Gerilim Düşümü %e = {}".format(l0,sisfaz,"(null)","(null)",
                                            "(null)","(null)","(null)","(null)","(null)"),bg="white",font="arial 8 bold")
        gerilim_dusumu_cikti2.pack()

    else:
       pass

    if box2.get() == "Priz": #sürekli butonları bloklayıp tekrardan aynı verileri giriyorduk. kaldırdık

        pass

        #box.delete(0, "end")
        #box2.delete(0, "end")

        #spinbox1.delete(0, "end")
        #spinbox2.delete(0, "end")
        #spinbox3.delete(0, "end")
        #spinbox4.delete(0, "end")

        #spinbox1["state"] = "disabled"
        #spinbox2["state"] = "disabled"
        #spinbox3["state"] = "disabled"
        #spinbox4["state"] = "disabled"

        #metraj_giris.delete(0, "end")

        #radio1["state"] = "disabled"
        #radio2["state"] = "disabled"
        #radio3["state"] = "disabled"
        #radio4["state"] = "disabled"
        #radio5["state"] = "disabled"
        #radio6["state"] = "disabled"
        #radio7["state"] = "disabled"
        #radio8["state"] = "disabled"

        #boxx1["state"] = "disabled"
        #boxx["state"] = "disabled"
        #box1["state"] = "disabled"
        #metraj_giris["state"] = "disabled"

    elif box2.get() == "Aydınlatma": #sürekli butonları bloklayıp tekrardan aynı verileri giriyorduk. kaldırdık

        pass

        #box.delete(0, "end")
        #box2.delete(0, "end")

        #spinbox5.delete(0, "end")
        #spinbox6.delete(0, "end")
        #spinbox7.delete(0, "end")
        #spinbox8.delete(0, "end")

        #metraj_giris.delete(0, "end")

        #spinbox5["state"] = "disabled"
        #spinbox6["state"] = "disabled"
        #spinbox7["state"] = "disabled"
        #spinbox8["state"] = "disabled"

        #radio1["state"] = "disabled"
        #radio2["state"] = "disabled"
        #radio3["state"] = "disabled"
        #radio4["state"] = "disabled"
        #radio5["state"] = "disabled"
        #radio6["state"] = "disabled"
        #radio7["state"] = "disabled"
        #radio8["state"] = "disabled"

        #boxx1["state"] = "disabled"
        #boxx["state"] = "disabled"
        #box1["state"] = "disabled"
        #metraj_giris["state"] = "disabled"

    elif box2.get() == "Yedek":

        boxx1.delete(0, "end")
        box.delete(0, "end")
        box2.delete(0, "end")

        boxx1["state"] = "disabled"
        boxx["state"] = "disabled"
        box1["state"] = "disabled"
        metraj_giris["state"] = "disabled"

    else:
        pass

 hesapla = tk.Button(program, text="Hesapla",width=8, bg="black", fg="white", command=islem)
 hesapla.place(x=90, y=410)

 fazsayisi = tk.Label(program, text="Faz Sayısı         :", bg="white", fg="black", font="arial 8 bold")
 fazsayisi.place(x=10, y=100)

 kablo_cinsi = tk.Label(program, text="İletken Türü    :", bg="white", fg="black", font="arial 8 bold")
 kablo_cinsi.place(x=10, y=124)

 sistemfazi = tk.Label(program, text="Linye Fazı        :", bg="white", fg="black", font="arial 8 bold")
 sistemfazi.place(x=10, y=147)

 radio1 = tk.Radiobutton(program, text="1 Faz", bg="white", variable=faz, value=1, activebackground="red")
 radio1.place(x=100, y=100)

 radio2 = tk.Radiobutton(program, text="3 Faz", bg="white", variable=faz, value=2, activebackground="red")
 radio2.place(x=166, y=100)

 radio3 = tk.Radiobutton(program, text="Cu", bg="white", variable=kablo, value=1, activebackground="red")
 radio3.place(x=100, y=122)

 radio4 = tk.Radiobutton(program, text="Al", bg="white", variable=kablo, value=2, activebackground="red")
 radio4.place(x=166, y=122)

 radio5 = tk.Radiobutton(program, text="R", bg="white", variable=faz2, value=1, activebackground="red")
 radio5.place(x=100, y=145)

 radio6 = tk.Radiobutton(program, text="S", bg="white", variable=faz2, value=2, activebackground="red")
 radio6.place(x=133, y=145)

 radio7 = tk.Radiobutton(program, text="T", bg="white", variable=faz2, value=3, activebackground="red")
 radio7.place(x=166, y=145)

 radio8 = tk.Radiobutton(program, text="R-S-T", bg="white", variable=faz2, value=4, activebackground="red")
 radio8.place(x=199, y=145)

 xx3 = tk.StringVar()

 gerilimseviyesi = tk.Label(program, text="Voltaj Değeri   :                     Volt", bg="white", fg="black", font="arial 8 bold")
 gerilimseviyesi.place(x=10, y=172)

 boxx1 = Combobox(program, values=gerilimsev, width=4, height=4, textvariable=xx3)
 boxx1.place(x=100, y=172)

 xx2 = tk.StringVar()

 kablotur = tk.Label(program, text="Kablo Türü       :", bg="white", fg="black", font="arial 8 bold")
 kablotur.place(x=10, y=200)

 boxx = Combobox(program, values=turbox, width=8, height=4, textvariable=xx2)
 boxx.place(x=100, y=200)

 xx1 = tk.StringVar()

 kesit = tk.Label(program, text="Kesit                 :                     mm2", bg="white", fg="black", font="arial 8 bold")
 kesit.place(x=10, y=227)

 box1 = Combobox(program, values=kesitbox, width=4, height=6, textvariable=xx1)
 box1.place(x=100, y=227)

 metraj = tk.Label(program, text="Metraj               :                Metre", bg="white", fg="black", font="arial 8 bold")
 metraj.place(x=10, y=258)

 metraj_giris = tk.Entry(program, bg="white", fg="black", bd=4 , width=4 )
 metraj_giris.place(x=100, y=255)

 #

 if box2.get() == "Priz":

     aydadetlabel1 = tk.Label(program, text="Opal DownLED :                22 Watt", fg="white", bg="white", font="arial 8 bold")
     aydadetlabel1.place(x=10, y=285)

     aydadetlabel2 = tk.Label(program, text="Opal LED           :                38 Watt", fg="white", bg="white", font="arial 8 bold")
     aydadetlabel2.place(x=10, y=315)

     aydadetlabel3 = tk.Label(program, text="Lineer LED       :                33 Watt", fg="white", bg="white", font="arial 8 bold")
     aydadetlabel3.place(x=10, y=345)

     aydadetlabel4 = tk.Label(program, text="Etanj LED          :                31 Watt", fg="white", bg="white", font="arial 8 bold")
     aydadetlabel4.place(x=10, y=375)

     #

     prizlabel1 = tk.Label(program, text="Tekli Şebeke  :                300 Watt", fg="black", bg="white", font="arial 8 bold")
     prizlabel1.place(x=10, y=285)

     x1 = tk.StringVar(value="0")

     spinbox1 = tk.Spinbox(program, to=20, textvariable=x1, font="arial 8 bold", bd=5, width=2, justify="center")
     spinbox1.pack()
     spinbox1.place(x=100, y=285)

     #

     prizlabel2 = tk.Label(program, text="İkili Şebeke     :                600 Watt", fg="black", bg="white", font="arial 8 bold")
     prizlabel2.place(x=10, y=315)

     x2 = tk.StringVar(value="0")

     spinbox2 = tk.Spinbox(program, to=20, textvariable=x2, font="arial 8 bold", bd=5, width=2, justify="center")
     spinbox2.pack()
     spinbox2.place(x=100, y=315)

     #

     prizlabel3 = tk.Label(program, text="Klemens          :                1000 Watt", fg="black", bg="white", font="arial 8 bold")
     prizlabel3.place(x=10, y=345)

     x3 = tk.StringVar(value="0")

     spinbox3 = tk.Spinbox(program, to=20, textvariable=x3, font="arial 8 bold", bd=5, width=2, justify="center")
     spinbox3.pack()
     spinbox3.place(x=100, y=345)

     #

     prizlabel4 = tk.Label(program, text="Kombine Priz  :                1500 Watt", fg="black", bg="white", font="arial 8 bold")
     prizlabel4.place(x=10, y=375)

     x4 = tk.StringVar(value="0")

     spinbox4 = tk.Spinbox(program, to=20, textvariable=x4, font="arial 8 bold", bd=5, width=2, justify="center")
     spinbox4.pack()
     spinbox4.place(x=100, y=375)

     #

 elif box2.get() == "Aydınlatma":

     prizlabel1 = tk.Label(program, text="Tekli Şebeke  :                300 Watt", fg="white", bg="white", font="arial 8 bold")
     prizlabel1.place(x=10, y=285)

     prizlabel2 = tk.Label(program, text="İkili Şebeke     :                600 Watt", fg="white", bg="white", font="arial 8 bold")
     prizlabel2.place(x=10, y=315)

     prizlabel3 = tk.Label(program, text="Klemens          :                1000 Watt", fg="white", bg="white", font="arial 8 bold")
     prizlabel3.place(x=10, y=345)

     prizlabel4 = tk.Label(program, text="Kombine Priz  :                1500 Watt", fg="white", bg="white", font="arial 8 bold")
     prizlabel4.place(x=10, y=375)

     #

     aydadetlabel1 = tk.Label(program, text="Opal DownLED :                22 Watt", fg="black", bg="white", font="arial 8 bold")
     aydadetlabel1.place(x=10, y=285)

     x5 = tk.StringVar(value="0")

     spinbox5 = tk.Spinbox(program, to=20, textvariable=x5, font="arial 8 bold", bd=5, width=2, justify="center")
     spinbox5.pack()
     spinbox5.place(x=100, y=285)

     #

     aydadetlabel2 = tk.Label(program, text="Opal LED           :                38 Watt", fg="black", bg="white", font="arial 8 bold")
     aydadetlabel2.place(x=10, y=315)

     x6 = tk.StringVar(value="0")

     spinbox6 = tk.Spinbox(program, to=20, textvariable=x6, font="arial 8 bold", bd=5, width=2, justify="center")
     spinbox6.pack()
     spinbox6.place(x=100, y=315)

     #

     aydadetlabel3 = tk.Label(program, text="Lineer LED       :                33 Watt", fg="black", bg="white", font="arial 8 bold")
     aydadetlabel3.place(x=10, y=345)

     x7 = tk.StringVar(value="0")

     spinbox7 = tk.Spinbox(program, to=20, textvariable=x7, font="arial 8 bold", bd=5, width=2, justify="center")
     spinbox7.pack()
     spinbox7.place(x=100, y=345)

     #

     aydadetlabel4 = tk.Label(program, text="Etanj LED          :                31 Watt", fg="black", bg="white", font="arial 8 bold")
     aydadetlabel4.place(x=10, y=375)

     x8 = tk.StringVar(value="0")

     spinbox8 = tk.Spinbox(program, to=20, textvariable=x8, font="arial 8 bold", bd=5, width=2, justify="center")
     spinbox8.pack()
     spinbox8.place(x=100, y=375)

 elif box2.get() == "Yedek":

     radio1["state"] = "disabled"
     radio2["state"] = "disabled"
     radio3["state"] = "disabled"
     radio4["state"] = "disabled"

     boxx1["state"] = "disabled"
     boxx["state"] = "disabled"
     box1["state"] = "disabled"
     metraj_giris["state"] = "disabled"

     frame1 = tk.Frame(program, height=125, width=260, bg="white") #yedek için spinboxlara perde
     frame1.pack()
     frame1.place(y=280)

 else:
     pass

ileri=tk.Button(program,text="Set",bg="black",width=8, fg="white",command=ilerle)
ileri.place(x=90, y=65)

program.mainloop()
