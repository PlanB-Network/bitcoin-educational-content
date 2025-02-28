---
term: GENESIS BLOCK

---
Genesis Block on Bitcoin-järjestelmän ensimmäinen lohko. Se merkitsee Bitcoinin konkreettista käynnistämistä. Genesis Blockin loi Bitcoinin nimetön perustaja Satoshi Nakamoto 3. tammikuuta 2009. Sen hash on:

```text
000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
```

Tämä lohko sisältää vain coinbase-transaktion, joka tuottaa 50 bitcoinia palkkioksi louhijalle (tässä tapauksessa Satoshi Nakamotolle itselleen). Tämä lohko sisältää coinbase-transaktioon upotetun viestin:

```text
The Times 03/Jan/2009 Chancellor on brink of second bailout for banks
```

Tämä lainaus on viittaus *The Times* -sanomalehden artikkeliin. Viesti tulkitaan kritiikiksi perinteistä rahoitusjärjestelmää ja sen ylilyöntejä kohtaan, mikä osaltaan motivoi Bitcoinin luomista rahavaihtoehdoksi.

Koska Genesis-lohko on Bitcoin-lohkoketjun ensimmäinen lohko, Genesis-lohkossa ei tietenkään ole kenttää, joka sisältää edellisen lohkon hashin (koska sellaista ei ole). Lisäksi tässä lohkossa palkkioksi luotuja 50 bitcoinia ei voi käyttää protokollatasolla.