---
name: Ashigaru - Pasażer na gapę
description: Jak mogę dokonać transakcji Payjoin na Ashigaru?
---
![cover](assets/cover.webp)



> *Zmusić szpiegów blockchain do przemyślenia wszystkiego, co myślą, że wiedzą*

Payjoin to struktura transakcji Bitcoin zaprojektowana w celu zwiększenia poufności użytkownika poprzez bezpośrednią współpracę z odbiorcą płatności. Istnieje kilka implementacji ułatwiających jej wdrożenie i automatyzujących proces. Najbardziej znanym z nich jest niewątpliwie Stowaway, początkowo opracowany przez zespół Samurai Wallet, a obecnie zintegrowany z jego fork Ashigaru.



## Jak działa Stowaway?



Jak wspomniano wcześniej, Ashigaru integruje narzędzie PayJoin o nazwie `Stowaway`. Jest ono dostępne w aplikacji Ashigaru na Androida. Aby przeprowadzić Payjoin, odbiorca (który również przyjmuje rolę współpracownika) musi korzystać z oprogramowania kompatybilnego ze Stowaway, czyli na razie tylko Ashigaru.



Stowaway opiera się na kategorii transakcji, które Samurai określił jako "Cahoots". Cahoot to transakcja oparta na współpracy między kilkoma użytkownikami, obejmująca wymianę informacji poza blockchainem Bitcoin. Ashigaru oferuje obecnie dwa narzędzia Cahoots: Stowaway (Payjoins) i StonewallX2.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b

Transakcje Cahoots wymagają wymiany częściowo podpisanych transakcji między użytkownikami. Proces ten może być długi i żmudny, zwłaszcza gdy jest przeprowadzany zdalnie. Nadal jednak można to zrobić ręcznie, jeśli współpracownicy znajdują się w tej samej lokalizacji. Konkretnie polega to na zeskanowaniu kolejno pięciu kodów QR wymienianych między dwoma uczestnikami.



Na odległość metoda ta staje się zbyt skomplikowana. Aby temu zaradzić, Samourai opracował szyfrowany protokół komunikacyjny oparty na sieci Tor o nazwie "*Soroban*". Dzięki Soroban, wymiany wymagane do Payjoin są zautomatyzowane i odbywają się w tle.



Ta szyfrowana komunikacja wymaga połączenia i uwierzytelnienia między uczestnikami Cahoot. Właśnie dlatego Soroban polega na Paynyms użytkowników. Jeśli nie wiesz jeszcze, jak działa Paynyms, zapoznaj się z tym dedykowanym samouczkiem, aby dowiedzieć się więcej:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

W skrócie, Paynym to unikalny identyfikator powiązany z Twoim wallet, umożliwiający aktywację różnych funkcji, w tym szyfrowanej wymiany. Ma on postać identyfikatora, któremu towarzyszy ilustracja. Oto na przykład ten, którego używam na Testnet:



![Image](assets/fr/01.webp)



**Podsumowując:**





- payjoin" = specyficzna struktura transakcji współpracy;





- `Stowaway` = implementacja Payjoin dostępna na Ashigaru;





- `Cahoots` = Nazwa nadana przez Samourai wszystkim rodzajom transakcji opartych na współpracy, w szczególności Payjoin `Stowaway`, przejętym dzisiaj na Ashigaru;





- soroban = zaszyfrowany protokół komunikacyjny ustanowiony na Torze, który umożliwia współpracę z innymi użytkownikami w ramach transakcji `Cahoots`;





- paynym" = Unikalny identyfikator wallet używany do nawiązania komunikacji z innym użytkownikiem na "Soroban" w celu przeprowadzenia transakcji "Chahoots".



Aby uzyskać bardziej szczegółowe spojrzenie na działanie Payjoins i ich przydatność w prywatności onchain, polecam ten inny samouczek:



https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

## Jak ustanowić połączenie między Paynyms?



Aby rozpocząć, należy oczywiście zainstalować Ashigaru i utworzyć plik :



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Aby przeprowadzić zdalną transakcję Cahoots, w tym PayJoin (*Stowaway*) za pośrednictwem Ashigaru, musisz najpierw "śledzić" użytkownika, z którym chcesz współpracować, używając jego Paynym. W przypadku pasażera na gapę oznacza to śledzenie osoby, do której chcesz wysłać bitcoiny. Jeśli nie wiesz jeszcze, jak podążać za innym Paynym, szczegółową procedurę znajdziesz w tym samouczku :



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Jak mogę dokonać Payjoin na Ashigaru?



Aby przeprowadzić transakcję Stowaway, kliknij na obraz swojego Paynym w lewym górnym rogu ekranu, a następnie otwórz menu `Collaborate`. Osoba biorąca udział w transakcji musi zrobić to samo, chyba że wymieniacie się kodami QR osobiście.



![Image](assets/fr/02.webp)



Masz dwie opcje: wybierz `Initiate`, jeśli jesteś nadawcą płatności, lub `Participate`, jeśli jesteś odbiorcą tej płatności.



![Image](assets/fr/03.webp)



Jeśli jesteś odbiorcą, procedura jest bardzo prosta. W przypadku zdalnej współpracy za pośrednictwem sieci Soroban, kliknij `Uczestnicz`, wybierz konto, którego chcesz użyć, a następnie naciśnij `OCZEKIWAJ NA ŻĄDANIA ZAPŁATY`, aby oczekiwać na żądanie wysłane przez płatnika.



