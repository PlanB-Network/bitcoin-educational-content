---
name: LN VPN

description: Podesi svoj VPN
---

![image](assets/cover.webp)


LN VPN je prilagodljiva VPN usluga koja prihvata samo lightning uplate. Danas ću vam pokazati kako da je koristite i ostavite manje tragova prilikom pretraživanja interneta.


Postoji mnogo kvalitetnih provajdera VPN usluga, a mi smo sproveli sveobuhvatan pregled u ovom članku (hiperveza). Međutim, LN VPN se izdvaja, i nismo mogli propustiti priliku da vam ga predstavimo.


Većina provajdera VPN usluga kao što su ProtonVPN i Mullvad nude opciju plaćanja bitcoinima, ali zahtevaju kreiranje naloga i kupovinu plana na duži ili kraći rok, što možda ne odgovara svačijem budžetu.


LN VPN omogućava korišćenje VPN-a na zahtev, u trajanju od samo jednog sata, zahvaljujući implementaciji Bitcoin plaćanja putem Lightning Network. Instantna i anonimna, lightning plaćanja otvaraju svet mogućnosti za mikroplaćanja.


Napomena💡: **Ovaj vodič opisuje kako koristiti LN VPN sa sistema Linux Ubuntu 22.04 LTS.**


## Preduslovi: Wireguard


U jednostavnim terminima, Wireguard se koristi za kreiranje sigurnog tunela između vašeg računara i udaljenog servera preko kojeg ćete pretraživati Internet. To je IP Address ovog servera koji će se pojaviti kao vaš za vreme trajanja zakupa koji ćete Contract prateći ovaj vodič.


Službeni vodič za instalaciju Wireguarda: https://www.wireguard.com/install/


```
Wireguard installation
$ sudo apt-get update
$ sudo apt install wireguard
```


## Preduuslovi: Lightning Bitcoin Wallet


Ako još uvek nemate Lightning Bitcoin Wallet, bez brige, napravili smo veoma jednostavan vodič za vas ovde. (sekcija sa LN uputstvom vam može pomoći)


## Korak 1: Contract a Lease


Sa https://lnvpn.com, trebaće da izaberete zemlju izlazne IP adrese VPN tunela i trajanje. Kada postavite ove parametre, kliknite na Pay with lightning.


![image](assets/1.webp)


Prikazaće se munja Invoice, a vi samo treba da je skenirate sa vašom munjom Wallet.


Kada se Invoice plati, moraćete da sačekate nekoliko sekundi do dva minuta da bi se generisala vaša Wireguard konfiguraciona podešavanja. Ako potraje malo duže, ne paničite, ovaj postupak smo radili na desetine puta i ponekad jednostavno traje malo duže.

Sledeći tekst je preveden na engleski jezik uz očuvanje istog markdown rasporeda kao i originalni tekst:


Sledeći ekran će se pojaviti i samo treba da kliknete na "Download as File" da biste primili svoj config fajl, koji će imati ime koje izgleda kao lnvpn-xx-xx.conf gde će "xx" odgovarati trenutnom datumu.

![image](assets/2.webp)


## Korak 2: Aktivirajte tunel


Prvo, treba da preimenujete config datoteku dobijenu u prethodnom koraku kako bi je Wireguard automatski prepoznao.


Idite u svoj folder za preuzimanje, bilo u terminal prozoru ili sa istraživačem datoteka, i preimenujte lnvpn-xx-xx.conf datoteku u wg0.conf ovako:


```
$ sudo ln -s usrbin/resolvectl usrlocal/bin/resolvconf
$ sudo wg-quick up ~/Downloads/wg0.conf
```


Evo ga! Tunel je aktiviran!


## Korak 3: Verifikuj


Koristite onlajn servis kao što je whatismyip da proverite da li je vaš javni IP Address sada onaj od VPN-a koji ste upravo aktivirali.


## Korak 4: Onemogući


Kada vam istekne zakup, moraćete da onemogućite vezu kako biste ponovo dobili pristup internetu. Zatim možete ponoviti korake od 1 do 3 kad god želite da uspostavite zakup sa LN VPN.


Onemogući tunel:


```
$ sudo ip link delete dev wg0
```


Tu imate to! Sada znate kako koristiti LN VPN, jedinstvenu VPN uslugu!