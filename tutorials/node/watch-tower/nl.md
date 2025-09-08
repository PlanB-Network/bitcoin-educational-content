---
name: Watch Tower
description: Een Watch Tower begrijpen en gebruiken
---

## Hoe werken wachttorens?


Watchtowers zijn een essentieel onderdeel van het Lightning Network ecosysteem en geven een extra mate van bescherming aan de bliksemkanalen van gebruikers. De belangrijkste verantwoordelijkheid is om de gezondheid van de kanalen in de gaten te houden en in te grijpen als een kanaalpartij de andere probeert op te lichten.


Hoe kan een Watchtower bepalen of een kanaal gecompromitteerd is? De Watchtower ontvangt de informatie die het nodig heeft van de klant, een van de kanaalpartijen, om een inbreuk goed te identificeren en erop te reageren. De meest recente transactiegegevens, de huidige toestand van het kanaal en de informatie die nodig is om straftransacties te creëren, zijn vaak in deze informatie opgenomen. Voordat de gegevens naar de Watchtower worden verzonden, kan de cliënt ze versleutelen om de privacy en geheimhouding te beschermen. Dit voorkomt dat de Watchtower de versleutelde gegevens kan ontsleutelen, tenzij er echt een inbreuk heeft plaatsgevonden, zelfs als hij de gegevens krijgt. De privacy van de cliënt wordt beschermd door dit versleutelingssysteem, dat ook voorkomt dat de Watchtower zonder toestemming toegang krijgt tot privégegevens.


## Hoe je je eigen Eye of Satoshi opzet en begint bij te dragen


Het Oog van Satoshi ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos?ref=blog.summerofbitcoin.org)) is een niet-custodiale Lightning Watchtower die voldoet aan [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Het heeft twee hoofdcomponenten:


1. teos: inclusief een CLI en de server-side kernfunctionaliteit van de toren. Twee binaries-teosd en teos-CLI-worden geproduceerd wanneer deze crate wordt gebouwd.

2. teos-common: Inclusief gedeelde server- en client-side functionaliteit (handig voor het maken van een client).


Om de toren succesvol te draaien, moet bitcoind draaien voordat je de toren draait met het teosd commando. Voordat je beide commando's uitvoert, moet je het Bitcoin.conf bestand instellen. Hier zijn de stappen om dit te doen:-


1. Installeer Bitcoin core vanaf de broncode of download het. Plaats na het downloaden het Bitcoin.conf bestand in de Bitcoin core gebruikersmap. Kijk op deze link voor meer informatie over waar je het bestand moet plaatsen, want het hangt af van het besturingssysteem dat je gebruikt.

2. Nadat u de plaats hebt geïdentificeerd waar het bestand moet worden gemaakt, voegt u deze opties toe:-


```
#RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

#chain
regtest=1```

- server: For RPC requests
- rpcuser and rpcpassword: RPC clients can authenticate with the server
- regtest: Not required but useful if you're planning for development.

rpcuser and rpcpassword need to be picked by you. They must be written without quotes. Eg:-

```

rpcuser=aniketh

rpcpassword=strongpassword``


Als je nu bitcoind uitvoert, zou het knooppunt moeten starten.


1. Voor het torengedeelte moet je eerst teos installeren vanaf de broncode. Volg de instructies in deze link.

2. Na het succesvol installeren van teos op je systeem en het uitvoeren van de tests, kun je verder gaan met de laatste stap, namelijk het instellen van het teos.toml bestand in de teos gebruikersmap. Het bestand moet worden geplaatst in een map met de naam .teos (let op de punt) onder je thuismap. Dat is bijvoorbeeld /home/<uw-gebruikersnaam>/.teos voor Linux. Als je de plek gevonden hebt, maak dan een teos.toml bestand aan en stel de opties in die overeenkomen met de dingen die we veranderd hebben op bitcoind.


```
#bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>```

Notice that here the username and password need to be written quoted, that is, for the same example as before:

```

btc_rpc_user = "aniketh"

btc_rpc_password = "strongpassword"```


Als je dat gedaan hebt, zou je klaar moeten zijn om de toren te laten draaien. Aangezien we op regtest draaien, is de kans groot dat er geen blokken gedolven zijn in ons Bitcoin testnetwerk als de toren voor het eerst verbinding maakt (als dat wel zo is, is er zeker iets mis). De toren bouwt een interne cache van de laatste 100 blokken van bitcoind, dus als we de toren voor de eerste keer draaien, kunnen we de volgende foutmelding krijgen:


teosd] Niet genoeg blokken om de toren te starten (vereist: 100). Minstens 100 meer_


Aangezien we op regtest draaien, kunnen we blokken mijnen door een RPC commando te geven, zonder te hoeven wachten op de 10-minuten median tijd die we gewoonlijk zien in andere netwerken (zoals Mainnet of Testnet). Bekijk de bitcoin-cli help en zoek op hoe je blokken kunt mijnen. Als je hulp nodig hebt, kun je dit artikel doornemen.


![image](assets/2.webp)


Dat is het, je hebt de toren succesvol uitgevoerd. Gefeliciteerd. 🎉