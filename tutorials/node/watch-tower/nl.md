---
name: Lightning Watchtower
description: Een Watchtower begrijpen en gebruiken op je Lightning-node
---
![cover](assets/cover.webp)



## Hoe werken Wachttorens?



Een essentieel onderdeel van het Lightning Network ecosysteem, _Watchtowers_ bieden een extra niveau van bescherming voor de Lightning-kanalen van gebruikers. Hun belangrijkste rol is het bewaken van de kanaalstatus en ingrijpen als de ene kant van het kanaal de andere probeert op te lichten.



Hoe kan een Watchtower bepalen of een kanaal gecompromitteerd is? Het ontvangt van de klant (een van de partijen in het kanaal) de informatie die nodig is om een inbreuk correct te identificeren en af te handelen. Deze informatie omvat details van de meest recente transactie, de huidige status van het kanaal en de Elements die nodig is om straftransacties te creëren. Voordat deze gegevens naar Watchtower worden verzonden, kan de klant ze versleutelen om de vertrouwelijkheid te bewaren. Dus zelfs als Watchtower de gegevens ontvangt, zal het niet in staat zijn om ze te ontsleutelen totdat er daadwerkelijk een overtreding heeft plaatsgevonden. Dit versleutelingsmechanisme beschermt de privacy van de klant en voorkomt dat Watchtower ongeautoriseerde toegang krijgt tot gevoelige informatie.



In deze tutorial bekijken we 3 manieren om een **Watchtower** te gebruiken:




- eerst de klassieke onbewerkte methode via LND,
- dan een andere benadering met Oog van Satoshi,
- en tot slot de vereenvoudigde configuratie van een Watchtower op je Lightning node gehost met Umbrel.



## 1 - Een Watchtower of een client via LND configureren



