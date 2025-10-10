---
name: Profesor Plan ₿ Network
description: Jak dodać lub zmodyfikować profil nauczyciela w Plan ₿ Network?
---
![cover](assets/cover.webp)


Jeśli planujesz wnieść swój wkład do Plan ₿ Network poprzez napisanie nowego samouczka lub kursu, będziesz potrzebować profilu nauczyciela. Profil ten umożliwi ci otrzymywanie odpowiednich kredytów za treści, które udostępniasz na platformie.


Ci z was, którzy byli już zaangażowani w tworzenie treści edukacyjnych na Plan ₿ Network, prawdopodobnie mają już profil nauczyciela. Można go znaleźć w folderze `/professors` [na naszym repozytorium GitHub](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors). Jeśli twój profil już istnieje, znajdź swój login w pliku `professor.yml`.


Aby wprowadzić zmiany w swoim profilu, przejdź do sekcji "Edytuj swój profil nauczyciela" na końcu tego samouczka.


## Dodaj nowego nauczyciela za pomocą naszego oprogramowania


Najprostszym sposobem na utworzenie profilu nauczyciela w Plan ₿ Network jest skorzystanie z naszego zintegrowanego narzędzia Python. Oto jak to działa.


### 1 - Konfiguracja środowiska lokalnego


