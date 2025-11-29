# Snake Game

> Klasyczna gra Snake - steruj wężem, zbieraj jedzenie i unikaj kolizji!

## 1. Opis Projektu

Snake Game to implementacja klasycznej gry węża z graficznym interfejsem użytkownika stworzonym w pygame. Gracz steruje wężem poruszającym się po planszy za pomocą strzałek klawiatury. Celem gry jest zbieranie jedzenia, które powoduje wydłużenie węża i zwiększenie wyniku o 10 punktów za każde zjedzone jedzenie. Gra kończy się, gdy wąż zderzy się ze ścianą lub własnym ciałem.

Aplikacja oferuje pełny system zarządzania użytkownikami z możliwością rejestracji i logowania. Najlepsze wyniki każdego użytkownika są automatycznie zapisywane i aktualizowane. Gra umożliwia również wyświetlanie rankingu najlepszych wyników wszystkich graczy.

### Funkcjonalności gry:

- Graficzny interfejs w pygame (okno 800x600 pikseli)
- Płynne sterowanie wężem za pomocą strzałek
- Wykrywanie kolizji ze ścianami i własnym ciałem
- Losowe pojawianie się jedzenia na planszy
- System punktacji z wyświetlaniem wyniku podczas gry
- Ekran końca gry z możliwością restartu
- Integracja z systemem użytkowników i zapisywanie najlepszych wyników

## 2. Główne Funkcjonalności (MVP)

Lista wymagań, które powinno zawierać MVP:

- [x] Rejestracja i autoryzacja użytkowników
- [x] Podstawowa logika biznesowa (sterowanie wężem, kolizje, zbieranie jedzenia)
- [x] System punktacji i najlepszych wyników
- [x] Eksport/Import danych (zapisywanie wyników)
- [x] Inicjalizacja repozytorium i środowiska pracy
- [x] Lokalne przechowywanie danych użytkowników w formacie JSON
- [x] Graficzny interfejs użytkownika w pygame

## 3. Stos Technologiczny

- **Język programowania:** Python 3.11-3.13 (zalecane Python 3.12)
- **Środowisko:** Visual Studio Code
- **Biblioteki standardowe:** json, os
- **Biblioteki zewnętrzne:** pygame >= 2.0.0

## 4. Struktura Projektu

```
snake_game/
├── src/
│   ├── main.py          # Główny plik aplikacji z logiką logowania i menu
│   └── game.py          # Moduł gry Snake z implementacją w pygame
├── assets/              # Folder na zasoby graficzne (opcjonalnie)
├── docs/                # Dokumentacja projektu
├── tests/               # Testy jednostkowe (opcjonalnie)
├── uzytkownicy.json     # Plik z danymi użytkowników i wynikami
├── requirements.txt     # Zależności projektu
└── README.md            # Ten plik
```

## 5. Przechowywanie Danych

Aplikacja wykorzystuje lokalne przechowywanie danych użytkowników w pliku `uzytkownicy.json` znajdującym się w głównym katalogu projektu. Plik ten zawiera:

- Nazwy użytkowników
- Hasła (w formie tekstowej - w przyszłości planowane hashowanie)
- Najlepsze wyniki każdego użytkownika

Dane są automatycznie wczytywane przy starcie aplikacji i zapisywane po każdej rejestracji nowego użytkownika lub aktualizacji wyniku.

**Uwaga:** Plik `uzytkownicy.json` jest obecnie commitowany do repozytorium zgodnie z planowanym działaniem projektu. W przyszłości można rozważyć przeniesienie go do `.gitignore` dla większego bezpieczeństwa.

## 6. Instrukcja Uruchomienia

### Wymagania

- Python 3.11-3.13 (zalecane Python 3.12)
  - **Uwaga:** Python 3.14 nie jest obecnie w pełni kompatybilny z pygame 2.6.1
- System operacyjny: Windows, macOS lub Linux
- pygame >= 2.0.0

### Instalacja zależności

1. **Sklonuj repozytorium** (jeśli jeszcze tego nie zrobiłeś):

   ```bash
   git clone <URL_REPOZYTORIUM>
   cd snake_game
   ```

2. **Utwórz wirtualne środowisko** (zalecane):

   ```bash
   python3.12 -m venv venv
   ```

   Lub jeśli masz inną wersję Python 3.11-3.13:

   ```bash
   python3.11 -m venv venv
   # lub
   python3.13 -m venv venv
   ```

3. **Aktywuj wirtualne środowisko**:

   ```bash
   source venv/bin/activate  # macOS/Linux
   # lub
   venv\Scripts\activate  # Windows
   ```

4. **Zainstaluj wymagane biblioteki**:

   ```bash
   pip install -r requirements.txt
   ```

   Lub na niektórych systemach:

   ```bash
   pip3 install -r requirements.txt
   ```

### Jak uruchomić grę

1. **Upewnij się, że wirtualne środowisko jest aktywowane**:

   ```bash
   source venv/bin/activate  # macOS/Linux
   # lub
   venv\Scripts\activate  # Windows
   ```

2. **Uruchom aplikację**:

   ```bash
   python src/main.py
   ```

   Lub na niektórych systemach:

   ```bash
   python3 src/main.py
   ```

3. **Po uruchomieniu**:
   - Zostaniesz poproszony o wybór opcji logowania:
     - **Opcja 1:** Zaloguj się (jeśli masz już konto)
     - **Opcja 2:** Zarejestruj się (aby utworzyć nowe konto)
     - **Opcja 3:** Kontynuuj bez logowania (tryb gościa)
   - Po zalogowaniu lub wyborze trybu gościa zobaczysz główne menu gry:
     - **Opcja 1:** Rozpocznij nową grę
     - **Opcja 2:** Wyświetl najlepsze wyniki
     - **Opcja 3:** Wyjście

### Sterowanie w grze

- **Strzałki (↑ ↓ ← →)** - sterowanie kierunkiem węża
- **ESC** - wyjście z gry
- **SPACE** - restart gry (po zakończeniu gry)

### Uruchomienie w Visual Studio Code

1. Otwórz folder projektu w VS Code
2. Otwórz terminal w VS Code (Ctrl + ` lub Terminal → New Terminal)
3. Zainstaluj zależności:
   ```bash
   pip install -r requirements.txt
   ```
4. Uruchom aplikację:
   ```bash
   python src/main.py
   ```

## 7. Autor

- Imię i Nazwisko
- [Link do mojego GitHuba](URL)
