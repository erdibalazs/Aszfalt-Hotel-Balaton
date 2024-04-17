Ez a kis program egy iskolai feladat beadandó feladataként készült.

Szálloda Szobafoglalási Rendszer
Ez a program egy egyszerű szálloda szobafoglalási rendszert valósít meg Pythonban. A rendszer lehetővé teszi a szobák kezelését, foglalások létrehozását, lemondását és listázását egy interaktív felhasználói interfészen keresztül.
A program az indítás után automatikusan létrehozza a szobákat (101,102,103). Ezeket a szobákat kell használni a foglalások kezelésekor.

Funkciók
Szobák kezelése: Szobák hozzáadása a szállodai kínálathoz.
Foglalás létrehozása: Új foglalások rögzítése a szállodában, dátum és szobaszám megadásával.
Foglalás lemondása: Már meglévő foglalások lemondása.
Foglalások listázása: Az összes aktív foglalás megtekintése.

Osztályok
Szoba: Absztrakt osztály, amely definiálja a szobák alapvető tulajdonságait, mint az ár és a szobaszám.
EgyagyasSzoba: Egy személyes szobák, saját árazással.
KetagyasSzoba: Két személyes szobák, saját árazással.
Szalloda: Ez az osztály kezeli a szobák és a foglalások listáját, valamint a foglalások kezeléséhez szükséges metódusokat.
Foglalas: Foglalásokat reprezentáló osztály, amely tárolja az érintett szoba számát, a foglalás dátumát és az árat.

Használat
Indítsa el a programot. A rendszer automatikusan betölt néhány adatot az induláskor.
Válasszon a következő lehetőségek közül az interaktív menüben:
1. Foglalás létrehozása: Meg kell adni a szoba számát és a kívánt dátumot. Hibás, vagy régi dátum esetén a program jelzi azt a felhasználónak.
2. Foglalás lemondása: Meg kell adni a szoba számát és a foglalás dátumát, amit le szeretne mondani.
3. Foglalások listázása: Megjeleníti az összes aktív foglalást, árazással együtt.
4. Kilépés: Kilép a programból.
   
A program validálja a bemeneteket, és értesíti a felhasználót, ha a megadott dátum a múltban van, vagy ha a szoba az adott napon már foglalt.