Musisz mieć własny Fork z [repozytorium Plan ₿ Network na GitHub] (https://github.com/PlanB-Network/Bitcoin-educational-content).


Zsynchronizuj główną gałąź (`dev`) Fork z repozytorium źródłowym.


Zaktualizuj lokalnego klona.


```bash
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<username>/bitcoin-educational-content.git
cd bitcoin-educational-content
# Ajouter le dépôt source en tant que remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git
# Récupérer les dernières modifications depuis le dépôt source
git fetch upstream
# Se positionner sur la branche principale 'dev'
git checkout dev
# Fusionner les modifications de la branche 'dev' du dépôt source dans votre fork
git merge upstream/dev
# Pousser les mises à jour vers votre fork sur GitHub
git push origin dev
```


### 2 - Utwórz nowy oddział


Upewnij się, że jesteś w gałęzi `dev`. Utwórz nową gałąź z opisową nazwą (np. `add-professor-loic-morel`).


Opublikuj tę gałąź w Fork online.


```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b add-professor-loic-morel
# Publiez cette branche sur votre fork en ligne
git push -u origin add-professor-loic-morel
```


### 3 - Utwórz swój profil nauczyciela


Przejdź do folderu `scripts/tutorial-related/data-creator/` na swoim lokalnym klonie. Upewnij się, że zainstalowałeś wszystkie zależności wymagane dla oprogramowania, najpierw instalując Python:


```bash
pip install -r requirements.txt
```


Następnie uruchom oprogramowanie za pomocą polecenia:


```bash
python3 main.py
```


Po wejściu na stronę główną wprowadź lokalną ścieżkę do klonu repozytorium, język, w którym piszesz i swój identyfikator GitHub. Jeśli tworzysz ten profil dla kogoś innego i masz już profil profesora, wprowadź swój identyfikator w polu "*PBN Professor's ID*". Jeśli tworzysz własny profil, nie będziesz mieć jeszcze identyfikatora profesora, ponieważ jesteś w trakcie jego tworzenia, więc pozostaw to pole puste.


Następnie kliknij przycisk "*Nowy profesor*".


![Image](assets/fr/01.webp)


Wypełnij wymagane informacje (pamiętaj, że wszystkie te informacje będą publiczne na naszej platformie, a także na GitHub):




- Nazwa pliku nauczyciela (użyj imienia i nazwiska lub pseudonimu, małymi literami) ;
- Imię i nazwisko lub pseudonim;
- Twoja strona internetowa i profil X (opcjonalnie) ;
- Błyskawica Address do przyjmowania darowizn od czytelników (opcjonalnie) ;
- Wybierz 2 lub 3 tagi z listy;
- Kliknij "*Wybierz obraz*", aby wybrać obraz profilu z folderów lokalnych (można użyć dowolnej nazwy i formatu obrazu, a oprogramowanie dostosuje go automatycznie. Upewnij się tylko, że obraz jest kwadratowy);
- Napisz krótki opis swojego profilu.


Zakończ tworzenie, klikając "*Create Professor*". Spowoduje to automatyczne generate wszystkich plików wymaganych dla profilu.


![Image](assets/fr/02.webp)


Zapisz zmiany lokalnie, tworząc zatwierdzenie z komunikatem wyjaśniającym. Prześlij zmiany do Fork GitHub.


```bash
# Créez un commit avec un message descriptif
git commit -m "*new professor Loïc Morel*"
# Poussez vos modifications sur votre fork
git push origin add-professor-loic-morel
```


Po zakończeniu utwórz Pull Request (PR) na GitHub, aby zaproponować integrację swoich modyfikacji. Dodaj tytuł i krótki opis do PR.


### 4 - Korekta i scalanie


Poczekaj na zatwierdzenie lub informację zwrotną od administratora. W razie potrzeby wprowadź poprawki i opublikuj nowe zatwierdzenia.


```bash
# Créez un commit décrivant les corrections apportées
git commit -m "*Corrections suite à la revue du tutoriel green-wallet*"
# Poussez les corrections sur votre fork
git push origin add-professor-loic-morel
```


Po scaleniu PR można usunąć gałąź roboczą.


## Modyfikowanie profilu nauczyciela


Jeśli opanowałeś już korzystanie z Git, zmodyfikuj swój profil nauczyciela, tworząc nową gałąź i edytując odpowiedni plik bezpośrednio w istniejącym folderze. Zmiany można wprowadzić w pliku `professor.yml` lub w pliku markdown, w zależności od informacji, które należy poprawić. Po wprowadzeniu zmian lokalnie, prześlij je do Fork i prześlij PR.


Początkującym polecam dokonanie modyfikacji bezpośrednio przez Interface w sieci GitHub. Upewnij się, że masz konto GitHub. Jeśli nie wiesz, jak je utworzyć, postępuj zgodnie z tym samouczkiem:


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
Przejdź do [repozytorium Plan ₿ Network GitHub poświęconego danym] (https://github.com/PlanB-Network/Bitcoin-educational-content/graphs/contributors).


![Image](assets/fr/03.webp)


Kliknij folder "*professors*", a następnie przejdź do folderu osobistego.


![Image](assets/fr/04.webp)


Aby zmienić metadane profilu, takie jak Lightning Address, nazwę lub linki, wybierz plik "*professor.yml*". Aby zmienić opis, kliknij plik YAML dla swojego języka (np. "*en.yml*" lub "*fr.yml*").


Jeśli zmodyfikujesz swój opis, pamiętaj o usunięciu wszystkich przestarzałych tłumaczeń. Następnie możesz zająć się tłumaczeniem opisu na inne języki z pomocą LLM lub pozostawić tylko opis w swoim ojczystym języku i wspomnieć w Pull Request, że opis wymaga tłumaczenia przez nasz zespół.


![Image](assets/fr/05.webp)


Po przejściu do pliku, który chcesz zmodyfikować, kliknij ikonę ołówka.


![Image](assets/fr/06.webp)


Jeśli nie masz jeszcze Fork z repozytorium Plan ₿ Network, GitHub zasugeruje utworzenie go. Kliknij "*Fork to repozytorium*".


![Image](assets/fr/07.webp)


Wprowadź żądane zmiany w pliku. Po zakończeniu kliknij "*Commit changes*".


![Image](assets/fr/08.webp)


Wprowadź wiadomość opisującą zmianę, a następnie wybierz opcję "*Zaproponuj zmiany*".


![Image](assets/fr/09.webp)


Wyświetlone zostanie podsumowanie wprowadzonych zmian. Jeśli chcesz wprowadzić dalsze zmiany w swoim profilu, możesz powrócić do folderów i dokonać kolejnych commitów. Po zakończeniu kliknij "*Create pull request*".


Pull Request to prośba o integrację zmian z gałęzi użytkownika do głównej gałęzi repozytorium Plan ₿ Network, umożliwiająca przeglądanie i omawianie zmian przed ich scaleniem.


![Image](assets/fr/10.webp)


Upewnij się, że na początku Interface twoja gałąź robocza jest połączona z gałęzią `dev` repozytorium Plan ₿ Network (która jest główną gałęzią).


Wprowadź tytuł, który krótko podsumowuje zmiany, które chcesz scalić z repozytorium źródłowym. Dodaj krótki komentarz opisujący te zmiany, a następnie kliknij przycisk Green "*Utwórz żądanie ściągnięcia*", aby potwierdzić żądanie ściągnięcia:


![Image](assets/fr/11.webp)


Twój PR będzie widoczny w zakładce "*Pull Request*" w głównym repozytorium Plan ₿ Network. Wszystko, co musisz teraz zrobić, to poczekać, aż administrator połączy twoją modyfikację.


![Image](assets/fr/12.webp)


Jeśli napotkasz jakiekolwiek trudności techniczne w przesłaniu zmiany, nie wahaj się poprosić o pomoc na [naszej grupie Telegram poświęconej składkom] (https://t.me/PlanBNetwork_ContentBuilder). Dziękujemy bardzo!