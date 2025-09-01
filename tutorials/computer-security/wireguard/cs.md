---
name: WireGuard
description: Nastavení služby WireGuard VPN v Debianu a Windows
---
![cover](assets/cover.webp)



___



*Tento návod vychází z původního obsahu Floriana BURNELA zveřejněného na stránkách [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). V původním textu mohly být provedeny změny.*



___



## I. Prezentace



V tomto návodu se dozvíte, jak nakonfigurovat VPN založenou na WireGuard, bezplatném řešení VPN s otevřeným zdrojovým kódem, které zvyšuje výkon, aniž by zanedbávalo zabezpečení.



WireGuard je relativně nové řešení, které je k dispozici ve stabilní verzi od března 2020 a má tu čest být integrováno přímo do **jádra Linuxu od verze 5.6**. To však nebrání tomu, aby byl přístupný i ze starších linuxových distribucí, které používají jinou verzi jádra. Ve srovnání s řešeními, jako jsou OpenVPN a IPSec, je WireGuard jednodušší na používání a mnohem rychlejší, jak uvidíme na konci tohoto článku.



Několik klíčových bodů o systému WireGuard:





- Jednoduché, lehké a velmi účinné!
- Provoz pouze v protokolu UDP (což může být nevýhoda při překonávání některých firewallů)
- Funguje na modelu peer-to-peer, nikoli klient-server
- Ověřování pomocí klíče Exchange na stejném principu jako SSH s privátními/veřejnými klíči
- Použití několika algoritmů: symetrické šifrování pomocí ChaCha20, ověřování zpráv pomocí Poly1305 a dalších, jako jsou Curve25519, BLAKE2 a SipHash24
- Podporuje IPv4 i IPv6
- Multiplatformní: Windows, Linux, BSD, macOS, Android, iOS, OpenWRT (a implementováno v ProtonVPN)
- Pouze 4 000 řádků kódu ve srovnání se stovkami tisíc řádků u jiných řešení



Pokud jde o kryptografickou část, jednotlivé použité algoritmy jsou ručně vybírány, kontrolovány několika způsoby a zkoumány bezpečnostními výzkumníky specializovanými na danou oblast.



