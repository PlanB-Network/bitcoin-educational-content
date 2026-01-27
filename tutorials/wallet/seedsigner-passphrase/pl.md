---
name: BIP-39 Passphrase SeedSigner
description: Jak dodać passphrase do mojego portfela SeedSigner?
---

![cover](assets/cover.webp)



passphrase BIP39 to opcjonalne hasło, które w połączeniu z frazą mnemoniczną zapewnia dodatkową warstwę zabezpieczeń dla deterministycznych i hierarchicznych portfeli Bitcoin. W tym samouczku wspólnie odkryjemy, jak skonfigurować passphrase na Bitcoin wallet używanym z SeedSigner.



![Image](assets/fr/01.webp)



## Wymagania wstępne przed dodaniem hasła



Przed rozpoczęciem tego samouczka, jeśli nie jesteś zaznajomiony z koncepcją passphrase, jego działaniem i implikacjami dla Bitcoin wallet, zdecydowanie zalecam zapoznanie się z tym innym artykułem teoretycznym, w którym wyjaśniam wszystko (jest to bardzo ważne, ponieważ korzystanie z passphrase bez pełnego zrozumienia jego działania może narazić twoje bitcoiny na ryzyko):



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Przed rozpoczęciem tego samouczka upewnij się, że zainicjowałeś już swój SeedSigner i wygenerowałeś frazę mnemoniczną. Jeśli jeszcze tego nie zrobiłeś, a Twój SeedSigner jest zupełnie nowy, postępuj zgodnie z samouczkiem w Plan ₿ Academy. Po wykonaniu tego kroku możesz powrócić do tego samouczka:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## Jak dodać passphrase do SeedSigner?



Dodanie passphrase do portfela zarządzanego przez SeedSigner tworzy zupełnie nowy portfel, generując całkowicie oddzielny zestaw kluczy. W związku z tym, jeśli masz już portfel zawierający satss, nie będziesz już mógł uzyskać do niego dostępu za pomocą passphrase, ponieważ generuje on zupełnie inny portfel.



Aby zastosować passphrase do SeedSigner, włącz urządzenie i zeskanuj SeedQR w zwykły sposób. SeedSigner wyświetli wtedy odcisk palca aktualnego wallet, odpowiadający temu **bez passphrase**. wallet z passphrase będzie miał inny odcisk palca.



Kliknij przycisk `BIP-39 Passphrase`.



![Image](assets/fr/02.webp)



Następnie wprowadź wybrany passphrase w odpowiednim polu, korzystając z klawiatury ekranowej. Pamiętaj, aby wykonać jedną lub więcej fizycznych kopii zapasowych (papierowych lub metalowych): utrata tego passphrase spowoduje trwałą utratę dostępu do twoich bitcoinów. **Aby przywrócić wallet, niezbędny jest zarówno mnemonik, jak i passphrase ** Jeśli którykolwiek z nich zostanie utracony, twoje bitcoiny zostaną nieodwracalnie zablokowane.



Po zakończeniu wprowadzania danych, zatwierdź je, naciskając przycisk `KEY3` w prawym dolnym rogu SeedSigner.



![Image](assets/fr/03.webp)



*W tym przykładzie użyłem passphrase `pba`. Jednak w twoim przypadku upewnij się, że wybrałeś solidny passphrase. Aby dowiedzieć się, jak zdefiniować optymalny passphrase, zapoznaj się z tym artykułem:*



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Następnie SeedSigner wyświetli nowy odcisk palca passphrase wallet. Utwórz kilka kopii tego odcisku palca: jest to ważne w przypadku korzystania z wallet z passphrase, ponieważ umożliwia sprawdzenie za każdym razem, gdy wprowadzasz passphrase, czy nie popełniłeś żadnych błędów w pisowni i czy uzyskujesz dostęp do właściwego wallet.



Na przykład, jeśli w moim przypadku omyłkowo wpiszę passphrase `Pba` podczas uruchamiania SeedSigner zamiast `pba`, ta prosta zmiana z małych liter na duże spowoduje utworzenie zupełnie innego portfela niż ten, do którego chcę uzyskać dostęp.



Ten odcisk palca nie stanowi zagrożenia dla bezpieczeństwa ani poufności wallet. Nie ujawnia on żadnych informacji, publicznych ani prywatnych, na temat kluczy. Tak więc, w przeciwieństwie do mnemonika i passphrase, odcisk palca można zapisać na nośniku cyfrowym. Zalecam przechowywanie kopii w kilku miejscach: na kartce papieru, w menedżerze haseł itp.



Po zapisaniu odcisku palca kliknij przycisk "Gotowe".



![Image](assets/fr/04.webp)



Masz wtedy dostęp do wszystkich funkcji swojego portfela, tak jak w klasycznym SeedSigner.



![Image](assets/fr/05.webp)



Możesz teraz zaimportować magazyn kluczy do Sparrow Wallet i normalnie korzystać z wallet. Przy każdym ponownym uruchomieniu będziesz musiał zarówno zeskanować SeedQR, jak i ponownie wprowadzić passphrase za pomocą klawiatury, tak jak zrobiliśmy to tutaj.



Przed faktycznym użyciem wallet z passphrase zdecydowanie zalecam wykonanie pełnego testu odzyskiwania danych. Pozwoli to potwierdzić, że kopie zapasowe frazy mnemonicznej i passphrase są prawidłowe. Aby dowiedzieć się, jak wykonać to sprawdzenie, zapoznaj się z poniższym samouczkiem:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895