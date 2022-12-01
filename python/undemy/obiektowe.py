class Sekwencja():

    def __init__(self, sekwencja, ident):
        self.sekwencja = sekwencja
        self.ident = ident
        self.dlugosc = len(self.sekwencja)

    def drukuj_informacje(self):
        print(f"Sekwencja: {self.sekwencja}")
        print(f"Nazwa: {self.ident}")
        print(f"Długosć {self.get_dlugosc()}")

#sekw = Sekwencja('hagakai', 'seq1')
#sekw.drukuj_informacje()

    def get_sekwencja(self):
        '''''zwraca sekwencje'''
        return self.sekwencja

    def set_sekwencja(self, sekwencja):
    #ustawia wartośc atrybutów sekwencja, długość
        self.sekwencja = sekwencja
        self.dlugosc = len(self.sekwencja)

    def get_odwrocona(self):
        #zwraca odwróconą sekwencje

        return self.sekwencja[::-1]

    def get_dlugosc(self):
        #zwraca długośc
# Sprawdzenie, czy długość jest właściwa, jeśli nie to zostaje
# ustawiona właściwa wartośc parametru dlugos
        if self.dlugosc != len(self.sekwencja):
            self.dlugosc = len(self.sekwencja)
        return self.dlugosc


sekw = Sekwencja('gajalal', 'seq1')
sekw.drukuj_informacje()
print(f"Sekwencja odwrócona: {sekw.get_odwrocona()}")
sekw.sekwencja = 'hatamina'
print(f"Sekwencja po zmianie: {sekw.get_sekwencja()}")
print(f"Długośc pobrana z atrybutu: {sekw.dlugosc}")
print(f"Długość pobrana z metody {sekw.get_dlugosc()}")




