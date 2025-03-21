---
name: Professori Plan ₿ Network
description: Miten voin lisätä tai muuttaa opettajaprofiiliani Plan ₿ Network:ssä?
---
![cover](assets/cover.webp)

Jos aiot osallistua Plan ₿ Network:een kirjoittamalla uuden opetusohjelman tai kurssin, tarvitset opettajan profiilin. Tämän profiilin avulla voit saada asianmukaiset hyvitykset alustalle tuottamastasi sisällöstä.

Niillä teistä, jotka ovat jo osallistuneet Plan ₿ Network:n opetussisällön luomiseen, on todennäköisesti jo opettajaprofiili. Löydät sen kansiosta `/professors` [GitHub-arkistossamme](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors). Jos profiilisi on jo olemassa, etsi kirjautumistietosi `professor.yml`-tiedostosta.

Jos haluat tehdä muutoksia profiiliisi, siirry tämän ohjeen lopussa olevaan osioon "Muokkaa opettajaprofiiliasi".

## Lisää uusi opettaja ohjelmistomme avulla

Helpoin tapa luoda opettajaprofiili Plan ₿ Network:een on käyttää integroitua Python-työkalua. Näin se toimii.

### 1 - Määritä paikallinen ympäristö

Sinulla on oltava oma Fork [Plan ₿ Network-repository GitHubissa](https://github.com/PlanB-Network/Bitcoin-educational-content).

Synkronoi Fork:n päähaara (`dev`) lähdekoodivaraston kanssa.

Päivitä paikallinen kloonisi.

```bash
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<username>/bitcoin-educational-content.git
cd bitcoin-educational-content
# Ajouter le dépôt source en tant que remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git
# Récupérer les dernières modifications depuis le dépôt source
git fetch upstream
# Se positionner sur la branche principale 'dev'
git checkout dev
# Fusionner les modifications de la branche 'dev' du dépôt source dans votre fork
git merge upstream/dev
# Pousser les mises à jour vers votre fork sur GitHub
git push origin dev
```

### 2 - Luo uusi haara

Varmista, että olet `dev`-haarassa. Luo uusi haara kuvaavalla nimellä (esim. `add-professor-loic-morel`).

Julkaise tämä haara Fork:ssä verkossa.

```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b add-professor-loic-morel
# Publiez cette branche sur votre fork en ligne
git push -u origin add-professor-loic-morel
```

### 3 - Luo opettajaprofiilisi

Siirry paikallisen kloonisi `scripts/tutorial-related/data-creator/`-kansioon. Varmista, että olet asentanut kaikki ohjelmiston tarvitsemat riippuvuudet, kun olet ensin asentanut Pythonin :

```bash
pip install -r requirements.txt
```

Käynnistä sitten ohjelmisto komennolla :

```bash
python3 main.py
```

Kun olet etusivulla, syötä arkistokloonin paikallinen polku, kieli, jolla kirjoitat, ja GitHub-tunnuksesi. Jos luot tämän profiilin jollekin toiselle ja sinulla on jo professorin profiili, kirjoita tunnuksesi kenttään "*PBN Professor's ID*". Jos olet luomassa omaa profiiliasi, sinulla ei ole vielä professorin tunnusta, koska olet luomassa sitä, joten jätä tämä kenttä tyhjäksi.

Napsauta sitten "*Uusi professori*"-painiketta.

![Image](assets/fr/01.webp)

Täytä vaaditut tiedot (huomaa, että kaikki nämä tiedot ovat julkisia alustallamme sekä GitHubissa) :


- Opettajatiedoston nimi (käytä etu- ja sukunimeäsi tai salanimeäsi pienin kirjaimin) ;
- Nimesi tai lempinimesi ;
- Kirjautumistunnuksen satunnainen luominen ;
- Verkkosivustosi ja profiilisi X (valinnainen) ;
- Lightning Address lahjoitusten vastaanottamiseksi lukijoilta (valinnainen) ;
- Valitse luettelosta 2 tai 3 tunnistetta;
- Valitse profiilikuva paikallisista kansioista napsauttamalla "*Valitse kuva*" (voit käyttää kuvalle mitä tahansa nimeä ja muotoa, ja ohjelmisto mukauttaa sen automaattisesti.). Varmista vain, että kuva on neliönmuotoinen);
- Kirjoita lyhyt kuvaus profiilistasi.

Viimeistele luominen napsauttamalla "*Luo professori*". Tämä tekee automaattisesti generate:sta kaikki profiilisi tarvitsemat tiedostot.

![Image](assets/fr/02.webp)

Tallenna muutoksesi paikallisesti luomalla komento, jossa on selittävä viesti. Siirrä muutokset Fork GitHubiin.

```bash
# Créez un commit avec un message descriptif
git commit -m "*new professor Loïc Morel*"
# Poussez vos modifications sur votre fork
git push origin add-professor-loic-morel
```

