import tkinter
class abc():
    def __init__(self):
        self.pencerem=tkinter.Tk()
        self.etiket_turler=tkinter.Label(self.pencerem,text="TÜRLER").grid(row=0,column=0)
        self.etiket_filmler=tkinter.Label(self.pencerem,text="FİMLER").grid(row=0,column=1)
        self.kümem=set()
        dosyam=open("oscars.txt","r")
        for line in dosyam:
            line=line.rstrip()
            line=line.split(",")
            self.kümem.add(line[1])
        dosyam.close()
        self.listem1=list(self.kümem)
        self.listem1.sort()
        self.listetutucu=tkinter.StringVar()
        self.listekutum=tkinter.Listbox(self.pencerem,width=9,height=len(self.listem1),listvariable=self.listetutucu)
        self.listekutum.grid(row=1,column=0,pady=10,sticky="n",padx=5)
        self.listetutucu.set(tuple(self.listem1))
        self.listekutum.bind("<<ListboxSelect>>",self.filmgetir)
        self.yöncubugum=tkinter.Scrollbar(self.pencerem,orient=tkinter.VERTICAL)
        self.yöncubugum.grid(row=1,column=2,sticky="ns")
        self.listetutucu2=tkinter.StringVar()
        self.listekutum2=tkinter.Listbox(self.pencerem,width=45,height=len(self.listem1),listvariable=self.listetutucu2,yscrollcommand=self.yöncubugum.set)
        self.yöncubugum.config(command=self.listekutum2.yview)


        self.listekutum2.grid(row=1,column=1,sticky="n",pady=10,padx=5)
        tkinter.mainloop()
    def filmgetir(self,e):
        self.index=self.listekutum.get(self.listekutum.curselection())
        l=[]
        dosyam=open("oscars.txt","r")
        for line in dosyam:
            line=line.rstrip()
            line=line.split(",")
            if self.index==line[1]:
                l.append(line[0])
        dosyam.close()
        self.listetutucu2.set(tuple(l))        
abc()        





        
        