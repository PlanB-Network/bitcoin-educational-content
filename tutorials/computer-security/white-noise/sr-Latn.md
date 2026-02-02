---
name: White Noise
description: Privatna, decentralizovana aplikacija za razmenu poruka zasnovana na Nostr i MLS protokolima
---

![cover](assets/cover.webp)




## Uvod



"Usred poteškoća leži prilika". Ovaj citat Alberta Ajnštajna podseća nas da problemi nisu konačni, već u sebi sadrže seme novih, inovativnih rešenja.



Motivacije iza pokretanja rešenja koje predstavljamo u ovom tutorijalu to savršeno ilustruju. To je **White Noise**, rođen iz potrebe.



Rečima osnivača, Max Hillebrand, prenosi *Bitcoin Magazine*: "Pokrenuli smo ovaj projekat zbog nedostatka alternativa." On objašnjava da "postojeće aplikacije za enkripciju nisu efikasne u velikim razmerama: dodavanje 100 ljudi u grupni razgovor značajno usporava enkripciju. Decentralizovane platforme, u međuvremenu, ne nude privatne poruke. Na kraju, otvorena mreža releja Nostr omogućava svima da šire ideje, ali zaštita direktnih poruka ostaje dramatično neadekvatna. Shvatili smo: da bismo zaštitili slobodu, morali smo spojiti ove sisteme."



## Šta je White Noise?



White Noise je aplikacija za razmenu poruka otvorenog koda koju je razvila neprofitna ekipa. Aplikacija promoviše sigurnost, privatnost i decentralizaciju. Za razliku od konvencionalnih aplikacija, ne zahteva ni broj telefona ni e-mail adresu.


White Noise se odlikuje integracijom dva osnovna protokola - Nostr i MLS - koji čine njegovu tehničku osnovu.



Nostr (Beleške i Druge Stvari Prenete Preko Releja) je decentralizovani, open-source protokol dizajniran da se odupre cenzuri. Protokol koristi releje, parove ključeva i klijente.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

Uz white Noise, možete čak odabrati sopstvene postavke releja kako biste maksimizirali privatnost.



MLS (Messaging Layer Security), s druge strane, je sigurnosni protokol koji omogućava end-to-end enkripciju poruka. Drugim rečima, poruke su dostupne samo na krajnjim tačkama, tj. pošiljaocu i primaocu poruke. To znači da releji uključeni u rutiranje poruka ne mogu pristupiti njihovom sadržaju.



Evo brze uporedbe između White Noise i nekoliko najpoznatijih aplikacija za razmenu poruka.





| Tačke poređenja             | White Noise | Telegram   | Whatsapp (Meta) | Bitchat | iMessage | Messenger (Meta) | Signal |
| --------------------------- | ----------- | ---------- | --------------- | ------- | -------- | ---------------- | ------ |
| E2EE šifrovanje / 1:1       | ✅ Da         | Opciono    | ✅ Da             | ✅ Da    | ✅ Da     | ✅ Da              | ✅ Da   |
| Grupno E2EE šifrovanje      | ✅ Da         | ❌ Ne       | ✅ Da             | ✅ Da    | ✅ Da     | Opciono           | ✅ Da   |
| Anonimizacija identiteta    | ✅ Da         | Opciono    | ❌ Ne             | ✅ Da    | ❌ Ne     | ❌ Ne              | ❌ Ne   |
| Server otvorenog koda       | ✅ Da         | ❌ Ne       | ❌ Ne             | ✅ Da    | ❌ Ne     | ❌ Ne              | ✅ Da   |
| Klijent otvorenog koda      | ✅ Da         | ✅ Da        | ❌ Ne             | ✅ Da    | ❌ Ne     | ❌ Ne              | ✅ Da   |
| Decentralizovani server     | ✅ Da         | ❌ Ne       | ❌ Ne             | ✅ Da    | ❌ Ne     | ❌ Ne              | ❌ Ne   |
| Godina osnivanja            | 2025        | 2013       | 2009            | 2025    | 2011     | 2011             | 2014   |

## Početak sa White Noise



### Instalacija White Noise



