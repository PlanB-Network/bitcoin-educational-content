---
name: Electrum Airgap
description: Pierwszy krok w stronę bezpieczeństwa, cold wallet z Electrum
---
![cover](assets/cover.webp)



## Cold Wallet



W tym samouczku wyjaśnię, jak stworzyć swoje pierwsze urządzenie podpisujące airgap, odłączone od Internetu, nawet bez posiadania dedykowanego Hardware Wallet. Wystarczy mieć do dyspozycji dwa komputery:




- stare urządzenie zostanie na zawsze pozbawione możliwości łączenia się z Internetem;
- komputer do codziennego użytku.



Ta konfiguracja pozwala na większy stopień bezpieczeństwa niż klasyczny "Hot Wallet": stary komputer - bez połączenia sieciowego - jest strażnikiem kluczy prywatnych, które nigdy nie są ujawniane w Internecie, ale przechowywane offline ("airgap" lub "Cold").



Zamiast tego zainstalujesz wyświetlacz Wallet ("tylko do oglądania") na swoim codziennym komputerze, który jest podłączony do sieci i za pomocą którego możesz na przykład sprawdzać salda i przygotowywać transakcje paragonowe.



## Wallet Airgap: Co i jak



Wykonując kroki opisane w tym przewodniku, zainstalujemy dwa Software Wallet Electrum na dwóch różnych komputerach i ostatecznie utworzymy dwa portfele z różnymi magazynami kluczy: Wallet airgap będzie korzystał z całej hierarchii Wallet HD, podczas gdy Wallet display zostanie wygenerowany przy użyciu głównego klucza publicznego.



Te dwa portfele będą pod każdym względem bardzo się od siebie różnić. Jedyną wspólną cechą, jak zobaczymy, będą adresy:




- gW-13 na komputerze airgap może tylko podpisywać, ale odłączony od sieci nie zna salda i używanych adresów;
- gW-12 na komputerze dziennym będzie mógł jedynie przygotowywać i propagować transakcje, bez możliwości dysponowania wydatkami, w przypadku braku kluczy prywatnych.



## Przygotowanie wstępne



Aby pobrać Electrum, zalecam wykonanie pierwszych kroków w tym samouczku:



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Po pobraniu zawsze zweryfikuj wersję przed jej zainstalowaniem, a następnie przejdź do konfiguracji "One Server", jak znajdziesz w sekcji pomocy, w sekcji `Start with a Dummy Wallet`.



Konfiguracja "One Server" jest konieczna tylko dla Wallet zainstalowanego na codziennym komputerze, ponieważ drugi komputer będzie zawsze w trybie offline.



Poniższe operacje obejmują ćwiczenia na dwóch różnych komputerach (i portfelach), więc dla wygody i skupienia wybrałem ustawienie Wallet airgap z jasnym motywem, podczas gdy wyświetlacz Wallet ma ciemny motyw.



## Wallet Tworzenie szczeliny powietrznej



Po pobraniu i zweryfikowaniu pobrania Electrum, wykonaj kopię pliku wykonywalnego i przenieś go do komputera w trybie offline. Następnie uruchom go i zainstaluj Electrum.



Kliknij dwukrotnie, aby uruchomić Electrum: komputer, na którym będziesz używać tego Wallet, jest offline, zignoruj ustawienia sieciowe i przejdź do tworzenia Wallet, który w tym przewodniku będziemy nazywać `airgap`.



![image](assets/en/01.webp)



Wybierz opcję _Standard wallet_.



![image](assets/en/02.webp)



Następnie wybierz _Create a new seed_, aby oprogramowanie generate utworzyło Mnemonic.



![image](assets/en/03.webp)



Dokładnie przepisz 12 słów generate z Electrum na papierowy podkład i przejdź do etapu weryfikacji, ponownie wprowadzając słowa w kolejności, gdy Electrum tego zażąda.



