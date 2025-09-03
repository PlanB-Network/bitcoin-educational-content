---
name: WireGuard
description: Configurazione di WireGuard VPN su Debian e Windows
---
![cover](assets/cover.webp)



___



*Questa esercitazione si basa su un contenuto originale di Florian BURNEL pubblicato su [IT-Connect](https://www.it-connect.fr/). Licenza [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Possono essere state apportate modifiche al testo originale



___



## I. Presentazione



In questa guida impareremo a configurare una VPN basata su WireGuard, una soluzione VPN gratuita e open-source che aumenta le prestazioni senza trascurare la sicurezza.



WireGuard è una soluzione relativamente recente, disponibile come versione stabile da marzo 2020, e ha l'onore di essere integrata direttamente nel **Kernel Linux dalla versione 5.6**. Ciò non impedisce che sia accessibile da distribuzioni Linux più vecchie che utilizzano una versione diversa del kernel. Rispetto a soluzioni come OpenVPN e IPSec, WireGuard è più semplice da usare e molto più veloce, come vedremo alla fine di questo articolo.



Alcuni punti chiave di WireGuard:





- Semplice, leggero e ultra-efficiente!
- Funzionamento solo UDP (che può essere uno svantaggio quando si attraversano alcuni firewall)
- Funziona su un modello peer-to-peer piuttosto che client-server
- Autenticazione tramite chiave Exchange, sullo stesso principio di SSH con chiavi private/pubbliche
- Utilizzo di diversi algoritmi: crittografia simmetrica con ChaCha20, autenticazione dei messaggi con Poly1305 e altri come Curve25519, BLAKE2 e SipHash24
- Supporta sia IPv4 che IPv6
- Multipiattaforma: Windows, Linux, BSD, macOS, Android, iOS, OpenWRT (e implementato in ProtonVPN)
- Solo 4.000 linee di codice, rispetto alle centinaia di migliaia di altre soluzioni



Per quanto riguarda la parte crittografica, i vari algoritmi utilizzati sono selezionati a mano, sottoposti a diversi controlli ed esaminati da ricercatori di sicurezza specializzati nel settore.



Il sito web ufficiale del progetto: [wireguard.com](https://www.wireguard.com/)



Siete convinti di questa soluzione dopo aver letto questa introduzione? Non resta che continuare a leggere!



## II. Schema WireGuard del laboratorio



Prima di presentare il mio laboratorio per la configurazione di WireGuard, è bene sapere che si può immaginare di **utilizzare WireGuard per interconnettere due infrastrutture remote**, ma anche per **collegare un client remoto a un'infrastruttura come una rete aziendale o la propria rete domestica**. Questo è lo stesso spirito di OpenVPN, come abbiamo visto di recente nell'esercitazione "[OpenVPN su Synology](https://www.it-connect.fr/tuto-vpn-configurer-openvpn-server-sur-un-nas-synology/)".



Se WireGuard non è impostato direttamente sul router o sul firewall, come è possibile con OpenWRT, è necessario impostare il port forwarding in modo che il flusso raggiunga la coppia WireGuard.



![Image](assets/fr/034.webp)



Ora vi parlerò del mio laboratorio e di ciò che organizzeremo oggi.



Utilizzerò una macchina Debian 11 come server WireGuard e un client Windows come client VPN WireGuard. Anche se è un po' fuorviante parlare di una relazione client-server, perché **WireGuard funziona su un modello "peer-to-peer "**. È un po' un termine improprio quando si cerca di impostare una connessione "client-to-site". Diciamo invece che avrò due coppie o **due punti di connessione WireGuard** se preferite: uno sotto Debian 11 e l'altro sotto Windows.



Queste due coppie possono comunicare tra loro in entrambe le direzioni, il che significa che dalla mia macchina Windows posso accedere alla LAN remota della macchina Debian 11 e viceversa: tutto dipende dalla configurazione del tunnel e del firewall del peer WireGuard.



In questo esempio, mi concentrerò sul caso seguente: **dal mio Windows Peer 1 collegato alla rete domestica, voglio accedere alla rete aziendale per accedere ai server della società tramite il tunnel VPN WireGuard**. Si ottiene il seguente diagramma:



![Image](assets/fr/035.webp)



In termini di indirizzi IP, questo dà:





- Rete domestica**: 192.168.1.0/24
- Rete aziendale**: 192.168.100.0/24
- Rete tunnel WireGuard**: 192.168.110.0/24


+ IP Address del Peer 1 (Windows) nel tunnel: 192.168.110.2/24


+ IP Address del Peer 2 (Debian) nel tunnel: 192.168.110.121/24



Questo è tutto! Passiamo alla configurazione!



**Nota: per impostazione predefinita, WireGuard opera in modalità UDP sulla **porta 51820**.



## III Installazione e configurazione del server WireGuard



In questa guida utilizzerò i termini "client" per la macchina Windows e "server" per la macchina Debian, perché anche se si tratta di un sistema peer-to-peer, sembra più significativo.



### A. Installazione di WireGuard su Debian 11



Il pacchetto di installazione di WireGuard è disponibile nei repository ufficiali di Debian 11, quindi tutto ciò che dobbiamo fare è aggiornare la cache dei pacchetti e installarlo:



```
sudo apt-get update
```



```
sudo apt-get install wireguard
```



![Image](assets/fr/022.webp)



Verrà installata la parte server di WireGuard, insieme a vari strumenti che danno accesso a comandi utili per la gestione della configurazione.



### B. Installazione di un WireGuard Interface



Utilizzando il **comando "wg "** è necessario creare una chiave privata e una chiave pubblica: essenziali per l'autenticazione tra due coppie, ovvero il server e un client (che avrà anch'esso bisogno di una coppia di chiavi).



Creeremo la chiave privata "**/etc/wireguard/wg-private.key**" e la chiave pubblica "**/etc/wireguard/wg-public.key**" con questa sequenza di comandi:



```
wg genkey | sudo tee /etc/wireguard/wg-private.key | wg pubkey | sudo tee /etc/wireguard/wg-public.key
```



![Image](assets/fr/023.webp)



Il valore della chiave pubblica verrà restituito nella console. Nel file di configurazione di WireGuard, dobbiamo **aggiungere il valore della nostra chiave privata**. Per recuperare questo valore, inserire il comando seguente e copiare il valore:



```
sudo cat /etc/wireguard/wg-private.key
```



È il momento di creare un file di configurazione in "**/etc/wireguard/**". Ad esempio, possiamo nominare questo file "**wg0.conf**", se pensiamo che la rete Interface associata a WireGuard sarà "wg0", sullo stesso principio di "eth0", ad esempio.



```
sudo nano /etc/wireguard/wg0.conf
```



In questo file, dobbiamo prima aggiungere il seguente contenuto (torneremo a completarlo in seguito):



```
[Interface]
Address = 192.168.110.121/24
SaveConfig = true
ListenPort = 51820
PrivateKey = <clé privée du serveur>
```



La sezione `[Interface]` è usata per dichiarare la parte server. Ecco alcune informazioni:





- Address**: l'IP Address del Interface WireGuard all'interno del tunnel VPN (subnet diversa da quella della LAN remota)
- SaveConfig**: la configurazione viene memorizzata (e protetta) per tutto il tempo in cui il Interface è attivo
- ListenPort**: Porta di ascolto di WireGuard. In questo caso, 51820 è la porta predefinita, ma è possibile personalizzarla
- PrivateKey**: il valore della chiave privata del nostro server (*wg-private.key*)



Salvare il file e chiuderlo. Con il comando "**wg-quick**", possiamo avviare questo Interface specificandone il nome (wg0, poiché il file si chiama wg0.conf):



```
sudo wg-quick up wg0
```



Se si elencano gli indirizzi IP del server Debian 11, si vedrà un nuovo Interface chiamato "wg0" con l'IP Address definito nel file di configurazione:



```
ip a
```



![Image](assets/fr/027.webp)



Nello stesso spirito, possiamo visualizzare la configurazione del Interface "wg0" con il comando "wg show":



```
sudo wg show wg0
```



![Image](assets/fr/024.webp)



Infine, dobbiamo attivare l'avvio automatico del nostro Interface wg0 WireGuard:



```
sudo systemctl enable wg-quick@wg0.service
```



Per il momento, lasceremo da parte la configurazione del lato server di WireGuard.



### C. Abilitare l'inoltro IP



Affinché la nostra macchina Debian 11 sia in grado di **indirizzare i pacchetti tra reti diverse (come un router)**, cioè tra la rete VPN e la rete locale, è necessario abilitare [IP Forwarding] (https://www.it-connect.fr/activer-lip-forwarding-sous-linux-ipv4ipv6/). Per impostazione predefinita, questa funzione è disabilitata.



Modificare questo file di configurazione:



```
sudo nano /etc/sysctl.conf
```



Aggiungere la seguente direttiva alla fine del file e salvare:



```
net.ipv4.ip_forward = 1
```



Non c'è altro da aggiungere.



### D. Abilitare la mascheratura IP



Affinché il nostro server instradi correttamente i pacchetti e la LAN remota sia accessibile alla macchina Windows, dobbiamo attivare IP Masquerade sul nostro server Debian. Si tratta di una sorta di attivazione del NAT. Eseguirò questa configurazione sul firewall Linux tramite UFW, che sono abituato a usare ([tutorial ufw su Debian](https://www.it-connect.fr/configurer-un-pare-feu-local-sous-debian-11-avec-ufw/)).



Se non avete già UFW e volete configurarlo (potete anche usare Nftables), iniziate installando:



```
sudo apt install ufw
```



Prima di tutto, è necessario abilitare SSH per non perdere il controllo del server remoto (adattare il numero di porta):



```
sudo ufw allow 22/tcp
```



Anche la porta 51820 in UDP deve essere autorizzata, poiché la utilizziamo per WireGuard (anche in questo caso, adattare il numero di porta):



```
sudo ufw allow 51820/udp
```



Continueremo poi con la configurazione per abilitare la mascheratura IP. A tale scopo, è necessario recuperare il nome del Interface collegato alla rete locale. Se non si conosce il nome, eseguire "ip a" per vedere il nome della scheda. Nel mio caso, si tratta della scheda "**ens192**".



![Image](assets/fr/036.webp)



Utilizzeremo queste informazioni. Modificare il seguente file:



```
sudo nano /etc/ufw/before.rules
```



Aggiungere queste righe alla fine del file per **abilitare la mascheratura IP sul Interface ens192** (adattare il nome del Interface) all'interno della stringa POSTROUTING della tabella NAT del firewall locale:



```
# NAT - IP masquerade
*nat
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING -o ens192 -j MASQUERADE

# End each table with the 'COMMIT' line or these rules won't be processed
COMMIT
```



L'immagine mostra:



![Image](assets/fr/037.webp)



Mantenere aperto questo file di configurazione e procedere al passo successivo. 😉



### E. Configurazione del firewall Linux per WireGuard



Sempre nello stesso file di configurazione, dichiareremo la rete aziendale "192.168.100.0/24" in modo da poterla contattare. Ecco le due regole da aggiungere (idealmente dopo la sezione "*# ok icmp code for FORWARD*" per raggruppare le regole):



```
# autoriser le forwarding pour le réseau distant de confiance (+ le réseau du VPN)
-A ufw-before-forward -s 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -s 192.168.110.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.110.0/24 -j ACCEPT
```



Se si desidera autorizzare un solo host, ad esempio "192.168.100.11", è facile:



```
-A ufw-before-forward -s 192.168.100.11/32 -j ACCEPT
-A ufw-before-forward -d 192.168.100.11/32 -j ACCEPT
```



Ora è possibile salvare il file e chiuderlo. Non resta che attivare UFW e riavviare il servizio per applicare le modifiche:



```
sudo ufw enable
```



```
sudo systemctl restart ufw
```



La prima parte della configurazione del server Debian è ora completa.



## IV. Client WireGuard per Windows



Il client WireGuard è disponibile per Windows, macOS, Android, ecc... Questa è un'ottima notizia. Tutti i download sono disponibili su questa pagina: [Client WireGuard](https://www.wireguard.com/install/). In questo esempio, imposterò il client su Windows. Per configurare il client WireGuard su Linux, seguire lo stesso principio della creazione del file wg0.conf sulla macchina Debian (senza tutti i NAT, ecc.).



### A. Installazione del client WireGuard per Windows



Una volta scaricato l'eseguibile o il pacchetto MSI, l'installazione è semplice: è sufficiente lanciare il programma di installazione e... voilà, è fatta! 🙂



![Image](assets/fr/038.webp)



### B. Creare un profilo WireGuard



Iniziare ad aprire il software per creare un nuovo tunnel. A tal fine, fare clic sulla freccia a destra del pulsante "**Aggiungi tunnel**" e fare clic sul pulsante "**Aggiungi tunnel vuoto**".



![Image](assets/fr/028.webp)



Si aprirà una finestra di configurazione. Ogni volta che viene creata una nuova configurazione di tunnel, WireGuard genera una coppia di chiavi private/pubbliche specifica per questa configurazione. **In questa configurazione, è necessario dichiarare il "peer", ovvero il server remoto:



```
[Interface]
PrivateKey = <la clé privée du PC>
```



Dobbiamo completare questa configurazione, in particolare dichiarare l'IP Address su questo Interface (*Address*), ma anche dichiarare il server WireGuard remoto tramite un blocco [Peer]. L'immagine sottostante dovrebbe ricordare il file di configurazione creato sul lato server Linux.



Iniziamo con il blocco `[Interface]`, aggiungendo l'IP Address "**192.168.110.2**"; ricordiamo che il server ha l'IP Address "**192.168.110.121**" su questo segmento di rete. In questo modo si ottiene:



```
[Interface]
PrivateKey = <la clé privée du PC>
Address = 192.168.110.2/24
```



Successivamente, occorre dichiarare il blocco "Peer" con tre proprietà, ottenendo questa configurazione:



```
[Peer]
PublicKey = 1D/Gf5yd3hUDoFyYQ3P1zayBHUJhJZq+k6Sv03HnJCQ=
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
Endpoint = <ip-serveur-debian>:51820
```



In immagini:



![Image](assets/fr/029.webp)



**Alcune spiegazioni sul blocco [Peer]:





- PublicKey**: è la chiave pubblica del server WireGuard Debian 11 (si può ottenere con il comando "*sudo wg*")
- AllowedIPs**: sono gli indirizzi IP/sottoreti accessibili tramite questa rete WireGuard VPN, in questo caso la sottorete specifica della mia WireGuard VPN (*192.168.110.0/24*) e della mia LAN remota (*192.168.100.0/24*)
- Endpoint**: è l'IP Address dell'host Debian 11, poiché è il punto di connessione di WireGuard (è necessario specificare l'IP pubblico Address)



Infine, inserire un nome nel campo "**Nome**" (senza spazi) e copiare e incollare la chiave pubblica del client, che dovrà essere dichiarata sul server. Fare clic su "**Registro**".



### C. Dichiarare il client sul server WireGuard



È ora di tornare al server Debian per dichiarare il "**Peer**", cioè il nostro PC Windows, nella configurazione di WireGuard. Prima di tutto, dobbiamo **arrestare il Interface "wg0"** per modificarne la configurazione:



```
sudo wg-quick down wg0
# ou
sudo wg-quick down /etc/wireguard/wg0.conf
```



Successivamente, modificare il file di configurazione creato in precedenza:



```
sudo nano /etc/wireguard/wg0.conf
```



In questo file, dopo il blocco `[Interface]`, dobbiamo dichiarare un blocco `[Peer]`:



```
[Peer]
PublicKey = 0i2Pg8nwDW2j7yOG09ZXht18o8l8Erb9Y5F4xyAyQV8=
AllowedIPs = 192.168.110.2/32
```



Questo blocco [Peer] contiene la chiave pubblica del PC Windows 10 (**PublicKey**) e l'IP Address del Interface del PC (**AllowedIPs**): il server comunicherà in questo tunnel WireGuard solo per contattare il client Windows, da cui il valore "**192.168.110.2/32**".



Non resta che salvare il file (*CTRL+O poi Invio poi CTRL+X via Nano*). Rilanciare il Interface "wg0":



```
sudo wg-quick up wg0
# ou
sudo wg-quick up /etc/wireguard/wg0.conf
```



Per verificare che la dichiarazione peer funzioni, si può usare questo comando:



```
sudo wg show
```



Una volta che l'host remoto ha impostato la sua connessione WireGuard, il suo IP Address verrà spostato sul valore "endpoint".



![Image](assets/fr/033.webp)



Infine, proteggeremo i file di configurazione per limitare l'accesso di root:



```
sudo chmod 600 /etc/wireguard/ -R
```



### D. Prima connessione WireGuard



Ora che la configurazione è pronta, possiamo avviarla dal PC Windows. A tal fine, nel client "**WireGuard**", fare clic sul pulsante "**Attiva**": la connessione passerà da "Off" a "On "**, ma ciò non significa che funzionerà. Tutto dipende dalla correttezza o meno della configurazione. **Quando la connessione è stabilita, le due macchine comunicano attraverso il Interface WireGuard configurato su ciascun lato!



![Image](assets/fr/030.webp)



In caso di problemi, questi saranno visibili nella scheda "**Logbook**". I due host invieranno regolarmente pacchetti Exchange per controllare lo stato della connessione, da cui i messaggi "*Receiving keepalive packet from peer 1*".



![Image](assets/fr/031.webp)



Se la scheda "**Journal**" di WireGuard visualizza un messaggio come quello riportato di seguito, è necessario verificare che le chiavi pubbliche dichiarate da entrambe le parti siano corrette.



```
Handshake for peer 1 (<ip>:51820) did not complete after 5 seconds, retrying (try 2)
```



Dal mio PC remoto, posso eseguire il ping dell'IP Address del mio Interface WireGuard sul lato server, nonché di un host sulla mia LAN remota.



![Image](assets/fr/032.webp)



### E. Prestazioni: OpenVPN vs WireGuard



Dal mio PC remoto connesso alla mia VPN WireGuard, ho potuto accedere a un file server e trasferire un file tramite [SMB](https://www.it-connect.fr/le-protocole-smb-pour-les-debutants/), per vedere la velocità di trasferimento. **Con WireGuard, la velocità massima è di circa 45 Mb/s, il che è ottimo, dato che sono in WiFi



![Image](assets/fr/025.webp)



Nelle stesse condizioni, ma questa volta tramite una connessione OpenVPN (in UDP), con lo stesso funzionamento, il throughput è totalmente diverso: circa 3 MB/s. La differenza è evidente!



![Image](assets/fr/026.webp)



Questo è interessante, perché se, ad esempio, si passa da una connessione WiFi a una connessione 4G/5G, la riconnessione sarà così veloce che l'interruzione non sarà visibile.



### F. Bonus: tunnel completo WireGuard



Con la configurazione attuale, parte del traffico passa attraverso la VPN e il resto attraverso la connessione Internet del cliente, compresa la navigazione in Internet. Se vogliamo passare a WireGuard in **modo tunnel completo**, in modo che tutto passi attraverso il tunnel VPN, dobbiamo apportare alcune modifiche alla nostra configurazione....



Per prima cosa, è necessario installare il pacchetto "resolvconf" sul file:



```
sudo apt-get update
sudo apt-get install resolvconf
```



Una volta fatto questo, è necessario modificare il profilo "wg0.conf" sulla macchina Debian: fermare Interface, modificarlo e riavviare.



```
sudo wg-quick down /etc/wireguard/wg0.conf
```



Quindi, **nel blocco `[Interface]`, si aggiunge il server DNS da usare**. Nel mio caso, si tratta del controller di dominio del mio laboratorio, ma si potrebbe anche installare Bind9 sulla macchina Debian per avere un resolver locale.



```
DNS = 192.168.100.11
```



Salvare il file, quindi riavviare Interface:



```
sudo wg-quick up /etc/wireguard/wg0.conf
```



Infine, nella configurazione del tunnel sulla workstation Windows 10, è necessario modificare la sezione "AllowedIPs" per indicare che tutto deve passare attraverso il tunnel. Sostituire:



```
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
```



Di:



```
AllowedIPs = 0.0.0.0/0
```



Si può notare che in questo modo si attiva anche l'opzione "**Commutatore di morte*".



![Image](assets/fr/040.webp)



Infine, ho approfittato della galleria piena per eseguire un piccolo test di portata, i cui risultati sono riportati di seguito:



![Image](assets/fr/039.webp)



La configurazione di WireGuard è piuttosto semplice e facile da capire, e soprattutto da mantenere. **WireGuard è considerato il futuro delle VPN**, quindi è meglio tenerlo d'occhio! Possiamo anche notare che il vantaggio è significativo in termini di prestazioni, il che rappresenta un enorme vantaggio per WireGuard rispetto a OpenVPN.



Documentazione aggiuntiva:





- [Uomo - Comando wg](https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8)
- [Uomo - Comando wg-quick](https://manpages.debian.org/unstable/wireguard-tools/wg-quick.8.en.html)



**La vostra VPN WireGuard è attiva e funzionante! Congratulazioni!