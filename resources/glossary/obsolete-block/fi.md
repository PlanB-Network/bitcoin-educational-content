---
term: (LOHKO)

---
Viittaa lohkoon, jolla ei ole lapsia: kelvollinen lohko, mutta joka on suljettu Bitcoinin pääketjun ulkopuolelle. Se tapahtuu, kun kaksi louhijaa löytää kelvollisen lohkon samalla ketjun korkeudella lyhyen ajan sisällä ja lähettää sen verkon kautta. Solmut valitsevat lopulta vain yhden lohkon ketjuun sisällytettäväksi sen periaatteen mukaisesti, että ketju, johon on kertynyt eniten työtä, tekee toisesta lohkosta "vanhentuneen". Prosessi, joka johtaa vanhentuneen lohkon tuottamiseen, on seuraava:


- Kaksi louhijaa löytää kelvollisen lohkon samalla ketjun korkeudella lyhyen ajan sisällä. Kutsutaan niitä lohkoksi A ja lohkoksi B;
- Kukin lähettää lohkonsa Bitcoin-solmujen verkkoon. Kullakin solmulla on nyt 2 lohkoa samalla korkeudella. Näin ollen on olemassa kaksi kelvollista ketjua;
- Louhijat jatkavat työtodistusten etsimistä seuraaville lohkoille, mutta sitä varten heidän on välttämättä valittava vain yksi lohko lohko A:n ja B:n väliltä, josta he louhivat;
- Louhija löytää lopulta kelvollisen lohkon lohkon B yläpuolelta. Kutsutaan sitä "lohkoksi B+1";
- Ne lähettävät "B+1-lohkon" verkon solmuihin;
- Koska solmut seuraavat pisintä ketjua (jossa on eniten kertynyttä työtä), ne arvioivat, että ketju B on se, jota kannattaa seurata;
- Ne hylkäävät "lohkon A", joka ei enää ole osa pääketjua. Siitä on siten tullut vanhentunut lohko.

![](../../dictionnaire/assets/9.webp)

> ► *Englanniksi sitä kutsutaan nimellä "Stale Block". Ranskassa sitä voidaan kutsua myös nimellä "bloc périmé" tai "bloc abandonné". Vaikka en ole samaa mieltä tästä käytännöstä, jotkut bitcoin-käyttäjät käyttävät termiä "bloc orphelin" viittaamaan siihen, että kyseessä on itse asiassa vanhentunut lohko.* *