Idite na [White Noise website](https://www.whitenoise.chat/), zatim kliknite na **Download**.



![screen](assets/fr/03.webp)



White Noise je trenutno dostupan samo na mobilnim uređajima.


Na novom interfejsu koji se pojavljuje, pritisnite :





- dugme **Zapstore** ili **Android APK** ako želite da ga preuzmete na Android ;
- na dugme **iOS TestFlight** ako koristite iPhone.



![screen](assets/fr/04.webp)



Za potrebe ovog tutorijala, izvršićemo preuzimanje za Android.


Ako odlučite da preuzmete putem **Zapstore**, bićete preusmereni na njega. Kada ste na Zapstore-u, upišite **White Noise** u traku za pretragu. Zatim nastavite sa preuzimanjem klikom na **Install**.



![screen](assets/fr/05.webp)



![screen](assets/fr/06.webp)



Ako odlučite da preuzmete APK datoteku, bićete preusmereni na White Noise GitHub repozitorijum da izaberete odgovarajuću verziju za vaš pametni telefon.



Dostupne APK datoteke su :





- whitenoise-0.2.1-arm64-v8a.apk** (57.7 MB), pogodan za novije telefone sa 64-bitnim procesorima;
- whitenoise-0.2.1-armeabi-v7a.apk** (47.5 MB) pogodan za starije telefone sa 32-bitnim procesorima.



Takođe imate **.sha256** datoteke, koje su samo kontrolne sume za verifikaciju integriteta preuzimanja.



![screen](assets/fr/07.webp)



Kada se preuzimanje završi, instalirajte i otvorite aplikaciju.



![screen](assets/fr/08.webp)



### Početno podešavanje korisničkog naloga



Za vašu prvu vezu sa White Noise, pritisnite dugme **Register**.



![screen](assets/fr/09.webp)



Zatim konfigurišite svoj profil odabirom profilne fotografije, imena i dodavanjem kratkog opisa o sebi. Ne morate uneti svoj pravi identitet (ime i fotografiju).


Imajte na umu da White Noise automatski bira ime (pseudonim) za vas, koje možete zadržati ili promeniti. Na kraju, pritisnite dugme **End**.



![screen](assets/fr/10.webp)



Bićete preusmereni na **početni ekran** White Noise, gde će biti navedeni vaši razgovori. Vaš nalog je sada podešen i spreman za korišćenje. Možete deliti svoj profil ili tražiti prijatelje da započnete razgovor.



![screen](assets/fr/11.webp)




### Otkrivanje White Noise interfejsa



Na glavnom interfejsu, na vrhu ekrana videćete :



U gornjem levom uglu, ikonica profila je sličica vaše profilne fotografije ili prvo slovo vašeg imena profila. Kliknite na nju da biste pristupili podešavanjima naloga.



![screen](assets/fr/12.webp)



![screen](assets/fr/13.webp)



U gornjem desnom uglu, pronaći ćete ikonu za započinjanje novog razgovora.



![screen](assets/fr/14.webp)



![screen](assets/fr/15.webp)




## Postavke korisničkog naloga



Pritisnite ikonu profila u gornjem levom uglu da biste pristupili podešavanjima.



![screen](assets/fr/16.webp)



Na vrhu interfejsa **Settings** pronaći ćete svoju fotografiju i ime profila, a zatim vaš javni ključ, koji možete deliti pomoću QR koda pored njega.



![screen](assets/fr/17.webp)



Odmah ispod, pronaći ćete dugme **Promeni nalog**, koje vam omogućava da se povežete sa drugim profilom unutar aplikacije.



![screen](assets/fr/18.webp)



Zatim imate prvi odeljak sa četiri (4) podmenija kao:





- Izmeni profil**



U ovom podmeniju možete izmeniti ime profila, Nostr adresu (NIP-05)... Ne zaboravite da kliknete na **Save** da biste sačuvali izmene.



![screen](assets/fr/19.webp)





- Ključevi profila**



Ovde imate pristup vašim javnim i privatnim (tajnim) ključevima. Kao što vas White Noise podseća, vaš privatni ključ ne sme biti otkriven ni pod kojim okolnostima.



![screen](assets/fr/20.webp)





- Glavni relej



U ovom podmeniju možete dodati ili ukloniti **opšte releje** (releje definisane za upotrebu u svim vašim Nostr aplikacijama), **inbox releje** i **key pack releje**.



Da biste to uradili, dodirnite ikonu **kanta za smeće** ispred releja da biste ga obrisali, ili dodirnite ikonu **+** (plus) da biste dodali novi.



![screen](assets/fr/21.webp)





- Prekidanje**



Kliknite na ovaj podmeni da biste isključili svoj nalog iz aplikacije. Ali, uverite se da ste sačuvali svoje privatne ključeve van mreže, inače nećete moći ponovo da se prijavite kasnije.



![screen](assets/fr/22.webp)




Drugi odeljak nudi podmenije:





- Postavke aplikacije



Ovde možete definisati izgled (temu i jezik prikaza) aplikacije, pa čak i obrisati podatke ako smatrate da su ugroženi, ili ako se sami osećate ugroženo.



![screen](assets/fr/23.webp)





- Donirajte White Noise



Možete podržati tim iza White Noise (neprofitna organizacija) donacijama putem njihove Lightning adrese ili njihove Bitcoin adrese za tiha plaćanja.



![screen](assets/fr/24.webp)



Na kraju, na samom dnu su **postavke za programere**.



![screen](assets/fr/25.webp)




## Započni razgovor



Sada da pogledamo kako započeti razgovor. U trenutku pisanja, White Noise nudi tri opcije komunikacije. Redom ćemo istražiti **Privatne Razgovore** (**Chat 1:1**), tj. između vas i još jedne osobe, **Grupne Razgovore** i **Slanje Multimedijalnih Fajlova**.




### Mačka 1:1



Sa glavnog interfejsa, da biste dodali novog dopisnika, kliknite na ikonu za započinjanje novog razgovora.


Zatim skenirajte QR kod javnog ključa (1) ili nalepite javni ključ (2) vašeg novog dopisnika u traku za pretragu da biste ga pronašli.



![screen](assets/fr/26.webp)



Zatim dodirnite dugme **Start conversation** da biste započeli razgovor sa svojim dopisnikom. Takođe možete **Follow** svog dopisnika ili ga/je pozvati u grupni razgovor pritiskom na dugme **Add to group**.



![screen](assets/fr/27.webp)



Vaša prva poruka novom dopisniku je slična pozivu za zahtev. Ovaj zahtev mora biti prihvaćen od strane vašeg dopisnika pre nego što možete komunicirati sa njim/njom. Ako odbiju, pa, razgovor nije moguć.



![screen](assets/fr/28.webp)



Štaviše, sve dok ne prihvate vaš poziv, neće moći da pročitaju sadržaj vaše početne poruke.



Jednom kada prihvati vaš poziv, sada vam može odgovoriti, i vas dvoje možete komunicirati besprekorno i sigurno.



![screen](assets/fr/29.webp)



Štaviše, u diskusiji imate dodatne funkcionalnosti.



Možete dugo pritisnuti određenu poruku da biste prikazali opcije kao što su:




- reaguj na poruku sa emotikonom (1) ;
- napravite **direktan citat** da biste odgovorili na poruku pritiskom na **Odgovori** (2) ;
- kopirajte poruku pritiskom na **Kopiraj** (3).



![screen](assets/fr/30.webp)





- izbriši poruku pomoću dugmeta **Delete** samo ako dolazi od tebe.



![screen](assets/fr/31.webp)



Možete pretraživati unutar razgovora.



Kliknite na avatar dopisnika na vrhu ekrana da biste pristupili "informacijama o razgovoru" i dodirnite dugme **Pretraži u razgovoru**.



![screen](assets/fr/32.webp)



![screen](assets/fr/33.webp)



U traku za pretragu koji se pojavljuje, unesite reč koju želite da pretražite i pokrenite pretragu. Zatim ćete videti vaše pretražene reči istaknute u **bold**.



![screen](assets/fr/34.webp)




### Grupni razgovori



Grupe za razgovor mogu se kreirati na White Noise.



Da biste to uradili, dodirnite ikonu u interfejsu za pokretanje novog razgovora, zatim kliknite na **Novi grupni razgovor**. Zatim, u traku za pretragu, unesite javni ključ prvog člana kojeg želite dodati u svoju grupu.



![screen](assets/fr/35.webp)



![screen](assets/fr/36.webp)



Na kraju, ako ova opcija ne funkcioniše, iz interfejsa **Započni novi razgovor**, unesite javni ključ prvog člana kojeg želite dodati u grupu u traku za pretragu. Takođe možete skenirati QR kod povezan sa njegovim ili njenim javnim ključem.



Ovog puta, umesto da dodirnete dugme **Start conversation**, kliknite na dugme **Add to group**.



![screen](assets/fr/37.webp)



Na iskačućem meniju koji se pojavi, dodirnite **Novi grupni razgovor**.



![screen](assets/fr/38.webp)



Zatim pritisnite **Nastavi** (ne morate ponovo unositi njegov javni ključ).



![screen](assets/fr/39.webp)



Kao kreator grupe, automatski ste njen administrator. Popunite detalje grupe, kao što su **ime grupe i opis**, zatim kliknite na dugme **Kreiraj grupu**.



![screen](assets/fr/40.webp)



Korisnik kojeg dodate kao prvog člana, kao i svi ostali koje kasnije dodate, dobijaju obaveštenje koje ih poziva da se pridruže grupi. Moraju prihvatiti klikom na **Prihvati** da bi se pridružili grupi.



![screen](assets/fr/41.webp)



Takođe je moguće dodati novog člana sa kojim već ćaskate u postojeću grupu. Da biste to uradili, kliknite na avatar sagovornika na vrhu ekrana da biste pristupili "informacijama o razgovoru" i dodirnite dugme **Dodaj u grupu**.



![screen](assets/fr/42.webp)



Na novom interfejsu koji se pojavljuje, **označite** grupu kojoj želite da ga dodate i dodirnite **Dodaj u grupu**. Sve što preostaje je da sačekate da pristane da se pridruži grupi.



![screen](assets/fr/43.webp)



Imajte na umu da samo administrator grupe može menjati informacije o grupi i dodavati ili izbacivati članove. Takođe, rotacija ključeva sprečava zabranjene članove da dešifruju buduće poruke.



Da biste uklonili člana, iz glavnog interfejsa grupe, dodirnite ikonu grupe na vrhu da biste pristupili interfejsu informacija o grupi.



![screen](assets/fr/44.webp)



![screen](assets/fr/45.webp)



Zatim kliknite na ime člana i **Ukloni iz grupe**. Iz ovog interfejsa, takođe možete poslati poruku, pratiti ga ili dodati u drugu grupu.



![screen](assets/fr/46.webp)



### Slanje multimedijalnih datoteka



Za sada, samo fotografije mogu biti deljene između korisnika na White Noise. Bilo da ste u privatnom razgovoru ili grupnom četu, da biste to uradili, potrebno je:





- pritisnite simbol **plus (+)** sa leve strane polja za unos tekstualne poruke.



![screen](assets/fr/47.webp)





- zatim kliknite na polje označeno **Fotografije** na dnu da biste pristupili svojoj galeriji.



![screen](assets/fr/48.webp)





- izaberite fotografiju(e) za slanje.



![screen](assets/fr/49.webp)



![screen](assets/fr/50.webp)



![screen](assets/fr/51.webp)





## Ključne tačke za pamćenje



White Noise nudi dobar nivo poverljivosti i superiornu sigurnost. S druge strane, to je veoma nova aplikacija, nije mnogo rasprostranjena i još uvek je u začetku. Shodno tome, još uvek je prerano donositi bilo kakve aktivne zaključke. Moguće je naići na nekoliko kvarova tokom korišćenja.



Trenutno mu nedostaju određene funkcionalnosti (nema audio ili video poziva, nema slanja audio ili video multimedijalnih datoteka) u poređenju sa popularnim aplikacijama za razmenu poruka.



Ipak, White Noise ostaje zanimljiva opcija za razgovore gde je poverljivost od najveće važnosti (npr. sa porodicom, bliskim prijateljima ili aktivistima u zajedničkom cilju), čak i ako zahteva malo truda za instalaciju (putem alternativnih prodavnica aplikacija ili APK fajlova) i učenje (savladavanje malo koncepta parova ključeva, klijenata i releja sa Nostr protokolom).



Sada znate kako da koristite White Noise za bezbednu komunikaciju sa prijateljima i porodicom. Molimo vas da nam date palac gore ako smatrate da je ovaj vodič koristan.



Preporučujemo naš vodič o Tox Chat, aplikaciji koja vam omogućava da ćaskate bez posrednika preko decentralizovanog Tox protokola.



https://planb.academy/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3