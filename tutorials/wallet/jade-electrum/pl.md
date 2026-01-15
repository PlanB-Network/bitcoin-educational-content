---
name: Jade - Electrum
description: Jak używać Jade lub Jade Plus z Electrum (komputer stacjonarny)
---

![cover](assets/cover.webp)



_Ten przewodnik pochodzi z lekcji [Bitcoin Workshops](https://officinebitcoin.it/lezioni/jadeele/index.html)_



Samouczek został stworzony przy użyciu Jade Classic, ale operacje są również ważne dla tych, którzy mają Jade Plus.



Po zainicjowaniu Jade można zacząć go używać i - w tym celu - wybrać wyświetlacz wallet.



Jade to urządzenie, które może być używane z kilkoma wallet lub aplikacjami towarzyszącymi, jak określa je Blockstream na swojej stronie internetowej.



W tym samouczku przedstawiono kroki korzystania z Electrum Wallet za pośrednictwem połączenia kablowego USB.



## Transfer klucza publicznego



Weź i włącz zainicjowaną Jade. Po włączeniu wygląda on następująco:




![img](assets/en/32.webp)



Po wybraniu opcji _Unlock Jade_ pojawi się menu, w którym należy wybrać sposób połączenia urządzenia z aplikacją towarzyszącą.



Z Electrum możesz podłączyć Jade tylko przez USB, więc wybierz tę metodę.



Uruchom Electrum, który otworzy się proponując jako domyślną opcję otwarcie ostatnio używanego wallet.



Jeśli po raz pierwszy łączysz Jade z Electrum, wybierz _Create New Wallet_, a następnie _Finish_.



![img](assets/en/34.webp)



Nazwa wallet.



![img](assets/en/35.webp)



Wybierz Standard Wallet.



![img](assets/en/36.webp)



Wybierając magazyn kluczy, należy koniecznie wybrać opcję _Użyj urządzenia sprzętowego_.



![img](assets/en/37.webp)



Electrum rozpoczyna skanowanie w poszukiwaniu urządzenia sprzętowego.



![img](assets/en/38.webp)



Po podłączeniu USB do komputera (już podłączonego po stronie USB C do Jade), sprzęt wallet pojawia się w trybie blokady. Jade odblokowuje się poprzez wprowadzenie sześciocyfrowego kodu PIN ustawionego podczas konfiguracji.




![img](assets/en/39.webp)



Odblokowane urządzenie sprzętowe, Electrum wykrywa Jade. Kontynuuj klikając _Next_.



![img](assets/en/40.webp)



W tym momencie Electrum prosi o ustawienie skryptu polityki: wybierz _Native Segwit_.



![img](assets/en/41.webp)



Rozpoczyna się faza transferu klucza publicznego z wallet z Jade do wyświetlacza Electrum.



Po zakończeniu eksportu klucza publicznego proces jest zakończony.



Watch-only jest gotowy i Electrum ostrzega o zakończeniu z następującym ekranem.



![img](assets/en/42.webp)



wallet jest faktycznie utworzony i można rozpocząć jego eksplorację: można zobaczyć _adresy_, _informacje o portfelu_ i - co najważniejsze - można zobaczyć w prawym dolnym rogu wskazanie, że jest to urządzenie Blockstream. Zielona kropka obok logo Blockstream wskazuje, że urządzenie jest włączone i prawidłowo podłączone do sieci lokalnej.



![img](assets/en/43.webp)



## Przyjmowanie i wydawanie transakcji



Z menu _Receive_ w Electrum, generate `scriptPubKey` (adres), aby otrzymać środki. Zawsze zaczynaj od małej kwoty i wykonaj test odbioru+wydania.



![img](assets/en/44.webp)



Po otrzymaniu wiadomości można sprawdzić ich przybycie w menu _Historia_.



![img](assets/en/45.webp)



![img](assets/en/46.webp)



Po potwierdzeniu transakcji możesz wydać UTXO i zakończyć test.



Wydatek wiąże się z użyciem Jade do podpisu.



Przejdź do menu _Send_ Electrum, wklej skryptPubKey i sprawdź go dobrze.



![img](assets/en/47.webp)



Po zakończeniu naciśnij przycisk _Pay_.



Otworzy się okno transakcji, w którym ważne jest ustawienie prawidłowych opłat transakcyjnych. Po zakończeniu wszystkich ustawień kliknij _Preview_ w prawym dolnym rogu.



![img](assets/en/48.webp)



Okno transakcji pokazuje kilka ważnych szczegółów, przede wszystkim status: `Unsigned`.



Na tym etapie widoczne jest również polecenie _Sign_, które należy kliknąć, aby złożyć podpis za pomocą Jade.



![img](assets/en/49.webp)



Teraz rozpoczyna się faza komunikacji między wyświetlaczem wallet a urządzeniem sprzętowym, w której Electrum ostrzega, aby postępować zgodnie z instrukcjami na urządzeniu sprzętowym, włączonym i gotowym do podpisania.



![img](assets/en/50.webp)



**Najpierw jednak lepiej zweryfikuj to, co podpisujesz: wszystkie parametry transakcji, które właśnie skonfigurowałeś, pojawiają się również na Jade** i możesz je wszystkie zweryfikować.



![img](assets/en/51.webp)



Aby kontynuować, upewnij się, że zawsze umieszczasz kursor na strzałce `→`, która prowadzi do kolejnych kroków, a nigdy na `X`, chyba że chcesz zakończyć operację bez jej ukończenia.



Część weryfikacyjna kończy się wyświetleniem opłaty. W tym momencie potwierdzenie jest równoznaczne ze złożeniem podpisu.



![img](assets/en/52.webp)



Przez krótką chwilę Jade przetwarza operację, a po jej zakończeniu powraca do menu głównego.



![img](assets/en/53.webp)



W Electrum możesz zobaczyć status transakcji, który zmienił się z `Unsigned` na `Signed` i teraz możesz ją propagować, klikając _Broadcast_.



![img](assets/en/54.webp)



Przetestowany w ten sposób wallet może być użyty do odbioru UTXO przeznaczonego do bezpiecznego przechowywania.



![img](assets/en/55.webp)



Ten przewodnik jest przykładem tego, jak używać Jade podłączonego przez USB do zegarka wallet. Electrum jest klasycznym przykładem, ale możesz preferować inne oprogramowanie wallet. Jade eksportuje klucz publiczny do wielu innych portfeli: znajdź podobne funkcje, o których przeczytasz w tym samouczku, aby poprowadzić Cię i znaleźć sposób na wykorzystanie go w swojej ulubionej aplikacji companio.