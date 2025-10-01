---
name: BIP-39 Passphrase Trezor
description: Jak dodać passphrase do mojego portfolio Trezor?
---
![cover](assets/cover.webp)



passphrase BIP39 to opcjonalne hasło, które w połączeniu z frazą Mnemonic zapewnia dodatkowy Layer bezpieczeństwa dla deterministycznych i hierarchicznych portfeli Bitcoin. W tym samouczku wspólnie odkryjemy, jak skonfigurować passphrase na bezpiecznym Bitcoin Wallet na Trezorze (Safe 3, Safe 5 i Model One).



![Image](assets/fr/01.webp)



Przed rozpoczęciem tego samouczka, jeśli nie jesteś zaznajomiony z koncepcją passphrase, jego działaniem i implikacjami dla Bitcoin Wallet, zdecydowanie zalecam zapoznanie się z tym innym artykułem teoretycznym, w którym wyjaśniam wszystko (jest to bardzo ważne, ponieważ używanie passphrase bez pełnego zrozumienia jego działania może narazić twoje bitcoiny na ryzyko):



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

passphrase na Trezorze jest obsługiwany w klasyczny sposób, jeśli wybrałeś standard BIP39 podczas konfiguracji (co polecam, jeśli nie potrzebujesz *Multi-share Backup*). Cechą szczególną Trezora jest to, że passphrase można wprowadzić bezpośrednio na Hardware Wallet lub za pomocą klawiatury komputera przy użyciu oprogramowania Trezor Suite. Ta druga opcja jest znacznie mniej bezpieczna, ponieważ komputer ma znacznie większą powierzchnię ataku niż Hardware Wallet. Jednak wpisywanie złożonego hasła passphrase może być szybsze na konwencjonalnej klawiaturze niż na Hardware Wallet, co może zachęcać do używania silnych haseł. Dlatego zawsze lepiej jest używać passphrase, nawet jeśli trzeba go wpisać, niż nie używać go wcale. Ważne jest jednak, aby mieć świadomość zwiększonego ryzyka ataków numerycznych, które się z tym wiążą.



Opcje te nie są dostępne we wszystkich programach do zarządzania portfelem kompatybilnych z Trezor. Na przykład dla Modelu One, passphrase można wprowadzić za pomocą klawiatury na Sparrow Wallet. W przypadku modeli Model T, Safe 3 i Safe 5 należy użyć Trezor Suite lub wprowadzić passphrase bezpośrednio na Hardware Wallet, ponieważ opcja wprowadzania za pośrednictwem Sparrow została wyłączona przez HWI kilka lat temu.



![Image](assets/fr/02.webp)



W Trezor Suite dostępne są dwa różne sposoby zarządzania zapotrzebowaniem na passphrase. Można aktywować opcję "*passphrase*" w zakładce "*Urządzenie*". Po jej włączeniu Trezor Suite i wszystkie inne programy do zarządzania portfelem będą systematycznie prosić o wprowadzenie passphrase przy każdym uruchomieniu. Jeśli wolisz bardziej dyskretne podejście do korzystania z passphrase, możesz pozostawić ustawienie "*Standard*". W takim przypadku należy ręcznie przejść do menu Hardware Wallet w lewym górnym rogu i kliknąć przycisk "*+ passphrase*" przy każdym uruchomieniu.



Przed rozpoczęciem tego samouczka należy upewnić się, że Trezor został już zainicjowany i wygenerowano frazę Mnemonic. Jeśli tego nie zrobiłeś, a twój Trezor jest nowy, postępuj zgodnie z samouczkiem dotyczącym konkretnego modelu dostępnym na Plan ₿ Network. Po wykonaniu tego kroku można powrócić do tego samouczka.



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02


## Dodanie passphrase do urządzenia Safe 3 lub Safe 5



Po utworzeniu Wallet, zapisaniu Mnemonic i ustawieniu kodu PIN zostaniesz przeniesiony do menu głównego Trezor Suite. W lewym górnym rogu powinno pojawić się okno z zaproszeniem do aktywacji passphrase BIP39.



![Image](assets/fr/03.webp)



Jeśli to okno się nie pojawi, należy ręcznie aktywować opcję "*passphrase*" w zakładce ustawień "*Urządzenie*".



![Image](assets/fr/04.webp)



W tym oknie zostanie wyświetlona prośba o wprowadzenie numeru passphrase. Wybierz silny passphrase i natychmiast wykonaj fizyczną kopię zapasową na nośniku takim jak papier lub metal. W tym przykładzie wybrałem passphrase: `fH3&kL@9mP#2sD5qR!82`. Jest to przykład, jednak zalecam wybranie nieco dłuższego passphrase. Od 30 do 40 znaków byłoby idealne (jak dobre hasło).



oczywiście nigdy nie należy udostępniać passphrase w Internecie, tak jak robię to w tym poradniku. Ten przykładowy Wallet będzie używany tylko na Testnet i zostanie usunięty po zakończeniu samouczka.



