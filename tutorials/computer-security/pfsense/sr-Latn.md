---
name: pfSense
description: Instaliranje Pfsense
---
![cover](assets/cover.webp)



___



*Ovaj vodič je zasnovan na originalnom sadržaju Floriana BURNEL-a objavljenom na [IT-Connect](https://www.it-connect.fr/). Licenca [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Značajne izmene su napravljene u originalnom tekstu autora kako bi se vodič ažurirao.*



___



![Image](assets/fr/027.webp)



## I. Prezentacija



pfSense je besplatan, open source operativni sistem koji transformiše bilo koji računar, dedicirani server ili hardverski uređaj u visokoperformansni, visoko konfigurisani ruter i firewall. Baziran na FreeBSD-u i poznat po svojoj stabilnoj, robusnoj mrežnoj arhitekturi, pfSense postavlja standard za open source firewalle za preduzeća, lokalne vlasti i zahtevne kućne korisnike već više od petnaest godina.



Njegove glavne funkcije su se značajno razvijale tokom godina i unapređivane su sa svakom novom verzijom. Do danas, pfSense nudi :





- Kompletna, centralizovana administracija putem modernog, intuitivnog i sigurnog Interface web Interface.
- Vatrozid visokih performansi sa podrškom za napredni NAT (uključujući NAT-T) i granularno upravljanje pravilima.
- Izvorna podrška za multi-WAN, omogućavajući agregaciju ili redundanciju Internet konekcija.
- Integrisani DHCP server i relej.
- Visoka dostupnost zahvaljujući CARP protokolu za preuzimanje u slučaju kvara i mogućnost konfiguracije pfSense klastera.
- Ravnoteža opterećenja između nekoliko veza ili servera.
- Puna podrška za VPN: IPsec, OpenVPN i WireGuard (zamena za L2TP, sada zastareo).
- Konfigurisani portal za goste za kontrolu pristupa, posebno u javnim ili hotelskim okruženjima.



pfSense takođe ima proširiv sistem paketa koji olakšava dodavanje naprednih funkcija kao što su transparentni proxy (Squid), filtriranje URL-ova ili IDS/IPS (Snort ili Suricata) direktno sa Interface weba.



pfSense se distribuira isključivo za 64-bitne platforme, u skladu sa trenutnim preporukama FreeBSD-a. Može se instalirati na standardni hardver (PC-jevi, serverski rack-ovi) ili na platforme sa niskom potrošnjom energije kao što su Netgate uređaji ili određene x86 kutije niskog profila, koje su daleko moćnije od starijih Alix kutija.



Konačno, vredi zapamtiti da pfSense zahteva najmanje dva fizička mrežna interfejsa: jedan posvećen eksternoj zoni (WAN) i jedan posvećen internoj mreži (LAN). U zavisnosti od složenosti vaše infrastrukture (DMZ, VLAN, više WAN-ova), može biti potrebno nekoliko dodatnih interfejsa kako bi se u potpunosti iskoristile njegove mogućnosti.



## II. Preuzmi sliku



Najnovija stabilna verzija pfSense, u trenutku pisanja ovog vodiča, je 2.8 (objavljena u junu 2025). Možete preuzeti ISO sliku ili instalacionu datoteku prilagođenu vašem hardverskom okruženju direktno sa zvaničnog sajta :





- [Preuzmi pfSense](https://www.pfsense.org/download/)



Portal za preuzimanje vam omogućava da izaberete :





- Arhitektura (generalno **AMD64** za savremeni hardver).
- Tip slike (**Installer USB Memstick** za instalaciju putem USB memorijskog štapića, **ISO Installer** za snimanje ili virtuelno uređivanje).
- Najbliže ogledalo za preuzimanje, za optimizaciju brzine prenosa.



Za one koji žele da implementiraju pfSense u virtualizovanom okruženju (Proxmox, VMware ESXi, VirtualBox...), dostupna je i **OVA** slika. Ova gotova virtualna mašina uveliko pojednostavljuje instalaciju i početnu konfiguraciju. Samo se pobrinite da prilagodite dodeljene resurse (CPU, RAM, mrežni interfejsi) u skladu sa očekivanim opterećenjem i vašom mrežnom topologijom.



Pre instalacije, preporučujemo proveru integriteta preuzetog fajla verifikacijom **SHA256** vrednosti koja je navedena na zvaničnoj stranici za preuzimanje. Ovo osigurava da slika nije izmenjena ili oštećena.



## III. Instalacija



U ovom primeru, instalacija se izvodi na virtuelnoj mašini koja koristi VirtualBox. Procedura ostaje potpuno ista na fizičkoj mašini ili bilo kom drugom hipervizoru, osim za upravljanje virtuelnim uređajima.



### 1. Minimalni hardverski zahtevi



Za standardno raspoređivanje, preporučujemo :





- 1 GB RAM** minimum (preporučeno je 2 GB ili više za omogućavanje dodatnih paketa ili podrške za ZFS).
- 8 GB disk prostora** (20 GB ili više je poželjno za naprednije konfiguracije, posebno ako instalirate proxy keš, IDS/IPS ili detaljne logove).
- Najmanje dva virtuelna mrežna interfejsa** (jedan za WAN, jedan za LAN). U VirtualBox-u, dodajte ih u podešavanja VM-a pre pokretanja.



### 2. Pokretanje instalatera



Montirajte preuzetu ISO sliku kao virtuelni optički disk u VirtualBox-u, ili umetnite USB ključ ako instalirate na fizičku mašinu. Pri pokretanju, pojavljuje se boot meni:



Ako ne izaberete nijednu opciju, pfSense će se automatski pokrenuti sa podrazumevanim opcijama nakon nekoliko sekundi. Pritisnite taster "**Enter**" za pokretanje u normalnom režimu.



![Image](assets/fr/027.webp)



Kada se glavni meni pojavi, brzo pritisnite dugme "**I**" da biste pokrenuli instalaciju.



![Image](assets/fr/001.webp)



### 3. Početne postavke instalatera



Prvi ekran vam omogućava da postavite nekoliko regionalnih parametara, kao što su font prikaza i kodiranje karaktera. Ova podešavanja su korisna u specifičnim slučajevima (nestandardne tastature, serijski ekrani, orijentalni jezici). Za većinu instalacija, zadržite podrazumevane vrednosti i izaberite "**Prihvati ova podešavanja**".



![Image](assets/fr/002.webp)



### 4. Izbor načina instalacije



Odaberite "**Quick/Easy Install**" da biste pokrenuli automatizovanu instalaciju sa preporučenim opcijama. Ova metoda briše izabrani disk i konfiguriše pfSense sa podrazumevanim particionisanjem.



![Image](assets/fr/003.webp)



Pojavljuje se upozorenje koje ukazuje da će svi podaci na disku biti obrisani. Potvrdite sa "**OK**".



Instalacioni program zatim kopira potrebne fajlove na disk. U zavisnosti od vašeg hardvera, ovo može trajati od nekoliko sekundi do nekoliko minuta.



### 5. Izbor jezgra



Kada vas instalacioni program upita da izaberete tip kernela, ostavite selektovano "**Standard Kernel**". Ovaj generički kernel je savršeno prilagođen standardnim implementacijama, bilo na PC-u, serveru ili VM-u.



### 6. Kraj instalacije i restartovanje



Kada je instalacija završena, izaberite "**Reboot**" da restartujete vašu mašinu na vašoj novoj pfSense instanci.



**Važna napomena**: uklonite ISO sliku ili isključite instalacioni USB ključ pre ponovnog pokretanja, kako biste izbegli ponovno pokretanje instalacionog programa sledeći put kada pokrenete računar.



## IV. Pokretanje pfSense-a po prvi put



Prilikom prvog pokretanja, pfSense mora biti konfigurisan da prepozna i pravilno dodeli svoje mrežne interfejse (WAN, LAN, DMZ, VLAN-ove, itd.). Pažljivo identifikovanje vaših mrežnih kartica je ključno kako biste izbegli greške u konfiguraciji koje bi vas mogle lišiti pristupa Interface webu ili učiniti vaš firewall neoperativnim.



Prilikom pokretanja, pfSense automatski detektuje i prikazuje sve dostupne mrežne interfejse, označavajući MAC Address za svaki. Ovo olakšava njihovo razlikovanje.



### 1. VLANs



Prvo pitanje se tiče konfiguracije VLAN-ova. U ovoj fazi, za osnovnu konfiguraciju, nećemo aktivirati VLAN-ove. Zato pritisnite taster "**N**" da preskočite ovaj korak.



![Image](assets/fr/004.webp)



### 2. WAN i LAN Interface Assignment



pfSense vas zatim upita da definišete koji Interface će biti korišćen za WAN (pristup Internetu). Možete birati između:





- Unesite ime Interface ručno (preporučuje se za virtuelna okruženja).
- Koristite automatsko otkrivanje pritiskom na "**A**". Ova opcija je korisna na fizičkom hostu, pod uslovom da su vaši mrežni kablovi povezani i da su linkovi aktivni.



![Image](assets/fr/005.webp)



U ovom primeru, ručno konfigurišemo WAN. Unesite tačan naziv Interface. Za Intel ploču, naziv će često biti "**em0**" pod FreeBSD, ali može varirati u zavisnosti od hardvera. Na primer, Realtek kartica će često biti prikazana kao "**re0**".



![Image](assets/fr/006.webp)



Ponovite istu operaciju da definišete Interface LAN. Ovde koristimo "**em1**".



pfSense potvrđuje da Interface LAN aktivira i firewall i NAT kako bi zaštitio vašu internu mrežu i upravljao Address prevođenjem.



Ako imate druge fizičke interfejse, možete konfigurisati dodatne interfejse (DMZ, Wi-Fi, specifični VLAN-ovi) u ovoj fazi. Svaki logički Interface zahteva odgovarajuću mrežnu karticu ili virtuelni Interface. Za početnu konfiguraciju, ograničićemo se na WAN i LAN.



Kada su zadaci završeni, pfSense prikazuje jasan pregled korespondencija između fizičkih interfejsa i dodeljenih uloga. Potvrdite sa "**Y**".



### 3. PfSense konzola



Kada je ovaj korak završen, pojavljuje se glavni meni konzole pfSense. On nudi nekoliko korisnih opcija za direktnu administraciju, kao što su resetovanje web lozinke, restartovanje, ponovno učitavanje konfiguracije ili ponovno dodeljivanje interfejsa.



![Image](assets/fr/007.webp)



Videćete i rezime trenutnih mrežnih podešavanja, uključujući podrazumevani IP Address za Interface LAN, obično **192.168.1.1**. Ovo je Address koji ćete morati uneti u svoj pregledač da biste pristupili administrativnom webu Interface.



**Napomena**: Ako vaša interna mreža koristi drugačiji opseg Address, izaberite "**2)** Postavi IP Interface(s) Address" u meniju da biste dodelili IP Address prilagođen vašem okruženju.



Podrazumevano, ako je vaš Interface WAN povezan na kutiju ili modem konfigurisan za DHCP, pfSense će automatski preuzeti javnu IP adresu Address. Stoga biste trebali imati neposredan pristup Internetu povezivanjem klijenta na pfSense Interface LAN.



## V. Prvi pristup Interface web



Kada je početno pokretanje završeno i mrežni interfejsi konfigurisani, možete pristupiti pfSense-ovom Interface webu da biste finalizirali i fino podesili vašu konfiguraciju.



### 1. Inicijalna konekcija



Povežite računar sa LAN portom (ili virtuelnim Interface LAN u vašem hipervizoru) i dodelite mu IP Address u istom opsegu ako je potrebno (po defaultu, pfSense automatski distribuira Address putem DHCP-a na LAN-u).



U vašem pregledaču, idite na Address naznačen od strane konzole (podrazumevano `https://192.168.1.1`). Imajte na umu da pfSense zahteva HTTPS čak i za prvu konekciju - tako da očekujte upozorenje o samopotpisanom sertifikatu, koje možete ignorisati dodavanjem izuzetka.



Pojavljuje se ekran za prijavu. Podrazumevane akreditive su :




- Korisničko ime:** `admin`
- Lozinka:** `pfsense`



Ovi identifikatori će biti izmenjeni tokom početne konfiguracije čarobnjaka.



## VI. Čarobnjak za postavljanje



Prilikom prve veze, pfSense vas poziva da pratite njegov **Setup Wizard**. Preporučujemo da ga koristite kako biste osigurali da su svi osnovni parametri ispravno definisani.



### 1. Opšti parametri



Možete:




- Navedite ime hosta i lokalni domen (primer: `pfsense` i `lan.local`).
- Definišite DNS servere i izaberite da li pfSense treba da koristi DNS vašeg ISP-a ili eksternu uslugu (Cloudflare, OpenDNS, Quad9...).



### 2. Vremenska zona



Naznačite vremensku zonu vaše lokacije kako bi dnevnici i rasporedi bili dosledni (npr. `Europe/Paris`).



### 3. WAN konfiguracija



Konfigurišite WAN vezu :




- Podrazumevano je **DHCP** (dovoljno ako ste iza kutije).
- Ako imate fiksnu IP adresu, unesite parametre (staticki IP, maska, gateway, DNS) ručno.
- Ako je potrebno, definišite VLAN ili PPPoE autentifikaciju (uobičajeno kod nekih ISP-ova).



### 4. LAN konfiguracija



Čarobnjak predlaže promenu podrazumevanog LAN podmreže. Ako imate specifičan plan adresiranja, sada je vreme da ga prilagodite.



### 5. Promeni lozinku administratora



Osigurajte svoj pfSense tako što ćete odmah postaviti jaku lozinku za korisnika `admin`.



## VII. Verifikacija i ažuriranja



Pre nego što implementirate svoj firewall, uverite se da imate najnoviju verziju:





- Idite na **System > Update**.
- Odaberite kanal za ažuriranje (obično **Stable**).
- Proverite ažuriranja i primenite ih.



Dobro je omogućiti obaveštenja o ažuriranjima kako biste bili informisani o sigurnosnim zakrpama.



## VIII. Čuvanje konfiguracije



Pre nego što napravite bilo kakve veće promene, implementirajte politiku bekapa:





- Idite na **Diagnostics > Backup & Restore**.
- Preuzmite kopiju trenutne konfiguracije (`config.xml`).
- Čuvajte ga na sigurnom mestu (šifrovani eksterni medij).



Za okruženja kritična za misiju, razmotrite automatsko pravljenje rezervnih kopija konfiguracije na eksternom serveru ili putem programiranog skripta.



## IX. Najbolje prakse nakon instalacije



Da završite svoje raspoređivanje s mirom u duši :





- Izmeni pravila vatrozida**: po podrazumevanim postavkama, pfSense dozvoljava sav odlazni saobraćaj na LAN-u i blokira dolazni saobraćaj na WAN-u. Prilagodi ova pravila prema potrebi.
- Konfigurišite siguran daljinski pristup**: ako je potrebno, omogućite pristup Interface webu sa WAN-a samo putem VPN-a ili sa IP ograničenjima.
- Omogući obaveštenja**: konfiguriši SMTP server za primanje upozorenja (neuspesi, ažuriranja, greške).
- Instalirajte korisne ekstenzije**: na primer, IDS/IPS (Snort, Suricata), proxy (Squid), DNS filtriranje (pfBlockerNG).



Vaš pfSense firewall je sada pokrenut i spreman da zaštiti vašu mrežu. Zahvaljujući svojoj fleksibilnosti i aktivnoj zajednici, imate moćan, skalabilan alat koji može da se prilagodi vašim budućim potrebama (multi-WAN, VLAN, site-to-site VPN, captive portal, itd.).



Redovno konsultujte zvaničnu dokumentaciju ([docs.netgate.com](https://docs.netgate.com/pfsense/en/latest/)) kako biste otkrili nove funkcije i osigurali da vaša konfiguracija bude ažurirana i sigurna.