Kun olet valmis, luo Pull Request (PR) GitHubiin ehdottaaksesi muutosten integrointia. Lisää PR:ään otsikko ja lyhyt kuvaus.

### 4 - Tarkistaminen ja yhdistäminen

Odota vahvistusta tai palautetta ylläpitäjältä. Tee tarvittaessa korjauksia ja lähetä uudet toimitukset.

```bash
# Créez un commit décrivant les corrections apportées
git commit -m "*Corrections suite à la revue du tutoriel green-wallet*"
# Poussez les corrections sur votre fork
git push origin add-professor-loic-morel
```

Kun PR on yhdistetty, voit poistaa työhaarasi.

## Muokkaa opettajan profiilia

Jos hallitset Gitin käytön, muokkaa opettajaprofiiliasi luomalla uusi haara ja muokkaamalla asiaankuuluvaa tiedostoa suoraan olemassa olevaan kansioon. Muutokset voidaan tehdä joko `professor.yml`-tiedostoon tai markdown-tiedostoon, riippuen korjattavista tiedoista. Kun olet tehnyt muutokset paikallisesti, siirrä ne Fork:ään ja lähetä PR.

Aloittelijoille suosittelen tekemään muutoksen suoraan GitHubin Interface-verkon kautta. Varmista, että sinulla on GitHub-tili. Jos et tiedä, miten sellainen luodaan, seuraa tätä ohjetta :

https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
Siirry [Plan ₿ Network:n GitHub-tietovarastoon, joka on omistettu tiedoille](https://github.com/PlanB-Network/Bitcoin-educational-content/graphs/contributors).

![Image](assets/fr/03.webp)

Napsauta kansiota "*professorit*" ja siirry sitten henkilökohtaiseen kansioosi.

![Image](assets/fr/04.webp)

Jos haluat muuttaa profiilisi metatietoja, kuten Lightning Address, nimeä tai linkkejä, valitse tiedosto "*professor.yml*". Jos haluat muuttaa kuvaustasi, valitse kielesi YAML-tiedosto (esim. "*en.yml*" tai "*fr.yml*").

Jos muutat kuvausta, muista poistaa kaikki vanhentuneet käännökset. Sitten voit joko huolehtia kuvauksesi kääntämisestä muille kielille LLM:n avulla tai jättää vain kuvauksen äidinkielelläsi ja mainita Pull Requestissa, että kuvauksesi vaatii tiimimme kääntämistä.

![Image](assets/fr/05.webp)

Kun olet sen tiedoston kohdalla, jota haluat muokata, napsauta kynäkuvaketta.

![Image](assets/fr/06.webp)

Jos sinulla ei vielä ole Fork:tä Plan ₿ Network-arkistosta, GitHub ehdottaa, että luot sellaisen. Klikkaa "*Fork this repository*".

![Image](assets/fr/07.webp)

Tee haluamasi muutokset tiedostoon. Kun olet valmis, napsauta "*Commit changes*".

![Image](assets/fr/08.webp)

Kirjoita muutosta kuvaava viesti ja valitse sitten "*Ehdota muutoksia*".

![Image](assets/fr/09.webp)

Yhteenveto muutoksistasi tulee näkyviin. Jos haluat tehdä lisää muutoksia profiiliisi, voit palata kansioihin ja tehdä lisää muutoksia. Kun olet valmis, napsauta "*Create pull request*".

Pull Request on pyyntö, jolla pyydetään integroimaan muutokset omasta haarastasi Plan ₿ Network-arkiston päähaaraan, jolloin muutoksia voidaan tarkastella ja niistä voidaan keskustella ennen niiden yhdistämistä.

![Image](assets/fr/10.webp)

Varmista Interface:n yläosassa, että työhaarasi on yhdistetty Plan ₿ Network-arkiston `dev`-haaraan (joka on päähaara).

Kirjoita otsikko, joka tiivistää lyhyesti muutokset, jotka haluat yhdistää lähdekoodivarastoon. Lisää lyhyt kommentti, jossa kuvataan nämä muutokset, ja vahvista vetopyyntö napsauttamalla Green:n "*Create pull request*"-painiketta:

![Image](assets/fr/11.webp)

PR-julkaisusi näkyy tämän jälkeen Plan ₿ Network:n pääarkiston "*Pull Request*"-välilehdellä. Nyt sinun tarvitsee vain odottaa, että ylläpitäjä yhdistää muutoksesi.

![Image](assets/fr/12.webp)

Jos sinulla on teknisiä vaikeuksia muutoksen lähettämisessä, älä epäröi pyytää apua [osallistumiselle omistetussa Telegram-ryhmässämme] (https://t.me/PlanBNetwork_ContentBuilder). Paljon kiitoksia!