---
name: Ashigaru Terminal
description: Bruk Ashigaru på skrivebordet for å lage coinjoins
---

![cover](assets/cover.webp)



Ashigaru Terminal er Ashigaru-teamets tilpasning av Sparrow Server, som implementerer Whirlpool coinjoin-protokollen. Denne programvaren er en videreføring av arbeidet som ble påbegynt av Samourai Wallet, spesielt på Whirlpool GUI, hvis grunnleggende prinsipper den tar i bruk: selvoppbevaring og bevaring av konfidensialitet.



Denne programvaren er en fork av Sparrow Server, modifisert og optimalisert for full integrering med Whirlpool-økosystemet, ZeroLink coinjoin-protokollen som opprinnelig ble utviklet av Samourai-teamene.



Ashigaru Terminal har et minimalistisk TUI-grensesnitt og kan installeres på en personlig datamaskin eller på en dedikert server. Den lar deg samhandle direkte med Whirlpool for å initiere "*Tx0*", administrere "*Deposit*", "*Premix*", "*Postmix*" og "*Badbank*"-kontoer, og utføre automatiske remixer for å styrke konfidensialiteten til delene dine.



Ashigaru Terminal vil kort sagt være spesielt nyttig hvis du ønsker å lage coinjoins ved hjelp av Whirlpool.



I denne første veiledningen tar jeg deg gjennom installasjon og bruk av Ashigaru Terminal. Deretter følger en mer avansert veiledning om hvordan man lager coinjoins.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef

## 1. Installer Ashigaru Terminal