*Deze tutorial komt uit [de officiële LND documentatie] (https://github.com/lightningnetwork/LND/blob/master/docs/Watchtower.md). Er kunnen enkele wijzigingen zijn aangebracht in de originele versie



Sinds v0.7.0 ondersteunt `LND` de uitvoering van een private altruïstische Watchtower als een volledig geïntegreerd subsysteem van `LND`. Watchtowers bieden een tweede verdedigingslinie tegen kwaadwillige of onopzettelijke inbraakscenario's wanneer het knooppunt van de klant offline is of niet in staat is om te reageren op het moment van de inbraak, wat een verhoogde mate van veiligheid biedt voor kanaalfondsen.



In tegenstelling tot een _beloning wachttoren_, die een deel van de fondsen van het kanaal vraagt in ruil voor zijn dienst, geeft een _altruïstische wachttoren_ alle fondsen van het slachtoffer terug (minus On-Chain kosten) zonder een commissie te vragen. Beloningstorens zullen in een latere versie worden geactiveerd; ze bevinden zich nog in de test- en verbeteringsfase.



Bovendien kan `LND` nu worden geconfigureerd om te functioneren als een _wachttoren cliënt_, die versleutelde inbraak herstel transacties (zogenaamde "gerechtigheid transacties") opslaat van andere altruïstische wachttorens. De Watchtower slaat versleutelde blobs van vaste grootte op en kan de justitietransactie alleen ontsleutelen en publiceren nadat de overtredende partij een herroepen Commitment status heeft uitgezonden. De communicatie tussen de klant en Watchtower wordt versleuteld en geauthenticeerd met kortstondige sleutelparen, wat de mogelijkheden van Watchtower beperkt om haar klanten te volgen via langlopende referenties.



Merk op dat we ervoor gekozen hebben om in deze release een beperkte set functies te implementeren die al aanzienlijke veiligheid bieden voor LND gebruikers. Veel andere Watchtower gerelateerde functies zijn bijna voltooid of vergevorderd; we zullen ze blijven leveren zodra we ze testen en zodra ze veilig geacht worden.



opmerking: voorlopig slaan wachttorens alleen de `to_local` en `to_remote` uitvoer van herroepen verbintenissen op; het opslaan van HTLC uitvoer zal in een toekomstige versie worden ingezet, aangezien het protocol kan worden uitgebreid om aanvullende handtekeninggegevens in versleutelde blobs op te nemen._



### Een Watchtower configureren



Om een Watchtower op te zetten, moeten command-line gebruikers de optionele `watchtowerrpc` sub-server compileren, die interactie met de Watchtower toestaat via gRPC of `lncli`. Gepubliceerde binaries bevatten standaard de `watchtowerrpc` sub-server.



De minimale configuratie om Watchtower te activeren is `Watchtower.active=1`.



Je kunt de configuratie-informatie van je Watchtower opvragen met `lncli tower info` :



```shell
$  lncli tower info
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"listeners": [
"[::]:9911"
],
"uris": [
],
}
```



De volledige set van Watchtower configuratieopties is beschikbaar via `LND -h` :



```shell
$  lnd -h
...
watchtower:
--watchtower.active                                     If the watchtower should be active or not
--watchtower.towerdir=                                  Directory of the watchtower.db (default: $HOME/.lnd/data/watchtower)
--watchtower.listen=                                    Add interfaces/ports to listen for peer connections
--watchtower.externalip=                                Add interfaces/ports where the watchtower can accept peer connections
--watchtower.readtimeout=                               Duration the watchtower server will wait for messages to be received before hanging up on client connections
--watchtower.writetimeout=                              Duration the watchtower server will wait for messages to be written before hanging up on client connections
...
```



#### Luisterinterfaces



Standaard luistert de Watchtower op `:9911`, wat overeenkomt met poort `9911` op alle beschikbare interfaces. Gebruikers kunnen hun eigen luisterinterfaces definiëren via de `--Watchtower.listen=` optie. Je kunt je configuratie controleren in het `"listeners"` veld van `lncli tower info`. Als je problemen hebt om verbinding te maken met je Watchtower, controleer dan of de `<port>` open is of dat je proxy correct geconfigureerd is op een actieve Interface.



#### Externe IP-adressen



Gebruikers kunnen ook Address's externe IP specificeren met `Watchtower.externalip=`, wat de volledige URI van de Watchtower blootstelt (pubkey@host:port) via RPC of `lncli tower info` :



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
]
```



Watchtower URI's kunnen worden doorgegeven aan klanten om verbinding te maken en te gebruiken met het volgende commando:



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Als Watchtower klanten op afstand toegang moeten krijgen, zorg er dan voor dat :




- Open poort 9911 (of een poort gedefinieerd via `Watchtower.listen`).
- Gebruik een proxy om verkeer van een open poort om te leiden naar de luisterende Address van de Watchtower.



#### Tor verborgen diensten



Watchtowers ondersteunt Tor verborgen services en kan er automatisch één generate bij het opstarten met de volgende opties:



```shell
$  lnd --tor.active --tor.v3 --watchtower.active
```



De .onion Address verschijnt dan in het `"uris"` veld tijdens een `lncli tower info` query:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@bn2kxggzjysvsd5o3uqe4h7655u7v2ydhxzy7ea2fx26duaixlwuguad.onion:9911"
]
```



opmerking: de openbare sleutel van Watchtower is verschillend van de openbare sleutel van het `LND` knooppunt. Voorlopig fungeert het als een "Soft witte lijst", omdat klanten de openbare sleutel van de Watchtower moeten kennen om hem als back-up te kunnen gebruiken, in afwachting van meer geavanceerde witte lijst mechanismen. We raden aan deze publieke sleutel NIET openlijk bekend te maken, tenzij je bereid bent je Watchtower aan het hele Internet bloot te stellen._



#### Watchtower databasemap



De Watchtower database kan verplaatst worden met de `Watchtower.towerdir=` optie. Merk op dat een `/Bitcoin/Mainnet/Watchtower.db` achtervoegsel wordt toegevoegd aan het gekozen pad om databases per string te isoleren. Dus, door `Watchtower.towerdir=/path/to/towerdir` in te stellen, wordt een database geproduceerd op `/path/to/towerdir/Bitcoin/Mainnet/Watchtower.db`.



Onder Linux bevindt de standaarddatabase van Watchtower zich bijvoorbeeld op :


`/home/$USER/.LND/data/Watchtower/Bitcoin/Mainnet/Watchtower.db`



### Een Watchtower-client configureren



Om een Watchtower client te configureren, heb je twee dingen nodig:





- Activeer de Watchtower client met de `--wtclient.active` optie.



```shell
$  lnd --wtclient.active
```





- De URI van een actieve Watchtower.



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Je kunt op deze manier meerdere wachttorens configureren.



#### Tarieven voor juridische transacties



