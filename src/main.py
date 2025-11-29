# Główny plik aplikacji
# Autor: [Twoje Imię]

import json
import os

# Ścieżka do pliku z danymi użytkowników
PLIK_UZYTKOWNICY = os.path.join(os.path.dirname(__file__), '..', 'uzytkownicy.json')

# Słownik przechowujący użytkowników
uzytkownicy = {}

def wczytaj_uzytkownikow():
    """Funkcja wczytująca użytkowników z pliku JSON"""
    global uzytkownicy
    if os.path.exists(PLIK_UZYTKOWNICY):
        try:
            with open(PLIK_UZYTKOWNICY, 'r', encoding='utf-8') as plik:
                uzytkownicy = json.load(plik)
            print(f"Wczytano {len(uzytkownicy)} użytkowników z bazy danych.")
        except (json.JSONDecodeError, IOError) as e:
            print(f"Błąd podczas wczytywania użytkowników: {e}")
            uzytkownicy = {}
    else:
        print("Brak pliku z użytkownikami. Zostanie utworzony nowy.")
        uzytkownicy = {}

def zapisz_uzytkownikow():
    """Funkcja zapisująca użytkowników do pliku JSON"""
    try:
        # Upewnij się, że katalog istnieje
        katalog = os.path.dirname(PLIK_UZYTKOWNICY)
        if katalog and not os.path.exists(katalog):
            os.makedirs(katalog)
        
        with open(PLIK_UZYTKOWNICY, 'w', encoding='utf-8') as plik:
            json.dump(uzytkownicy, plik, ensure_ascii=False, indent=2)
        return True
    except IOError as e:
        print(f"Błąd podczas zapisywania użytkowników: {e}")
        return False

def rejestracja():
    """Funkcja rejestrująca nowego użytkownika"""
    print("\n--- REJESTRACJA ---")
    nazwa_uzytkownika = input("Podaj nazwę użytkownika: ")
    
    if nazwa_uzytkownika in uzytkownicy:
        print("Użytkownik o tej nazwie już istnieje!")
        return None
    
    haslo = input("Podaj hasło: ")
    uzytkownicy[nazwa_uzytkownika] = {
        'haslo': haslo,
        'najlepszy_wynik': 0
    }
    
    # Zapisanie użytkownika do pliku
    if zapisz_uzytkownikow():
        print(f"Użytkownik {nazwa_uzytkownika} został zarejestrowany i zapisany!")
    else:
        print(f"Użytkownik {nazwa_uzytkownika} został zarejestrowany, ale wystąpił błąd podczas zapisu.")
    
    return nazwa_uzytkownika

def logowanie():
    """Funkcja logująca istniejącego użytkownika"""
    print("\n--- LOGOWANIE ---")
    nazwa_uzytkownika = input("Podaj nazwę użytkownika: ")
    
    if nazwa_uzytkownika not in uzytkownicy:
        print("Użytkownik nie istnieje! Zarejestruj się najpierw.")
        return None
    
    haslo = input("Podaj hasło: ")
    
    if uzytkownicy[nazwa_uzytkownika]['haslo'] == haslo:
        print(f"Zalogowano jako {nazwa_uzytkownika}!")
        return nazwa_uzytkownika
    else:
        print("Nieprawidłowe hasło!")
        return None

def obsluga_logowania():
    """Funkcja obsługująca proces logowania/rejestracji użytkownika"""
    print("\n=== SYSTEM LOGOWANIA ===")
    print("1. Zaloguj się")
    print("2. Zarejestruj się")
    print("3. Kontynuuj bez logowania")
    
    wybor = input("Wybierz opcję (1-3): ")
    
    if wybor == "1":
        return logowanie()
    elif wybor == "2":
        return rejestracja()
    elif wybor == "3":
        print("Kontynuujesz jako gość.")
        return None
    else:
        print("Nieprawidłowa opcja!")
        return obsluga_logowania()

def aktualizuj_wynik(uzytkownik, nowy_wynik):
    """Funkcja aktualizująca najlepszy wynik użytkownika i zapisująca do pliku"""
    if uzytkownik and uzytkownik in uzytkownicy:
        if nowy_wynik > uzytkownicy[uzytkownik]['najlepszy_wynik']:
            uzytkownicy[uzytkownik]['najlepszy_wynik'] = nowy_wynik
            zapisz_uzytkownikow()
            return True
    return False

def wyswietl_menu(uzytkownik=None):
    """Funkcja wyświetlająca główne opcje programu"""
    print("\n--- GRA SNAKE v1.0 ---")
    if uzytkownik:
        print(f"Zalogowany jako: {uzytkownik}")
        print(f"Twój najlepszy wynik: {uzytkownicy[uzytkownik]['najlepszy_wynik']}")
    else:
        print("Tryb gościa")
    print("1. Rozpocznij nową grę")
    print("2. Wyświetl najlepsze wyniki")
    print("3. Wyjście")

def start_aplikacji():
    print("Uruchamianie modułów...")
    wczytaj_uzytkownikow()  # Wczytanie użytkowników przy starcie aplikacji
    zalogowany_uzytkownik = obsluga_logowania()
    wyswietl_menu(zalogowany_uzytkownik)

# Punkt startowy programu
if __name__ == "__main__":
    start_aplikacji()