Oficiální webové stránky projektu: [wireguard.com](https://www.wireguard.com/)



Jste po přečtení tohoto úvodu o tomto řešení přesvědčeni? Pak už zbývá jen číst dál!



## II. Laboratorní schéma WireGuard



Než vám představím svou laboratoř pro nastavení systému WireGuard, měli byste vědět, že si můžete představit **použití systému WireGuard k propojení dvou vzdálených infrastruktur**, ale také k **připojení vzdáleného klienta k infrastruktuře, jako je firemní síť nebo vaše domácí síť**. To je ve stejném duchu jako u OpenVPN, jak jsme si nedávno ukázali v tutoriálu "[OpenVPN na Synology](https://www.it-connect.fr/tuto-vpn-configurer-openvpn-server-sur-un-nas-synology/)".



Pokud není systém WireGuard nastaven přímo na směrovači nebo bráně firewall, což je možné u systému OpenWRT, budete muset nastavit přesměrování portů tak, aby se tok dostal do dvojice WireGuard.



![Image](assets/fr/034.webp)



Nyní vám povím o své laboratoři a o tom, co dnes budeme připravovat.



Jako server WireGuard budu používat počítač Debian 11 a jako klienta WireGuard VPN klient Windows. I když je trochu zavádějící mluvit o vztahu klient-server, protože **WireGuard funguje na modelu "peer-to-peer "**. To je trochu chybný název, když se snažíte nastavit spojení "klient-server". Řekněme, že místo toho budu mít dva páry nebo **dva body připojení WireGuard**, chcete-li: jeden pod Debianem 11 a druhý pod Windows.



Tyto dva páry spolu mohou komunikovat oběma směry, což znamená, že ze svého počítače se systémem Windows mohu přistupovat do vzdálené sítě LAN počítače s Debianem 11 a naopak: vše závisí na konfiguraci tunelu a firewallu partnerského počítače WireGuard.



V tomto příkladu se zaměřím na následující případ: **z mého počítače Windows Peer 1 připojeného k domácí síti chci přistupovat k firemní síti, abych mohl přistupovat k firemním serverům prostřednictvím tunelu VPN WireGuard**. Vznikne tak následující schéma:



![Image](assets/fr/035.webp)



Z hlediska IP adres to znamená, že:





- Domácí síť**: 192.168.1.0/24
- Firemní síť**: 192.168.100.0/24
- Tunelová síť WireGuard**: 192.168.110.0/24


+ IP Address účastníka 1 (Windows) v tunelu: 192.168.110.2/24


+ IP Address partnera 2 (Debian) v tunelu: 192.168.110.121/24



To je vše! Přejděme ke konfiguraci!



**Poznámka: ve výchozím nastavení pracuje WireGuard v režimu UDP na **portu 51820**.



## III Instalace a konfigurace serveru WireGuard



V tomto návodu budu používat termíny "klient" pro počítač se systémem Windows a "server" pro počítač s Debianem, protože i když se jedná o peer-to-peer, zdá se mi to smysluplnější.



### A. Instalace WireGuard v Debianu 11



Instalační balíček WireGuard je k dispozici v oficiálních repozitářích Debianu 11, takže stačí aktualizovat mezipaměť balíčků a nainstalovat jej:



```
sudo apt-get update
```



```
sudo apt-get install wireguard
```



![Image](assets/fr/022.webp)



Nainstaluje se serverová část WireGuard a různé nástroje umožňující přístup k užitečným příkazům pro správu konfigurace.



### B. Instalace zařízení Interface WireGuard



Pomocí **příkazu "wg "** potřebujeme generate soukromý a veřejný klíč: to je nezbytné pro ověření mezi dvěma páry, tj. serverem a klientem (který bude také potřebovat pár klíčů).



Soukromý klíč "**/etc/wireguard/wg-private.key**" a veřejný klíč "**/etc/wireguard/wg-public.key**" vytvoříme pomocí této sekvence příkazů:



```
wg genkey | sudo tee /etc/wireguard/wg-private.key | wg pubkey | sudo tee /etc/wireguard/wg-public.key
```



![Image](assets/fr/023.webp)



Hodnota veřejného klíče bude vrácena do konzoly. V konfiguračním souboru WireGuard musíme **přidat hodnotu našeho soukromého klíče**. Chcete-li tuto hodnotu získat, zadejte níže uvedený příkaz a zkopírujte hodnotu:



```
sudo cat /etc/wireguard/wg-private.key
```



Je čas vytvořit konfigurační soubor v adresáři "**/etc/wireguard/**". Tento soubor můžeme například pojmenovat "**wg0.conf**", pokud si myslíme, že síť Interface přidružená ke službě WireGuard bude "wg0", na stejném principu jako například "eth0".



```
sudo nano /etc/wireguard/wg0.conf
```



Do tohoto souboru musíme nejprve přidat následující obsah (k jeho doplnění se vrátíme později):



```
[Interface]
Address = 192.168.110.121/24
SaveConfig = true
ListenPort = 51820
PrivateKey = <clé privée du serveur>
```



Sekce `[Interface]` slouží k deklaraci serverové části. Zde je několik informací:





- Address**: IP adresa Address zařízení Interface WireGuard v tunelu VPN (jiná podsíť než vzdálená LAN)
- SaveConfig**: konfigurace je uložena (a chráněna) po dobu, kdy je Interface aktivní
- ListenPort**: Port naslouchání WireGuard. V tomto případě je výchozím portem 51820, ale můžete si jej přizpůsobit
- PrivateKey**: hodnota soukromého klíče našeho serveru (*wg-private.key*)



Uložte soubor a zavřete jej. Pomocí příkazu "**wg-quick**" můžeme spustit tento Interface zadáním jeho názvu (wg0, protože soubor se jmenuje wg0.conf):



```
sudo wg-quick up wg0
```



Pokud zobrazíte seznam IP adres serveru Debian 11, uvidíte nový Interface s názvem "wg0" s IP Address definovanou v konfiguračním souboru:



```
ip a
```



![Image](assets/fr/027.webp)



Ve stejném duchu můžeme zobrazit konfiguraci Interface "wg0" pomocí příkazu "wg show":



```
sudo wg show wg0
```



![Image](assets/fr/024.webp)



Nakonec musíme aktivovat automatické spuštění našeho zařízení Interface wg0 WireGuard:



```
sudo systemctl enable wg-quick@wg0.service
```



Konfiguraci serveru WireGuard prozatím ponecháme stranou.



### C. Povolit předávání IP



Aby náš počítač s Debianem 11 mohl **přesměrovávat pakety mezi různými sítěmi (jako směrovač)**, tj. mezi sítí VPN a místní sítí, musíme povolit [IP Forwarding](https://www.it-connect.fr/activer-lip-forwarding-sous-linux-ipv4ipv6/). Ve výchozím nastavení je tato funkce zakázána.



Upravte tento konfigurační soubor:



```
sudo nano /etc/sysctl.conf
```



Na konec souboru přidejte následující direktivu a uložte:



```
net.ipv4.ip_forward = 1
```



To je vše.



### D. Povolit IP maškarádu



Aby náš server správně směroval pakety a aby byla vzdálená síť LAN přístupná počítači se systémem Windows, musíme na serveru Debian aktivovat funkci IP Masquerade. Jedná se o druh aktivace NAT. Tuto konfiguraci provedu na linuxovém firewallu prostřednictvím UFW, který jsem zvyklý používat ([ufw tutorial on Debian](https://www.it-connect.fr/configurer-un-pare-feu-local-sous-debian-11-avec-ufw/)).



Pokud ještě nemáte UFW a chcete jej nastavit (můžete také použít Nftables), začněte instalací:



```
sudo apt install ufw
```



Nejprve je třeba povolit SSH, abyste neztratili kontrolu nad vzdáleným serverem (přizpůsobte číslo portu):



```
sudo ufw allow 22/tcp
```



Port 51820 v UDP musí být také autorizován, protože jej používáme pro WireGuard (opět přizpůsobte číslo portu):



```
sudo ufw allow 51820/udp
```



Dále budeme pokračovat v konfiguraci pro povolení maškarády IP. K tomu potřebujeme načíst název zařízení Interface připojeného k místní síti. Pokud název neznáte, spusťte příkaz "ip a" a zobrazte název karty. V mém případě je to karta "**ens192**".



![Image](assets/fr/036.webp)



Tyto informace použijeme. Upravte následující soubor:



```
sudo nano /etc/ufw/before.rules
```



Na konec souboru přidejte tyto řádky, abyste **povolili maškarádu IP na ens192** Interface (upravte název Interface) v řetězci POSTROUTING tabulky NAT našeho místního firewallu:



```
# NAT - IP masquerade
*nat
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING -o ens192 -j MASQUERADE

# End each table with the 'COMMIT' line or these rules won't be processed
COMMIT
```



Na obrázku je:



![Image](assets/fr/037.webp)



Tento konfigurační soubor nechte otevřený a přejděte k dalšímu kroku. 😉



### E. Konfigurace brány firewall Linux pro WireGuard



Ve stejném konfiguračním souboru deklarujeme firemní síť "192.168.100.0/24", abychom ji mohli kontaktovat. Zde jsou dvě pravidla, která je třeba přidat (ideálně za část "*# ok icmp code for FORWARD*", aby se pravidla seskupila):



```
# autoriser le forwarding pour le réseau distant de confiance (+ le réseau du VPN)
-A ufw-before-forward -s 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -s 192.168.110.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.110.0/24 -j ACCEPT
```



Pokud chcete autorizovat pouze jednoho hostitele, například "192.168.100.11", je to snadné:



```
-A ufw-before-forward -s 192.168.100.11/32 -j ACCEPT
-A ufw-before-forward -d 192.168.100.11/32 -j ACCEPT
```



Nyní můžete soubor uložit a zavřít. Zbývá jen aktivovat UFW a restartovat službu, aby se naše změny uplatnily:



```
sudo ufw enable
```



```
sudo systemctl restart ufw
```



První část konfigurace serveru Debian je nyní dokončena.



## IV. Klient WireGuard pro Windows



Klient WireGuard je k dispozici pro systémy Windows, macOS, Android atd.. To je skvělá zpráva. Všechny soubory ke stažení jsou k dispozici na této stránce: [Klient WireGuard](https://www.wireguard.com/install/). V tomto příkladu budu nastavovat klienta v systému Windows. Chcete-li nastavit klienta WireGuard v systému Linux, postupujte podle stejného principu jako při vytváření souboru wg0.conf v počítači s Debianem (bez všech NAT atd.).



### A. Instalace klienta WireGuard pro systém Windows



Po stažení spustitelného souboru nebo balíčku MSI je instalace jednoduchá: stačí spustit instalační program a... voilà, je hotovo! 🙂



![Image](assets/fr/038.webp)



### B. Vytvoření profilu WireGuard



Začněte otevřením softwaru a vytvořte nový tunel. To provedete kliknutím na šipku vpravo od tlačítka "**Přidat tunel**" a kliknutím na tlačítko "**Přidat prázdný tunel**".



![Image](assets/fr/028.webp)



Otevře se konfigurační okno. Při každém vytvoření nové konfigurace tunelu vygeneruje WireGuard pár soukromý/veřejný klíč specifický pro tuto konfiguraci. **V této konfiguraci musíme deklarovat "peera", tj. vzdálený server:



```
[Interface]
PrivateKey = <la clé privée du PC>
```



Tuto konfiguraci musíme dokončit, zejména deklarovat IP adresu Address na tomto serveru Interface (*Address*), ale také deklarovat vzdálený server WireGuard prostřednictvím bloku [Peer]. Následující obrázek by vám měl připomenout konfigurační soubor, který jsme vytvořili na straně linuxového serveru.



Začneme blokem `[Interface]` a přidáme IP adresu Address "**192.168.110.2**"; nezapomeňte, že server má v tomto segmentu sítě IP adresu Address "**192.168.110.121**". Tím získáte:



```
[Interface]
PrivateKey = <la clé privée du PC>
Address = 192.168.110.2/24
```



Dále je třeba deklarovat blok "Peer" se třemi vlastnostmi, čímž vznikne tato konfigurace:



```
[Peer]
PublicKey = 1D/Gf5yd3hUDoFyYQ3P1zayBHUJhJZq+k6Sv03HnJCQ=
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
Endpoint = <ip-serveur-debian>:51820
```



Na obrázcích:



![Image](assets/fr/029.webp)



**Několik vysvětlení k bloku [Peer]:





- PublicKey**: jedná se o veřejný klíč serveru WireGuard Debian 11 (jeho hodnotu můžete získat příkazem "*sudo wg*")
- AllowedIPs**: jedná se o IP adresy / podsítě přístupné prostřednictvím této sítě WireGuard VPN, v tomto případě podsíť specifická pro mou síť WireGuard VPN (*192.168.110.0/24*) a mou vzdálenou LAN (*192.168.100.0/24*)
- Koncový bod**: jedná se o IP adresu Address hostitele Debianu 11, protože to je náš bod připojení WireGuard (musíte zadat veřejnou IP adresu Address)



Nakonec zadejte jméno do pole "**Název**" (bez mezer) a zkopírujte a vložte veřejný klíč klienta, protože jej budeme potřebovat deklarovat na serveru. Klikněte na tlačítko "**Registrovat**".



### C. Deklarování klienta na serveru WireGuard



Je čas vrátit se na server Debian a deklarovat "**Peer**", tj. náš počítač se systémem Windows, v konfiguraci WireGuard. Nejprve musíme **zastavit Interface "wg0"**, abychom mohli upravit jeho konfiguraci:



```
sudo wg-quick down wg0
# ou
sudo wg-quick down /etc/wireguard/wg0.conf
```



Dále upravte dříve vytvořený konfigurační soubor:



```
sudo nano /etc/wireguard/wg0.conf
```



V tomto souboru musíme za blokem `[Interface]` deklarovat blok `[Peer]`:



```
[Peer]
PublicKey = 0i2Pg8nwDW2j7yOG09ZXht18o8l8Erb9Y5F4xyAyQV8=
AllowedIPs = 192.168.110.2/32
```



Tento blok [Peer] obsahuje veřejný klíč počítače se systémem Windows 10 (**PublicKey**) a IP adresu Address počítače Interface (**AllowedIPs**): server bude v tomto tunelu WireGuard komunikovat pouze za účelem kontaktu s klientem systému Windows, proto hodnota "**192.168.110.2/32**".



Zbývá jen soubor uložit (*CTRL+O, pak Enter a CTRL+X přes Nano*). Znovu spusťte Interface "wg0":



```
sudo wg-quick up wg0
# ou
sudo wg-quick up /etc/wireguard/wg0.conf
```



Chcete-li zkontrolovat, zda deklarace partnera funguje, můžete použít tento příkaz:



```
sudo wg show
```



Jakmile vzdálený hostitel nastaví připojení WireGuard, bude jeho IP adresa Address přesunuta na hodnotu "endpoint".



![Image](assets/fr/033.webp)



Nakonec zabezpečíme konfigurační soubory, abychom omezili přístup roota:



```
sudo chmod 600 /etc/wireguard/ -R
```



### D. První připojení WireGuard



Nyní je konfigurace připravena a můžeme ji spustit z počítače se systémem Windows. Za tímto účelem klikněte v klientovi "**WireGuard**" na tlačítko "**Aktivovat**": připojení se **změní z "Vypnuto" na "Zapnuto "**, což však neznamená, že bude fungovat. Vše závisí na tom, zda je vaše konfigurace správná, nebo ne. **Když je spojení navázáno, naše dva počítače komunikují prostřednictvím Interface WireGuard nakonfigurovaného na každé straně!



![Image](assets/fr/030.webp)



V případě problému bude tato skutečnost viditelná na kartě "**Logbook**". Oba hostitelé budou pravidelně kontrolovat stav spojení pomocí paketů Exchange, proto se zobrazují zprávy "*Přijímáme keepalive paket od peera 1*".



![Image](assets/fr/031.webp)



Pokud se na kartě "**Journal**" programu WireGuard zobrazí zpráva jako níže, je třeba zkontrolovat, zda jsou veřejné klíče deklarované na obou stranách správné.



```
Handshake for peer 1 (<ip>:51820) did not complete after 5 seconds, retrying (try 2)
```



Ze vzdáleného počítače mohu pingovat na IP adresu Address svého zařízení Interface WireGuard na straně serveru i na hostitele ve vzdálené síti LAN.



![Image](assets/fr/032.webp)



### E. Výkonnost: E.: OpenVPN vs WireGuard



Ze vzdáleného počítače připojeného k síti WireGuard VPN jsem mohl přistoupit k souborovému serveru a přenést soubor prostřednictvím [SMB](https://www.it-connect.fr/le-protocole-smb-pour-les-debutants/), abych zjistil rychlost přenosu. **S WireGuardem jsem dosáhl maximální rychlosti kolem 45 Mb/s, což je skvělé, protože jsem na WiFi



![Image](assets/fr/025.webp)



Za stejných podmínek, ale tentokrát prostřednictvím připojení OpenVPN (v protokolu UDP) a při stejné operaci je propustnost zcela jiná: přibližně 3 MB/s. Rozdíl je zřejmý!



![Image](assets/fr/026.webp)



To je zajímavé, protože pokud například přepnete z připojení WiFi na připojení 4G/5G, opětovné připojení bude tak rychlé, že přerušení nebude viditelné.



### F. Bonus: plný tunel WireGuard



Při současné konfiguraci část provozu proudí přes síť VPN a zbytek přes internetové připojení zákazníka, včetně prohlížení internetu. Pokud chceme přepnout na **plný tunelový režim** WireGuard, aby vše procházelo tunelem VPN, musíme provést několik změn v konfiguraci.....



Nejprve je třeba nainstalovat balíček "resolvconf" na:



```
sudo apt-get update
sudo apt-get install resolvconf
```



Jakmile to provedete, musíte upravit profil "wg0.conf" v počítači s Debianem: zastavte Interface, upravte jej a znovu spusťte.



```
sudo wg-quick down /etc/wireguard/wg0.conf
```



Dále **v bloku `[Interface]` přidáme server DNS, který má být použit**. V mém případě je to doménový řadič mé laboratoře, ale můžeme také nainstalovat Bind9 na počítač s Debianem, abychom měli místní resolver.



```
DNS = 192.168.100.11
```



Uložte soubor a restartujte Interface:



```
sudo wg-quick up /etc/wireguard/wg0.conf
```



Nakonec je třeba v konfiguraci tunelu na pracovní stanici se systémem Windows 10 upravit část "AllowedIPs" tak, aby bylo uvedeno, že vše musí procházet tunelem. Nahraďte položku:



```
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
```



Autor::



```
AllowedIPs = 0.0.0.0/0
```



Vidíte, že tím také povolíte možnost "**Kill switch*".



![Image](assets/fr/040.webp)



Nakonec jsem tento plný tunel využil k provedení malého průtokového testu, jehož výsledky jsou uvedeny níže:



![Image](assets/fr/039.webp)



Konfigurace systému WireGuard je poměrně jednoduchá, snadno pochopitelná a především snadno udržovatelná. **WireGuard je považován za budoucnost VPN**, takže bychom ho měli bedlivě sledovat! Vidíme také, že přínos je značný z hlediska výkonu, což je pro WireGuard ve srovnání s OpenVPN obrovská výhoda.



Další dokumentace:





- [Man - Command wg](https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8)
- [Man - Příkaz wg-quick](https://manpages.debian.org/unstable/wireguard-tools/wg-quick.8.en.html)



**Vaše síť WireGuard VPN je spuštěna! Gratulujeme!