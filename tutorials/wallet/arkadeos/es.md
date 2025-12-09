---
name: ArkadeOS
description: Guía completa de la cartera Arkade y el protocolo Ark
---

![cover](assets/cover.webp)



La red Bitcoin se enfrenta a un reto importante: la escalabilidad. Aunque la capa principal (capa 1) ofrece una seguridad y descentralización inigualables, sólo puede gestionar un número limitado de transacciones por segundo. Lightning Network ha surgido como una prometedora solución de segunda capa (capa 2), que permite pagos rápidos y de bajo coste. Sin embargo, Lightning impone sus propias limitaciones: gestión de canales, necesidad de liquidez entrante y una complejidad técnica que puede echar para atrás a los nuevos usuarios.



Este es el trasfondo de **Ark**, un nuevo protocolo de capa 2 diseñado para ofrecer una experiencia de usuario simplificada sin sacrificar la soberanía. **ArkadeOS** (o Arkade) es la primera gran implementación de este protocolo, que ofrece una cartera Bitcoin de nueva generación.



Este tutorial te guiará por el mundo de Arkade. Exploraremos cómo funciona el protocolo Ark, cómo instalar y configurar la wallet Arkade y cómo utilizarla para enviar y recibir bitcoins de forma instantánea, confidencial y sin las fricciones habituales de la Lightning Network.



## Comprender el protocolo Ark



Antes de entrar de lleno en el uso de Arkade, es esencial comprender los conceptos clave del protocolo Ark que lo impulsa. Ark no es una cadena de bloques independiente, sino un mecanismo de coordinación inteligente sobre Bitcoin.



### El concepto VTXO


En el corazón de Ark se encuentra el **VTXO** (UTXO virtual). Un VTXO es un UTXO aún no publicado en la blockchain Bitcoin: existe fuera de la cadena principal (off-chain) pero está respaldado por transacciones pre-firmadas en la blockchain.



A diferencia de un saldo en una bolsa centralizada, un VTXO te pertenece realmente. Usted posee una prueba criptográfica que le permite, en cualquier momento, reclamar los bitcoins reales correspondientes en la blockchain, incluso si el servidor Ark desaparece. Los VTXO permiten transferir valor instantáneamente entre usuarios sin esperar a las confirmaciones de bloque.



### El papel del ASP (Proveedor de Servicios Arca)


El protocolo Ark funciona según un modelo cliente-servidor. El servidor se denomina **ASP** (Ark Service Provider). El ASP desempeña el papel de conductor:




- Proporciona la liquidez necesaria para la red.
- Coordina las transacciones entre usuarios.
- Organiza "rondas" de liquidación en la cadena de bloques.



Es crucial tener en cuenta que ASP es **no custodio**. Nunca tiene sus claves privadas, ni puede robar sus fondos. Su papel es puramente técnico y logístico. Si un ASP censura sus transacciones o deja de funcionar, siempre podrá recuperar sus fondos mediante un procedimiento de salida unilateral.



### Rondas y privacidad


Las transacciones en Arca se finalizan en lotes denominados **Rondas**. Periódicamente (por ejemplo, cada pocos segundos), el ASP reúne todas las transacciones pendientes y las ancla en la blockchain Bitcoin en una única transacción optimizada.


Este mecanismo ofrece dos grandes ventajas:




- Escalabilidad**: Una sola transacción on-chain puede validar miles de pagos off-chain, lo que reduce drásticamente los costes para los usuarios.
- Confidencialidad**: Cada ronda actúa como un **CoinJoin**. Los fondos de todos los participantes se mezclan en un fondo común antes de ser redistribuidos en forma de nuevos VTXO. Esto rompe el vínculo entre emisor y receptor, lo que hace extremadamente difícil, si no imposible, que un observador externo pueda rastrear los pagos.



## Presentación de ArkadeOS



ArkadeOS es la aplicación concreta que pone el protocolo Ark a disposición del público en general. Desarrollado por Ark Labs, es un ecosistema completo compuesto por una cartera (Wallet), un servidor (Operator) y herramientas para desarrolladores.



Para el usuario final, Arkade adopta la forma de una elegante e intuitiva web wallet (PWA - Progressive Web App). Oculta la complejidad criptográfica de los VTXO y las rondas tras una interfaz familiar. Con Arkade, tienes una dirección para recibir, un botón para enviar y un historial de transacciones, como en una wallet clásica, pero con la potencia de la inmediatez y confidencialidad de Arkade.



