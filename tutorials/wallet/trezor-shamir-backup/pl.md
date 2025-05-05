---
name: Trezor Shamir Backup
description: Pojedyncze i wieloczęściowe frazy Mnemonic na Trezor
---
![cover](assets/cover.webp)



*Źródło zdjęcia: [Trezor.io](https://trezor.io/)*



## Nowe opcje tworzenia kopii zapasowych w Trezor



Od 2023 r. Trezor oferuje nowy format kopii zapasowej o nazwie ***Single-share Backup***, stopniowo zastępując klasyczne podejście oparte na BIP39, które można znaleźć w większości portfeli. W przeciwieństwie do tradycyjnych 12- lub 24-wyrazowych fraz Mnemonic, ten nowy format opiera się na pojedynczej 20-wyrazowej frazie pochodzącej ze standardu opracowanego przez SatoshiLabs: **SLIP39**. Celem jest poprawa solidności i czytelności kopii zapasowych, przy jednoczesnym umożliwieniu płynnej migracji do rozproszonego modelu tworzenia kopii zapasowych.



Ten rozproszony model nazywa się ***Multi-share Backup***. Opiera się on na tej samej zasadzie, ale zamiast generować pojedynczą frazę Mnemonic, dzieli ją na kilka fragmentów zwanych ***shares***, z których każdy jest frazą Mnemonic samą w sobie. Aby przywrócić portfel, pewna liczba tych *udziałów* (określona przez *prog*) musi zostać ponownie połączona. Na przykład w schemacie 3 z 5, dowolne 3 *udziały* z 5 przywrócą portfel. Należy pamiętać, że rozproszony system tworzenia kopii zapasowych Trezor różni się od portfeli Multisig. Do wydawania bitcoinów wymagany jest tylko portfel Hardware Wallet Trezor. Wymagany jest tylko jeden podpis. Dystrybucja ma zastosowanie tylko na poziomie frazy Mnemonic, czyli kopii zapasowej.



![Image](assets/fr/01.webp)



System ten rozwiązuje problem pojedynczego punktu awarii frazy Mnemonic bez wad związanych z zarządzaniem Multisig lub passphrase BIP39. Proces odzyskiwania nie opiera się już na jednej informacji, ale na kilku, z dodatkową korzyścią w postaci tolerancji na straty dzięki progowi.



Użytkownicy, którzy utworzyli portfolio za pomocą *Single-share Backup*, mogą w dowolnym momencie przełączyć się na *Multi-share Backup* bez konieczności migracji portfolio. Adresy odbiorcze i konta pozostaną identyczne. System *Multi-share* wpływa tylko na kopię zapasową, podczas gdy reszta portfela pozostaje niezmieniona.



Funkcja Multi-share Backup* jest dostępna w urządzeniach Trezor Model T, Safe 3 i Safe 5. Funkcja ta nie jest obsługiwana przez Trezor Model One.



**Ważna uwaga:** System *Multi-share* Trezora jest kryptograficznie bezpieczny, ponieważ do dystrybucji wykorzystuje schemat *Shamir's Secret Sharing*. Zdecydowanie odradzamy stosowanie podobnego systemu ręcznie, poprzez samodzielne dzielenie klasycznej frazy Mnemonic. Jest to zła praktyka, która znacznie zwiększa ryzyko kradzieży i utraty bitcoinów, więc nie rób tego. Klasyczna fraza Mnemonic jest przechowywana w całości.



## Tajne udostępnianie Shamira w SLIP39



Mechanizm kryptograficzny leżący u podstaw kopii zapasowych *Multi-share* na Trezorze to *Shamir's Secret Sharing Scheme* (SSSS). Zasada jego działania jest następująca: tajne informacje (w tym przypadku seed portfela) są przekształcane w wielomian matematyczny. Następnie obliczanych jest kilka punktów tego wielomianu, z których każdy staje się udziałem. Oryginalny sekret jest rekonstruowany za pomocą interpolacji wielomianowej, poprzez zebranie minimalnej liczby punktów (próg).



Żadna tajna informacja nie może zostać wydedukowana z liczby udziałów poniżej progu, gwarantując doskonałe teoretyczne bezpieczeństwo tajnych informacji. Innymi słowy, nawet atakujący z nieograniczoną mocą obliczeniową nie może odgadnąć seed, jeśli próg nie zostanie osiągnięty.



SLIP39 wykorzystuje ten schemat do dystrybucji portfela seed. Każdy udział to zdanie składające się z 20 słów, zbudowane z listy 1024 słów (innej niż lista BIP39).



## Konfigurowanie wielodostępnej kopii zapasowej na urządzeniu Trezor



Podczas tworzenia portfolio na Trezor dostępne są trzy różne opcje:




- Użyj klasycznej frazy BIP39 Mnemonic składającej się z 12 lub 24 słów;
- Użyj pojedynczej frazy Mnemonic (SLIP39);
- Konfiguracja wielu fraz Mnemonic w trybie Multi-share (SLIP39).



Jeśli zdecydujesz się na frazę Single-share SLIP39 Mnemonic, będziesz mógł uaktualnić ją do Multi-share w późniejszym terminie bez konieczności resetowania portfela. Z drugiej strony, jeśli zaczniesz od klasycznego portfela BIP39 (fraza 12- lub 24-wyrazowa), nie będziesz w stanie przekonwertować go bezpośrednio na Multi-share. Konieczne będzie utworzenie nowego portfela Multi-share od podstaw i przeniesienie środków ze starego portfela do nowego za pośrednictwem jednej lub kilku transakcji Bitcoin. Jest to bardziej złożona i kosztowna operacja. Jeśli chcesz dokonać tej migracji, zalecam zakup nowego Trezora Hardware Wallet, aby uniknąć konieczności wprowadzania seed do oprogramowania portfela.



W tym samouczku najpierw przyjrzymy się, jak skonfigurować Multi-share podczas tworzenia portfela, a następnie, w kolejnej sekcji, zobaczymy, jak przekonwertować Single-share na Multi-share w istniejącym portfelu.



Jeśli potrzebujesz pomocy w początkowej konfiguracji urządzenia, mamy również szczegółowy samouczek dla każdego modelu Trezor:



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

### Nowe portfolio



Zakończyłeś wstępną konfigurację Trezora i jesteś gotowy do utworzenia portfolio. W Trezor Suite kliknij przycisk "*Utwórz nowy Wallet*".



![Image](assets/fr/02.webp)



Wybierz opcję "*Multi-share Backup*", a następnie kliknij "*Create Wallet*".



![Image](assets/fr/03.webp)



Zaakceptuj warunki korzystania z Trezora i potwierdź utworzenie portfolio.



![Image](assets/fr/04.webp)



W Trezor Suite kliknij "*Kontynuuj tworzenie kopii zapasowej*".



![Image](assets/fr/05.webp)



Przeczytaj uważnie instrukcje, potwierdź je, a następnie kliknij "*Twórz kopię zapasową Wallet*".



![Image](assets/fr/06.webp)



Aby uzyskać więcej informacji na temat właściwego sposobu zapisywania i zarządzania frazami Mnemonic, zdecydowanie polecam skorzystanie z tego samouczka, zwłaszcza jeśli jesteś początkującym:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Na urządzeniu Trezor wybierz całkowitą liczbę udziałów, które chcesz skonfigurować. Najpopularniejsze konfiguracje to 2-de-3 i 3-de-5. W tym przykładzie utworzę konfigurację 2-de-3, więc wybiorę 3 udziały. Każdy udział będzie reprezentował 20-wyrazową frazę Mnemonic.



*W przypadku użytkowników Safe 5, mimo że na ekranie pojawi się komunikat "*Tap to continue*", w celu potwierdzenia należy przesunąć palcem w górę



![Image](assets/fr/07.webp)



Następnie potwierdź próg, tj. liczbę akcji wymaganych do odzyskania dostępu do Wallet i zawartych w nim bitcoinów.



![Image](assets/fr/08.webp)



Trezor utworzy różne akcje (frazy Mnemonic) przy użyciu generatora liczb losowych. Upewnij się, że nie jesteś obserwowany podczas tej operacji. Zapisz słowa wyświetlone na ekranie na wybranym nośniku fizycznym. Ważne jest, aby słowa były ponumerowane i ułożone w kolejności.



Zalecam zanotowanie każdego udziału na osobnym nośniku i ostrożne zarządzanie ich przechowywaniem, aby uniknąć dostępu do kilku w tym samym miejscu. Na przykład w przypadku konfiguracji 2 na 3, takiej jak moja, jedną z opcji byłoby przechowywanie jednego udziału w moim domu, drugiego u zaufanego przyjaciela, a ostatniego w sejfie bankowym. Wybór miejsca przechowywania zależy od osobistej strategii bezpieczeństwa.



W górnej części ekranu możesz zobaczyć, który udział aktualnie przeglądasz.



oczywiście nigdy nie wolno dzielić się tymi słowami w Internecie, tak jak ja to robię w tym samouczku. Ten przykład Wallet będzie używany tylko na Testnet i zostanie usunięty po zakończeniu samouczka



![Image](assets/fr/09.webp)



Aby przejść do kolejnych słów, kliknij na dole ekranu. Możesz cofać się, przesuwając palcem w dół. Po zapisaniu wszystkich słów, przytrzymaj palec na ekranie, aby przejść do następnej akcji i powtórz operację.



![Image](assets/fr/10.webp)



Pod koniec każdego nagrania akcji zostaniesz poproszony o wybranie słów w swojej frazie Mnemonic, aby potwierdzić, że zapisałeś je poprawnie.



![Image](assets/fr/11.webp)



I to wszystko, pomyślnie utworzono kopię zapasową portfela przy użyciu opcji Multi-share. Możesz teraz kontynuować pozostałe instrukcje konfiguracji.



### Na istniejącym portfelu pojedynczych akcji



Jeśli posiadasz już Trezor Wallet z kopią zapasową single-share (fraza SLIP39 Mnemonic, a nie klasyczna fraza BIP39) i chciałbyś zwiększyć dostępność i bezpieczeństwo swojej kopii zapasowej Wallet, możesz skonfigurować system multi-share bez konieczności transferu bitcoinów.



Aby to zrobić, podłącz i odblokuj Hardware Wallet. W aplikacji Trezor Suite przejdź do Ustawień.



![Image](assets/fr/12.webp)



Przejdź do zakładki "*Urządzenie*".



![Image](assets/fr/13.webp)



Następnie kliknij "*Twórz kopię zapasową wielu udziałów*".



![Image](assets/fr/14.webp)



Przeczytaj instrukcje, a następnie kliknij "*Create Multi-share Backup*".



![Image](assets/fr/15.webp)



Następnie należy wprowadzić bieżącą frazę Mnemonic (pojedynczy udział) na ekranie Trezor. Wybierz liczbę słów (domyślnie 20).



![Image](assets/fr/16.webp)



Następnie użyj klawiatury ekranowej Trezora, aby wprowadzić każde słowo bieżącej frazy Mnemonic.



![Image](assets/fr/17.webp)



Następnie można wybrać konfigurację kopii zapasowej Multi-share, postępując zgodnie z instrukcjami podanymi w poprzedniej sekcji.



![Image](assets/fr/18.webp)



Po utworzeniu kopii zapasowej z wieloma udziałami należy zdecydować, co zrobić z oryginalną frazą Mnemonic z jednym udziałem. Ponieważ portfel Bitcoin pozostaje taki sam, ta pojedyncza fraza zawsze będzie umożliwiać dostęp do niego. Będzie to zależeć od strategii bezpieczeństwa, ale ogólnie zaleca się zniszczenie tej frazy, aby wyeliminować ten pojedynczy punkt awarii, co jest właśnie celem Multi-share Backup. Jeśli zdecydujesz się go zniszczyć, upewnij się, że robisz to bezpiecznie, ponieważ **wciąż daje dostęp do twoich bitcoinów**.



Gratulacje, jesteś teraz na bieżąco z korzystaniem z jedno- i wielostanowiskowych kopii zapasowych w portfelach sprzętowych Trezor. Jeśli chcesz pójść o krok dalej w kwestii bezpieczeństwa Wallet, zapoznaj się z tym samouczkiem na temat haseł BIP39:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Jeśli uznałeś ten poradnik za przydatny, będę wdzięczny za pozostawienie kciuka Green poniżej. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dziękuję bardzo!



## Dodatkowe zasoby





- [SLIP-0039: Shamir's Secret-Sharing for Mnemonic Codes](https://github.com/satoshilabs/slips/blob/master/slip-0039.md);
- [Multi-share Backup na Trezor](https://trezor.io/learn/a/multi-share-backup-on-trezor);
- [Wikipedia: Shamir's secret sharing](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing).