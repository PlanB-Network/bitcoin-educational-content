---
name: Specter Desktop
description: Gestione sus carteras Bitcoin multifirma en total soberanía con su propio nodo
---

![cover](assets/cover.webp)



Specter Desktop es una aplicación de código abierto (licencia MIT) desarrollada por Cryptoadvance desde 2019 que facilita la gestión de monederos Bitcoin con sus monederos hardware (Ledger, Trezor, Coldcard, BitBox02, Passport, etc.) y su propia infraestructura Bitcoin (nodo Bitcoin Core o servidor Electrum). La aplicación destaca especialmente en configuraciones multi-firma, permitiéndole asegurar grandes sumas distribuyendo la potencia de firma entre varios monederos hardware independientes.



**En este tutorial, aprenderás a:**




- Instale y configure Specter Desktop en su ordenador (Windows, macOS o Linux)
- Conecte Specter a un servidor Electrum (utilizaremos Umbrel en este ejemplo)
- Crear una wallet sencilla con hardware wallet (Coldcard)
- Recibir y enviar bitcoins con total soberanía
- Configuración de un wallet multifirma 2 contra 3 con varios monederos físicos
- Instalar Specter en un servidor Umbrel (bonificación avanzada)



Todas sus transacciones serán validadas localmente a través de su propia infraestructura, sin transmitir ninguna información a servidores externos, garantizando su confidencialidad y soberanía financiera. Compruebe siempre las transacciones en la pantalla de su hardware wallet antes de firmar.



## Descarga e instalación



Visita el sitio web oficial de Specter Desktop para descargar la aplicación.