![Image](assets/fr/04.webp)



Z drugiej strony, w przypadku współpracy osobistej poprzez skanowanie kodu QR, przejdź do strony głównej wallet, naciśnij ikonę kodu QR u góry ekranu, a następnie zeskanuj kod QR dostarczony przez płatnika inicjującego transakcję.



![Image](assets/fr/05.webp)



Jeśli jesteś w roli płatnika, tj. osoby inicjującej transakcję, przejdź do menu `Współpracuj`, a następnie wybierz `Inicjuj`.



![Image](assets/fr/06.webp)



Dla typu transakcji, ponieważ chcemy dokonać Payjoin Stowaway, wybierz tę opcję.



![Image](assets/fr/07.webp)



Następnie można wybrać między współpracą online (*Cahoots* za pośrednictwem *Soroban*) lub współpracą twarzą w twarz, z wymianą kodów QR.



![Image](assets/fr/08.webp)



### Cahoots online



Jeśli wybrałeś opcję `Online`, wybierz odbiorcę z Paynyms, które śledzisz.



![Image](assets/fr/09.webp)



Kliknij `Set up transaction`, a następnie wybierz konto, z którego chcesz dokonać wydatku.



![Image](assets/fr/10.webp)



Na następnej stronie wprowadź szczegóły transakcji: kwotę do wysłania do odbiorcy i stawkę opłaty. Nie ma potrzeby wprowadzania adresu odbiorczego, ponieważ odbiorca sam go prześle podczas wymiany PSBT.



Następnie kliknij `Review transaction setup`.



![Image](assets/fr/11.webp)



Sprawdź dokładnie informacje, upewnij się, że twój współpracownik słucha żądań *Cahoots*, a następnie kliknij zielony przycisk `BEGIN TRANSACTION`, aby zainicjować wymianę PSBT przez Soroban.



![Image](assets/fr/12.webp)



Poczekaj, aż obaj uczestnicy podpiszą transakcję, a następnie wyemituj ją w sieci Bitcoin.



![Image](assets/fr/13.webp)



### Rozmowy twarzą w twarz



Jeśli chcesz przeprowadzić wymianę osobiście, wybierz typ transakcji `STONEWALL X2`, a następnie wybierz opcję `In Person / Manual`.



![Image](assets/fr/14.webp)



Kliknij `Set up transaction`, a następnie wybierz konto, z którego chcesz dokonać wydatku.



![Image](assets/fr/15.webp)



Na następnej stronie wprowadź szczegóły transakcji: kwotę do wysłania do odbiorcy i stawkę opłaty. Nie ma potrzeby wprowadzania adresu odbiorczego, ponieważ odbiorca sam go prześle podczas wymiany PSBT.



Następnie kliknij `Review transaction setup`.



![Image](assets/fr/16.webp)



Sprawdź szczegóły, a następnie naciśnij zielony przycisk "ROZPOCZNIJ TRANSAKCJĘ", aby rozpocząć wymianę PSBT za pomocą skanowania kodu QR.



![Image](assets/fr/17.webp)



Wymiana odbywa się poprzez naprzemienne skanowanie ze współpracownikiem: kliknij `SHOW QR CODE`, aby wyświetlić swój kod QR współpracownikowi, który go zeskanuje. On następnie kliknie `SHOW QR CODE`, aby wyświetlić swój kod, a ty zeskanujesz go za pomocą `LAUNCH QR Scanner`. Powtarzaj ten proces, aż wszystkie pięć kroków wymiany zostanie ukończonych.



![Image](assets/fr/18.webp)



Po zakończeniu wszystkich wymian sprawdź szczegóły transakcji, a następnie zwolnij ją, przeciągając zieloną strzałkę u dołu ekranu.



![Image](assets/fr/19.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/82efd3700bba87b0f172e9cc045e441b38622c95a60df9f39a21f63eb4590a96). Jego struktura jest następująca:



![Image](assets/fr/20.webp)



*Kredyt: [mempool.space](https://mempool.space/)*



Jeśli przeanalizujemy tę transakcję, zobaczymy moje UTXO w wysokości `164,211 sats` po stronie wejściowej, a także UTXO w wysokości `190,002 sats` należące do faktycznego odbiorcy płatności. Po stronie wyjściowej otrzymuję UTXO w wysokości `63 995 sats`, podczas gdy odbiorca otrzymuje UTXO w wysokości `290 002 sats`. Porównując dane wejściowe i wyjściowe, widzimy, że odbiorca rzeczywiście zarobił `100 000 sats`, co odpowiada kwocie mojej rzeczywistej płatności, a ja straciłem `100 000 sats`, do których dodałem koszty mining.



Oczywiście mogę opisać tę strukturę, ponieważ sam zbudowałem transakcję. Ale dla obserwatora z zewnątrz, generalnie niemożliwe jest określenie, które UTXO należą do którego uczestnika, zarówno w wejściach, jak i wyjściach.



Aby pogłębić swoją wiedzę na temat zarządzania prywatnością onchain na Bitcoin, polecam wziąć udział w moim szkoleniu BTC 204 na Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c