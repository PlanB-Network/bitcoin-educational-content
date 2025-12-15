---
name: Joinstr
description: CoinJoins descentralizados a través de la red Nostr para la confidencialidad soberana de Bitcoin
---

![cover](assets/cover.webp)



La transparencia de la blockchain Bitcoin permite rastrear el historial de las transacciones. CoinJoins rompe estos vínculos mezclando múltiples transacciones simultáneas, restableciendo un nivel de confidencialidad comparable al del efectivo.



Sin embargo, las soluciones tradicionales dependen de un coordinador central como único punto de fallo. Wasabi y Samourai cesaron su actividad en 2024 por presiones normativas.



**Joinstr** elimina esta debilidad utilizando la red descentralizada Nostr para la coordinación. Esta aplicación de código abierto permite CoinJoins verdaderamente soberanos, en los que ninguna autoridad central puede censurar, supervisar o interrumpir el servicio.



## ¿Qué es Joinstr?



Joinstr es una herramienta de código abierto que revoluciona el enfoque de CoinJoins aprovechando el protocolo Nostr como infraestructura de coordinación. A diferencia de las soluciones centralizadas que requieren un servidor dedicado, Joinstr se basa en una red distribuida de repetidores Nostr para permitir a los participantes coordinarse directamente entre pares.



**Arquitectura descentralizada** : La red Nostr sustituye al coordinador central. Los participantes crean "pools" o se unen a ellos publicando anuncios cifrados a través de los relés Nostr. Esta información (importes, participantes, direcciones) permanece ininteligible para los relés, lo que garantiza que ninguna entidad central pueda supervisar, censurar o filtrar CoinJoins.



**Mecanismo SIGHASH_ALL|ANYONECANPAY**: Joinstr explota esta bandera de firma Bitcoin, permitiendo a cada participante firmar sólo su entrada mientras valida todas las salidas. Cada usuario genera su PSBT localmente y luego la distribuye a través de Nostr. Cada usuario genera su PSBT localmente, la firma y luego la distribuye a través de Nostr. Sus bitcoins permanecen bajo su control exclusivo hasta la firma final.



**Filosofía**: Joinstr sigue la filosofía cypherpunk de Bitcoin, con tres objetivos: **resistencia a la censura** (ninguna autoridad puede detener el servicio), **no custodia total** (conservas tus claves privadas), e **igualdad de trato** (ningún UTXO puede ser discriminado).



### Características principales



**Peñas flexibles**: A diferencia de las denominaciones fijas, cualquier usuario puede crear una peña con la cantidad exacta deseada y el número objetivo de participantes, optimizando el uso de UTXO sin divisiones artificiales.



**Tarifas transparentes**: No hay gastos de coordinación. Solo las comisiones de transacción de Bitcoin se reparten a partes iguales entre los participantes (unos miles de satoshis por persona).



**Efímero**: No se conservan datos del usuario. La información transita a través de mensajes efímeros encriptados Nostr, inmediatamente olvidados tras la transacción.



### Plataformas disponibles



Este tutorial se centra en la aplicación **Android**, la única solución actualmente estable y recomendada. Existe un plugin para Electrum pero tiene problemas de compatibilidad que lo hacen inestable. Se está desarrollando una interfaz web.



## Bitcoin Configuración del núcleo



Joinstr Android requiere una conexión a un nodo Bitcoin a través de RPC. Primero debes configurar Bitcoin Core en tu ordenador para que acepte conexiones desde tu teléfono.



**Nota**: Para más detalles sobre la configuración completa de Bitcoin Core, consulte nuestros tutoriales dedicados :



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3


### Requisitos de la red



#### Localice su dirección IP local



Su teléfono Android debe ser capaz de alcanzar su nodo Bitcoin en la red local. Encuentre la dirección IP de su ordenador:



**En macOS** :



```bash
ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print $2}' | head -n 1
```



Una alternativa sencilla:



```bash
ipconfig getifaddr en0
# or for WiFi: ipconfig getifaddr en1
```



**En Linux** :



```bash
hostname -I | awk '{print $1}'
```



**En Windows** :



```cmd
ipconfig
```



Encontrar la dirección IPv4 (formato `192.168.x.x` o `10.0.x.x`)



### Configuración RPC



#### Editar bitcoin.conf



![LOCALISATION BITCOIN.CONF](assets/fr/01.webp)



Localice su archivo `bitcoin.conf`:




- Linux**: `~/.bitcoin/bitcoin.conf
- macOS**: `~/Library/Application Support/Bitcoin/bitcoin.conf
- Windows**: `%APPDATA%\Bitcoin\bitcoin.conf`



![CONTENU BITCOIN.CONF](assets/fr/02.webp)



Abre el archivo con tu editor de texto favorito y añade esta configuración para activar el servidor RPC.



**Configuración recomendada para empezar (marcador)** :



```conf
# Enable signet (test network)
signet=1
prune=550

# Enable the RPC server
server=1
rpcbind=0.0.0.0

# Allow connections from your local network
# Adjust according to your network (192.168.x.0/24 or 10.0.x.0/24)
rpcallowip=192.168.1.0/24

# RPC Credentials (CHANGE THESE VALUES!)
rpcuser=your_username
rpcpassword=your_strong_password

# Specific signet configuration
[signet]
rpcport=38332
```



*configuración *mainnet** (para uso en producción) :



```conf
# RPC Server
server=1
rpcbind=0.0.0.0
rpcallowip=192.168.1.0/24

# RPC Credentials
rpcuser=your_username
rpcpassword=your_strong_password

# Mainnet Port
rpcport=8332
```



**Importante** :




- Signet es muy recomendable** para sus primeras pruebas: la aplicación está aún en fase de desarrollo (beta), y es posible que aún existan errores. Signet le permite probar gratuitamente, sin arriesgar fondos reales
- Sustituye "192.168.1.0/24" por la subred de tu red (por ejemplo, si tu IP es "192.168.68.57", utiliza "192.168.68.0/24")



**Seguridad**: Generar una contraseña segura :



```bash
openssl rand -base64 32
```



### Inicialización



#### Reiniciar y comprobar



1. Apagar completamente el Bitcoin Core


2. Reinícielo para aplicar la configuración




![SYNCHRONISATION BITCOIN CORE](assets/fr/03.webp)



Cuando Bitcoin Core se pone en marcha por primera vez, descarga y sincroniza la blockchain de marcadores. Esta operación es mucho más rápida que en mainnet (sólo unos minutos). Por favor, espere hasta que la sincronización se haya completado antes de continuar.



![CRÉATION DE WALLET](assets/fr/04.webp)



Una vez sincronizada, cree una nueva cartera haciendo clic en "Crear una nueva wallet". Dale un nombre explícito como `tuto_joinstr_signet`.



![WALLET CRÉÉ](assets/fr/05.webp)



Tu wallet ya está creado y listo para recibir bitcoins marcados para realizar pruebas.



#### Obtener bitcoins marcados (prueba)



Para probar Joinstr en marcadores, necesitas bitcoins de prueba gratis :



![SIGNET FAUCET](assets/fr/06.webp)



Utiliza un marcador público como :