Aby uzyskać bardziej szczegółowe zalecenia dotyczące wyboru passphrase, ponownie zapraszam do zapoznania się z tym artykułem:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Jeśli chcesz wprowadzić swój numer passphrase za pomocą klawiatury komputera, wprowadź go w odpowiednim polu, a następnie kliknij "*Access passphrase Wallet*".



![Image](assets/fr/05.webp)



Następnie Hardware Wallet wyświetli passphrase. Upewnij się, że jest on zgodny z fizyczną kopią zapasową (papierową lub metalową) przed kliknięciem ekranu, aby kontynuować.



![Image](assets/fr/06.webp)



Zapewni to dostęp do portfela chronionego przez passphrase.



![Image](assets/fr/07.webp)



Jeśli wolisz zwiększyć bezpieczeństwo, wprowadzając passphrase tylko na Trezorze, po wyświetleniu monitu kliknij "*Wprowadź passphrase na Trezorze*".



![Image](assets/fr/08.webp)



Na urządzeniu Trezor pojawi się klawiatura T9, umożliwiająca wprowadzenie passphrase. Po wprowadzeniu danych kliknij przycisk Green, aby zastosować passphrase do Wallet.



![Image](assets/fr/09.webp)



Uzyskasz wtedy dostęp do zabezpieczonego passphrase i Wallet.



![Image](assets/fr/10.webp)



Aby użyć Sparrow Wallet, procedura jest podobna, ale dla modeli T, Safe 3 i Safe 5, passphrase musi być wprowadzony na Hardware Wallet, a nie za pomocą klawiatury komputera.



Za każdym razem, gdy Sparrow Wallet wymaga dostępu do Trezora, a passphrase nie został jeszcze zastosowany od ostatniego uruchomienia, musisz wprowadzić go za pomocą klawiatury T9.



![Image](assets/fr/11.webp)



## Dodawanie passphrase do modelu One



W przypadku Modelu One użycie passphrase BIP39 jest niemal niezbędne. Ponieważ urządzenie to nie zawiera bezpiecznego elementu, stosunkowo łatwo jest wyodrębnić poufne informacje. Dlatego też nie jest ono odporne na atak fizyczny. Ponieważ jednak passphrase nie jest przechowywany na urządzeniu po jego wyłączeniu, użycie silnego (niebrutalnego) passphrase może chronić przed większością znanych ataków fizycznych na ten model.



W Modelu One nie jest możliwe wprowadzenie passphrase bezpośrednio na Hardware Wallet. Konieczne będzie wprowadzenie go za pomocą klawiatury komputera.



Po utworzeniu Wallet, zapisaniu Mnemonic i ustawieniu kodu PIN zostaniesz przeniesiony do menu głównego Trezor Suite. W lewym górnym rogu powinno pojawić się okno z zaproszeniem do aktywacji passphrase BIP39.



![Image](assets/fr/12.webp)



Jeśli to okno się nie pojawi, należy aktywować opcję "*passphrase*" w zakładce "*Urządzenie*" w ustawieniach.



![Image](assets/fr/13.webp)



Zostanie wyświetlone okno z prośbą o wprowadzenie numeru passphrase. Wybierz silny passphrase i natychmiast wykonaj fizyczną kopię zapasową na nośniku takim jak papier lub metal. W tym przykładzie wybrałem passphrase: `fH3&kL@9mP#2sD5qR!82`. To tylko przykład, jednak zalecam wybranie nieco dłuższego passphrase. Od 30 do 40 znaków byłoby idealne (jak dobre hasło).



Aby uzyskać bardziej szczegółowe zalecenia dotyczące wyboru passphrase, ponownie zapraszam do zapoznania się z tym artykułem:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Wprowadź swój passphrase w odpowiednim polu, a następnie kliknij przycisk "*Access passphrase Wallet*".



![Image](assets/fr/14.webp)



Hardware Wallet wyświetli passphrase. Upewnij się, że jest on zgodny z fizyczną kopią zapasową (papierową lub metalową), a następnie kliknij przycisk po prawej stronie, aby kontynuować.



![Image](assets/fr/15.webp)



Spowoduje to przejście do portfela chronionego przez passphrase.



![Image](assets/fr/16.webp)



Aby później korzystać z urządzenia Sparrow Wallet, procedura pozostaje taka sama. Za każdym razem, gdy Sparrow wymaga dostępu do Hardware Wallet, a passphrase nie został wprowadzony od ostatniego uruchomienia urządzenia, należy go wprowadzić.



![Image](assets/fr/17.webp)



Gratulacje, jesteś teraz gotowy do korzystania z passphrase BIP39 na portfelach sprzętowych Trezor. Jeśli chcesz pójść o krok dalej w kwestii bezpieczeństwa Wallet, zapoznaj się z tym samouczkiem na temat systemów kopii zapasowych Trezor *Multi-share* (*Shamir's Secret Sharing Scheme*):



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

Jeśli uznałeś ten poradnik za przydatny, będę wdzięczny za pozostawienie kciuka Green poniżej. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dziękuję bardzo!