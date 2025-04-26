---
term: UUDELLEENKÄYTETTÄVÄ MAKSUKOODI

---
BIP47:ssä uudelleenkäytettävä maksukoodi on Bitcoin-lompakosta luotu staattinen tunniste, joka mahdollistaa ilmoitustapahtuman ja yksilöllisten osoitteiden johtamisen. Näin vältetään osoitteiden uudelleenkäyttö, joka johtaa yksityisyyden menetykseen, ilman että uusia, käyttämättömiä osoitteita tarvitsee johtaa ja lähettää manuaalisesti jokaista maksua varten. BIP47:ssä uudelleenkäytettävät maksutunnukset rakennetaan seuraavasti:


- Tavu 0 vastaa versiota;
- Tavu 1 on bittikenttä tietojen lisäämiseksi erityiskäyttöä varten;
- Tavu 2 ilmaisee julkisen avaimen "y"-pariteetin;
- Tavusta 3 tavuun 34 löydät julkisen avaimen x-arvon;
- Tavusta 35 tavuun 66 on julkiseen avaimeen liittyvä ketjukoodi;
- Tavusta 67 tavuun 79 ei ole pehmustetta.

Maksukoodin alkuun lisätään yleensä ihmisen luettavissa oleva osa (Human-Readable Part, HRP) ja sen loppuun tarkistussumma, minkä jälkeen se koodataan base58-koodilla. Maksukoodin rakenne on siis melko samanlainen kuin laajennetun avaimen rakenne. Tässä on esimerkiksi oma BIP47-maksukoodini base58-muodossa:

```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```

BIP47:n PayNym-toteutuksessa maksukoodit voidaan ilmaista myös robotin kuvaan liittyvinä tunnuksina. Tässä on esimerkiksi minun:

```text
+throbbingpond8B1
```

Maksukoodien käyttö PayNym-toteutuksen kanssa on tällä hetkellä saatavilla Sparrow-lompakossa tietokoneella ja Samourai-lompakossa matkapuhelimella.