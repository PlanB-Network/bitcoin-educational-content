---
termi: UUDELLEENKÄYTETTÄVÄ MAKSUKOODI
---

BIP47:ssä uudelleenkäytettävä maksukoodi on staattinen tunniste, joka on generoitu Bitcoin-lompakosta ja mahdollistaa ilmoitustransaktion sekä uniikkien osoitteiden johdannon. Tämä välttää osoitteiden uudelleenkäytön, mikä johtaa yksityisyyden menetykseen, ilman että uusia, käyttämättömiä osoitteita tarvitsee manuaalisesti johtaa ja välittää jokaiselle maksulle. BIP47:ssä uudelleenkäytettävät maksukoodit rakennetaan seuraavasti:
* Tavu 0 vastaa versiota;
* Tavu 1 on bittikenttä lisätiedon lisäämiseksi tietyssä käytössä;
* Tavu 2 ilmaisee julkisen avaimen `y`:n pariteetin;
* Tavusta 3 tavuun 34 löydät julkisen avaimen `x` arvon;
* Tavusta 35 tavuun 66 on julkiseen avaimen liitetty ketjukoodi;
* Tavusta 67 tavuun 79 on nollatäyte.

Yleensä maksukoodin alkuun lisätään Ihmisluettava Osa (Human-Readable Part, HRP) ja loppuun tarkistussumma, ja sitten se koodataan base58-muotoon. Maksukoodin rakentaminen on siis melko samankaltaista kuin laajennetun avaimen rakentaminen. Tässä on oma BIP47 maksukoodini base58-muodossa esimerkkinä:

```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```

PayNym-toteutuksessa BIP47:ssä maksukoodit voidaan myös ilmaista robotin kuvan kanssa yhdistettyjen tunnisteiden muodossa. Tässä on esimerkiksi omani:

```text
+throbbingpond8B1
```

Maksukoodien käyttö PayNym-toteutuksessa on tällä hetkellä saatavilla Sparrow Walletissa PC:llä ja Samourai Walletissa mobiililaitteilla.