## Caesar_cipher
#### Simple app to encode and decode text by using Ceasar cipher. Created with Python.
### Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [More detail about functionality](#more-detail-about-functionality)

### [General info](#general-info)
<details>
<summary>Click here to see general information about <b>Project</b>!</summary>
Aplikacja stworzona w celach ćwiczeniowych. W projekcie zostały zastosowane wzorce projektowe: Facade, FactoryMethod oraz Abstract Factory.
Funkcjonalność aplikacji została przetestowana przy użyciu biblioteki pytest. Stylistyka i zgodność z zasadami PEP8 zostały sprawdzone i poprawione przy uzyciu biblioteki PEP8 Black. Użytkownik obługuje aplikację z poziomu Menu.
Do stworzenia Menu została użyta paczka console-menu.
</details>

### [Technologies](#technologies)
<details>
<summary>Click here to see general information about <b>Technologies</b>!</summary>
Project is created with:
<ul>
<li>Python</li>
<li>consolemenu</li>
<li>abc</li>
<li>typing</li>
<li>dataclasses</li>
<li>unitest</li>
<li>pytest</li>
<li>json</li>
</ul>
</details>

### [Setup](#setup)
<details>
<summary>Click here to see general information about <b>Setup</b>!</summary>
Zapytać Stacha czy to wrzucać!
</details>

### [More detail about functionality](#more-detail-about-functionality)
<details>
<summary>Click here to see general information about <b>Functionality</b>!</summary>
Aplikacja posiada Menu oraz Submenu. Z poziomu Menu są obsługiwane takie funkcjonalności jak:
<ul>
<li>wyboru typu operacji, który chcemy wykonać (encrypt/decrypt)</li>
<li>wczytania danych z pliku</li>
<li>przejście do Submenu (Memory Buffer Menu)</li>
<li>wyjście z aplikacji</li>
</ul>
Podczas działania programu wprowadzane oraz wczytywane dane są przechowywane w liście (funkcjonalność Memory Buffer). 
Co po przejściu do Submenu pozwala na:
<ul>
<li>wyświetlenie przchowywanych danych (Show Buffer)</li>
<li>wyczyszczenie pamięci (CLear Buffer)</li>
<li>usunięcie pojedynczych pozycji z pamięci (Delete position from Memory Buffer)</li>
<li>zapisanie danych do pliku w formacie json(Save Buffer to file)</li>
<li>powrót do głównego menu</li>
</ul>
</details>
