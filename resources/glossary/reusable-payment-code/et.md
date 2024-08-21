---
term: KORDUVKASUTATAV MAKSEKOOD
---

BIP47-s on korduvkasutatav maksekood staatiline identifikaator, mis genereeritakse Bitcoin'i rahakotist ja võimaldab teavitustehingu sooritamist ning unikaalsete aadresside tuletamist. See väldib aadresside korduvkasutust, mis viib privaatsuse kaotamiseni, ilma et peaks käsitsi tuletama ja edastama iga makse jaoks uusi, kasutamata aadresse. BIP47-s konstrueeritakse korduvkasutatavad maksekoodid järgnevalt:
* Bait 0 vastab versioonile;
* Bait 1 on bitiväli lisainformatsiooni lisamiseks spetsiifilisel kasutusel;
* Bait 2 näitab avaliku võtme `y` pariteeti;
* Baitidest 3 kuni 34 leiate avaliku võtme `x` väärtuse;
* Baitidest 35 kuni 66 on avaliku võtmega seotud ahelakood;
* Baitidest 67 kuni 79 on nullitäide.

Maksekoodi algusesse lisatakse tavaliselt Inimloetav Osa (Human-Readable Part, HRP) ja lõppu kontrollsumma, seejärel kodeeritakse see base58-sse. Maksekoodi konstruktsioon on seega üsna sarnane laiendatud võtme omaga. Siin on näiteks minu enda BIP47 maksekood base58-s:

```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```

BIP47 PayNym implementatsioonis saab maksekoode väljendada ka roboti kujutisega seotud identifikaatorite kujul. Siin on näiteks minu oma:

```text
+throbbingpond8B1
```

Maksekoodide kasutamine PayNym implementatsioonis on hetkel saadaval Sparrow Wallet'is arvutis ja Samourai Wallet'is mobiilis.