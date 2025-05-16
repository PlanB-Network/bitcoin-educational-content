---
name: Test odzyskiwania
description: Jak przetestować kopie zapasowe, aby nie stracić bitcoinów?
---
![cover](assets/cover.webp)


Podczas tworzenia Bitcoin Wallet użytkownik jest proszony o zanotowanie frazy Mnemonic, zwykle składającej się z 12 lub 24 słów. Fraza ta umożliwia odzyskanie dostępu do bitcoinów w przypadku utraty, uszkodzenia lub kradzieży urządzenia obsługującego Wallet. Przed rozpoczęciem korzystania z nowego Bitcoin Wallet bardzo ważne jest zweryfikowanie ważności tej frazy Mnemonic. Najlepszym sposobem na to jest wykonanie testu odzyskiwania na sucho.


Test ten polega na symulacji przywrócenia Wallet przed zdeponowaniem w nim jakichkolwiek bitcoinów. Dopóki Wallet jest pusty, symulujemy sytuację, w której urządzenie przechowujące nasze klucze zostało utracone, a jedyne, co nam pozostało, to nasza fraza Mnemonic, aby spróbować odzyskać nasze bitcoiny.


![RECOVERY TEST](assets/notext/01.webp)


## Jaki jest tego cel?


Ten proces testowania pozwala zweryfikować, czy fizyczna kopia zapasowa frazy Mnemonic, w formie papierowej lub metalowej, jest funkcjonalna. Niepowodzenie podczas tego testu odzyskiwania sygnalizuje błąd w kopii zapasowej frazy, narażając tym samym bitcoiny na ryzyko. Z drugiej strony, jeśli test zakończy się pomyślnie, potwierdza to, że fraza Mnemonic jest w pełni sprawna i można spokojnie zabezpieczyć bitcoiny za pomocą Wallet.


Przeprowadzenie testu odzyskiwania na sucho ma podwójną zaletę. Nie tylko pozwala sprawdzić dokładność frazy Mnemonic, ale także daje możliwość zapoznania się z procesem odzyskiwania Wallet. W ten sposób odkryjesz potencjalne trudności, zanim pojawi się prawdziwa sytuacja. W dniu, w którym faktycznie będziesz musiał odzyskać Wallet, będziesz mniej zestresowany, ponieważ będziesz już znał proces, zmniejszając ryzyko błędu. Dlatego ważne jest, aby nie zaniedbywać tego etapu testowania i poświęcić niezbędną ilość czasu na jego prawidłowe wykonanie.


## Co to jest test odzyskiwania?


Proces testu jest dość prosty:


- Po utworzeniu nowego Bitcoin Wallet, a przed zdeponowaniem pierwszych satoshi, zanotuj informacje o świadku, takie jak xpub, pierwszy otrzymany Address, a nawet odcisk palca klucza głównego;
- Następnie celowo usuń wciąż pusty Wallet, na przykład resetując Hardware Wallet do ustawień fabrycznych;
- Następnie przeprowadź symulację odzyskiwania Wallet, korzystając wyłącznie z papierowych kopii zapasowych frazy Mnemonic i passphrase, jeśli z nich korzystasz;
- Na koniec sprawdź, czy informacje o świadku są zgodne z informacjami o zregenerowanym Wallet. Jeśli informacje się zgadzają, możesz być pewny niezawodności swojej fizycznej kopii zapasowej, a następnie możesz wysłać swoje pierwsze bitcoiny do tego Wallet.

Należy uważać, aby podczas testu odzyskiwania **używać tego samego urządzenia, które jest przeznaczone dla ostatecznego Wallet**, aby nie zwiększyć powierzchni ataku Wallet. Na przykład, jeśli tworzysz Wallet na Trezor Safe 5, upewnij się, że wykonujesz test odzyskiwania na tym samym Trezor Safe 5. Ważne jest, aby nie wprowadzać frazy odzyskiwania do żadnego innego oprogramowania, ponieważ naruszyłoby to bezpieczeństwo zapewniane przez Hardware Wallet, nawet jeśli Wallet jest nadal pusty.


## Jak przeprowadzić test odzyskiwania?


W tym samouczku wyjaśnię, jak wykonać test odzyskiwania na Bitcoin Software Wallet, używając Sparrow Wallet (dla Hot Wallet). Jednak proces pozostaje taki sam dla każdego innego typu urządzenia. Ponownie, **jeśli używasz Hardware Wallet, nie wykonuj testu odzyskiwania na Sparrow Wallet** (patrz poprzednia sekcja).


Właśnie utworzyłem nowy Hot Wallet na Sparrow Wallet. W tej chwili nie wysłałem jeszcze na niego żadnych bitcoinów. Jest pusty.


![RECOVERY TEST](assets/notext/02.webp)