For å installere Ashigaru Terminal trenger du Tor Browser, siden de binære filene kun distribueres via Tor-nettverket. Hvis du ikke allerede har gjort det, [installer det på maskinen din](https://www.torproject.org/download/).



### 1.1. Last ned Ashigaru Terminal



Fra Tor Browser kan du gå til [utgivelsessiden til Git-arkivet](http://ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/) for å laste ned den nyeste versjonen av Ashigaru Terminal for operativsystemet ditt.



```txt
ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/
```



![Image](assets/fr/01.webp)



Last ned følgende to filer for operativsystemet ditt:




- Binærfilen (`ashigaru_terminal_v1.0.0_amd64.deb` for Debian/Ubuntu, `.dmg` for macOS eller `.zip` for Windows) ;
- Den signerte hash-filen: `ashigaru_terminal_v1.0.0_signed_hashes.txt`.



### 1.2. Sjekk Ashigaru Terminal



Før du kjører programvaren på enheten din, må du sjekke ektheten og integriteten. Dette er et viktig skritt, da det forhindrer deg i å installere en falsk versjon som kan kompromittere bitcoinsene dine eller infisere maskinen din.



Åpne en ny nettleserfane og gå til [Keybase-verifiseringsverktøy](https://keybase.io/verify). Lim inn innholdet i `.txt`-filen du nettopp har lastet ned i det angitte feltet, og klikk deretter på `Verify`-knappen.



![Image](assets/fr/02.webp)



For å diversifisere bekreftelseskildene dine, kan du også sammenligne meldingen med den som er tilgjengelig på nettstedet clearnet [ashigaru.rs](https://ashigaru.rs/download/), i `/download`-delen.



![Image](assets/fr/03.webp)



Hvis signaturen er gyldig, vil Keybase vise en melding som bekrefter at filen er signert av Ashigarus utviklere.



![Image](assets/fr/04.webp)



Du kan også klikke på profilen `ashigarudev` som vises av Keybase og sjekke at deres nøkkelfingeravtrykk samsvarer nøyaktig: `A138 06B1 FA2A 676B`.



![Image](assets/fr/05.webp)



Hvis det vises en feilmelding på dette stadiet, er signaturen ugyldig. I så fall skal du **ikke installere den nedlastede programvaren**. Begynn på nytt fra begynnelsen, eller be om hjelp fra fellesskapet før du fortsetter.



Keybase har gitt deg den autentiserte hashen til applikasjonen. Vi skal nå sjekke at hashen til `.deb`-, `.zip`- eller `.dmg`-filen du har lastet ned, samsvarer med den som er validert på Keybase. For å gjøre dette går du til [HASH FILE ONLINE](https://hash-file.online/).



Klikk på knappen `BROWSE...` og velg filen `.deb`, `.zip` eller `.dmg` som du lastet ned i trinn 1.1. Velg deretter hashfunksjonen `SHA-256`, og klikk på `CALCULATE HASH` for å generate hashen for filen din.



![Image](assets/fr/06.webp)



Nettstedet vil deretter vise programvarens hash. Sammenlign den med hashen du verifiserte på Keybase.io. Hvis de to stemmer perfekt overens, har ekthets- og integritetskontrollen vært vellykket. Du kan da bruke programvaren.



![Image](assets/fr/07.webp)



### 1.3 Start Ashigaru Terminal





- Debian / Ubuntu



For å installere programvaren, kjør kommandoen :



```bash
cd ~/Downloads
sudo apt install ./ashigaru_terminal_v1.0.0_amd64.deb
```



Endre rekkefølgen i henhold til den nedlastede versjonen.



Kontroller deretter installasjonen:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal --version
```



Start deretter programvaren:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal
```





- Windows**



Høyreklikk på `.zip`-filen du har lastet ned og sjekket, og velg deretter `Extract All...` for å pakke ut innholdet.



Når utpakkingen er fullført, dobbeltklikker du på filen `Ashigaru-terminal.exe` for å starte programvaren.



![Image](assets/fr/08.webp)



## 2. Kom i gang med Ashigaru Terminal



Ashigaru Terminal er et TUI-program (*Text-based User Interface*), dvs. et minimalistisk grensesnitt som kjører direkte i terminalen. Du samhandler med det ved hjelp av menyer og tastatursnarveier, men uten noe virkelig klassisk grafisk miljø.



![Image](assets/fr/09.webp)



Det er enkelt å bruke: Bruk piltastene på tastaturet til å navigere gjennom menyene, og trykk på "Enter"-tasten for å validere en handling eller bekrefte et valg.



## 3. Koble noden din til Ashigaru Terminal



Som standard kobler Ashigaru Terminal seg til en offentlig Electrum-server. Dette innebærer selvsagt en risiko når det gjelder konfidensialitet og suverenitet. Så vi skal konfigurere den til å koble direkte til din egen Electrum Server.



Dette gjør du ved å åpne menyen `Preferences > Server`.



![Image](assets/fr/10.webp)



Klikk på knappen <Rediger>.



![Image](assets/fr/11.webp)



Velg `Private Electrum Server`, og klikk deretter på `<Fortsett>`.



![Image](assets/fr/12.webp)



Skriv inn URL-adressen og porten til serveren din. Du kan angi en Tor-adresse i `.onion`. Klikk deretter på `< Test >` for å bekrefte tilkoblingen.



![Image](assets/fr/13.webp)



Hvis tilkoblingen er vellykket, vises meldingen `Success` sammen med informasjon om serveren din.



![Image](assets/fr/14.webp)



Hvis du ennå ikke har en Bitcoin-node, anbefaler jeg at du tar dette kurset:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

*I mitt tilfelle, for denne veiledningen, kommer jeg til å koble fra Electrs-serveren min fordi jeg jobber på testnet. Operasjonen forblir imidlertid helt identisk på mainnet.*



## 4. Opprett en portefølje på Ashigaru Terminal



Nå som programvaren er riktig konfigurert, kan vi legge til en Bitcoin-portefølje.



Du har to alternativer:




- Du kan opprette en ny wallet fra bunnen av og bruke den utelukkende på Ashigaru Terminal. I så fall må du åpne denne programvaren hver gang du ønsker å samhandle med wallet;
- Alternativt kan du importere din eksisterende Ashigaru wallet direkte fra telefonen din til Ashigaru Terminal. Ulempen med denne metoden er at den reduserer sikkerheten i oppsettet ditt noe, ettersom wallet da blir eksponert for to risikable miljøer i stedet for ett. På den annen side har den fordelen at du kan la Ashigaru Terminal kjøre kontinuerlig for å blande myntene dine, samtidig som du kan bruke dem eksternt via Ashigarus mobilapp.



I denne veiledningen velger vi den andre metoden. Hvis du foretrekker å opprette en helt ny mappe, er fremgangsmåten den samme: Den eneste forskjellen er at du må lagre den nye huskeregelen og den nye passphrase under opprettelsen.



Merk også at Ashigaru Terminal ikke lar deg bruke bitcoinene dine direkte. Du kan enten synkronisere den samme lommeboken på Ashigaru Terminal og Ashigaru-appen (noe jeg skal gjøre i denne veiledningen), eller på Sparrow Wallet.



Hvis du ennå ikke har en wallet på Ashigaru-applikasjonen, kan du følge den dedikerte veiledningen :



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Gå til menyen `Lommebøker`.



![Image](assets/fr/15.webp)



Velg deretter `Opprett/gjenopprett wallet...`. Med alternativet `Åpne Wallet...` kan du få tilgang til en portefølje som allerede er lagret i Ashigaru Terminal på et senere tidspunkt.



![Image](assets/fr/16.webp)



Gi porteføljen din et navn.



![Image](assets/fr/17.webp)



Velg deretter porteføljetype `Hot Wallet`.






![Image](assets/fr/18.webp)



Det er på dette stadiet at prosedyren varierer avhengig av ditt opprinnelige valg:




- Hvis du ønsker å opprette en ny portefølje fra bunnen av, klikker du på `<Generere ny Wallet>`, definerer en passphrase BIP39, og lagrer deretter den mnemoniske frasen og din passphrase på et fysisk medium;



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



- Hvis du ønsker å bruke samme wallet som Ashigaru-applikasjonen, skriver du inn de 12 ordene i den mnemoniske frasen og passphrase BIP39 direkte i de tilsvarende feltene. Skriv ordene med små bokstaver, hele, i rekkefølge, adskilt av et mellomrom, uten tall eller ekstra tegn.



Når dette trinnet er fullført, klikker du på `< Neste >`.



*Merknad*: Hvis du ikke kan klikke på denne knappen, er minnefrasen din ugyldig. Sjekk nøye at ingen av ordene er feil eller feilstavet.



![Image](assets/fr/19.webp)



Deretter må du angi et passord. Dette brukes til å låse opp Ashigaru-terminalen wallet og beskytte den mot uautorisert fysisk tilgang. Det er ikke involvert i den kryptografiske utledningen av nøklene dine: Med andre ord, selv uten dette passordet vil hvem som helst med din mnemoniske frase og passphrase kunne gjenopprette wallet og få tilgang til bitcoinsene dine.



Velg et langt, komplekst og tilfeldig passord. Oppbevar en kopi på et trygt sted: helst på et fysisk medium eller i en sikker passordbehandler.



Klikk på `< OK >` når du er ferdig.



![Image](assets/fr/20.webp)



## 5. Bruk av porteføljen



Deretter kan du velge hvilken konto du vil ha tilgang til. For øyeblikket har vi ikke startet noen miksing, så vi bruker kontoen `Deposit`.



![Image](assets/fr/21.webp)



Betjeningen er da identisk med Sparrow, siden Ashigaru Terminal er en fork av Sparrow Server. Du finner de samme menyene:



![Image](assets/fr/22.webp)





- transaksjoner": lar deg se historikken til transaksjoner knyttet til denne kontoen. I mitt tilfelle vises noen av dem allerede, ettersom jeg hadde gjort noen med Ashigaru-applikasjonen på den samme wallet.



![Image](assets/fr/23.webp)





- receive`: genererer en ny, tom kvitteringsadresse for plassering av satss på innskuddskontoen.



![Image](assets/fr/24.webp)





- addresses`: viser en liste over alle adressene dine, enten de tilhører kontoens interne eller eksterne kjede.



![Image](assets/fr/25.webp)





- `UTXOs`: viser alle tilgjengelige UTXO-er.



![Image](assets/fr/26.webp)





- innstillinger: gir tilgang til porteføljens *deskriptor*. Du kan også se din seed, justere *Gap Limit* eller endre opprettelsesdatoen for porteføljen din.



![Image](assets/fr/27.webp)



Du vet nå hvordan du installerer og tar i bruk Ashigaru Terminal. I neste veiledning skal vi se hvordan du utfører coinjoin med denne programvaren og hvordan du administrerer midler i "*Postmix*".
https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef
