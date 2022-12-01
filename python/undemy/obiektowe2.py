class Sekwencja():
    """Przechowuje dane sekwencji i wykonuje na niej proste operacje."""

    def drukuj_informacje(self):
        print(f"Sekwencja: {self.sekwencja}")

sekw = Sekwencja()
sekw.sekwencja = 'AAGGATC'
sekw.drukuj_informacje()

