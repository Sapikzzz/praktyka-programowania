# Produkt
class Dom:
    def __init__(self):
        self.fundamenty = None
        self.sciany = None
        self.dach = None
    
    def __str__(self):
        return f"Dom: fundamenty={self.fundamenty}, ściany={self.sciany}, dach={self.dach}"

# Budowniczy
class Budowniczy:
    def zbuduj_fundamenty(self):
        pass
    
    def zbuduj_sciany(self):
        pass
    
    def zbuduj_dach(self):
        pass
    
    def zwroc_dom(self):
        pass

# Konkretni budowniczy
class BudowniczyDrewno(Budowniczy):
    def __init__(self):
        self.dom = Dom()
    
    def zbuduj_fundamenty(self):
        self.dom.fundamenty = "Drewniane fundamenty"
    
    def zbuduj_sciany(self):
        self.dom.sciany = "Sciany drewniane"
        
    def zbuduj_dach(self):
        self.dom.dach = "Dach drewniany"
    
    def zwroc_dom(self):
        return self.dom

class BudowniczyCegla(Budowniczy):
    def __init__(self):
        self.dom = Dom()
    
    def zbuduj_fundamenty(self):
        self.dom.fundamenty = "Fundamenty ceglane"
    
    def zbuduj_sciany(self):
        self.dom.sciany = "Sciany ceglane"
    
    def zbuduj_dach(self):
        self.dom.dach = "Dachowka"
    
    def zwroc_dom(self):
        return self.dom

# Kierownik
class Kierownik:
    def __init__(self, budowniczy):
        self.budowniczy = budowniczy

    def zmien_budowniczego(self, budowniczy):
        self.budowniczy = budowniczy
    
    def zbuduj_dom(self):
        self.budowniczy.zbuduj_fundamenty()
        self.budowniczy.zbuduj_sciany()
        self.budowniczy.zbuduj_dach()
        return self.budowniczy.zwroc_dom()

budowniczy_drewno = BudowniczyDrewno()
budowniczy_cegla = BudowniczyCegla()

director = Kierownik(budowniczy_drewno)
drewniany_dom = director.zbuduj_dom()
print(drewniany_dom)

director.zmien_budowniczego(budowniczy_cegla)
murowany_dom = director.zbuduj_dom()
print(murowany_dom)