# Snake Game

> Klasyczna gra Snake - steruj wężem, zbieraj jedzenie i unikaj kolizji!

## 1. Opis Projektu

Snake Game to implementacja klasycznej gry węża, w której gracz steruje wężem poruszającym się po planszy. Celem gry jest zbieranie jedzenia, które powoduje wydłużenie węża i zwiększenie wyniku. Gra kończy się, gdy wąż zderzy się ze ścianą lub własnym ciałem. Aplikacja umożliwia śledzenie najlepszych wyników i zapewnia rozrywkę użytkownikom.

## 2. Główne Funkcjonalności (MVP)

Lista wymagań, które powinno zawierać MVP:

- [x] Rejestracja i autoryzacja użytkowników
- [ ] Podstawowa logika biznesowa (sterowanie wężem, kolizje, zbieranie jedzenia)
- [ ] System punktacji i najlepszych wyników
- [x] Eksport/Import danych (zapisywanie wyników)
- [x] Inicjalizacja repozytorium i środowiska pracy
- [x] Lokalne przechowywanie danych użytkowników w formacie JSON

## 3. Stos Technologiczny

- **Język programowania:** Python
- **Środowisko:** Visual Studio Code
- **Biblioteki standardowe:** json, os
- **Inne:** (np. planowana biblioteka graficzna: pygame)

## 4. Przechowywanie Danych

Aplikacja wykorzystuje lokalne przechowywanie danych użytkowników w pliku `uzytkownicy.json` znajdującym się w głównym katalogu projektu. Plik ten zawiera:

- Nazwy użytkowników
- Hasła (w formie tekstowej - w przyszłości planowane hashowanie)
- Najlepsze wyniki każdego użytkownika

Dane są automatycznie wczytywane przy starcie aplikacji i zapisywane po każdej rejestracji nowego użytkownika lub aktualizacji wyniku.

**Uwaga:** Plik `uzytkownicy.json` jest obecnie commitowany do repozytorium zgodnie z planowanym działaniem projektu. W przyszłości można rozważyć przeniesienie go do `.gitignore` dla większego bezpieczeństwa.

## 5. Autor

- Imię i Nazwisko
- [Link do mojego GitHuba](URL)