![image](assets/en/04.webp)



![image](assets/en/05.webp)



Po zakończeniu tworzenia Wallet ustaw złożone hasło (`Strong`), aby zaszyfrować plik Wallet na urządzeniu airgap. Ten krok jest bardzo delikatny i ważny, ponieważ wybrane teraz hasło uniemożliwia dostęp do Wallet, który ma moc rozporządzania, będąc w stanie wydawać fundusze i podpisywać transakcje.



![image](assets/en/06.webp)



Po kliknięciu _Finish_ Wallet zostanie zdefiniowany i pojawi się na ekranie. Oczywiście wskaźnik połączenia sieciowego, tj. kolorowa kropka w prawym dolnym rogu, jest czerwony, ponieważ komputer jest odłączony i nie pozwala Wallet na wyświetlenie kluczy online.



![image](assets/en/07.webp)



## Tworzenie Wallet wizualizacji



Teraz, gdy twój Wallet ma klucze prywatne offline, musisz skonfigurować Wallet z wyświetlaczem lub "tylko do oglądania", który pozwoli ci zobaczyć saldo, a także przygotować transakcje paragonowe, aby kontynuować bezpieczne gromadzenie Sats.



W Wallet znajdującym się na urządzeniu offline wybierz menu _Wallet_ -> _Information_



![image](assets/en/08.webp)



Pojawi się okno zawierające wszystkie informacje Wallet, w którym można zaznaczyć `ścieżkę derywacji` i `mistrzowski odcisk palca`, na przykład w celu zaznaczenia ich obok słów w zdaniu Mnemonic (zdecydowanie zalecane).



![image](assets/en/09.webp)



Pamiętaj, że pobierasz te dane z niepodłączonego komputera, więc będziesz musiał skopiować/wkleić `zpub` do pliku tekstowego i zapisać go na pendrive.



Teraz możesz przejść do komputera podłączonego do Internetu, aby uruchomić Electrum i utworzyć nowy Wallet.



Z menu _File_ (Plik) wybierz opcję _New/Restore_ (Nowy/Przywróć).



![image](assets/en/10.webp)



Nowy Wallet jest tylko do oglądania, więc na potrzeby tego przewodnika nazwiemy go "tylko do oglądania".



![image](assets/en/12.webp)



Na następnym ekranie wybierz _Standard wallet_ i kontynuuj klikając _Next_.



![image](assets/en/13.webp)



Wybierając `Keystore` bądź ostrożny: aby utworzyć wyświetlany Wallet wybierz _Use a master key_. Następnie przejdź do _Next_.



![image](assets/en/14.webp)



Wklej tutaj `zpub` skopiowany z Wallet offline i przeniesiony na ten komputer przez nośnik usb.



![image](assets/en/15.webp)



Zakończ, ustawiając silne hasło również dla tego Wallet, być może inne niż hasło wybrane dla odpowiadającego mu Cold.



Na wyświetlaczu pojawi się Wallet z ostrzeżeniem. Komunikat przypomina, że jest to Wallet tylko do wyświetlania i nie można za jego pomocą wydawać powiązanych środków.



**Uwaga**: **w związku z tym będziesz musiał zawsze posiadać klucze prywatne do dysponowania UTXO tego Wallet**. Dzięki dobremu systemowi kopii zapasowych nie będzie trudno pozostać w pełnym posiadaniu swoich Bitcoinów.



![image](assets/en/16.webp)



To ostrzeżenie pojawi się za każdym razem, gdy otworzysz Wallet. Kliknij _Ok_ i przejdźmy do etapu weryfikacji.



## Weryfikacja dwóch Wallet



Jak dowiedzieliśmy się na początku tego przewodnika, Wallet airgap i jego wyświetlacz Wallet to dwa portfele, które mają różne funkcje, ale **dzielą te same adresy**.



