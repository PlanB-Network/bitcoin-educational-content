---
name: Coordinador Coinjoin - WabiSabi
description: Cómo configurar y ejecutar un coordinador coinjoin siguiendo el protocolo WabiSabi (utilizado en Wasabi Wallet 2.0)
---

![cover](assets/cover.webp)


---

## Introducción 👋


En esta guía para expertos te ayudaremos a configurar un coordinador coinjoin, esencialmente un servidor que reúne a personas que quieren ahorrar en tasas de transacción o aumentar su privacidad onchain en transacciones colaborativas. Dado que ya no hay un coordinador gestionado por la empresa incluido en Wasabi Wallet, los usuarios tienen que encontrar y seleccionar su propio servidor coordinador preferido. Sólo unos pocos coordinadores han aparecido pidiendo una tasa de coordinación del 0%, por lo que los desarrolladores de Wasabi Wallet han estado trabajando duro para que sea lo más fácil posible empezar a gestionar tu propio coordinador de comunidad (¡en un hardware tan pequeño como una Raspberry Pi5!). Los coordinadores actualmente activos que piden un 0% de tasa de coordinación se pueden encontrar en [LiquiSabi](https://liquisabi.com) y, lo que es más importante, en [nostr](https://github.com/Kukks/WasabiNostr).


## Requisitos 🫴



- VPS (nodo alojado) u ordenador/servidor (nodo autoalojado)
- Nodo central Bitcoin podado/completo (probado con v29.0)


Opcional:


- (sub)Dominio que reenvía el tráfico al nodo (por ejemplo, coinjoin.[sudominio].io)


Se recomienda tener algo de experiencia con la línea de comandos y bash, ya que no todos los pasos se pueden automatizar.


En cuanto al hardware, es aconsejable tener un sistema con:


- 4 núcleos
- 16 GB RAM
- 2 TB SSD o NVMe (para un nodo completo) / 128 GB SSD (para un nodo pruned)


Tales requisitos pueden ser proporcionados por una Raspberry Pi 5 por solo 120 $, excluyendo el almacenamiento que cuesta alrededor de 100 $ para un stick NVMe de 2TB.


VPS baratos suelen venir con sólo 1 núcleo y 4 GB de RAM, que he encontrado es demasiado poco para sincronizar y verificar todo el bitcoin blockchain en blockheight 911817.


En cuanto al almacenamiento, un nodo completo necesitará como mínimo 2 TB de almacenamiento en disco, preferiblemente SSD o de tipo NVMe. Cuando se poda el blockchain, es aceptable una unidad de almacenamiento mucho más pequeña (por ejemplo, un SSD de 128 GB).


Si pretende ejecutar un coordinador para coinjoins de gran tamaño (más de 300 entradas), es aconsejable elegir un sistema con núcleos más rápidos/nuevos con un mayor rendimiento para todas las verificaciones de firmas.


## Instalación 🛠️


En el nodo que queremos descargar e instalar la última versión liberada de Wasabi Wallet, que incluye un backend y coordinador como ejecutables independientes junto a la wallet.


Busca la última versión: [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) y verifica la firma PGP de la versión con las claves: [PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


Los detalles de despliegue difieren dependiendo del hardware (arquitectura CPU) y la elección del SO, a continuación se dan los diferentes detalles para una Raspberry Pi (ARM-64) con RaspiBlitz basado en Debian como punto de partida. Siga adelante para el despliegue del SO Ubuntu (X86-64) usando Nix.


Encuentre las instrucciones de instalación aquí: [Wasabi Docs](https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### Despliegue de RaspiBlitz/Debian


Para los nodos RaspiBlitz (probados con v1.11) se puede utilizar una implementación script construida a partir del código fuente: [home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### Fácil despliegue


Para un despliegue mínimo, basta con extraer los ejecutables para su plataforma en una carpeta.

Ejemplo de códigos de línea de comandos para Debian/Ubuntu:


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


El resultado debería ser el siguiente mensaje de firma válido:


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


Y puede proceder a instalar el paquete descargado:


```
sudo apt install ./Wasabi-2.7.2.deb
```



## Configuración 🧾


Antes de ejecutar el coordinador es necesario editar el archivo Config.json con su:


- Bitcoin RPC credenciales
- Parámetros de ronda preferidos
- Clave pública ampliada del coordinador (crear una nueva SegWit wallet para recibir el polvo recogido)

**Atención**: ¡Taproot wallet resultará en UTXO no gastables! Utilice un Segwit nativo wallet aquí.


- Tipos de dirección de entrada y salida permitidos
- Configuración del anunciador para publicar a través de nostr (nombre, descripción, Uri, entradas mínimas, relé nostr, clave privada nostr)


Puede ejecutar el coordinador accesible sólo a través de la dirección .onion, o utilizar su dominio clearnet personalizado.


Busca o crea el archivo de configuración en esta ruta:


`~/.walletwasabi/coordinator/Config.json`


Edítalo con el comando:


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


Vea este ejemplo Config.json:


```
{
"Network": "Main",
"MainNetBitcoinRpcUri": "http://localhost:8332",
"TestNetBitcoinRpcUri": "http://localhost:48332",
"RegTestBitcoinRpcUri": "http://localhost:18443",
"BitcoinRpcConnectionString": "your_bitcoin_rpcuser:your_bitcoin_rpcpassword",
"ConfirmationTarget": 21,
"DoSSeverity": "0.02",
"DoSMinTimeForFailedToVerify": "1d 21h 0m 0s",
"DoSMinTimeForCheating": "1d 0h 0m 0s",
"DoSPenaltyFactorForDisruptingConfirmation": 0.2,
"DoSPenaltyFactorForDisruptingSignalReadyToSign": 1.0,
"DoSPenaltyFactorForDisruptingSigning": 1.0,
"DoSPenaltyFactorForDisruptingByDoubleSpending": 3.0,
"DoSMinTimeInPrison": "0d 0h 20m 0s",
"MinRegistrableAmount": "0.000021",
"MaxRegistrableAmount": "1000.00",
"AllowNotedInputRegistration": true,
"StandardInputRegistrationTimeout": "0d 0h 21m 0s",
"BlameInputRegistrationTimeout": "0d 0h 3m 0s",
"ConnectionConfirmationTimeout": "0d 0h 1m 0s",
"OutputRegistrationTimeout": "0d 0h 1m 0s",
"TransactionSigningTimeout": "0d 0h 1m 0s",
"FailFastOutputRegistrationTimeout": "0d 0h 3m 0s",
"FailFastTransactionSigningTimeout": "0d 0h 1m 0s",
"RoundExpiryTimeout": "0d 0h 5m 0s",
"MaxInputCountByRound": 100,
"MinInputCountByRoundMultiplier": 0.21,
"MinInputCountByBlameRoundMultiplier": 0.21,
"RoundDestroyerThreshold": 375,
"CoordinatorExtPubKey": "xpub_fill_in_your_new_wallet_here",
"CoordinatorExtPubKeyCurrentDepth": 0,
"MaxSuggestedAmountBase": "100.00",
"RoundParallelization": 1,
"CoordinatorIdentifier": "CoinJoinCoordinatorIdentifier",
"AllowP2wpkhInputs": true,
"AllowP2trInputs": true,
"AllowP2wpkhOutputs": true,
"AllowP2trOutputs": true,
"AllowP2pkhOutputs": true,
"AllowP2shOutputs": true,
"AllowP2wshOutputs": true,
"DelayTransactionSigning": false,
"AnnouncerConfig": {
"CoordinatorName": "Your Coordinator Name",
"IsEnabled": true,
"CoordinatorDescription": "Privacy is a human right!",
"CoordinatorUri": "https://coinjoin.yourdomain/",
"AbsoluteMinInputCount": 21,
"ReadMoreUri": "https://coinjoin.yourdomain/",
"RelayUris": [
"wss://relay.primal.net"
],
"Key": "nsec_your_coordinator_nostr_privatekey"
},
"PublishAsOnionService": true,
"OnionServicePrivateKey": your_onion_service_private_key
}
```

### Configuración de Tor 🧅


Para rellenar tu OnionServicePrivateKey es probable que necesites generar una primero.


Wasabi Wallet generará una clave privada por ti si lo ejecutas la primera vez con ```"PublishAsOnionService": true,``` configurado en el archivo Config.json.


Ejecute el coordinador una vez con el comando


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Para ver la dirección de su servicio oculto Onion, compruebe los registros del coordinador con:


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


y encontrarás algo como:


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


La URL larga que termina en .onion es tu dirección de servicio oculta o CoordinatorUri.


O compruebe de nuevo su archivo de configuración del coordinador con:


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


Que ahora debería rellenarse automáticamente.


## Correr ⚡


Una vez establecidos todos los parámetros de configuración, puede ejecutar el servicio de coordinación y empezar a anunciar su primera ronda 🕶️


Basta con iniciar el coordinador con el comando


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Puedes monitorizar la ronda actual y el número de UTXO's/coins registrados comprobándolo (en el navegador Tor para .onion):


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### Opcional: depuración del servidor coordinador


Puede consultar cualquier problema o error en el archivo de registro ```~/.walletwasabi/backend/Logs.txt``


Los problemas típicos incluyen problemas de conexión RPC, esto tiene que ser habilitado en ```~/.bitcoin/bitcoin.conf`` con:


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### Opcional: Ejecutar el servidor backend


Junto con el coordinador también puede proporcionar un servidor backend para los usuarios que no tienen su propio nodo bitcoin para conectarse a las estimaciones de tasas y blockfilters.


Inicie este servicio con el comando:


```
wbackend
```


## Invitar a usuarios de Wasabi a tu coordinador 🫂


Para que otros usuarios encuentren tu servicio puedes apoyarte en el anunciador nostr, o compartir un enlace mágico con tu dominio (clearnet) o servicio oculto (enlace .onion) y parámetros redondos como este:


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


Cuando un usuario copie el enlace mágico y abra su Wasabi Wallet, el programa mostrará automáticamente el cuadro de diálogo del coordinador con su dominio y parámetros.


![detected](assets/en/02.webp)


💚🍣 Enhorabuena por descentralizar la privacidad de bitcoin 🕶️


Recuerda tu entrenamiento [wasabika](https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika), Wasabi Wallet es sólo para defensa 🛡️