- [signetfaucet.com](https://signetfaucet.com)
- [alt.signetfaucet.com](https://alt.signetfaucet.com)
- [bookmark257.bublina.eu.org](https://signet257.bublina.eu.org)



En Bitcoin Core, generate una nueva dirección de recepción (pestaña "Recibir"), cópiala y pégala en el formulario del grifo. Resuelve el captcha si es necesario. Recibirás bitcoins gratis marcados en cuestión de segundos.



## Aplicación Android



### Instalación



![APPLICATION ANDROID](assets/fr/07.webp)



Vaya a [gitlab.com/invincible-privacy/joinstr-kmp/-/releases](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases) para descargar la última versión APK. En su navegador Android, descargue el archivo y ábralo para iniciar la instalación. Si es necesario, tendrás que permitir la instalación desde fuentes desconocidas en la configuración de seguridad de tu teléfono.



### Configuración de la aplicación



![PERMISSIONS VPN](assets/fr/08.webp)



En el primer inicio, la aplicación Joinstr solicitará permisos para controlar la VPN integrada. Acepte ambas solicitudes de permiso: Control OpenVPN y Conexión VPN. Estos permisos son necesarios para la integración VPN, que protege la privacidad de su red.



![INTERFACE APPLICATION](assets/fr/09.webp)



La aplicación Joinstr está organizada en tres pestañas principales:




- Inicio**: Pantalla de inicio
- Pools**: Creación y gestión de pools CoinJoin
- Configuración**: Configuración de la aplicación



![CONFIGURATION SETTINGS](assets/fr/13.webp)



Configure los ajustes en la pestaña "Ajustes":



**1. Nostr Relay**: Dirección de retransmisión Nostr para la coordinación del pool




- Ejemplo: `wss://relay.damus.io`
- Otros relés recomendados: `wss://nos.lol`, `wss://relay.nostr.band`, `wss://nostr.fmt.wiz.biz`
- ⚠️ **Importante**: Todos los participantes deben utilizar el **mismo repetidor Nostr** para ver y unirse a las mismas quinielas. Si utilizas un relé diferente, no podrás ver los grupos creados en otros relés



**2. URL del nodo**: Dirección IP de su nodo Bitcoin (sin puerto)




- Formato: `http://VOTRE_IP_LOCALE`
- Example: `http://192.168.68.57`



**3. Nombre de usuario RPC** : El nombre de usuario configurado en `rpcuser=` en su bitcoin.conf




- Ejemplo: `satoshi



**4. RPC Contraseña** : La contraseña establecida en `rpcpassword=` en su bitcoin.conf



**5. Puerto RPC** : Puerto RPC en función de la red




- Mainnet** : `8332`
- Marcador**: `38332`



**6. Wallet**: Seleccione la cartera de Bitcoin Core que contiene los UTXOs a mezclar




- Ejemplo: `tuto_joinstr_signet`



**7. Puerta de enlace VPN**: Seleccione un servidor VPN de Riseup




- Ejemplo: `(París) vpn07-par.riseup.net`
- Otros disponibles: Ámsterdam, Seattle, etc.
- ⚠️ **Importante**: Todos los participantes del mismo grupo deben utilizar la **misma puerta de enlace VPN** para participar en CoinJoin. Durante la ronda de mezcla, todos los participantes deben aparecer con la misma dirección IP de salida para evitar que el análisis de red correlacione a los participantes



La aplicación Joinstr **integra de forma nativa** la VPN Riseup, simplificando la coordinación entre los participantes.



**Importante** :




- Asegúrate de que tu teléfono y tu ordenador están en la misma red WiFi local
- La conexión VPN se activará automáticamente al participar en un pool
- Haga clic en **"Guardar "** una vez que haya configurado todos los parámetros



## Uso práctico



### Crear una agrupación o unirse a ella



![CRÉATION POOL ANDROID](assets/fr/10.webp)



Tiene dos opciones para participar en un CoinJoin:



**Opción 1: Crear una nueva piscina**



Haga clic en "Crear nueva peña" en la pestaña "Peñas". Especifique la denominación en BTC (por ejemplo, 0,002 BTC) y el número deseado de participantes (mínimo 2, recomendado 3-5 para un mayor anonimato). A continuación, la aplicación espera a que otros usuarios se unan a tu pool. Una vez alcanzado el número requerido, el proceso de registro de salida comienza automáticamente, y tendrás que seleccionar tu UTXO para mezclar y hacer clic en "Registrar".



**⏱️ Importante**: Las quinielas caducan tras **10 minutos** de inactividad. Si no se alcanza el número necesario de participantes, la quiniela se cerrará automáticamente.



**Opción 2: Unirse a una agrupación existente**



En la pestaña "Ver otras agrupaciones", examine las agrupaciones disponibles creadas por otros usuarios. Seleccione un pool correspondiente a su cantidad y únase a él. Asegúrese de haber configurado el mismo relé Nostr y la misma pasarela VPN que los demás participantes (consulte la sección Configuración).



**Regla de selección de UTXO**: Su UTXO debe ser ligeramente superior a la denominación de la quiniela (entre +500 y +5000 sats de excedente).



**Ejemplo**: Para un fondo común de 0,002 BTC (200.000 sats), utilice un UTXO entre 200.500 y 205.000 sats.



![PROCESSUS COINJOIN](assets/fr/11.webp)



El proceso es **totalmente automático**: una vez registrada su entrada, la aplicación espera a que todos los participantes registren sus entradas. Una vez registradas todas las entradas, se crea la PSBT, se firma automáticamente con tus claves y se combina con las firmas de los demás participantes. Por último, la transacción completa se difunde en la red Bitcoin. Recibirá el TXID (identificador de transacción) una vez finalizada la emisión. No se requiere ninguna manipulación manual de PSBT en Android.



### Verificación on-chain



![TRANSACTION MEMPOOL](assets/fr/12.webp)



Una vez emitida la transacción, recibirás el TXID (identificador de transacción). Visualízalo en [mempool.space](https://mempool.space) o en tu navegador favorito. Para probarlo en un marcador, utiliza [mempool.space/signet](https://mempool.space/signet).



Puede observar :





- N entradas**: Una por participante (en nuestro ejemplo, 2 entradas)
- N salidas idénticas**: importe exacto de la denominación (aquí, 2 salidas de 0,00199800 BTC cada una)
- Diagrama de flujo**: mempool.space muestra visualmente la combinación de entradas y salidas
- Características** : La transacción puede identificarse como SegWit, Taproot, RBF, etc.



Como todas las salidas principales tienen la misma cantidad, es **imposible determinar cuál pertenece a quién**. Este es el principio fundamental de CoinJoin: la indistinguibilidad de las salidas.



**Exemple de transaction signet** : [404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c](https://mempool.space/signet/tx/404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c)



**Nota**: Si sus UTXOs eran superiores a la denominación del pool, tendrá salidas de divisas (excedentes). Estos UTXOs de cambio siguen siendo trazables y deben gestionarse por separado de sus salidas anonimizadas. Nunca los combine con sus salidas mixtas.



## CoinJoin paquetes de calidad y anonimato



La eficacia de una CoinJoin se mide por su **anonimato**: el número de outputs de idéntico valor producidos por la operación. Cuanto mayor sea este número, más difícil será determinar qué entrada corresponde a qué salida.



Joinstr genera actualmente pools de **2 a 5 participantes** de media. Estas cifras son inferiores a las de coordinadores centralizados tradicionales como Wasabi (50-100 participantes) o Whirlpool (5-10 participantes), pero ese es el precio de la descentralización.



💡 **Para entender en detalle los conjuntos de anonimato y su cálculo**, consulta nuestro curso completo: [Conjuntos de anonimato](https://planb.academy/fr/courses/65c138b0-4161-4958-bbe3-c12916bc959c/les-ensembles-danonymat-be1093dc-1a74-40e5-9545-2b97a7d7d431).



### Joinstr frente a otras CoinJoins



| Aspect | Wasabi | Whirlpool/Ashigaru | JoinMarket | **Joinstr** |
|--------|--------|--------------------|------------|-------------|
| **Participants par pool** | 50-100 | 5-10 | Variable (P2P) | **2-5** |
| **Coordinateur** | Centralisé (fermé 2024) | Centralisé (actif) | P2P maker/taker | **Aucun (Nostr)** |
| **Résistance à la censure** | Faible | Moyenne | Très élevée | **Très élevée** |
| **Frais de coordination** | Pourcentage | Frais d'entrée | Payés aux makers | **Aucun** |
| **Discrimination UTXO** | Oui (blacklists) | Non | Non | **Non** |

💡 **Otras soluciones activas de CoinJoin** :




- Ashigaru**: Implementación de código abierto del protocolo Whirlpool con coordinador centralizado pero desplegable de forma descentralizada. Sigue funcionando tras la toma de Samourai Wallet en 2024.
- JoinMarket**: Solución P2P descentralizada sin coordinador central, basada en un modelo de negocio maker/taker en el que los "makers" proporcionan liquidez y son remunerados por los "takers".



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

**El compromiso fundamental**: Joinstr y JoinMarket son las dos únicas soluciones sin coordinador central. JoinMarket utiliza un modelo de negocio P2P con incentivos financieros, mientras que Joinstr utiliza Nostr para una coordinación sin costes. Joinstr sacrifica el anonimato inmediato a gran escala en favor de la simplicidad (sin gestión de creador/tomador) y la ausencia total de tasas de coordinación.



**Recomendación práctica**: Para compensar los grupos más pequeños, organice varias rondas sucesivas de CoinJoin con distintos participantes. Espacia las rondas y cambia los relevos de Nostr entre cada ronda para maximizar la confidencialidad.



No dude en consultar nuestro curso completo sobre la privacidad de bitcoin para obtener más información sobre este tema:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Ventajas y limitaciones



### Destacados



**Privacidad mejorada**: La combinación del cifrado de las comunicaciones Nostr, la VPN compartida entre los participantes y el uso recomendado de Tor crea una protección multicapa difícil de eludir.



**Transparente, costes mínimos**: Sin costes de coordinación, sólo los costes de mining se reparten equitativamente entre los participantes. Ningún porcentaje recaudado por ningún operador.



### Limitaciones a tener en cuenta





- Liquidez variable**: Grupos más pequeños, pueden esperar a que los participantes se reúnan
- Proyecto en curso**: Aplicación en beta, posibles errores. Pruebe primero con pequeñas cantidades en el marcador
- Ataques sibilinos**: Posibilidad de que un adversario controle a varios participantes de la quiniela



## Buenas prácticas



**Aislamiento de UTXO**: Nunca combine un UTXO mezclado con otro sin mezclar. Utilice una cartera separada para sus resultados anonimizados.



**Imprescindible realizar varias rondas**: Realice un mínimo de 3 rondas sucesivas con distintos participantes. Variar las cantidades y los tiempos para evitar patrones. Separe las rondas varias horas.



**Protección de red**: Utilice Tor sistemáticamente además de la VPN incorporada. Genere claves Nostr efímeras para cada sesión importante.



**Progreso prudente**: Empieza a marcar con pequeñas cantidades.



## Conclusión



Joinstr representa una solución de privacidad Bitcoin verdaderamente descentralizada. Al utilizar Nostr para la coordinación, elimina la dependencia de coordinadores centrales al tiempo que preserva la soberanía del usuario.



**Para usuarios que valoran la resistencia a la censura y están dispuestos a realizar varias rondas de CoinJoin para compensar los grupos más pequeños.



En un contexto de creciente escrutinio financiero, las herramientas descentralizadas para proteger la privacidad se están convirtiendo en esenciales.



## Recursos



### Documentación oficial




- [Sitio web oficial de Joinstr](https://joinstr.xyz)
- [Documentación del usuario](https://docs.joinstr.xyz/users/using-joinstr)
- [Documentación técnica](https://docs.joinstr.xyz/overview/how-does-it-work)
- [Código fuente de GitLab](https://gitlab.com/invincible-privacy/joinstr)
- [Aplicación Android](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases)



### Tutoriales




- [Electrum plugin tutorial](https://uncensoredtech.substack.com/p/tutorial-electrum-plugin-for-joinstr) - Guía completa por Uncensored Tech



### Comunidad y apoyo




- [Telegram Joinstr Group](https://t.me/joinstr) - Soporte comunitario y rincones favoritos
- [Debate técnico sobre DelvingBitcoin](https://delvingbitcoin.org/t/who-will-run-the-coinjoin-coordinators/934)



### Herramientas adicionales




- [Bookmark Faucet](https://signetfaucet.com) - Prueba gratis Bitcoins
- [Alt Signet Faucet](https://alt.signetfaucet.com) - Alternativa Faucet
- [Mempool.space](https://mempool.space) - Block explorer con análisis de privacidad