Jeśli spojrzymy na dwa portfele obok siebie, wizualnie zauważymy, że w szczelinie powietrznej Wallet znajduje się symbol "seed", podczas gdy w samym zegarku go nie ma. Nawet ten szczegół pomoże zapamiętać, że wyświetlacz Wallet nie ma kluczy prywatnych.



![image](assets/en/17.webp)



Aby jednak dokonać dokładnego pierwszego sprawdzenia, wybierz w obu portfelach menu `Addresses`: ponieważ dzielą one te same adresy, lista adresów powinna być identyczna dla obu.



![image](assets/en/18.webp)



⚠️ **UWAGA**: **nie może być pośredniego rozwiązania; adresy muszą być takie same. Jeśli są różne, konieczne jest usunięcie całej dotychczasowej pracy i rozpoczęcie od nowa**.



Teraz możesz przystąpić do dwóch różnych testów. Najpierw spróbuj usunąć oba portfele i przywrócić je od zera, każdy na odpowiednim komputerze. W przypadku przystąpienia do tej weryfikacji, procedury dla wyświetlacza Wallet są identyczne z opisanymi powyżej.



W przypadku Wallet airgap, na ekranie `keystore` będziesz musiał wybrać _I already have a seed_ i wprowadzić słowa kopiując je z papierowej kopii zapasowej.



Po zakończeniu okresu próbnego "no-load" możesz spróbować dokonać transakcji na niewielką kwotę i natychmiast ją wydać.



## Otrzymywanie i wydawanie transakcji



Aby rozpocząć korzystanie ze swojego airgapu Electrum, możesz dokonać transakcji paragonowej z niewielką kwotą, a następnie wydać ją na własny Address. Następnie możesz zapoznać się z procedurą, sprawdzając, czy masz pełną kontrolę nad środkami.



**Uwaga**: Nie zalecam wpłacania dużej ilości środków na Wallet przed upewnieniem się, że można płynnie wykonywać wszystkie operacje.



Opisane poniżej kroki mogą na pierwszy rzut oka wydawać się skomplikowane. Nie pozwól, by cię to zniechęciło: po wykonaniu ich po raz pierwszy przekonasz się, że ich ukończenie zajmuje tylko kilka minut.



Aby otrzymać środki, należy koniecznie użyć wyświetlacza Wallet znajdującego się na komputerze podłączonym do Internetu. W menu `Receive` kliknij na _Create request_, aby Electrum generate otrzymał pierwszy dostępny Address i użył go do wysłania nam kilku Satss.



![image](assets/en/19.webp)



![image](assets/en/20.webp)



Po propagacji transakcji można już zauważyć, że - co jest naturalne - jest ona widoczna tylko na wyświetlaczu Wallet, a nie na szczelinie powietrznej Wallet.



![image](assets/en/21.webp)



Po otrzymaniu potwierdzenia transakcji można przygotować wydatek, a tym samym wypróbować procedurę podpisywania z Wallet poza siecią. Następnie przygotuj transakcję tylko na zegarku i naciśnij _Preview_, aby ją sprawdzić



![image](assets/en/22.webp)



Pojawi się zaawansowane okno transakcji, w którym można to zobaczyć:




