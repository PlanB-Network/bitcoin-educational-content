---
term: passphrase (BIP39)
---

Opcjonalne hasło, które w połączeniu z frazą odzyskiwania zapewnia dodatkowe zabezpieczenie Layer dla deterministycznych i hierarchicznych portfeli Bitcoin. Portfele HD są zwykle generowane na podstawie frazy odzyskiwania składającej się z 12 lub 24 słów. Ta fraza odzyskiwania jest bardzo ważna, ponieważ pozwala na przywrócenie wszystkich kluczy w Wallet w przypadku ich utraty. Stanowi ona jednak pojedynczy punkt awarii (SPOF). Jeśli zostanie on naruszony, bitcoiny są zagrożone. W tym miejscu pojawia się passphrase. Jest to opcjonalne hasło, wybrane przez użytkownika, które jest dodawane do frazy odzyskiwania w celu zwiększenia bezpieczeństwa Wallet. Nie mylić z kodem PIN lub zwykłym hasłem, passphrase odgrywa rolę w wyprowadzaniu kluczy kryptograficznych.


Działa on w parze z frazą odzyskiwania, modyfikując seed, z którego generowane są klucze. Dlatego nawet jeśli ktoś uzyska frazę odzyskiwania, bez passphrase nie będzie mógł uzyskać dostępu do środków. Użycie passphrase zasadniczo tworzy nowy Wallet z odrębnymi kluczami. Modyfikacja (nawet niewielka) passphrase spowoduje utworzenie innego Wallet.


passphrase jest dowolny i może być dowolną kombinacją znaków wybraną przez użytkownika. Korzystanie z passphrase ma kilka zalet. Po pierwsze, zmniejsza ryzyko związane z naruszeniem frazy odzyskiwania, wymagając drugiego czynnika w celu uzyskania dostępu do środków. Następnie można go wykorzystać strategicznie do tworzenia fałszywych portfeli zawierających niewielkie ilości bitcoinów, w przypadku fizycznego przymusu kradzieży środków. Wreszcie, jego użycie jest interesujące, gdy chcemy kontrolować losowość generacji HD Wallet seed. passphrase musi być wystarczająco złożony, aby oprzeć się atakom brute force i musi być niezawodnie zapisywany. Utrata passphrase może prowadzić do niemożności uzyskania dostępu do środków, podobnie jak utrata frazy odzyskiwania.


> gW-12 jest czasami określany również jako: "dwuskładnikowa fraza seed", "hasło", "rozszerzenie seed", "słowo rozszerzające" lub nawet "13. lub 25. słowo" Warto zauważyć, że istnieją dwa rodzaje haseł na Bitcoin. Najbardziej znanym jest ten opisany powyżej, który zależy od BIP-39 i pozwala zabezpieczyć cały HD Wallet. Jednak BIP-38 określił również sposób zabezpieczenia unikalnego klucza prywatnego za pomocą passphrase. Ten drugi typ passphrase jest obecnie prawie nieużywany*