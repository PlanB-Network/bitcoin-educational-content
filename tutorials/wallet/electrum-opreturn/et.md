---
name: Electrum OP_RETURN
description: Registreeri sõnum Blockchain Bitcoin koos Electrumiga
---

![cover](assets/cover.webp)




See samm-sammult õpetus näitab teile, kuidas kirjutada Blockchain Bitcoin sõnum Wallet Electrumi abil. See toiming kasutab OP_RETURN juhendit, et sisestada Blockchain-s avalikult nähtavale tehingule tekst. Järgige neid lihtsaid samme edukaks registreerimiseks.



---
## Eeltingimused





- Arvuti (Windows, macOS või Linux).
- Internetiühendus.
- Mõned satoshid (Sats) või bitcoinid (BTC) teie Wallet-s, et katta tehingu summa ja tasud.
- Tekst-hekstarvete teisendaja (nt veebisait) või spetsiaalne tööriist, nagu [see OP_RETURN skriptigeneraator](https://resources.davidcoen.it/opreturnelectrum/).



---

## Samm 1: Laadige alla ja installige Electrum



![image](assets/fr/01.webp)



1. Külastage Electrumi ametlikku veebisaiti: [electrum.org](https://electrum.org/).


2. Laadige alla oma operatsioonisüsteemile vastav versioon (Windows, macOS, Linux).


3. Paigaldage Electrum vastavalt paigaldaja juhistele.


4. Kontrollige allalaaditud faili terviklikkust (valikuline, kuid turvalisuse huvides soovitatav), võrreldes faili allkirja või Hash.



→ Rohkem üksikasju Electrumi õpetuse kohta :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Samm 2: Looge või importige Wallet



1. Käivitage Electrum.


2. Valige Loo uus Wallet või Taasta olemasolev Wallet, kui teil on juba olemas seed fraas (taastamisfraas).


3. Järgige juhiseid Wallet seadistamiseks:




 - Uue Wallet puhul märkige oma seed lause üles ja hoidke seda turvalises kohas (paber, seif jne).
 - Olemasoleva Wallet puhul sisestage selle taastamiseks seed fraas.


4. Seadke oma Wallet turvamiseks parool.



→ Rohkem üksikasju Electrumi õpetuse kohta :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## 3. samm: kontrollige olemasolevaid vahendeid



Veenduge, et teie Wallet sisaldab piisavalt bitcoine (BTC) või satoshisid (Sats), et :




- Tehingu summa (näiteks 0,00001 BTC või 1000 Sats).
- Tehingutasud, mis varieeruvad vastavalt võrgu suurusele (tavaliselt mõned tuhanded Sats).



Vaadake oma vahendite kontrollimiseks saldot Electrumis.



![image](assets/fr/02.webp)



Vajaduse korral kandke BTC või Sats üle, et toita oma Wallet. Selleks minge vahekaardile "Receive" ja klõpsake "Create Request" :



![image](assets/fr/03.webp)



See näitab vastuvõttu Address:



![image](assets/fr/04.webp)



→ Rohkem üksikasju Electrumi õpetuse kohta :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## 4. samm: valmistage ette kirjutatav sõnum



Valige sõnum, mille soovite sisestada (nt "Tänu Satoshi"). Märkus: OP_RETURN sõnumid on piiratud 80 baidiga, st umbes 80 ASCII tähemärgiga.



*Võtke hetkeks aega ja mõelge: see, mida te kirjutate Blockchain Bitcoin on igavene ja kõigile kättesaadav, seega :*




- jätta meie inimlikkuse kaunis väljendus,
- vältige sisu sisestamist, mida võite kahetseda



*Blockchain ruum ja teie bitcoinid on väärtuslikud, kasutage neid targalt ja tahtlikult*



Teisenda oma sõnum heksadetsimaalseks :




- Võite kasutada [veebipõhist vahendit](https://www.rapidtables.com/convert/number/ascii-to-hex.html), kuid olge ettevaatlik, et seal ei töödelda tundlikke andmeid (kuigi põhimõtteliselt ei tekita OP_RETURN kaudu Blockchain Bitcoin avaldamiseks mõeldud teave konfidentsiaalsuse probleeme);
- Suurema konfidentsiaalsuse tagamiseks tehke konverteerimine lokaalselt, kasutades väikest Python :



```py
#!/usr/bin/env python3

def main():
ascii_text = input("Enter ASCII text: ")
try:
hex_output = ascii_text.encode('ascii').hex()
print(hex_output)
except UnicodeEncodeError:
print("Error: Input contains non-ASCII characters.", file=sys.stderr)

if __name__ == "__main__":
import sys
main()
```



Näide: `Thanks Satoshi` ASCII-keeles annab `5468616e6b73205361746f736869` heksadekaalarvudes.



Valmistage ette tehinguskript. Siin on näide oodatavast vormingust:



```script
bc1q879cv4p5q6s9537orange3zss33d3turzad8, 0.00001
script(OP_RETURN 5468616e6b73205361746f736869), 0
```



mis koosneb :





- **Sihtkoht Address**: Kehtiv Bitcoin Address. Ici, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`. See võib olla teie enda Address, kui soovite ülekantud raha endale tagasi maksta;
- **Ülekantud summa**: tehingu summa, siin `0.00001` BTC. **Palun tähelepanek**: kuna Electrumis kasutatav ühik on BTC, siis tuleb ka tehingu skriptis märgitud summa väljendada BTC-s, mitte Sats ;
- Skript **OP_RETURN**: Sõnum konverteeritakse kuueteistkümnendsüsteemi, millele eelneb script(`OP_RETURN <sõnum>`), 0. Siin `5468616e6b73205361746f736869` kuueteistkümnendsõnumi jaoks.



⚠️ **Ohoiatus**: On väga oluline märkida "0" pärast OP_RETURN, kuna see opkood märgib skripti kehtetuks, muutes väljundi lõplikult kasutamatuks. Võrgu sõlmed kustutavad selle väljundi oma UTXO komplektist. Kui sisestate muu väärtuse kui `0`, on see pöördumatult kadunud: teie bitcoinid loetakse põletatuks. Seetõttu tuleks alati sisestada `0` koos OP_RETURN-ga, et salvestada soovitud andmed, kuid seostamata sellega rahalisi vahendeid, mis läheksid kaduma.



Vihje: Kasutage [OP_RETURN Generator] tööriista (https://resources.davidcoen.it/opreturnelectrum/), et generate skripti automaatselt koostada. Isegi kui see tööriist soovitab summa sisestada BTC-s, hoidke ühikuna seadistatud Electrum.



![image](assets/fr/05.webp)



Electrumi kasutatava ühiku muutmiseks leiate menüüribalt "Eelistused", seejärel valige vahekaardilt "Ühikud" BTC / mBTC / bitid või Sats :



![image](assets/fr/06.webp)




---

## 5. samm: Tehingu saatmine



Mine Electrumis vahekaardile Saada.



![image](assets/fr/07.webp)



Sisestage väljale "Pay to" ettevalmistatud skript (näiteks ülaltoodud skript).



![image](assets/fr/08.webp)



Väli "Pay to" peaks olema kuvatud Green ja tehingu summa peaks ilmuma alloleval real.



Kontrollige summa ja selle ühik väljal Amount (Summa).



Klõpsake nupule "Maksa..." ja kohandage oma tehingutasu vastavalt summale, mida olete nõus maksma, ja kiirusele, millega soovite, et Miner töötleks teie tehingu ja integreeriks selle plokki.



![image](assets/fr/09.webp)



Klõpsake OK ja kinnitage tehing oma parooliga. Ilmub kinnitusaken.




---

## 6. samm: Registreerimise kontrollimine



Kui tehing on kinnitatud (see võib võtta paar minutit), minge vahekaardile "Ajalugu".



![image](assets/fr/10.webp)



Tehingu üksikasjade vaatamiseks tehke tehingul paremklõps ja valige "View on Explorer".



Teise võimalusena kopeerige sihtkoha Address (näiteks `bc1q879cv4p5q6s9537orange3zss33d3turzad8`) ja vaadake seda Blockchain ekspluatris, näiteks [Mempool.space](https://Mempool.space/) või [blockstream.info](https://blockstream.info/).



Otsige tehingu üksikasjadest välja OP_RETURN, et näha oma sõnumit.



![image](assets/fr/11.webp)




![image](assets/fr/12.webp)




---

## Näpunäited ja parimad tavad





- Katsetage väikese kogusega: Alustage väikese tehinguga (nt Sats 1000), et vältida kulukaid vigu.
- Veenduge, et OP_RETURN sisaldav väljund oleks võrdne nulliga, vastasel juhul lähevad teie bitcoinid lõplikult kaduma.
- Kontrollige seadet: Veenduge, et sisestatud summa vastab Electrumis kuvatavale ühikule (BTC, mBTC või Sats).
- Tehingutasu: Kui võrk on ülekoormatud, suurendage tasu kiirema kinnituse saamiseks.
- Lühisõnum: OP_RETURN kirjed on piiratud 80 baidiga. Planeerige oma sõnum vastavalt.



---

## Kasulikud ressursid





- Electrumi allalaadimine: [electrum.org](https://electrum.org/)
- OP_RETURN skripti generaator: [resources.davidcoen.it/opreturnelectrum/](https://resources.davidcoen.it/opreturnelectrum/)
- Blockchain Explorers: [Mempool.space](https://Mempool.space/), [blockstream.info](https://blockstream.info/)