- transakcja nie jest podpisana (`Status: Niepodpisana);
- komendy `Sign` i `Broadcast` są zablokowane.



Jedyne, co można zrobić, to wyeksportować transakcję w niezmienionej formie, zabrać ją do luki powietrznej Wallet i podpisać.



Podłącz dysk flash USB do komputera i z menu w lewym dolnym rogu wybierz _Share_.



![image](assets/en/23.webp)



Następnie wybierz _Zapisz do pliku_.



![image](assets/en/24.webp)



Zapisz transakcję na karcie pamięci USB.



Zauważysz, że Electrum nadaje plikowi nazwę zawierającą pierwsze cyfry transaction ID, a rozszerzenie pliku to `.PSBT`, co oznacza `Partially Signed Bitcoin Transaction`.



Wyodrębnij nośnik z plikiem `.PSBT` i podłącz go do komputera w trybie offline.



W oknie Wallet airgap wybierz menu _Tools_, a następnie _Load transaction_ i wybierz opcję From file_.



![image](assets/en/25.webp)



Za pomocą menedżera plików wybierz plik `.PSBT` z jego lokalizacji.



![image](assets/en/29.webp)



Oprogramowanie komputera poza siecią automatycznie otworzy zaawansowane okno transakcji, całkowicie identyczne z tym, które było widoczne na wyświetlaczu Wallet. Status to "Niepodpisany", ale różnica polega na tym, że komenda "Podpisz" jest tutaj aktywna. I właśnie to polecenie należy wykonać.



![image](assets/en/26.webp)



![image](assets/en/27.webp)



Teraz, gdy transakcja została podpisana, należy pamiętać, że Wallet znajduje się na maszynie offline. Dlatego - nawet jeśli widzisz aktywne polecenie `Broadcast` - twój Wallet nie będzie w stanie propagować transakcji do sieci Bitcoin.



Teraz należy powtórzyć operację eksportowania podpisanej transakcji do pamięci USB, aby móc ją zaimportować do komputera podłączonego do Internetu i propagować.



Z menu w lewym dolnym rogu wybierz ponownie _Share_, a następnie _Save to file_.



![image](assets/en/28.webp)



Teraz plik ma inne rozszerzenie: **zamiast `.PSBT` teraz transakcja ma rozszerzenie `.txn`. Od teraz w ten sposób Electrum będzie rozpoznawać transakcje podpisane od niepodpisanych**.



![image](assets/en/30.webp)



W celu ostatecznej propagacji transakcji należy wyjąć pamięć USB z komputera off-line i włożyć ją do komputera podłączonego do Internetu.



Z poziomu samego zegarka powtórz procedurę importu, czyli z menu _Tools_ wybierz _Load transaction_ i na koniec _From file_.



![image](assets/en/31.webp)



Electrum otworzy dla ciebie okno transakcji, znacznie różniące się od tego pokazanego wcześniej na tym Wallet, ponieważ jest ono teraz podpisane (`Status: Signed`) i dostępna jest komenda `Broadcast`.



Jest to ostatnia operacja, którą należy wykonać:



![image](assets/en/32.webp)



## Wnioski



Twoje testy dobiegły końca. Jeśli postępowałeś zgodnie z instrukcją i uzyskałeś takie same wyniki, utworzyłeś Wallet Cold z Electrum na dwóch różnych komputerach, których możesz używać w sposób airgap do przechowywania Bitcoinów.



Jedyne rzeczy, na które należy zwrócić szczególną uwagę, to dwie kwestie:


1) **nigdy nie używaj Wallet airgap do adresów odbiorczych generate**. Ponieważ jest offline, zawsze zaoferuje ci pierwszy Address, który pokrywa się z tym, którego właśnie użyłeś do wykonania transakcji testowej;



![image](assets/en/33.webp)



jak widać na powyższym obrazku, Wallet offline nie zna własnej historii Address. Pod tym względem jest całkowicie ślepy. **Jego jedynym zadaniem jest przechowywanie kluczy offline i podpisywanie transakcji**_.



2) Używaj pamięci USB przeznaczonej tylko do tego celu, **nie używaj nośnika, którego używasz często**. Codzienne narzędzia są bardziej narażone na cyberataki, a nieumyślnie można zaatakować nawet komputer, który jest odłączony od sieci. Pamięć USB, której używasz tylko do tego celu, ma bardzo mało możliwości nawiązania kontaktu z komputerem online, zwłaszcza jeśli jesteś hodowcą, który nie musi wydawać, zmniejszając w ten sposób prawdopodobieństwo otrzymania, a następnie przesłania wirusów, złośliwego oprogramowania itp.