Starannie zanotowałem moją 12-wyrazową frazę Mnemonic na kartce papieru. A ponieważ chcę zwiększyć bezpieczeństwo tego Wallet, utworzyłem również BIP39 passphrase, który zapisałem na innej kartce papieru:


```txt
1. shield
2. brass
3. sentence
4. cube
5. marble
6. glad
7. satoshi
8. door
9. project
10. panic
11. prepare
12. general
```


```text
Passphrase: YfaicGzXH9t5C#g&47Kzbc$JL
```


***Oczywiście nigdy nie powinieneś udostępniać swojej frazy Mnemonic i passphrase w Internecie, w przeciwieństwie do tego, co robię w tym samouczku. Ten przykład Wallet nie będzie używany i zostanie usunięty po zakończeniu samouczka.***


Zanotuję teraz na szkicu informację o świadku z mojego Wallet. Możesz wybrać różne informacje, takie jak pierwszy odbierający Address, xpub lub odcisk palca klucza głównego. Osobiście zalecam wybranie pierwszego otrzymującego Address. Pozwala to zweryfikować, czy jesteś w stanie znaleźć pełną pierwszą ścieżkę derywacji prowadzącą do tego Address.


W aplikacji Sparrow kliknij zakładkę "*Adresy*".


![RECOVERY TEST](assets/notext/03.webp)


Następnie zanotuj na kartce papieru pierwszy otrzymany Address z twojego Wallet. W moim przykładzie Address to:


```txt
tb1qxv56mma5x5r7uhdkn0ldvcx6m0gj6f3kre0gwd
```


Po zanotowaniu informacji, przejdź do menu "*File*", a następnie wybierz "*Delete Wallet*". Przypominam jeszcze raz, że Bitcoin Wallet musi być pusty przed przystąpieniem do tej operacji.


![RECOVERY TEST](assets/notext/04.webp)


Jeśli Wallet jest rzeczywiście pusty, potwierdź usunięcie Wallet.


![RECOVERY TEST](assets/notext/05.webp)


Teraz musisz powtórzyć proces tworzenia Wallet, ale używając naszych papierowych kopii zapasowych. Kliknij menu "*File*", a następnie "*New Wallet*".


![RECOVERY TEST](assets/notext/06.webp)


Wprowadź ponownie nazwę urządzenia Wallet.


![RECOVERY TEST](assets/notext/07.webp)


W menu "*Script Type*" należy wybrać ten sam typ skryptu, co usunięty wcześniej Wallet.


![RECOVERY TEST](assets/notext/08.webp)


Następnie kliknij przycisk "*Nowy lub zaimportowany Software Wallet*".


![RECOVERY TEST](assets/notext/09.webp)


Wybierz odpowiednią liczbę słów dla swojego seed.


![RECOVERY TEST](assets/notext/10.webp)


Wprowadź frazę Mnemonic do oprogramowania. Jeśli pojawi się komunikat "*Invalid Checksum*", oznacza to, że kopia zapasowa frazy Mnemonic jest nieprawidłowa. Będziesz musiał rozpocząć tworzenie Wallet od zera, ponieważ test odzyskiwania nie powiódł się.


![RECOVERY TEST](assets/notext/11.webp)


Jeśli masz passphrase, tak jak w moim przypadku, również go wprowadź.


![RECOVERY TEST](assets/notext/12.webp)


Kliknij "*Create Keystore*", a następnie "*Import Keystore*".


![RECOVERY TEST](assets/notext/13.webp)


Na koniec kliknij przycisk "*Zastosuj*".


![RECOVERY TEST](assets/notext/14.webp)


Możesz teraz powrócić do zakładki "*Adresy*".


![RECOVERY TEST](assets/notext/15.webp)


Na koniec sprawdź, czy pierwszy odbierający Address jest zgodny z tym, który został odnotowany jako świadek w projekcie.


![RECOVERY TEST](assets/notext/16.webp)


Jeśli adresy odbiorcze są zgodne, test odzyskiwania zakończył się pomyślnie i można używać nowego Bitcoin Wallet. Jeśli adresy nie są zgodne, może to oznaczać albo błąd w wyborze typu skryptu, który powoduje, że ścieżka derywacji jest nieprawidłowa, albo problem z kopią zapasową frazy Mnemonic lub passphrase. W obu przypadkach zdecydowanie zalecam rozpoczęcie od zera i utworzenie nowego Bitcoin Wallet od początku, aby uniknąć ryzyka. Tym razem należy zwrócić uwagę, aby fraza Mnemonic nie zawierała błędów.

Gratulacje, jesteś teraz gotowy do przeprowadzenia testu odzyskiwania! Radzę uogólnić ten proces do tworzenia wszystkich portfeli Bitcoin. Jeśli ten poradnik okazał się pomocny, będę wdzięczny za pozostawienie kciuka w górę poniżej. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dziękuję bardzo!