Gebruikers kunnen optioneel het tarief voor gerechtigheidstransacties instellen via de `wtclient.sweep-fee-rate` optie, die waarden in sat/byte accepteert. De standaardwaarde is 10 sat/byte, maar het is mogelijk om hogere tarieven na te streven om hogere prioriteit te krijgen tijdens piekkosten. Het wijzigen van `sweep-fee-rate` is van toepassing op alle nieuwe updates na het herstarten van daemon.



#### Toezicht



Met het `lncli wtclient` commando kunnen gebruikers nu direct communiceren met de Watchtower client om informatie over alle geregistreerde wachttorens te verkrijgen of te wijzigen.



Met `lncli wtclient tower` kun je bijvoorbeeld het aantal sessies achterhalen waarover momenteel onderhandeld wordt met de Watchtower die hierboven is toegevoegd en bepalen of deze gebruikt wordt voor back-ups dankzij het `active_session_candidate` veld.



```shell
$  lncli wtclient tower 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": []
}
```



Gebruik de `--include_sessions` optie om informatie over Watchtower sessies te verkrijgen.



```shell
$  lncli wtclient tower --include_sessions 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": [
{
"num_backups": 0,
"num_pending_backups": 0,
"max_backups": 1024,
"sweep_sat_per_vbyte": 10
}
]
}
```



Alle configuratieopties voor de Watchtower client zijn beschikbaar via `lncli wtclient -h` :



```shell
$  lncli wtclient -h
NAME:
lncli wtclient - Interact with the watchtower client.

USAGE:
lncli wtclient command [command options] [arguments...]

COMMANDS:
add     Register a watchtower to use for future sessions/backups.
remove  Remove a watchtower to prevent its use for future sessions/backups.
towers  Display information about all registered watchtowers.
tower   Display information about a specific registered watchtower.
stats   Display the session stats of the watchtower client.
policy  Display the active watchtower client policy configuration.

OPTIONS:
--help, -h  show help
```




## 2 - Je eigen oog van Satoshi installeren