![Page d'accueil Specter](assets/fr/01.webp)



En la página de descarga, elija la versión correspondiente a su sistema operativo: macOS, Windows o Linux.



![Téléchargement selon l'OS](assets/fr/02.webp)



Una vez descargada, instala la aplicación siguiendo las instrucciones habituales de tu sistema operativo. Para macOS, arrastre el icono a Aplicaciones. Para Windows, ejecute el instalador. Para Linux, siga las instrucciones del paquete.



## Configuración inicial



En el primer inicio, Specter Desktop le pide que elija su tipo de conexión. Puede conectarse a un servidor Electrum o a su propio nodo Bitcoin Core.



![Choix du type de connexion](assets/fr/03.webp)



En este ejemplo, utilizaremos una conexión a un servidor Electrum que se ejecuta en Umbrel.



Para más información, consulte nuestro tutorial sobre Umbrel:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Esta opción ofrece una sincronización más rápida que Bitcoin Core. Si lo prefiere, puede seleccionar "Bitcoin Core" y configurar la conexión con su nodo local. Los pasos siguientes siguen siendo los mismos independientemente de su elección.



Seleccione "Conexión Electrum" y elija "Introducir la mía" para configurar su propio servidor Electrum.



![Configuration Electrum](assets/fr/04.webp)



Introduzca la dirección de su servidor Electrum. En nuestro caso con Umbrel, la dirección será `umbrel.local` con el puerto `50001`. Haga clic en "Conectar" para establecer la conexión.



Una vez conectado, aparece la pantalla de bienvenida, con una lista de comprobación para empezar. Ahora tienes que añadir tus monederos de hardware.



![Écran d'accueil](assets/fr/05.webp)



## Añadir hardware wallet



En el menú de la izquierda, haz clic en "Añadir dispositivo" para añadir tu hardware wallet.



Specter Desktop soporta numerosas billeteras de hardware: Trezor, Ledger, BitBox02, Coldcard, KeepKey, Keystone, Cobo Vault, y muchos otros.



Si quieres saber más, echa un vistazo a nuestros tutoriales sobre hardware wallet.



![Sélection du type de hardware wallet](assets/fr/06.webp)



Seleccione el hardware de su wallet. En este ejemplo, estamos usando una Coldcard MK4.



A continuación encontrará nuestro tutorial para este hardware wallet:



https://planb.academy/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

Para una Coldcard, es necesario exportar las claves públicas desde el hardware wallet, ya sea mediante una conexión USB o una tarjeta microSD.



![Import des clés du Coldcard](assets/fr/07.webp)



Sigue las instrucciones que se muestran para exportar las claves de tu Coldcard. Dale un nombre a tu hardware wallet (aquí "MK4 Tuto"). Una vez importadas las claves, puedes crear una wallet con una sola clave, o añadir otros monederos hardware para una wallet multifirma.



![Dispositif ajouté](assets/fr/08.webp)



## Creación de carteras



Después de añadir su hardware wallet, haga clic en "Crear wallet de clave única" para crear un wallet de clave única.



Dale un nombre a tu cartera (por ejemplo, "Wallet para tuto") y selecciona el tipo de dirección. Selecciona "Segwit" para utilizar direcciones nativas bech32 que optimizan los costes de transacción.



![Configuration du portefeuille](assets/fr/09.webp)



Una vez creada su cartera, Specter le ofrece guardar un archivo PDF de copia de seguridad que contiene toda la información pública necesaria para restaurar su cartera (descriptores, claves públicas ampliadas). Este archivo no contiene sus claves privadas.



![Sauvegarde du portefeuille](assets/fr/10.webp)



## Recibir bitcoins



Para recibir bitcoins, seleccione su wallet en el menú de la izquierda y, a continuación, haga clic en la pestaña "Recibir".



Specter genera automáticamente una nueva dirección de recepción con un código QR.



![Génération d'une adresse de réception](assets/fr/11.webp)



Puedes copiar la dirección o escanear el código QR. Comprueba siempre la dirección en la pantalla de tu hardware wallet antes de pasársela a nadie.



## Ver historial y direcciones



Una vez que hayas recibido bitcoins, puedes ver tus transacciones en la pestaña "Transacciones".



![Historique des transactions](assets/fr/12.webp)



La pestaña "Direcciones" le permite visualizar todas las direcciones generadas por su cartera, con su estado de utilización y los importes asociados.



![Liste des adresses](assets/fr/13.webp)



## Enviar bitcoins



Para enviar bitcoins, haz clic en la pestaña "Enviar". Introduzca la dirección del destinatario, la cantidad a enviar y marque las opciones avanzadas si desea seleccionar manualmente los UTXOs (control de monedas).



![Création d'une transaction](assets/fr/14.webp)



Haga clic en "Crear transacción sin firmar" para crear la transacción. A continuación, Specter le pedirá que firme la transacción con su hardware wallet.



![Signature de la transaction](assets/fr/15.webp)



Si utiliza una tarjeta Coldcard, tendrá la opción de firmar a través de USB o utilizando la tarjeta microSD (air-gapped). Confirma la transacción en la pantalla de hardware de tu wallet, comprobando cuidadosamente la dirección de destino y el importe.



Una vez firmada la transacción, puede difundirla en la red Bitcoin.



![Options de diffusion](assets/fr/16.webp)



Haga clic en "Enviar transacción" para enviar la transacción. Specter le confirmará que su transacción ha sido enviada y podrá seguir su estado en la pestaña Transacciones.



![Diffusion de la transaction](assets/fr/17.webp)



## Crear y utilizar una cartera multifirma



Una de las principales ventajas de Specter Desktop es su capacidad para simplificar la gestión de carteras multifirma. Una wallet multifirma requiere varias firmas para autorizar una transacción, eliminando así el punto único de fallo. Una configuración 2 en 3, por ejemplo, requiere dos firmas de tres carteras de hardware distintas para validar cualquier gasto.



Para crear una wallet multisig, comience añadiendo todos los monederos hardware de firma a través de "Añadir dispositivo". En este ejemplo, utilizaremos tres monederos hardware diferentes: una Coldcard MK4 (ya añadida anteriormente), un Passport y una Ledger. Esta diversificación de fabricantes refuerza la seguridad al evitar la dependencia de una única cadena de suministro o firmware.



Aquí están los enlaces a los tutoriales de Ledger y Passport:



https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Añade el Passport dando un nombre al hardware wallet (por ejemplo, "Passport multi") e importando sus claves mediante tarjeta microSD o código QR. A continuación, haz clic en "Continuar" para proseguir.



![Ajout du Passport](assets/fr/23.webp)



A continuación, añada el Ledger conectándolo vía USB y abriendo la aplicación Bitcoin en el hardware wallet. Dale un nombre (por ejemplo, "ledger multi") y haz clic en "Get via USB" y luego en "Continue" para importar sus claves públicas.



![Ajout du Ledger](assets/fr/24.webp)



Una vez que haya registrado sus tres carteras de hardware en Specter, haga clic en "Añadir wallet" y seleccione la opción "Firma múltiple" para crear una wallet de firma múltiple.



![Choix du type de wallet](assets/fr/25.webp)



Seleccione los tres monederos hardware que desea incluir en su quórum multifirma: MK4 Tuto, Passport multi y ledger multi. Haz clic en "Continuar" para pasar al siguiente paso.



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



Elija su configuración multifirma. Seleccione "Segwit" como tipo de dirección para beneficiarse de tarifas optimizadas. El parámetro "Firmas requeridas para autorizar transacciones (m de 3)" le permite definir el umbral: para una configuración 2 de 3, se requieren 2 firmas. Cada hardware wallet muestra su clave multisig correspondiente. Haga clic en "Crear wallet" para finalizar la creación.



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



Su portafolio multifirma "Multi tuto" está ahora creado. Specter recomienda inmediatamente que guarde el archivo PDF de copia de seguridad que contiene el descriptor de la cartera. Haga clic en "Guardar PDF de copia de seguridad" para descargar este archivo crítico.



![Wallet multisig créé](assets/fr/28.webp)



Specter también le permite exportar la información wallet a cada uno de sus monederos hardware mediante código QR o archivo. Esto permite a determinados monederos físicos (como Coldcard o Passport) almacenar la configuración multisig directamente en su memoria.



Para Passport, desbloquee su dispositivo y luego vaya a "Gestionar cuenta" > "Conectar Wallet" > "Specter" > "Multisig" > "Código QR", luego escanee el código QR generado por Specter. A continuación, su Passport le pedirá que escanee una dirección de recepción de su wallet para validar la configuración multisig.



Para el MK4, conéctalo a tu PC y desbloquéalo. Luego haz clic en "Guardar archivo MK4 Tuto" y guarda el archivo en tu MK4. La próxima vez que firme su hardware wallet, el MK4 utilizará este archivo para terminar de configurar el multisig.



![Export vers les hardware wallets](assets/fr/29.webp)



Para su información, puede acceder a las copias de seguridad en cualquier momento desde la pestaña "Configuración" de su cartera y, a continuación, "Exportar":



![Accès au backup PDF](assets/fr/30.webp)



El uso cotidiano sigue siendo similar al de una wallet sencilla: se generate direcciones de recepción con normalidad. Para enviar bitcoins, ve a la pestaña "Enviar", introduce la dirección del destinatario y el importe, y haz clic en "Crear transacción sin firmar".



![Création d'une transaction multisig](assets/fr/31.webp)



Specter construye una PSBT (Partially Signed Bitcoin Transaction) y muestra "Adquirida 0 de 2 firmas". Ahora debe firmar con al menos dos de sus tres carteras de hardware. Haga clic en el primer hardware wallet (por ejemplo, "MK4 Tuto") para firmar con su Coldcard, luego en el segundo (por ejemplo, "Passport multi") para obtener la segunda firma requerida.



![Signature de la transaction](assets/fr/32.webp)



Una vez obtenidas las 2 firmas requeridas (la interfaz muestra "Adquiridas 2 de 2 firmas" y "Transacción lista para enviar"), pulse "Enviar transacción" para difundir la transacción en la red Bitcoin.



![Transaction prête à être diffusée](assets/fr/33.webp)



Este enfoque multifirma es especialmente adecuado para empresas (varios directivos deben aprobar los gastos), familias (protección de una herencia multigeneracional) o particulares que gestionan grandes sumas (distribución geográfica de monederos físicos para resistir catástrofes localizadas).



### La importancia crítica de las copias de seguridad multifirma



**Nota**: la copia de seguridad de una cartera multisig es fundamentalmente diferente de la copia de seguridad de una cartera individual. Sus frases de recuperación (frases seed) por sí solas no son suficientes para restaurar una cartera multisig. También debe hacer una copia de seguridad de la **output descriptor** (output descriptor), que contiene la información de configuración de su cartera multisig.



El output descriptor incluye datos esenciales: las claves públicas extendidas (xpubs) de cada cofirmante, el umbral de firma (2 sobre 3 en nuestro ejemplo), el tipo de script utilizado (Segwit nativo, anidado o heredado) y las rutas de bypass para cada hardware wallet. Sin este descriptor, aunque tengas dos de tus tres frases de recuperación, no podrás reconstruir tu wallet ni acceder a tus bitcoins. El descriptor permite a tu software saber cómo combinar las claves públicas para generate las direcciones Bitcoin correspondientes a tus fondos.



Specter Desktop genera automáticamente un archivo PDF de copia de seguridad cuando crea su cartera multisig. Este PDF contiene el descriptor completo, las huellas digitales de cada hardware wallet y toda la información pública necesaria para la restauración. **Este archivo no contiene sus claves privadas** y por lo tanto no le permite por sí mismo gastar sus bitcoins, pero sí permite a cualquiera que acceda a él ver su historial completo de transacciones y su saldo.



Para hacer una copia de seguridad correcta de su configuración de multifirma, siga este procedimiento: después de crear su cartera, haga clic en la pestaña "Configuración", luego en "Exportar" y seleccione "Guardar copia de seguridad en PDF". Cree varias copias de este PDF: imprima al menos dos copias en papel y guarde también una copia digital cifrada. Guarde una copia del PDF con cada una de sus frases de recuperación, en lugares geográficamente separados.



Grabe sus frases de recuperación en placas metálicas ignífugas e impermeables para garantizar su longevidad. Nunca subestime la importancia de estas copias de seguridad: si pierde la carpeta `~/.specter` de su ordenador Y pierde uno de sus monederos hardware sin una copia de seguridad del descriptor, todos sus fondos se perderán irremediablemente, incluso con una configuración 2 contra 3. La redundancia multifirma protege contra la pérdida del hardware de wallet, pero sólo si ha realizado correctamente una copia de seguridad del descriptor de su wallet.



## Ventajas y limitaciones de Specter Desktop



**Ventajas**: Confidencialidad óptima con validación local completa sin servidores de terceros. Flexibilidad multifirma para configuraciones avanzadas (corporativa, familiar, individual). Amplia compatibilidad de hardware wallet con interoperabilidad total (USB y air-gapped).



**Limitaciones**: Curva de aprendizaje significativa en conceptos avanzados de Bitcoin (UTXOs, descriptores, rutas de derivación).



## Buenas prácticas



Compruebe siempre las direcciones y los importes en la pantalla wallet de su hardware antes de la validación, para protegerse contra los programas maliciosos.



Guarda las copias de seguridad en PDF separadas de tus semillas. Estos descriptores públicos pueden almacenarse en una cámara acorazada bancaria o en una nube cifrada, lo que facilita la recuperación sin exponer tus claves privadas.



Pruebe la recuperación de importes token antes de utilizar sus carteras con grandes fondos. Cree, pruebe, elimine y restaure para validar sus procedimientos.



Mantenga Specter y su firmware actualizados. Distribuya geográficamente (casa/oficina/cerca) a sus cofirmantes multi-firma para soportar desastres localizados. Utilice etiquetas descriptivas para facilitar la contabilidad y las declaraciones de impuestos.



## Bonificación: Instalación en un servidor Bitcoin (Umbrel, RaspiBlitz, Start9)



Si ya posees un servidor Bitcoin como Umbrel, RaspiBlitz, MyNode o Start9, puedes instalar Specter Desktop directamente desde su tienda de aplicaciones. Este enfoque ofrece varias ventajas significativas: la aplicación se configura automáticamente con su nodo local Bitcoin Core, sigue siendo accesible 24/7 a través de una interfaz web desde cualquier dispositivo de su red, e incluso se puede acceder de forma segura de forma remota a través de Tor. Toda su infraestructura de Bitcoin está centralizada en un único servidor dedicado, lo que simplifica la gestión y refuerza su soberanía.



### Instalación desde la Umbrel App Store



Desde la interfaz de Umbrel, ve a la App Store y busca Specter Desktop. Haz clic en "Instalar" para iniciar la instalación.



![App Store Umbrel - Specter Desktop](assets/fr/18.webp)



Una vez finalizada la instalación, abre Specter Desktop en tu Umbrel. La pantalla de bienvenida te pedirá que elijas tu tipo de conexión. Si utilizas Specter en tu Umbrel, haz clic en "Actualizar configuración" para configurar la conexión.



![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)



Seleccione "Conexión USB Specter remota" para permitir el uso de monederos hardware USB conectados a su ordenador local mientras utiliza Specter en el servidor Umbrel remoto.



![Configuration Remote Specter USB](assets/fr/20.webp)



Siga las instrucciones que se muestran para configurar el puente HWI. Debe acceder a la configuración del puente del dispositivo y añadir el dominio `http://umbrel.local:25441` a la lista blanca. Haga clic en "Actualizar" para guardar la configuración.



![HWI Bridge Settings](assets/fr/21.webp)



Si también desea utilizar sus monederos hardware USB desde su ordenador local, descargue la aplicación Specter Desktop en su máquina y configure "Sí, ejecuto Specter remotamente". Haga clic en "Guardar" para finalizar la configuración.



![Configuration connexion remote dans l'app](assets/fr/22.webp)



## Conclusión



Specter Desktop democratiza las configuraciones avanzadas de Bitcoin, haciendo accesible la multifirma sin sacrificar su soberanía o confidencialidad. Para los usuarios que gestionan cantidades importantes de dinero, transforma las prácticas institucionales en soluciones que pueden desplegar los particulares.



Aunque la aplicación requiere una inversión inicial en infraestructura y aprendizaje, ofrece una soberanía total: control de la infraestructura de validación, propiedad física de las claves y transacciones libres de la vigilancia de terceros. Tanto si eres un particular que asegura sus ahorros, una familia que crea una caja fuerte multigeneracional o una empresa que gestiona el flujo de efectivo, Specter Desktop es la herramienta de referencia para conciliar la máxima seguridad y la soberanía absoluta.



## Recursos



### Documentación oficial




- [Sitio web oficial de Specter Desktop](https://specter.solutions/desktop/)
- [Código fuente GitHub](https://github.com/cryptoadvance/specter-desktop)
- [Documentación completa](https://docs.specter.solutions/)



### Comunidad y apoyo




- [Grupo de la comunidad de Telegram Specter](https://t.me/spectersupport)
- [Foro de debate Reddit](https://reddit.com/r/specterdesktop/)
- [Informes de errores en GitHub](https://github.com/cryptoadvance/specter-desktop/issues)