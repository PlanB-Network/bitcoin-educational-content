---
name: passphrase BIP39
description: Zrozumienie sposobu działania passphrase
---
![cover](assets/cover.webp)


## Co to jest BIP39 passphrase?


Portfele HD są zazwyczaj generowane na podstawie frazy Mnemonic składającej się z 12 lub 24 słów. Fraza ta jest bardzo ważna, ponieważ umożliwia przywrócenie wszystkich kluczy Wallet w przypadku utraty jego fizycznego nośnika (na przykład Hardware Wallet). Stanowi ona jednak pojedynczy punkt awarii, ponieważ jeśli zostanie naruszona, atakujący może ukraść wszystkie bitcoiny.


![PASSPHRASE BIP39](assets/notext/01.webp)


W tym miejscu pojawia się passphrase. Jest to opcjonalne hasło, które można dowolnie wybrać, które jest dodawane do frazy Mnemonic w procesie wyprowadzania klucza w celu zwiększenia bezpieczeństwa Wallet.


![PASSPHRASE BIP39](assets/notext/02.webp)


Należy uważać, aby nie pomylić passphrase z kodem PIN Hardware Wallet lub hasłem używanym do odblokowania dostępu do Wallet na komputerze. W przeciwieństwie do wszystkich Elements, passphrase odgrywa rolę w tworzeniu kluczy Wallet. **Oznacza to, że bez niego nigdy nie będziesz w stanie odzyskać swoich bitcoinów


passphrase działa w tandemie z frazą Mnemonic, zmieniając seed, z którego generowane są klucze. Tak więc, nawet jeśli ktoś uzyska 12- lub 24-wyrazową frazę, bez passphrase nie będzie mógł uzyskać dostępu do środków. **Użycie passphrase zasadniczo tworzy nowy Wallet z odrębnymi kluczami. Modyfikacja (nawet niewielka) passphrase spowoduje, że generate będzie innym Wallet.**


## Dlaczego warto używać passphrase?


passphrase jest dowolny i może być dowolną kombinacją znaków wybraną przez użytkownika. Korzystanie z passphrase ma zatem kilka zalet. Po pierwsze, zmniejsza wszelkie ryzyko związane z naruszeniem frazy Mnemonic, wymagając drugiego czynnika w celu uzyskania dostępu do środków (włamanie, dostęp do domu itp.).


Następnie można go wykorzystać strategicznie do stworzenia wabika Wallet, aby poradzić sobie z fizycznymi ograniczeniami w celu kradzieży środków, takich jak niesławny "atak kluczem 5 $". W tym scenariuszu chodzi o posiadanie Wallet bez passphrase zawierającego tylko niewielką ilość bitcoinów, wystarczającą do zaspokojenia potencjalnego agresora, przy jednoczesnym posiadaniu ukrytego Wallet. Ten ostatni wykorzystuje tę samą frazę Mnemonic, ale jest zabezpieczony dodatkowym passphrase.


Wreszcie, użycie passphrase jest interesujące, gdy chcemy kontrolować losowość generowania seed przez HD Wallet.


## Jak wybrać dobry passphrase?

Aby hasło passphrase było skuteczne, musi być wystarczająco długie i losowe. Podobnie jak w przypadku silnego hasła, zalecam wybranie passphrase, który jest tak długi i losowy, jak to możliwe, z różnymi literami, cyframi i symbolami, aby uniemożliwić atak siłowy.


Ważne jest również, aby prawidłowo zapisać ten passphrase, w taki sam sposób jak frazę Mnemonic. **Jego utrata oznacza utratę dostępu do bitcoinów**. Zdecydowanie odradzam zapamiętywanie go wyłącznie w głowie, ponieważ nadmiernie zwiększa to ryzyko jego utraty. Idealnym rozwiązaniem jest zapisanie go na fizycznym nośniku (papierowym lub metalowym) oddzielnie od frazy Mnemonic. Ta kopia zapasowa musi być oczywiście przechowywana w innym miejscu niż fraza Mnemonic, aby zapobiec jednoczesnemu naruszeniu obu.


## Samouczki


Aby skonfigurować passphrase na urządzeniu Ledger (Stax, Flex lub Nano), zapoznaj się z tym samouczkiem:


https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

Na karcie COLDCARD:


https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

Na Jade Plus:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

Na paszporcie (partia 2):


https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Na urządzeniu Trezor (Safe 3, Safe 5 lub Model One):


https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42