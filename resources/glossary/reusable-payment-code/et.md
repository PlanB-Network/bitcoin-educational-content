---
term: KORDUVKASUTATAV MAKSEKOOD

---
BIP47 puhul on korduvkasutatav maksekood staatiline identifikaator, mis genereeritakse Bitcoini rahakotist, mis võimaldab teatamistehingut ja unikaalsete aadresside tuletamist. Sellega välditakse aadresside korduvkasutamist, mis toob kaasa privaatsuse kadumise, ilma et iga makse puhul oleks vaja käsitsi tuletada ja edastada uusi, kasutamata aadresse. BIP47 puhul on korduvkasutatavad maksekoodid konstrueeritud järgmiselt:


- Baid 0 vastab versioonile;
- 1. bait on bitt-väli teabe lisamiseks erikasutuse korral;
- 2. bait näitab avaliku võtme "y" pariteeti;
- Alates 3. baidist kuni 34. baidini leiate avaliku võtme väärtuse "x";
- Alates 35. baidist kuni 66. baidini on avaliku võtmega seotud ahelakood;
- Alates baidist 67 kuni baidini 79 on täitmine null.

Maksekoodi algusesse lisatakse üldjuhul inimloetav osa (HRP) ja lõppu kontrollsumma ning seejärel kodeeritakse see baas58-ga. Seega on maksekoodi ülesehitus üsna sarnane laiendatud võtme omale. Siin on näiteks minu enda BIP47 maksekood base58-s:

```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```

BIP47 PayNymi rakenduses saab maksekoode väljendada ka roboti kujutisega seotud identifikaatorite kujul. Siin on näiteks minu oma:

```text
+throbbingpond8B1
```

Maksekoodide kasutamine koos PayNymi rakendusega on praegu saadaval Sparrow Wallet'is arvutis ja Samourai Wallet'is mobiilis.