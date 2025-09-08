---
name: WireGuard
description: Postavljanje WireGuard VPN-a na Debian i Windows
---
![cover](assets/cover.webp)



___



*Ovaj vodič je zasnovan na originalnom sadržaju autora Florian BURNEL objavljenom na [IT-Connect](https://www.it-connect.fr/). Licenca [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Moguće je da su napravljene izmene u originalnom tekstu.*



___



## I. Prezentacija



U ovom vodiču ćemo naučiti kako da konfigurišemo VPN baziran na WireGuard-u, besplatnom, open-source VPN rešenju koje poboljšava performanse bez zanemarivanja sigurnosti.



WireGuard je relativno nedavno rešenje, dostupno kao stabilna verzija od marta 2020. godine, i ima čast da bude direktno integrisan u **Linux kernel od verzije 5.6**. Ovo ga ne sprečava da bude dostupan na starijim Linux distribucijama koje koriste drugačiju verziju kernela. U poređenju sa rešenjima kao što su OpenVPN i IPSec, WireGuard je jednostavniji za korišćenje i mnogo brži, što ćemo videti na kraju ovog članka.



Neke ključne tačke o WireGuard-u:





- Jednostavan, lagan i ultra-efikasan!
- Rad samo preko UDP-a (što može biti nedostatak pri prolasku kroz određene vatrozide)
- Radi na modelu "peer-to-peer" umesto "klijent-server" modela
- Autentifikacija pomoću ključa Exchange, po istom principu kao SSH sa privatnim/javnim ključevima
- Korišćenje nekoliko algoritama: simetrična enkripcija sa ChaCha20, autentifikacija poruka sa Poly1305, kao i drugih kao što su Curve25519, BLAKE2 i SipHash24
- Podržava i IPv4 i IPv6
- Više platformi: Windows, Linux, BSD, macOS, Android, iOS, OpenWRT (i implementiran u ProtonVPN)
- Samo 4.000 linija koda, u poređenju sa stotinama hiljada za druga rešenja



Za deo koji se odnosi na kriptografiju, korišćeni algoritmi su pažljivo odabrani, provereni na više načina i ispitani od strane istraživača bezbednosti specijalizovanih u toj oblasti.



Zvanična veb stranica projekta: [wireguard.com](https://www.wireguard.com/)



Da li vas je ovo rešenje ubedilo nakon čitanja ovog uvoda? Sve što preostaje je da nastavite sa čitanjem!



## II. Dijagram laboratorije WireGuard



Pre nego što predstavim svoj laboratorijski rad za postavljanje WireGuard-a, trebalo bi da znate da možete zamisliti **korišćenje WireGuard-a za međusobno povezivanje dve udaljene infrastrukture**, ali i za **povezivanje udaljenog klijenta sa infrastrukturom kao što je korporativna mreža ili vaša kućna mreža**. Ovo je u istom duhu kao sa OpenVPN-om, kao što smo nedavno videli u tutorijalu "[OpenVPN na Synology](https://www.it-connect.fr/tuto-vpn-configurer-openvpn-server-sur-un-nas-synology/)".



Ako WireGuard nije direktno postavljen na ruteru ili firewall-u, što je zamislivo sa OpenWRT-om, potrebno je postaviti prosleđivanje portova kako bi protok stigao do WireGuard para.



![Image](assets/fr/034.webp)



Sada ću vam reći o mojoj laboratoriji i šta ćemo danas postaviti.



Koristiću Debian 11 mašinu kao WireGuard server i Windows klijent kao WireGuard VPN klijent. Iako je malo zavaravajuće govoriti o odnosu klijent-server, jer **WireGuard radi na "peer-to-peer"** modelu. To je pomalo pogrešan naziv kada pokušavate da postavite "client-to-site" vezu. Recimo umesto toga da ću imati dva para ili **dve WireGuard tačke povezivanja** ako vam više odgovara: jednu pod Debian 11 i drugu pod Windows.



Ova dva para mogu međusobno komunicirati u oba smera, što znači da sa svog Windows računara mogu pristupiti udaljenoj LAN mreži Debian 11 mašine, i obrnuto: sve zavisi od konfiguracije tunela i vatrozida WireGuard čvora.



U ovom primeru, fokusiraću se na sledeći slučaj: **sa mog Windows Peer 1 povezanog na moju kućnu mrežu, želim da pristupim svojoj korporativnoj mreži kako bih pristupio serverima kompanije putem WireGuard VPN tunela**. Ovo daje sledeći dijagram:



![Image](assets/fr/035.webp)



U smislu IP adresa, ovo daje:





- Kućna mreža**: 192.168.1.0/24
- Korporativna mreža**: 192.168.100.0/24
- WireGuard tunnel network**: 192.168.110.0/24


+ IP Address Peera 1 (Windows) u tunelu: 192.168.110.2/24


+ IP Address Peera 2 (Debian) u tunelu: 192.168.110.121/24



To je sve što treba uraditi! Hajde da pređemo na konfiguraciju!



**Napomena: po defaultu, WireGuard radi u UDP modu na **portu 51820**.



## III Instalacija i konfiguracija WireGuard servera



U ovom vodiču koristiću termine "klijent" za Windows mašinu i "server" za Debian mašinu, jer iako je peer-to-peer, čini se smislenijim.



### A. Instaliranje WireGuard-a na Debian 11



Paket za instalaciju WireGuard-a dostupan je u zvaničnim Debian 11 riznicama, tako da sve što treba da uradimo je da ažuriramo keš paketa i instaliramo ga:



```
sudo apt-get update
```



```
sudo apt-get install wireguard
```



![Image](assets/fr/022.webp)



WireGuard server deo će biti instaliran, zajedno sa raznim alatima koji omogućavaju pristup korisnim komandama za upravljanje konfiguracijom.



### B. Instaliranje Interface WireGuard



Koristeći **komandu "wg "** treba da generate privatni ključ i javni ključ: neophodni za autentifikaciju između dva para, tj. servera i klijenta (koji će takođe trebati par ključeva).



Kreiraćemo privatni ključ "**/etc/wireguard/wg-private.key**" i javni ključ "**/etc/wireguard/wg-public.key**" sa ovom sekvencom komandi:



```
wg genkey | sudo tee /etc/wireguard/wg-private.key | wg pubkey | sudo tee /etc/wireguard/wg-public.key
```



![Image](assets/fr/023.webp)



Vrednost javnog ključa će biti vraćena u konzoli. U WireGuard konfiguracionu datoteku, potrebno je **dodati vrednost našeg privatnog ključa**. Da biste preuzeli ovu vrednost, unesite naredbu ispod i kopirajte vrednost:



```
sudo cat /etc/wireguard/wg-private.key
```



Vreme je da kreiramo konfiguracioni fajl u "**/etc/wireguard/**". Na primer, možemo nazvati ovaj fajl "**wg0.conf**", ako mislimo da će mreža Interface povezana sa WireGuard-om biti "wg0", po istom principu kao "eth0", na primer.



```
sudo nano /etc/wireguard/wg0.conf
```



U ovu datoteku prvo moramo dodati sledeći sadržaj (vratićemo se kasnije da ga dovršimo):



```
[Interface]
Address = 192.168.110.121/24
SaveConfig = true
ListenPort = 51820
PrivateKey = <clé privée du serveur>
```



Sekcija `[Interface]` se koristi za deklarisanje serverskog dela. Ovde su neke informacije:





- Address**: IP Address WireGuard-a Interface unutar VPN tunela (drugačija podmreža od udaljenog LAN-a)
- SaveConfig**: konfiguracija se čuva (i zaštićena je) sve dok je Interface aktivan
- ListenPort**: WireGuard-ov port za slušanje. U ovom slučaju, 51820 je podrazumevani port, ali ga možete prilagoditi po želji.
- PrivateKey**: vrednost privatnog ključa našeg servera (*wg-private.key*)



Sačuvaj datoteku i zatvori je. Sa komandom "**wg-quick**", možemo pokrenuti ovaj Interface navodeći njegovo ime (wg0, pošto je datoteka nazvana wg0.conf):



```
sudo wg-quick up wg0
```



Ako navedete IP adrese vašeg Debian 11 servera, videćete novi Interface nazvan "wg0" sa IP Address definisanim u konfiguracionoj datoteci:



```
ip a
```



![Image](assets/fr/027.webp)



U istom duhu, možemo prikazati konfiguraciju Interface "wg0" putem komande "wg show":



```
sudo wg show wg0
```



![Image](assets/fr/024.webp)



Konačno, treba da aktiviramo automatsko pokretanje našeg Interface wg0 WireGuard:



```
sudo systemctl enable wg-quick@wg0.service
```



Za sada ćemo ostaviti po strani konfiguraciju serverske strane WireGuard-a.



### C. Omogući IP prosleđivanje



Da bi naš Debian 11 mašina mogla **rutirati pakete između različitih mreža (kao ruter)**, tj. između VPN mreže i lokalne mreže, potrebno je omogućiti [IP Forwarding](https://www.it-connect.fr/activer-lip-forwarding-sous-linux-ipv4ipv6/). Podrazumevano, ova funkcija je onemogućena.



Izmenite ovu konfiguracionu datoteku:



```
sudo nano /etc/sysctl.conf
```



Dodajte sledeću direktivu na kraj datoteke i sačuvajte:



```
net.ipv4.ip_forward = 1
```



To je sve što treba da se uradi.



### D. Omogući IP Masquerade



Da bi naš server ispravno rutirao pakete i da bi udaljeni LAN bio dostupan Windows mašini, potrebno je aktivirati IP Masquerade na našem Debian serveru. Ovo je vrsta NAT aktivacije. Izvršiću ovu konfiguraciju na Linux firewall-u putem UFW-a, koji sam navikao koristiti ([ufw tutorial na Debian-u](https://www.it-connect.fr/configurer-un-pare-feu-local-sous-debian-11-avec-ufw/)).



Ako već nemate UFW i želite da ga postavite (takođe možete koristiti Nftables), počnite instaliranjem:



```
sudo apt install ufw
```



Prvo, morate omogućiti SSH kako ne biste izgubili kontrolu nad udaljenim serverom (prilagodite broj porta):



```
sudo ufw allow 22/tcp
```



Port 51820 u UDP-u takođe mora biti autorizovan, jer ga koristimo za WireGuard (ponovo, prilagodite broj porta):



```
sudo ufw allow 51820/udp
```



Dalje ćemo nastaviti sa konfiguracijom za omogućavanje IP maskiranja. Da bismo to uradili, potrebno je da pribavimo ime Interface povezanog na lokalnu mrežu. Ako ne znate ime, pokrenite "ip a" da biste videli ime kartice. U mom slučaju, to je kartica "**ens192**".



![Image](assets/fr/036.webp)



Koristićemo ove informacije. Uredite sledeću datoteku:



```
sudo nano /etc/ufw/before.rules
```



Dodajte ove linije na kraj datoteke da **omogućite IP maskiranje na Interface ens192** (prilagodite ime Interface) unutar POSTROUTING niza NAT tabele našeg lokalnog firewall-a:



```
# NAT - IP masquerade
*nat
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING -o ens192 -j MASQUERADE

# End each table with the 'COMMIT' line or these rules won't be processed
COMMIT
```



Slika prikazuje:



![Image](assets/fr/037.webp)



Držite ovu konfiguracionu datoteku otvorenom i pređite na sledeći korak. 😉



### E. Konfiguracija Linux firewall-a za WireGuard



Još uvek u istoj konfiguracionoj datoteci, proglasićemo korporativnu mrežu "192.168.100.0/24" kako bismo mogli da je kontaktiramo. Evo dva pravila koja treba dodati (idealno nakon sekcije "*# ok icmp code for FORWARD*" kako bismo grupisali pravila zajedno):



```
# autoriser le forwarding pour le réseau distant de confiance (+ le réseau du VPN)
-A ufw-before-forward -s 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -s 192.168.110.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.110.0/24 -j ACCEPT
```



Ako želite da autorizujete samo jednog domaćina, na primer "192.168.100.11", to je jednostavno:



```
-A ufw-before-forward -s 192.168.100.11/32 -j ACCEPT
-A ufw-before-forward -d 192.168.100.11/32 -j ACCEPT
```



Sada možete sačuvati datoteku i zatvoriti je. Sve što preostaje je da aktivirate UFW i restartujete uslugu kako biste primenili naše izmene:



```
sudo ufw enable
```



```
sudo systemctl restart ufw
```



Prvi deo konfiguracije Debian servera je sada završen.



## IV. WireGuard klijent za Windows



WireGuard klijent je dostupan za Windows, macOS, Android, itd... Ovo su sjajne vesti. Svi preuzimanja su dostupna na ovoj stranici: [WireGuard Client](https://www.wireguard.com/install/). U ovom primeru, postaviću klijent na Windows. Da biste postavili WireGuard klijent na Linux, pratite isti princip kao za kreiranje wg0.conf fajla na Debian mašini (bez svih NAT, itd.).



### A. Instaliranje WireGuard Windows klijenta



Kada preuzmete izvršnu datoteku ili MSI paket, instalacija je jednostavna: samo pokrenite instalacioni program, i... voilà, gotovo je! 🙂



![Image](assets/fr/038.webp)



### B. Kreiraj WireGuard profil



Počnite tako što ćete otvoriti softver za kreiranje novog tunela. Da biste to uradili, kliknite na strelicu desno od dugmeta "**Dodaj tunel**" i kliknite na dugme "**Dodaj prazan tunel**".



![Image](assets/fr/028.webp)



Otvoriće se prozor za konfiguraciju. Svaki put kada se kreira nova konfiguracija tunela, WireGuard generiše privatni/javni par ključeva specifičan za ovu konfiguraciju. **U ovoj konfiguraciji, potrebno je da deklarisemo "peer", tj. udaljeni server:**



```
[Interface]
PrivateKey = <la clé privée du PC>
```



Moramo dovršiti ovu konfiguraciju, posebno da deklariramo IP Address na ovom Interface (*Address*), ali takođe da deklariramo udaljeni WireGuard server putem [Peer] bloka. Slika ispod bi vas trebala podsetiti na konfiguracionu datoteku koju smo kreirali na strani Linux servera.



Hajde da počnemo sa blokom `[Interface]`, dodajući IP Address "**192.168.110.2**"; zapamti da server ima IP Address "**192.168.110.121**" na ovom segmentu mreže. Ovo daje:



```
[Interface]
PrivateKey = <la clé privée du PC>
Address = 192.168.110.2/24
```



Zatim, treba da deklarišemo blok "Peer" sa tri svojstva, što rezultira ovom konfiguracijom:



```
[Peer]
PublicKey = 1D/Gf5yd3hUDoFyYQ3P1zayBHUJhJZq+k6Sv03HnJCQ=
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
Endpoint = <ip-serveur-debian>:51820
```



Na slikama:



![Image](assets/fr/029.webp)



**Nekoliko objašnjenja o [Peer] bloku:





- PublicKey**: ovo je javni ključ WireGuard Debian 11 servera (možete dobiti njegovu vrednost pomoću "*sudo wg*" komande)
- AllowedIPs**: ovo su IP adrese / podmreže dostupne putem ove WireGuard VPN mreže, u ovom slučaju podmreža specifična za moj WireGuard VPN (*192.168.110.0/24*) i moja udaljena LAN mreža (*192.168.100.0/24*)
- Endpoint**: ovo je IP Address Debian 11 hosta, pošto je ovo naša WireGuard tačka povezivanja (moraćete da navedete javni IP Address)



Konačno, unesite ime u polje "**Name**" (bez razmaka) i kopirajte i nalepite klijentov javni ključ, jer ćemo ga morati deklarisati na serveru. Kliknite na "**Register**".



### C. Deklariši klijenta na WireGuard serveru



Vreme je da se vratimo na Debian server da bismo deklarisali "**Peer**", tj. naš Windows PC, u WireGuard konfiguraciji. Pre svega, potrebno je **zaustaviti Interface "wg0"** kako bismo izmenili njegovu konfiguraciju:



```
sudo wg-quick down wg0
# ou
sudo wg-quick down /etc/wireguard/wg0.conf
```



Zatim, izmenite prethodno kreiranu konfiguracionu datoteku:



```
sudo nano /etc/wireguard/wg0.conf
```



U ovoj datoteci, nakon bloka `[Interface]`, treba da deklariramo blok `[Peer]`:



```
[Peer]
PublicKey = 0i2Pg8nwDW2j7yOG09ZXht18o8l8Erb9Y5F4xyAyQV8=
AllowedIPs = 192.168.110.2/32
```



Ovaj [Peer] blok sadrži javni ključ Windows 10 računara (**PublicKey**) i IP Address računara Interface (**AllowedIPs**): server će komunicirati u ovom WireGuard tunelu samo da bi kontaktirao Windows klijent, stoga vrednost "**192.168.110.2/32**".



Sve što preostaje je da sačuvate fajl (*CTRL+O zatim Enter pa CTRL+X preko Nano*). Ponovo pokrenite Interface "wg0":



```
sudo wg-quick up wg0
# ou
sudo wg-quick up /etc/wireguard/wg0.conf
```



Da biste proverili da deklaracija partnera funkcioniše, možete koristiti ovu komandu:



```
sudo wg show
```



Kada udaljeni host postavi svoju WireGuard vezu, njegov IP Address će biti pomeren na vrednost "endpoint".



![Image](assets/fr/033.webp)



Konačno, osiguraćemo konfiguracione fajlove kako bismo ograničili pristup root-u:



```
sudo chmod 600 /etc/wireguard/ -R
```



### D. Prva WireGuard veza



Sada kada je konfiguracija spremna, možemo je pokrenuti sa Windows računara. Da bismo to uradili, u "**WireGuard**" klijentu, kliknite na dugme "**Activate**": veza će se **promeniti sa "Off" na "On"**, ali to ne znači da će raditi. Sve zavisi od toga da li je vaša konfiguracija ispravna ili ne. **Kada je veza uspostavljena, naša dva računara komuniciraju putem Interface WireGuard-a konfigurisanog na svakoj strani!**



![Image](assets/fr/030.webp)



U slučaju problema, ovo će biti vidljivo na kartici "**Logbook**". Dva domaćina će redovno slati Exchange pakete kako bi proverili status veze, otuda poruke "*Receiving keepalive packet from peer 1*".



![Image](assets/fr/031.webp)



Ako WireGuard-ova kartica "**Journal**" prikazuje poruku kao što je ona ispod, potrebno je proveriti da li su javni ključevi deklarisani na obe strane ispravni.



```
Handshake for peer 1 (<ip>:51820) did not complete after 5 seconds, retrying (try 2)
```



Sa mog udaljenog računara mogu pingovati IP Address mog Interface WireGuard na serverskoj strani, kao i host na mojoj udaljenoj LAN mreži.



![Image](assets/fr/032.webp)



### E. Performanse: OpenVPN vs WireGuard



Sa mog udaljenog računara povezanog na moj WireGuard VPN, uspeo sam da pristupim fajl serveru i prenesem fajl putem [SMB](https://www.it-connect.fr/le-protocole-smb-pour-les-debutants/), da vidim brzinu prenosa. **Sa WireGuard-om, dostižem maksimalno oko 45 Mb/s, što je odlično, s obzirom da sam na WiFi-u.



![Image](assets/fr/025.webp)



Pod istim uslovima, ali putem OpenVPN veze (u UDP) ovog puta, sa istom operacijom, protok je potpuno drugačiji: oko 3 MB/s. Razlika je očigledna!



![Image](assets/fr/026.webp)



Ovo je zanimljivo, jer ako, na primer, pređete sa WiFi veze na 4G/5G vezu, ponovno povezivanje će biti toliko brzo da prekid neće biti vidljiv.



### F. Bonus: full tunnel WireGuard



Sa trenutnom konfiguracijom, deo saobraćaja prolazi kroz VPN, a ostatak kroz korisnikovu Internet konekciju, uključujući pretraživanje Interneta. Ako želimo da pređemo na WireGuard **full tunnel mode**, tako da sve prolazi kroz VPN tunel, potrebno je da napravimo nekoliko izmena u našoj konfiguraciji....



Prvo, treba da instalirate paket "resolvconf" na:



```
sudo apt-get update
sudo apt-get install resolvconf
```



Kada se to uradi, potrebno je izmeniti profil "wg0.conf" na Debian mašini: zaustavite Interface, izmenite ga i ponovo pokrenite.



```
sudo wg-quick down /etc/wireguard/wg0.conf
```



Dalje, **u bloku `[Interface]`, dodajemo DNS server koji će se koristiti**. U mom slučaju, to je kontroler domena mog laboratorija, ali mogli bismo takođe instalirati Bind9 na Debian mašinu da imamo lokalni resolver.



```
DNS = 192.168.100.11
```



Sačuvaj datoteku, zatim ponovo pokreni Interface:



```
sudo wg-quick up /etc/wireguard/wg0.conf
```



Konačno, u konfiguraciji tunela na Windows 10 radnoj stanici, potrebno je izmeniti odeljak "AllowedIPs" kako bi se naznačilo da sve mora proći kroz tunel. Zameni:



```
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
```



Od:



```
AllowedIPs = 0.0.0.0/0
```



Možete videti da ovo takođe omogućava opciju "**Kill switch*".



![Image](assets/fr/040.webp)



Konačno, iskoristio sam ovaj puni tunel da sprovedem mali test protoka, čiji su rezultati prikazani ispod:



![Image](assets/fr/039.webp)



WireGuardova konfiguracija je prilično jednostavna i laka za razumevanje, a pre svega za održavanje. **WireGuard se smatra budućnošću VPN-ova**, tako da bi bilo bolje da ga pažljivo pratimo! Takođe možemo videti da je prednost značajna u smislu performansi, što je ogromna prednost za WireGuard u poređenju sa OpenVPN-om.



Dodatna dokumentacija:





- [Man - Komanda wg](https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8)
- [Man - Komanda wg-quick](https://manpages.debian.org/unstable/wireguard-tools/wg-quick.8.sr.html)



**Vaš WireGuard VPN je pokrenut i radi! Čestitamo!