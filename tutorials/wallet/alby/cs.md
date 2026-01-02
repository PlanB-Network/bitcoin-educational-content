---
name: Alby

description: Rozšíření prohlížeče pro Bitcoin a Lightning Network
---

![cover](assets/cover.webp)




Stále snadnější provádění plateb pomocí bitcoinu je výzvou, které čelí mnoho společností v tomto odvětví. Společnost Alby vystupuje z řady se svým rozšířením Alby wallet pro prohlížeče. Cílem tohoto rozšíření je nastavit plynulý rámec, který automaticky rozpozná adresy a umožní provádět platby bitcoiny bez tření. V tomto návodu objevíme rozšíření Alby a vyzkoušíme, jak usnadňuje platby z prohlížeče.




![video](https://youtu.be/nd5fX2vHuDw)




## Prodloužení Alby



Rozšíření Alby je nástroj, který umožňuje webovému prohlížeči snadno a bezpečně komunikovat se sítí Bitcoin a její vrstvou Lightning Network. Vyznačuje se třemi aspekty:




- Lightning Network wallet: Propojte svůj uzel nebo účet Alby a posílejte a přijímejte bitcoiny rychle a levně prostřednictvím vrstvy Lightning Network.
- Plynulé platby přes web: Na webových stránkách, které podporují technologii Lightning, není nutné skenovat QR kódy nebo přepínat mezi aplikacemi pro platby v bitcoinech. Umožňuje plynulé transakce na jedno kliknutí, případně bez potvrzení, pokud máte nastavený rozpočet.
- Manažer Nostr: Rozšíření spravuje vaše klíče Nostr a usnadňuje připojení a interakci s aplikacemi Nostr, které fungují jako bezpečný podepisující subjekt, aniž by váš soukromý klíč byl vystaven každé platformě.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Připojení k rozšíření



V tomto návodu budeme používat rozšíření Alby v prohlížeči Firefox pod operačním systémem Ubuntu. Je však k dispozici také v systému Windows a v prohlížečích, jako je Chrome.



Rozšíření Alby můžete do prohlížeče přidat v obchodě s rozšířeními [Firefox] (https://addons.mozilla.org/fr/firefox/addon/alby/) nebo v obchodě s rozšířeními [Chrome] (https://chromewebstore.google.com/detail/alby-bitcoin-wallet-for-l/iokeahhehimjnekafflcihljlcjccdbe).



![firefox](assets/fr/01.webp)



![chrome](assets/fr/02.webp)



ℹ️ Je důležité zkontrolovat, zda je autorem rozšíření skutečně oficiální účet Alby, abyste se vyhnuli jakékoli formě pirátství nebo krádeže vašich bitcoinů.



Kliknutím na tlačítko vpravo přidejte rozšíření do prohlížeče.


Udělte potřebná oprávnění k instalaci a používání rozšíření a poté je připněte na panel nástrojů, abyste je mohli snadno vyhledat.



![pin](assets/fr/03.webp)



Měli byste také definovat odemykací kód (velmi důležité), který zaručí bezpečný přístup k aplikaci Lightning wallet z prohlížeče. Doporučujeme nastavit silné alfanumerické heslo.



ℹ️ Heslo si uložte na bezpečné místo, abyste se k němu mohli dostat, pokud ho zapomenete, protože ho lze změnit, ale nelze ho získat zpět.



https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

![pass](assets/fr/04.webp)



Alby prokazuje svou přizpůsobivost tím, že vám nabízí dvě možnosti:




- Pokud chcete využívat aplikace a zároveň mít kontrolu nad svými bitcoiny, pokračujte s účtem Alby.
- Připojte vlastní uzel wallet nebo Lightning, pokud již máte uzel podporovaný tímto rozšířením.



https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


V tomto návodu se rozhodneme pokračovat s účtem Alby, abychom mohli využívat funkce ekosystému Alby.



https://planb.academy/tutorials/wallet/mobile/alby-go-40202802-b346-4a3c-9863-465c3bde9903

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Přihlaste se ke svému účtu Alby nebo si ho vytvořte, pokud ho ještě nemáte.



![signup](assets/fr/05.webp)



## Provedení prvních plateb



Po přihlášení můžete kliknout na rozšíření Alby na panelu nástrojů a získat přístup ke svému portfoliu.



![buzzin](assets/fr/06.webp)



Jakmile si vytvoříte účet Alby, musíte jej připojit k účtu wallet, abyste mohli utrácet satoši. Chcete-li propojit bitcoinový wallet s účtem Alby, doporučujeme použít uzel Alby Hub, který si můžete buď nastavit na svém počítači, nebo si předplatit plán nabízený společností Alby.



![hubplan](assets/fr/13.webp)




V tomto tutoriálu je náš účet Alby podporován místní instalací v našem počítači.


Chcete-li si sestavit vlastní uzel Alby, doporučujeme náš návod Alby Hub.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Tento uzel umožňuje vytvářet vlastní portfolia Lightning a efektivně spravovat kanály Lightning pro odesílání a přijímání satošů.



![channels](assets/fr/14.webp)



Otevřete přijímací kanály, které definují celkový počet satelitů, které můžete přijímat.



![receivechanal](assets/fr/15.webp)



Otevřete kanály pro odesílání blokováním satoshis na bitcoinové adrese onchainu. Zablokované satoshi určují celkový počet satoshi, které můžete utratit.



![spend](assets/fr/16.webp)



Nyní můžete odesílat a přijímat satoši prostřednictvím rozšíření Alby.



![exchange](assets/fr/08.webp)



Od této chvíle je rozšíření Alby schopné detekovat adresy Lightning a faktury dostupné na webových stránkách, které navštívíte, a navrhne vám, abyste je zaplatili v bitcoinech nebo Lightningu přímo z vašeho rozšíření.



![suggest](assets/fr/09.webp)



![pay](assets/fr/10.webp)




## Zabezpečení klíčů pro obnovení pomocí hlavního klíče



Hlavní klíč nabízený rozšířením Alby funguje jako ochranné překrytí, které umožňuje bezpečnou komunikaci s hlavní síťovou vrstvou Bitcoin (Onchain), systémem Nostr a umožňuje aktivovat připojení Lightning s aplikacemi Nostr.



![masterKey](assets/fr/11.webp)



Tento hlavní klíč má podobu 12 slov podobných vaší frázi pro obnovení. Doporučujeme proto, abyste jej uložili pomocí bezpečných metod, a zajistili tak, že k němu budete mít kdykoli přístup.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


![masterKey](assets/fr/12.webp)



S rozšířením Alby si nyní můžete vyzkoušet bezproblémové platby bitcoinem a Lightningem. Pokud se vám tento návod líbil, doporučujeme vám náš návod Alby Hub, který vám umožní nastavit si vlastní uzel Alby a ovládat všechny aspekty peněženek Alby z hladkého a výkonného rozhraní.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a