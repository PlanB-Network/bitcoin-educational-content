---
name: Ashigaru - Rykoszet
description: Zrozumienie i korzystanie z transakcji Ricochet
---
![cover ricochet](assets/cover.webp)



> *Narzędzie premium, które dodaje dodatkową historię do transakcji. Pomaga chronić się przed niesprawiedliwym zamknięciem konta przez osoby trzecie

## Co to jest rykoszet?



Ricochet to technika polegająca na wykonywaniu kilku fikcyjnych transakcji wobec samego siebie w celu symulacji przeniesienia własności bitcoinów. Narzędzie to różni się od innych transakcji Ashigaru (odziedziczonych po Samurai Wallet) tym, że nie zapewnia anonimowości prospektywnej, ale raczej formę anonimowości retrospektywnej. W rzeczywistości Ricochet zaciera specyfikę, która może zagrozić zamienności części Bitcoin.



Na przykład, jeśli wykonasz coinjoin, twoja część wychodząca z miksu zostanie zidentyfikowana jako taka. Narzędzia do analizy łańcucha są w stanie wykryć paterny transakcji coinjoin i przypisać etykietę do części wychodzących z nich. W efekcie coinjoin ma na celu zerwanie historycznych powiązań monety, ale jej przejście przez coinjoiny pozostaje wykrywalne. Analogicznie, zjawisko to przypomina szyfrowanie tekstu: chociaż nie można uzyskać dostępu do oryginalnego tekstu w postaci czystego tekstu, łatwo jest zidentyfikować, że zastosowano szyfrowanie.



Etykieta "coinjoined" może wpływać na zamienność UTXO. Podmioty regulowane, takie jak platformy wymiany, mogą odmówić przyjęcia UTXO coinjoined, a nawet zażądać wyjaśnień od jego właściciela, ryzykując zablokowanie konta lub zamrożenie środków. W niektórych przypadkach platforma może nawet zgłosić zachowanie użytkownika organom państwowym.



W tym miejscu pojawia się metoda Ricochet. Aby zatrzeć ślad pozostawiony przez coinjoin, Ricochet wykonuje cztery kolejne transakcje, w których użytkownik przelewa swoje środki do siebie na różne adresy. Po tej sekwencji transakcji narzędzie Ricochet ostatecznie kieruje bitcoiny do miejsca docelowego, takiego jak platforma wymiany. Celem jest stworzenie dystansu między pierwotną transakcją coinjoin a ostatecznym aktem wydatkowania. W ten sposób narzędzia do analizy blockchain zakładają, że prawdopodobnie doszło do przeniesienia własności po coinjoin, a zatem nie ma potrzeby podejmowania działań przeciwko emitentowi.



![image](assets/fr/01.webp)



W obliczu metody Ricochet można by sobie wyobrazić, że oprogramowanie do analizy łańcucha pogłębiłoby badanie powyżej czterech odbić. Platformy te stają jednak przed dylematem optymalizacji progu wykrywania. Muszą one ustalić progową liczbę przeskoków, po których akceptują, że prawdopodobnie nastąpiła zmiana właściciela, a link do poprzedniego coinjoina powinien zostać zignorowany. Określenie tego progu jest jednak ryzykowne: każde zwiększenie liczby obserwowanych skoków wykładniczo zwiększa liczbę wyników fałszywie dodatnich, tj. osób błędnie oznaczonych jako uczestnicy coinjoin, podczas gdy w rzeczywistości operacja została przeprowadzona przez kogoś innego. Scenariusz ten stanowi poważne ryzyko dla tych firm, ponieważ fałszywe alarmy prowadzą do niezadowolenia, które może doprowadzić klientów do konkurencji. W dłuższej perspektywie zbyt ambitny próg wykrywalności prowadzi platformę do utraty większej liczby klientów niż jej konkurenci, co może zagrozić jej rentowności. W związku z tym skomplikowane jest dla tych platform zwiększenie liczby zaobserwowanych odrzuceń, a 4 jest często wystarczającą liczbą, aby przeciwdziałać ich analizom.



