import os

os.chdir("C:/Users/urbi1/Desktop/scrapy/Clases")
import clase_D1
import clase_Lavaquita

class supermercados:
    def __init__(self,Nombre_super,ID,tipo) -> None:
        self.Nombre_super = Nombre_super
        self.ID = ID
        self.tipo = tipo
        self.instance = clase_D1.D1(tipo) if Nombre_super == "D1" else clase_Lavaquita.Vaquita(tipo)
        
    def getNombre_super(self):
        return self.Nombre_super

    def setNombre_super(self):
        self.Nombre_super = str(input())

    def getID(self):
        return self.ID
    
    def setID(self):
        self.ID = int(input())

    def getTipo(self):
        return self.tipo

    def setTipo(self):
        self.tipo = str(input())

    def __getattr__(self, name):
        # assume it is implemented by self.instance
        return self.instance.__getattribute__(name)

supermercado = supermercados("Vaquita",1,"all")

supermercado1 = supermercados("D1",0,"vegetales")

vaquit = clase_Lavaquita.Vaquita("all")

d1no = clase_D1.D1("all")

try:
    d1no.fetchinfo_D1()
except Exception as E:
    print(E)
try:
    vaquit.fetchinfo_vaquita()
except Exception as E:
    print(E)

#supermercado.fetchinfo_vaquita()

#supermercado1.fetchinfo_D1()
    

    