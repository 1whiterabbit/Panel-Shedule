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
#program2.attributes("-topmost",1) #isteğe bağlı. ben tercih etmiyorum 2. pencere için

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

excelsayfasi["A1"].value = "Linye No"
excelsayfasi["B1"].value = "Linye Türü"
excelsayfasi["C1"].value = "Faz"
excelsayfasi["D1"].value = "İletken Cinsi"
excelsayfasi["E1"].value = "Kablo Kesiti"
excelsayfasi["F1"].value = "Metraj"
excelsayfasi["G1"].value = "Güç"
excelsayfasi["H1"].value = "Akım"
excelsayfasi["I1"].value = "Sigorta"
excelsayfasi["J1"].value = "Gerilim Düşümü"

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

      l1 = box.get()

      y1 = "Linye 1"
      y2 = "Linye 2"
      y3 = "Linye 3"
      y4 = "Linye 4"
      y5 = "Linye 5"
      y6 = "Linye 6"
      y7 = "Linye 7"
      y8 = "Linye 8"
      y9 = "Linye 9"
      y10 = "Linye 10"
      y11 = "Linye 11"
      y12 = "Linye 12"
      y13 = "Linye 13"
      y14 = "Linye 14"
      y15 = "Linye 15"
      y16 = "Linye 16"
      y17 = "Linye 17"
      y18 = "Linye 18"
      y19 = "Linye 19"
      y20 = "Linye 20"
      y21 = "Linye 21"
      y22 = "Linye 22"
      y23 = "Linye 23"
      y24 = "Linye 24"
      y25 = "Linye 25"

      if l1 == y1:
          l0 = 1
      elif l1 == y2:
          l0 = 2
      elif l1 == y3:
          l0 = 3
      elif l1 == y4:
          l0 = 4
      elif l1 == y5:
          l0 = 5
      elif l1 == y6:
          l0 = 6
      elif l1 == y7:
          l0 = 7
      elif l1 == y8:
          l0 = 8
      elif l1 == y9:
          l0 = 9
      elif l1 == y10:
          l0 = 10
      elif l1 == y11:
          l0 = 11
      elif l1 == y12:
          l0 = 12
      elif l1 == y13:
          l0 = 13
      elif l1 == y14:
          l0 = 14
      elif l1 == y15:
          l0 = 15
      elif l1 == y16:
          l0 = 16
      elif l1 == y17:
          l0 = 17
      elif l1 == y18:
          l0 = 18
      elif l1 == y19:
          l0 = 19
      elif l1 == y20:
          l0 = 20
      elif l1 == y21:
          l0 = 21
      elif l1 == y22:
          l0 = 22
      elif l1 == y23:
          l0 = 23
      elif l1 == y24:
          l0 = 24
      elif l1 == y25:
          l0 = 25
      else:
          pass

      toplam_prizguc=int(p1)*teklipriz_guc+int(p2)*ikilipriz_guc+int(p3)*klemens_guc+int(p4)*kombinepriz_guc

      u1 = int(boxx1.get())
      akım1=float(toplam_prizguc/u1)
      akım1 = round(akım1, 2)

      if 0 < akım1 < 16:

            sigorta1 = "MCB C 16 A"

      elif 16 < akım1 < 20:

            sigorta1 = "MCB C 20 A"

      elif 20 < akım1 < 25:

            sigorta1 = "MCB C 25 A"

      elif 25 < akım1 < 40:

            sigorta1 = "MCB C 40 A"

      elif 40 < akım1 < 50:

            sigorta1 = "MCB C 50 A"

      elif 50 < akım1:

            sigorta1 = "MCB C 100 A"

      elif akım1==0:

            sigorta1 = "-----"

      else:
            pass

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

      l2=l0+1

      excelsayfasi["A{}".format(l2)].value = l0
      excelsayfasi["B{}".format(l2)].value = box2.get()
      excelsayfasi["C{}".format(l2)].value = sisfaz
      excelsayfasi["D{}".format(l2)].value = boxx.get()
      excelsayfasi["E{}".format(l2)].value = box1.get()
      excelsayfasi["F{}".format(l2)].value = lx
      excelsayfasi["G{}".format(l2)].value = toplam_prizguc
      excelsayfasi["H{}".format(l2)].value = akım1
      excelsayfasi["I{}".format(l2)].value = sigorta1
      excelsayfasi["J{}".format(l2)].value = yuzde_e1

      exceldosyasi.save("panel.xlsx")

      gerilim_dusumu_cikti1 = tk.Label(program2, text="\nLinye {} (Priz) :  Faz = {}  --  Kablo Türü = {}  --  Kesit = {} mm2  --  Metraj = {} Metre  --  Güç = {} Watt  --  Akım = {} Amper "
                                                      " --  Sigorta : {}  --  Gerilim Düşümü %e = {}".format(l0,sisfaz,boxx.get(),box1.get(),lx,toplam_prizguc,akım1,sigorta1,yuzde_e1)
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

      l1 = box.get()
      y1 = "Linye 1"
      y2 = "Linye 2"
      y3 = "Linye 3"
      y4 = "Linye 4"
      y5 = "Linye 5"
      y6 = "Linye 6"
      y7 = "Linye 7"
      y8 = "Linye 8"
      y9 = "Linye 9"
      y10 = "Linye 10"
      y11 = "Linye 11"
      y12 = "Linye 12"
      y13 = "Linye 13"
      y14 = "Linye 14"
      y15 = "Linye 15"
      y16 = "Linye 16"
      y17 = "Linye 17"
      y18 = "Linye 18"
      y19 = "Linye 19"
      y20 = "Linye 20"
      y21 = "Linye 21"
      y22 = "Linye 22"
      y23 = "Linye 23"
      y24 = "Linye 24"
      y25 = "Linye 25"

      if l1 == y1:
          l0 = 1
      elif l1 == y2:
          l0 = 2
      elif l1 == y3:
          l0 = 3
      elif l1 == y4:
          l0 = 4
      elif l1 == y5:
          l0 = 5
      elif l1 == y6:
          l0 = 6
      elif l1 == y7:
          l0 = 7
      elif l1 == y8:
          l0 = 8
      elif l1 == y9:
          l0 = 9
      elif l1 == y10:
          l0 = 10
      elif l1 == y11:
          l0 = 11
      elif l1 == y12:
          l0 = 12
      elif l1 == y13:
          l0 = 13
      elif l1 == y14:
          l0 = 14
      elif l1 == y15:
          l0 = 15
      elif l1 == y16:
          l0 = 16
      elif l1 == y17:
          l0 = 17
      elif l1 == y18:
          l0 = 18
      elif l1 == y19:
          l0 = 19
      elif l1 == y20:
          l0 = 20
      elif l1 == y21:
          l0 = 21
      elif l1 == y22:
          l0 = 22
      elif l1 == y23:
          l0 = 23
      elif l1 == y24:
          l0 = 24
      elif l1 == y25:
          l0 = 25
      else:
          pass

      u1 = int(boxx1.get())
      akım2=float(toplam_aydguc/u1)
      akım2 = round(akım2, 2)

      if 0 < akım2 < 10:

            sigorta2 = "MCB C 10 A"

      elif 10 < akım2 < 20:

            sigorta2 = "MCB C 20 A"

      elif 20 < akım2 < 25:

            sigorta2 = "MCB C 25 A"

      elif 25 < akım2 < 40:

            sigorta2 = "MCB C 40 A"

      elif 40 < akım2 < 50:

            sigorta2 = "MCB C 50 A"

      elif 50 < akım2:

            sigorta2 = "MCB C 100 A"

      elif akım2 == 0:

            sigorta2 = "-----"

      else:
            pass

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

      l2 = l0 + 1

      excelsayfasi["A{}".format(l2)].value = l0
      excelsayfasi["B{}".format(l2)].value = box2.get()
      excelsayfasi["C{}".format(l2)].value = sisfaz
      excelsayfasi["D{}".format(l2)].value = boxx.get()
      excelsayfasi["E{}".format(l2)].value = box1.get()
      excelsayfasi["F{}".format(l2)].value = lx
      excelsayfasi["G{}".format(l2)].value = toplam_aydguc
      excelsayfasi["H{}".format(l2)].value = akım2
      excelsayfasi["I{}".format(l2)].value = sigorta2
      excelsayfasi["J{}".format(l2)].value = yuzde_e2

      exceldosyasi.save("panel.xlsx")

      gerilim_dusumu_cikti2 = tk.Label(program2, text="\nLinye {} (Aydınlatma) :  Faz = {}  --  Kablo Türü = {}  --  Kesit = {} mm2  --  Metraj = {} Metre  --  Güç = {} Watt  --  Akım = {} Amper "
                                                      " --  Sigorta : {}  --  Gerilim Düşümü %e = {}".format(l0,sisfaz,boxx.get(),box1.get(),lx,toplam_aydguc,akım2,sigorta2,yuzde_e2),
                                                      bg="white", font="arial 8 bold")
      gerilim_dusumu_cikti2.pack()

    elif box2.get() == "Yedek":

        l1 = box.get()
        y1 = "Linye 1"
        y2 = "Linye 2"
        y3 = "Linye 3"
        y4 = "Linye 4"
        y5 = "Linye 5"
        y6 = "Linye 6"
        y7 = "Linye 7"
        y8 = "Linye 8"
        y9 = "Linye 9"
        y10 = "Linye 10"
        y11 = "Linye 11"
        y12 = "Linye 12"
        y13 = "Linye 13"
        y14 = "Linye 14"
        y15 = "Linye 15"
        y16 = "Linye 16"
        y17 = "Linye 17"
        y18 = "Linye 18"
        y19 = "Linye 19"
        y20 = "Linye 20"
        y21 = "Linye 21"
        y22 = "Linye 22"
        y23 = "Linye 23"
        y24 = "Linye 24"
        y25 = "Linye 25"

        if l1 == y1:
            l0 = 1
        elif l1 == y2:
            l0 = 2
        elif l1 == y3:
            l0 = 3
        elif l1 == y4:
            l0 = 4
        elif l1 == y5:
            l0 = 5
        elif l1 == y6:
            l0 = 6
        elif l1 == y7:
            l0 = 7
        elif l1 == y8:
            l0 = 8
        elif l1 == y9:
            l0 = 9
        elif l1 == y10:
            l0 = 10
        elif l1 == y11:
            l0 = 11
        elif l1 == y12:
            l0 = 12
        elif l1 == y13:
            l0 = 13
        elif l1 == y14:
            l0 = 14
        elif l1 == y15:
            l0 = 15
        elif l1 == y16:
            l0 = 16
        elif l1 == y17:
            l0 = 17
        elif l1 == y18:
            l0 = 18
        elif l1 == y19:
            l0 = 19
        elif l1 == y20:
            l0 = 20
        elif l1 == y21:
            l0 = 21
        elif l1 == y22:
            l0 = 22
        elif l1 == y23:
            l0 = 23
        elif l1 == y24:
            l0 = 24
        elif l1 == y25:
            l0 = 25
        else:
            pass

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

        l2 = l0 + 1

        tire = "(null)"

        excelsayfasi["A{}".format(l2)].value = l0
        excelsayfasi["B{}".format(l2)].value = box2.get()
        excelsayfasi["C{}".format(l2)].value = sisfaz
        excelsayfasi["D{}".format(l2)].value = tire
        excelsayfasi["E{}".format(l2)].value = tire
        excelsayfasi["F{}".format(l2)].value = tire
        excelsayfasi["G{}".format(l2)].value = tire
        excelsayfasi["H{}".format(l2)].value = tire
        excelsayfasi["I{}".format(l2)].value = tire
        excelsayfasi["J{}".format(l2)].value = tire

        exceldosyasi.save("panel.xlsx")

        gerilim_dusumu_cikti2 = tk.Label(program2,text="\nLinye {} (Yedek) :  Faz = {}  --  Kablo Türü = {} --  Kesit = {} mm2  --  Metraj = {} --  Güç = {} -- Akım = {} "
                                            "-- Sigorta : {} -- Gerilim Düşümü %e = {}".format(l0,sisfaz,tire,tire,tire,tire,tire,tire,tire,),bg="white",
                                            font="arial 8 bold")
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