W związku z tym **najczęstszy przypadek użycia Ricochet pojawia się, gdy konieczne jest ukrycie wcześniejszego udziału w coinjoin na UTXO, którego jesteś właścicielem **. Najlepiej jest unikać przekazywania bitcoinów, które zostały poddane coinjoin podmiotom regulowanym. Niemniej jednak, w przypadku braku innej opcji, szczególnie w przypadku pilnej potrzeby upłynnienia bitcoinów w walucie państwowej, Ricochet oferuje skuteczne rozwiązanie.



## Jak Ricochet działa na Ashigaru?



Ricochet to po prostu metoda wysyłania bitcoinów do siebie, pierwotnie wynaleziona przez twórców Samurai Wallet. W związku z tym możliwe jest ręczne symulowanie rykoszetu, bez potrzeby korzystania ze specjalistycznego narzędzia. Jednak dla tych, którzy chcą zautomatyzować proces, ciesząc się bardziej dopracowanym rezultatem, narzędzie Ricochet dostępne za pośrednictwem aplikacji Ashigaru (która jest Samurai fork) stanowi dobre rozwiązanie.



Ponieważ Ashigaru pobiera opłaty za swoje usługi, Ricochet kosztuje `100,000 sats` jako opłata za usługę, plus opłata mining. Jego użycie jest zatem zalecane w przypadku przelewów na znaczne kwoty.



Aplikacja Ashigaru oferuje dwa warianty Ricochet:





- Reinforced Ricochet, czyli "dostawa rozłożona w czasie", która oferuje korzyść w postaci rozłożenia opłat za usługi Ashigaru na pięć kolejnych transakcji. Ta opcja zapewnia również, że każda transakcja jest nadawana w osobnym czasie i rejestrowana w innym bloku, naśladując jak najdokładniej zachowanie zmiany właściciela. Metoda ta, choć wolniejsza, jest preferowana dla tych, którzy się nie spieszą, ponieważ maksymalizuje wydajność Ricochet poprzez wzmocnienie jego odporności na analizę łańcucha;





- Klasyczny Ricochet, który ma na celu szybkie wykonanie operacji, transmituje wszystkie transakcje w skróconym przedziale czasowym. Metoda ta oferuje zatem mniejszą poufność i mniejszą odporność na analizę niż metoda wzmocniona. Powinna być stosowana tylko w przypadku pilnych przesyłek.



## Jak wykonać rykoszet na Ashigaru?



Wykonanie rykoszetu na Ashigaru jest bardzo proste: wystarczy aktywować odpowiednią opcję podczas tworzenia transakcji wysyłania. Aby rozpocząć, kliknij przycisk `+`, a następnie `Wyślij` i wybierz konto, z którego chcesz wysłać środki.



![Image](assets/fr/02.webp)



Wypełnij informacje o transakcji: kwotę do wysłania i końcowy adres odbiorcy po skokach Ricochet. Następnie zaznacz opcję `Ricochet`.



![Image](assets/fr/03.webp)



Następnie można wybrać jeden z dwóch trybów Ricochet omówionych w sekcji teoretycznej: klasyczny Ricochet, w którym wszystkie transakcje są zawarte w tym samym bloku, lub dostarczanie rozłożone w czasie, które poprawia jakość Ricochet kosztem większego opóźnienia.



Po dokonaniu wyboru naciśnij strzałkę u dołu ekranu, aby potwierdzić.



![Image](assets/fr/04.webp)



Na następnym ekranie zobaczysz pełne podsumowanie transakcji. W tym miejscu można również dostosować stawkę opłaty za transakcje Ricochet do warunków rynkowych. Jeśli wszystko jest satysfakcjonujące, przeciągnij zieloną strzałkę, aby podpisać i rozpowszechnić transakcje Ricochet.



![Image](assets/fr/05.webp)



Poczekaj, aż różne skoki uruchomią się automatycznie.



![Image](assets/fr/06.webp)



Twoje transakcje zostały pomyślnie wysłane.



![Image](assets/fr/07.webp)



Jesteś teraz w pełni zaznajomiony z opcją Ricochet dostępną w aplikacji Ashigaru. Aby pójść dalej, polecam wziąć udział w moim szkoleniu BTC 204, które szczegółowo nauczy Cię, jak wzmocnić swoją poufność onchain.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c