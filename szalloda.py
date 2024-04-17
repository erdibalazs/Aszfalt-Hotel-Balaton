from abc import ABC, abstractmethod
from datetime import datetime

class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 5000)  # 5000 Ft / éj az ár

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 8000)  # például 8000 Ft / éj az ár

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_hozzaad(self, szoba):
        self.szobak.append(szoba)

    def foglalas_hozzaadasa(self, szobaszam, datum):
        formatum = "%Y-%m-%d"

        # megnezzük, hogy valós e a dátum
        try:
            bool(datetime.strptime(datum, formatum))
        except ValueError:
            return "-!- Helytelen dátumot adott meg"

        bevitt_datum = datetime.strptime(datum, formatum)
        most = datetime.now()
        if bevitt_datum.date() < most.date():
            return "-!- Régi dátumot adott meg"

        if any(f.szobaszam == szobaszam and f.datum == datum for f in self.foglalasok):
            return "-!- A szoba már foglalt ezen a napon."
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                self.foglalasok.append(Foglalas(szobaszam, datum, szoba.ar))
                return f"Foglalás sikeres! Az ár {szoba.ar} Ft."
        return "Nincs ilyen szobaszám."

    def foglalas_lemondas(self, szobaszam, datum):
        for f in self.foglalasok:
            if f.szobaszam == szobaszam and f.datum == datum:
                self.foglalasok.remove(f)
                return "Foglalás lemondva."
        return "Nincs ilyen foglalás."

    def foglalasok_listazasa(self):

        return [f"{f.szobaszam} szoba, dátum: {f.datum}, ár: {f.ar} Ft" for f in self.foglalasok]

class Foglalas:
    def __init__(self, szobaszam, datum, ar):
        self.szobaszam = szobaszam
        self.datum = datum
        self.ar = ar


def main():
    szalloda = Szalloda("Aszfalt Hotel Balaton")
    # megadjuk, hogy milyen szobáink vannak
    szalloda.szoba_hozzaad(EgyagyasSzoba(101))
    szalloda.szoba_hozzaad(KetagyasSzoba(102))
    szalloda.szoba_hozzaad(EgyagyasSzoba(103))

    # feltöltjük pár előre definiált foglalással
    szalloda.foglalas_hozzaadasa(101, "2024-04-20")
    szalloda.foglalas_hozzaadasa(102, "2024-04-21")
    szalloda.foglalas_hozzaadasa(103, "2024-04-22")
    szalloda.foglalas_hozzaadasa(101, "2024-04-23")
    szalloda.foglalas_hozzaadasa(102, "2024-04-24")

    while True:
        print("\n"+szalloda.nev+" - Menü")
        print("1. Foglalás létrehozása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Válasszon egy opciót: ")

        if valasztas == "1":
            szobaszam = int(input("Adja meg a szoba számát: "))
            datum = input("Adja meg a dátumot (YYYY-MM-DD): ")
            print(szalloda.foglalas_hozzaadasa(szobaszam, datum))
        elif valasztas == "2":
            szobaszam = int(input("Adja meg a szoba számát: "))
            datum = input("Adja meg a dátumot (YYYY-MM-DD): ")
            print(szalloda.foglalas_lemondas(szobaszam, datum))
        elif valasztas == "3":
            foglalasok = szalloda.foglalasok_listazasa()
            print("\nFoglalások listája:")
            for foglalas in foglalasok:
                print(foglalas)
        elif valasztas == "4":
            break
        else:
            print("Érvénytelen opció.")

if __name__ == "__main__":
    main()