*Deze tutorial is gedeeltelijk overgenomen uit een artikel op de [Summer of Bitcoin Blog] (https://blog.summerofbitcoin.org/). Er zijn wijzigingen aangebracht in de originele versie*



Het Oog van Satoshi ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos)) is een niet-depot Watchtower Lightning, conform [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Het bestaat uit twee hoofdonderdelen:





- teos**: bevat een commandoregel Interface (CLI) en de essentiële serverfuncties van Watchtower. Twee binairen - **teosd** en **teos-CLI** - worden geproduceerd wanneer deze _crate_ wordt gecompileerd.





- teos-common**: bevat gedeelde server- en client-side functionaliteit (handig voor het maken van een client).



Om Watchtower correct te draaien, moet je **bitcoind** draaien voordat je Watchtower start met het **teosd** commando. Voordat je deze twee commando's uitvoert, moet je je **Bitcoin.conf** bestand configureren. Zo doe je dat:





- Installeer Bitcoin core vanaf de broncode of download het. Plaats na het downloaden het **Bitcoin.conf** bestand in de Bitcoin core gebruikersmap. Zie deze link voor meer informatie over waar het bestand geplaatst moet worden, omdat dit afhankelijk is van het gebruikte besturingssysteem.





- Zodra de locatie is geïdentificeerd, voegt u de volgende opties toe:



```shell
# RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

# chaîne
regtest=1
```





- server**: voor RPC verzoeken





- rpcuser** en **rpcpassword**: authenticeren RPC cliënten bij de server





- regtest**: niet vereist, maar handig als je ontwikkeling plant.



De waarden voor **rpcuser** en **rpcpassword** moet je zelf kiezen. Ze moeten zonder aanhalingstekens worden geschreven. Bijvoorbeeld:



```shell
rpcuser=aniketh
rpcpassword=strongpassword
```



Als je nu **bitcoind** uitvoert, zou het knooppunt moeten starten.





- Voor het Watchtower gedeelte moet je eerst **teos** vanaf broncode installeren. Volg de instructies in deze link.





- Als **teos** met succes geïnstalleerd is op het systeem en de tests zijn uitgevoerd, kan de laatste stap genomen worden: het instellen van het **teos.toml** bestand in de teos gebruikersdirectory. Het bestand moet worden geplaatst in een map met de naam **.teos** (let op de punt) onder uw homedirectory. Bijvoorbeeld **/home//.teos** onder Linux. Als de locatie is gevonden, maak dan een **teos.toml** bestand aan en stel deze opties in overeenkomstig de wijzigingen die zijn aangebracht op **bitcoind** :



```shell
# bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>
```



Merk op dat de gebruikersnaam en het wachtwoord hier **tussen aanhalingstekens** moeten worden geschreven. Gebruikmakend van het vorige voorbeeld :



```shell
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```



Als dit gedaan is, zou je klaar moeten zijn om de Watchtower te starten. Omdat we op **regtest** draaien, zijn er waarschijnlijk geen blokken gedolven op ons Bitcoin testnetwerk, toen de Watchtower voor het eerst verbinding maakte (als dat wel zo is, is er iets mis). Watchtower bouwt een interne cache van de laatste 100 blokken van **bitcoind**; dus, bij de eerste lancering, kunt u de volgende foutmelding krijgen:



```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```



Omdat we **regtest** gebruiken, kunnen we Miner blokken door een RPC commando te geven, zonder te hoeven wachten op de mediane vertraging van 10 minuten die we op andere netwerken zien (zoals Mainnet of Testnet). Zie **bitcoin-cli** help voor details over hoe Miner blokken werkt.



![Image](assets/fr/01.webp)



Dat is alles: je hebt met succes de Watchtower uitgevoerd. Gefeliciteerd. 🎉




## 3 - Een Watchtower configureren op Umbrel



Op Umbrel is verbinding maken met een Watchtower om je Lightning-knooppunt te beschermen extreem eenvoudig, omdat alles via de grafische Interface gebeurt. Nadat je op afstand verbinding hebt gemaakt met je knooppunt, open je de toepassing "**Lightning Node**".



![Image](assets/fr/02.webp)



Klik op de drie kleine puntjes rechtsboven op de Interface en selecteer dan "**Geavanceerde instellingen**".



![Image](assets/fr/03.webp)



In het menu "**Watchtower**" zijn twee opties beschikbaar:





- Watchtower Service**: met deze optie kun je een Watchtower beheren, d.w.z. een dienst die de kanalen van andere nodes controleert op pogingen tot fraude. In het geval van een inbreuk, publiceert jouw Watchtower een transactie op de Blockchain, waardoor gebruikers hun geblokkeerde fondsen kunnen terugkrijgen. Eenmaal geactiveerd, verschijnt de URI van jouw Watchtower en kan gecommuniceerd worden naar andere nodes, zodat ze het kunnen toevoegen aan hun Watchtower client;





- Watchtower Client**: met deze optie kun je verbinding maken met externe wachttorens om je eigen kanalen te beschermen. Eenmaal geactiveerd, kun je Watchtower diensten toevoegen, waaraan je node de benodigde informatie over zijn kanalen doorgeeft. Deze wachttorens bewaken dan hun status en grijpen in bij pogingen tot fraude.



De prioriteit voor jou is natuurlijk om de *Watchtower Client* te activeren om je node te beschermen, maar ik raad je ook aan om de *Watchtower Service* te activeren om bij te dragen aan de veiligheid van andere gebruikers.



![Image](assets/fr/04.webp)



Klik dan op de Green "**Opslaan en opnieuw opstarten Node**" knop. Uw LND zal herstarten.



In hetzelfde menu vindt u ook de URI van uw Watchtower dienst, als u die geactiveerd hebt. U kunt ook de URI van een externe Watchtower toevoegen om uw kanalen te beschermen. Klik op "**ADD**" om te bevestigen.



![Image](assets/fr/05.webp)



Er zijn verschillende Watchtowers online beschikbaar. Bijvoorbeeld, [LN+ en Voltage bieden een altruïstische Watchtower](https://lightningnetwork.plus/Watchtower) waarmee je verbinding kunt maken:



```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



![Image](assets/fr/06.webp)



Een andere optie is om je Watchtower URI te Exchange-en met je mede-bitcoiners, zodat ieder de node van de ander beschermt.



Ik raad je ook aan om meerdere wachttorens in te stellen om de risico's te beperken in het geval dat een van hen onbeschikbaar wordt.



Tenslotte kun je de parameter "**Watchtower Client Sweep Fee Rate**" aanpassen. Dit definieert het maximale tarief dat u bereid bent te betalen om een Watchtower broadcast straf transactie in een blok op te nemen. Zorg ervoor dat je een voldoende hoge waarde instelt, aangepast aan de bedragen die in je kanalen zijn vergrendeld.