## Instalación y configuración



Como Arkade es una Progressive Web App, es particularmente fácil de instalar, y no implica necesariamente tiendas de aplicaciones tradicionales.



### Acceso e instalación


Puedes acceder a Arkade directamente desde cualquier navegador web moderno (Chrome, Safari, Brave) en ordenador o móvil.





- Visite el sitio web oficial de la aplicación: **[arkade.money](https://arkade.money)**.



![arkade homepage](assets/fr/01.webp)



Te recibirán una serie de pantallas introductorias que te presentarán los conceptos clave de Arkade: un nuevo ecosistema para Bitcoin, la importancia de la autocustodia y las ventajas de las transacciones por lotes.



![arkade onboarding](assets/fr/02.webp)





- En Android (Chrome/Brave)** : Pulsa el menú del navegador (tres puntos) y selecciona "Instalar aplicación" o "Añadir a la pantalla de inicio".
- En iOS (Safari)**: Pulsa el botón de compartir (cuadrado con una flecha hacia arriba) y elige "En pantalla de inicio".



Una vez instalado, Arkade se inicia como una aplicación nativa, a pantalla completa y sin barra de direcciones.



### Creación de carteras


En el primer inicio, se le pedirá que configure su cartera.





- Haga clic en **"Crear nuevo Wallet"**.



![create wallet](assets/fr/03.webp)





- La wallet se crea al instante. A diferencia de los monederos Bitcoin tradicionales, **Arkade no utiliza una frase de recuperación de 12 o 24 palabras**. En su lugar, Arkade genera automáticamente una **clave privada** en formato Nostr (nsec), que se utilizará para respaldar y restaurar su wallet. Recuerde guardar esta clave inmediatamente (consulte la siguiente sección).





- Verás la pantalla "¡Tu nuevo wallet está en vivo!", confirmando que tu wallet está listo para usar. Haga clic en **"IR A CARTERA "** para acceder a la interfaz principal.



Una vez en tu wallet, accederás a la interfaz principal de Arkade. Aquí encontrará su saldo, botones para enviar y recibir fondos, y una pestaña "Apps" que da acceso a aplicaciones integradas como Boltz (intercambio Lightning), LendaSat y LendaSwap (servicios de préstamo), y Fuji Money (activos sintéticos).



![wallet interface](assets/fr/04.webp)



### Conexión a ASP


Por defecto, la cartera se configura automáticamente para conectarse al ASP oficial de Arkade Labs. Puede comprobar a qué servidor está conectado yendo a **Configuración** > **Acerca de** donde verá la dirección del servidor (actualmente `https://arkade.computer`).



En la versión actual de Arkade (Beta), no es posible modificar manualmente el servidor ASP. La aplicación se conecta automáticamente al ASP oficial de Arkade Labs. En el futuro, es posible que los usuarios puedan elegir entre diferentes ASP según sus preferencias, pero esta función aún no está disponible.



### Copia de seguridad de la clave privada


**Arkade utiliza una clave privada en formato Nostr (nsec) como método de copia de seguridad y recuperación. Para hacer una copia de seguridad de su clave privada :





- Vaya a **Configuración** desde la pantalla principal.
- Selecciona **"Copia de seguridad y privacidad "**.
- Verá su **clave privada** en formato `nsec...`. Esta larga cadena de caracteres es tu único medio de restaurar tu wallet.
- Pulsa **"COPIAR NSEC A CLIPBOARD "** para copiar tu clave privada.
- Guarda esta clave en un lugar seguro**: escríbela en papel, guárdala en un gestor de contraseñas seguro o utiliza cualquier otro método de copia de seguridad que te convenga.
- Arkade también ofrece la opción **"Activar copias de seguridad Nostr "**. Esta función utiliza el protocolo Nostr (una red descentralizada) para realizar copias de seguridad automáticas de ciertos datos de tu wallet de forma encriptada en los relés Nostr. Esto facilita la sincronización entre múltiples dispositivos y ofrece una recuperación más sencilla del estado de tu wallet.



**Importante**: Las copias de seguridad de nostr son sólo una **función de comodidad**. No sustituyen a la copia de seguridad de su clave nsec. Las copias de seguridad nostr no garantizan el almacenamiento permanente de los datos. Su clave privada nsec sigue siendo su único medio garantizado de recuperar sus fondos.



![backup private key](assets/fr/05.webp)




## Uso de Arkade



Una vez que haya configurado su wallet, estará listo para explorar las capacidades de Arkade. La interfaz está diseñada para unificar a la perfección los distintos tipos de pagos de Bitcoin (On-chain, Lightning, Ark).



### Recepción de fondos



Para financiar su cartera, pulse **"Recibir "**. Arkade ofrece tres métodos de recepción:





- Pago con Ark**: Si el remitente también utiliza Arkade, comparta su dirección Ark para realizar una transferencia instantánea, confidencial y prácticamente gratuita.
- Depósito en cadena (Embarque)**: Utilice la dirección Bitcoin (`bc1p...`) para recibir de un wallet clásico o de un intercambio. Espere confirmación (~10 min) antes de que los fondos se conviertan en VTXOs.
- Permuta Lightning**: Genera una factura Lightning y págala desde un wallet Lightning externo. Los fondos llegan al instante a través de un swap automático.



![receive amount](assets/fr/06.webp)



La pantalla de recibo muestra todas las opciones disponibles: Código QR, dirección Ark, dirección Bitcoin (BIP21) y factura Lightning. Para los pagos Lightning, mantenga la aplicación abierta durante la transacción.



![receive confirmation](assets/fr/07.webp)



### Envío de fondos



Para enviar fondos, pulsa **"Enviar "** y pega la dirección del destinatario o escanea el código QR. Arkade detecta automáticamente el tipo de pago requerido:





- Pago con Ark**: A una dirección de Arca, la transferencia es instantánea, privada y prácticamente gratuita (0 comisión SATS). No es necesario que el destinatario esté en línea.
- Pago Lightning**: Escanea una factura Lightning (`lnbc...`) y Arkade realiza automáticamente un canje. El ASP paga la factura por ti y carga tu saldo de Arkade.
- Pago en cadena**: Hacia una dirección clásica de Bitcoin (`bc1q...` o `bc1p...`), Arkade inicia una "Salida Colaborativa" que se incluirá en la siguiente ronda de on-chain.



Compruebe los detalles en la pantalla "Firmar transacción" y, a continuación, confirme con **"TAPAR PARA FIRMAR "**.



![send payment](assets/fr/08.webp)



**Limitación actual (Beta)**: Los VTXOs creados hace menos de 24 horas no pueden utilizarse para las salidas on-chain. Si se encuentra con un error, por favor espere hasta que sus VTXOs estén "maduros".



**on-chain confidencialidad de salida**: El siguiente ejemplo muestra una [transacción de salida Ark en mempool.space](https://mempool.space/fr/tx/153a70384d1c8a183c0e408e29b0a11820fd71a8bd5b4b00b12bc9b7f9decacb). Observamos una entrada distribuida a 4 salidas diferentes, como un CoinJoin. Para un observador externo, es imposible determinar qué cantidad pertenece a qué usuario.



![transaction ark mempool](assets/fr/11.webp)



## Funciones avanzadas



### Gestión de vencimientos VTXO


Una característica técnica del protocolo Ark es que los VTXO tienen una **vida útil limitada**. Esta limitación temporal es inherente al diseño del protocolo. El tiempo de expiración es configurable por cada servidor ASP; en el ASP oficial de Arkade Labs, este periodo es de unas **4 semanas (≈30 días)**.



**Esta limitación permite al servidor de Ark gestionar eficazmente la liquidez y limpiar los VTXOs de los usuarios inactivos. Tras el vencimiento, el servidor de Ark puede reclamar técnicamente los fondos restantes en el árbol de VTXO.



**Para mantener tus VTXOs activos, es necesario "refrescarlos" antes de que caduquen. El refresco consiste en participar en una nueva "ronda" en la que sus VTXO próximos a caducar se intercambian por nuevos VTXO con un nuevo periodo de validez completo (≈30 días en los ASP de Arkade Labs).



La cartera Arkade gestiona este proceso automáticamente: la aplicación supervisa constantemente el estado de sus VTXO y los actualiza automáticamente unos días antes de que caduquen. Siempre que abras la aplicación con regularidad (al menos una vez a la semana), tus VTXO se mantendrán activos automáticamente.



**Si no abre su cartera durante más de 4 semanas, sus VTXO caducarán. Sin embargo, no pierde sus fondos: conserva la posibilidad de recuperarlos mediante una **salida unilateral** (véase el apartado siguiente). Este procedimiento es más costoso y lento, pero garantiza que sus fondos sigan siendo recuperables.



La necesidad de abrir la aplicación regularmente hace de Arkade una **"Hot Wallet"** diseñada para el gasto diario, no una caja fuerte para ahorros a largo plazo. Para almacenar bitcoins sin usarlos durante largos periodos, prefiere un hardware frío wallet.



**Comprueba el estado de tus VTXOs**: Puede controlar el estado de sus VTXOs en **Configuración** > **Avanzado**. Consulta "Próxima renovación" para ver cuándo se producirá la próxima renovación automática, y "Monedas virtuales" para ver una lista detallada de todos tus VTXOs con su fecha de caducidad.



![vtxo management](assets/fr/09.webp)



### Sortie Unilatérale (Salida unilateral)



La salida unilateral es una **garantía criptográfica fundamental** del protocolo Arca que le asegura recuperar sus fondos, incluso si el ASP desaparece, censura sus transacciones o se niega a cooperar. Técnicamente, tus VTXOs son **transacciones Bitcoin pre-firmadas** que te pertenecen. En caso de emergencia absoluta, puedes difundir estas transacciones en la blockchain de Bitcoin para recuperar tus fondos sin la autorización de nadie.



**¿Cómo funciona? El proceso se desarrolla en dos etapas. Primero, el **Desbloqueo**: emites secuencialmente las transacciones pre-firmadas que componen tus VTXOs en el árbol de transacciones. A continuación, la **Finalización**: una vez que los timelocks han expirado (normalmente 24 horas), recoges tus bitcoins de una dirección estándar.



**Estado actual en Arkade**: En la versión Beta, todavía no hay un botón o una interfaz de usuario sencilla para la salida unilateral. Esta funcionalidad requiere actualmente el uso del SDK de Arkade y conocimientos técnicos de programación TypeScript.



**Aunque el procedimiento no sea accesible con sólo pulsar un botón, la garantía criptográfica está ahí. Tus VTXOs contienen transacciones pre-firmadas que te pertenecen legítimamente. Es esta garantía técnica la que hace de Arca un protocolo **no custodiable**: incluso en el peor de los casos, sus fondos siguen siendo técnicamente recuperables. En futuras versiones de Arkade se añadirá probablemente una interfaz simplificada.



## Ventajas y limitaciones



Para situar Arkade en el contexto adecuado, resumamos sus puntos fuertes y débiles actuales.



### Destacados




- Experiencia de usuario (UX)**: Sin gestión de canales, capacidad entrante ni complejas copias de seguridad de canales como con Lightning. Basta con instalar y utilizar.
- Privacidad** : La arquitectura por defecto de CoinJoin ofrece un nivel de anonimato mucho mayor que las transacciones estándar de on-chain o Lightning.
- Interoperabilidad**: Pague cualquier código QR Bitcoin (On-chain o Lightning) desde una única interfaz.



### Restricciones




- Protocolo joven**: Ark es una tecnología muy reciente. Pueden existir errores. Se aconseja no utilizar Arca para almacenar sumas cuya pérdida sería crítica.
- Dependencia del ASP**: Aunque no es custodial, el sistema depende de la disponibilidad del ASP para su fluidez. Si el ASP está fuera de línea, ya no podrá realizar transacciones instantáneas (solo emitir sus fondos on-chain).
- Sólo Hot Wallet** : La necesidad de abrir la aplicación regularmente para refrescar los VTXOs no es adecuada para el almacenamiento en frío (Cold Storage).



## Comparación: Arkade vs Rayo vs Cashu



Para comprender mejor el posicionamiento de Arkade, comparémoslo con las otras dos grandes soluciones de escalabilidad.



| Critère | Arkade (Ark) | Lightning Network | Cashu (E-cash) |
| :--- | :--- | :--- | :--- |
| **Modèle** | UTXO partagé coordonné par serveur (ASP) | Réseau P2P de canaux de paiement | Jetons aveugles émis par une banque (Mint) |
| **Custodie** | **Non-custodial** (vous avez les clés) | **Non-custodial** (vous avez les clés) | **Custodial** (le Mint a les fonds) |
| **Confidentialité** | **Élevée** (CoinJoin natif, aveugle pour le public) | **Moyenne** (Routage en oignon, mais canaux visibles) | **Très Élevée** (Aveugle même pour le Mint) |
| **Scalabilité** | Excellente (Batching massif on-chain) | Excellente (Transactions infinies off-chain) | Excellente (Simples signatures serveur) |
| **Expérience** | Simple (proche d'un wallet on-chain) | Complexe (gestion de canaux, liquidité) | Très simple (comme du cash numérique) |
| **Risque principal** | Disponibilité de l'ASP & Expiration | Gestion des canaux & Backups | Confiance dans le Mint (risque de vol) |

**Arkade** es el compromiso ideal: la sencillez y confidencialidad de Cashu, pero con la soberanía (no custodia) de Lightning.



## Apoyo y asistencia



Si encuentras algún problema o tienes alguna pregunta mientras utilizas Arkade, la aplicación ofrece varias opciones de asistencia:





- Vaya a **Configuración** > **Soporte**.
- Encontrarás varias opciones:
  - Atención al cliente**: Obtén ayuda con tu cartera, informa de errores o haz preguntas.
  - Chat seguro**: Tus conversaciones son seguras y privadas, y el historial se mantiene entre sesiones.
  - Informes de errores**: Informa de cualquier problema que encuentres, incluyendo los pasos para reproducirlo.
  - Seguimiento del progreso**: Realice un seguimiento de sus tickets de soporte y conversaciones en todo momento.



![support](assets/fr/10.webp)



El equipo de Arkade también está activo en Telegram a través del canal @arkade_os para soporte y oportunidades de integración.



## Nota importante: Aplicación en Beta



**⚠️ Arkade está actualmente en Beta Pública en el mainnet Bitcoin**. Aunque la aplicación es funcional con bitcoins reales, es importante tomar ciertas precauciones.



### Recomendaciones de uso




- Utiliza pequeñas cantidades**: Evita almacenar grandes sumas en Arkade. Utiliza esta wallet para tus gastos cotidianos y guarda tus ahorros en un hardware wallet frío.
- Posibles errores y limitaciones**: Como cualquier aplicación en desarrollo activo, Arkade puede presentar errores o comportamientos inesperados. Informe de cualquier problema a través del soporte integrado.
- Rápida evolución** : La aplicación y el protocolo se mejoran constantemente. Algunas funciones pueden cambiar o añadirse en futuras versiones.



### Limitaciones actuales conocidas




- retraso de 24 horas en VTXOs** : Los VTXOs recién creados no pueden utilizarse inmediatamente para las salidas on-chain.
- ASP único**: Todavía no es posible cambiar el servidor ASP en la aplicación.
- Salida unilateral técnica**: Aún no hay interfaz simplificada para la salida unilateral (requiere SDK).



El equipo de Arkade Labs está trabajando activamente para relajar estas limitaciones en futuras versiones.



## Conclusión



ArkadeOS representa un gran avance en el ecosistema Bitcoin. Al implantar el protocolo Ark, demuestra que es posible conciliar la sencillez de uso con los principios fundamentales de Bitcoin: no confíes, verifica.



Aunque todavía está en sus inicios, Arkade ofrece una fascinante visión de lo que podría ser el futuro de los pagos Bitcoin: instantáneos, privados y accesibles para todos sin requisitos técnicos previos. Es la herramienta perfecta para sus gastos diarios, complementando su solución de ahorro seguro (Cold Wallet).



Te animamos a que pruebes Arkade con pequeñas cantidades para descubrir por ti mismo este nuevo protocolo. El ecosistema evoluciona rápidamente y Arkade está a la vanguardia de esta innovación.



## Recursos



Para saber más, consulte los recursos oficiales:





- Sitio web de Arkade**: [arkadeos.com](https://arkadeos.com)
- Documentación**: [docs.arkadeos.com](https://docs.arkadeos.com)
- Protocolo Ark**: [ark-protocol.org](https://ark-protocol.org)
- Código fuente** : [GitHub Arkade](https://github.com/arkade-os)