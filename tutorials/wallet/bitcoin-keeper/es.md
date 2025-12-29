---
name: Bitcoin Keeper
description: Bitcoin móvil wallet para la seguridad y multi-sig
---

![cover](assets/cover.webp)



La gestión segura de bitcoins representa un reto importante para cualquier poseedor consciente de lo que está en juego en materia de soberanía financiera. Entre la sencillez de una wallet móvil y la solidez de una solución multi-sig, la brecha técnica puede parecer desalentadora para muchos usuarios. Bitcoin Keeper se sitúa precisamente en esta intersección, ofreciendo un enfoque progresivo de la seguridad que acompaña a los usuarios en su evolución.



Bitcoin Keeper es una aplicación móvil de código abierto, dedicada exclusivamente a Bitcoin, desarrollada por el equipo de BitHyve. Su ambición es hacer accesible la gestión avanzada de carteras, especialmente las configuraciones multifirma, manteniendo al mismo tiempo una interfaz intuitiva para los principiantes. La aplicación adopta el lema "Secure today, Plan for tomorrow", que refleja su filosofía de apoyo a largo plazo.



A diferencia de los monederos generalistas que gestionan múltiples criptomonedas, Bitcoin Keeper mantiene un enfoque estricto en Bitcoin. Este enfoque exclusivo para bitcoin reduce la superficie potencial de ataque y simplifica enormemente la experiencia del usuario. La aplicación también destaca por su integración nativa de los monederos hardware más extendidos y sus avanzadas funciones de gestión de UTXO.



## ¿Qué es la Bitcoin Keeper?



### Filosofía y objetivos



Bitcoin Keeper se diseñó para satisfacer las necesidades específicas de los bitcoiners que desean conservar el control total de sus claves privadas. El proyecto adopta plenamente los principios fundamentales de Bitcoin: código fuente abierto y auditable, respeto a la privacidad y soberanía del usuario. No es necesario registrarse ni proporcionar información personal para utilizar la aplicación, que incluso puede ejecutarse sin conexión para operaciones de firma.



El objetivo central es ofrecer una herramienta flexible y preparada para el futuro que permita almacenar BTC durante varios años, e incluso varias generaciones, gracias a las funcionalidades heredadas. La aplicación permite a los usuarios empezar simplemente con un wallet móvil, y luego evolucionar gradualmente hacia soluciones multifirma más seguras.



### Arquitectura de aplicaciones



Bitcoin Keeper organiza la gestión de fondos en torno a dos conceptos distintos. La **Hot Wallet** es una wallet sencilla de una sola llave, almacenada en el teléfono, diseñada para gastos cotidianos y cantidades modestas. Las cámaras acorazadas** son cajas fuertes multifirma (multi-llave) que requieren varias llaves para autorizar un gasto, diseñadas para el almacenamiento seguro a largo plazo.



### Características principales



Bitcoin Keeper soporta casi todos los monederos hardware del mercado: Coldcard, Trezor, Ledger, Keystone, BitBox02, Jade, Seedsigner, Passport y Tapsigner de Coinkite. La integración se realiza a través de diferentes métodos en función del dispositivo: Escaneado de códigos QR, conexión NFC o importación de archivos.



La aplicación también ofrece gestión avanzada de UTXO con etiquetado de transacciones, control de monedas para seleccionar manualmente las entradas al enviar y compatibilidad con el formato PSBT para transacciones parcialmente firmadas.



## Instalación y configuración inicial



Bitcoin Keeper está disponible gratis en Android a través de Google Play Store y en iOS a través de App Store. El editor que aparece es BitHyve. Antes de instalarla, asegúrate de que tu dispositivo no tiene malware, está actualizado y no está rooteado ni tiene jailbreak.



En el primer inicio, la aplicación le pide que cree un código PIN de seguridad. Este código protege el acceso a tu wallet y cifra los datos sensibles localmente. Elija un código seguro y memorícelo. A continuación, puede activar la autenticación biométrica (huella dactilar o Face ID) para un desbloqueo más rápido.



![Installation et configuration du PIN](assets/fr/01.webp)



A continuación, la aplicación presenta varias pantallas introductorias que explican sus tres pilares: Creación de wallet para enviar y recibir bitcoins, gestión de claves con compatibilidad con hardware wallet y planificación de legados para transmitir bitcoins. Pulsa "Empezar" y elige "Empezar de nuevo" para crear una nueva configuración.



![Écrans d'introduction](assets/fr/02.webp)



## Descubrir la interfaz



La interfaz de Bitcoin Keeper se organiza en torno a cuatro pestañas principales accesibles desde la barra de navegación inferior:



![Les quatre onglets de l'application](assets/fr/03.webp)



La pestaña **Monederos** muestra tus monederos y sus saldos. Aquí es donde accedes a tus monederos para enviar y recibir bitcoins. Las etiquetas "Hot Wallet" y "Single-Key" o "Multi-Key" te permiten identificar rápidamente el tipo de cada wallet.



La pestaña **Llaves** centraliza la gestión de tus claves de firma. Aquí encontrarás la Clave Móvil generada por la aplicación, así como todas las claves importadas desde monederos hardware. Aquí es también donde añades nuevos dispositivos de firma.



La pestaña **Concierge** ofrece servicios de asistencia: envíe preguntas al equipo de asistencia y conecte con los asesores de Bitcoin para obtener ayuda personalizada.



La pestaña **Más** (Más opciones) da acceso a ajustes como la conexión al servidor personal, la copia de seguridad de claves, los documentos heredados, las preferencias de visualización y la gestión de wallet.



## Conexión a su propio servidor



Para reforzar su confidencialidad, Bitcoin Keeper le permite conectar la aplicación a su propio servidor Electrum, en lugar de utilizar los servidores públicos predeterminados.



![Configuration du serveur Electrum](assets/fr/04.webp)



En la pestaña Más, desplácese hacia abajo hasta encontrar la configuración del servidor. Pulsa "Añadir servidor" para configurar una nueva conexión. Puedes elegir entre "Servidor público" (servidores públicos preconfigurados) y "Electrum privado" (tu propio servidor).



Para un servidor privado, introduzca la URL (por ejemplo, umbrel.local para un nodo Umbrel) y el número de puerto (normalmente 50001). Active SSL si su servidor lo admite. También puedes escanear un código QR de configuración. Una vez introducidos los parámetros, pulse "Conectar con el servidor".



Si aún no tiene su propio nudo Bitcoin, eche un vistazo a nuestro tutorial sobre Umbrel, una forma sencilla y asequible de hacer su propio nudo:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Recibir bitcoins



En la pestaña Billeteras, seleccione la wallet de la que desea recibir fondos pulsándola. La pantalla wallet muestra el saldo y tres botones de acción: Enviar Bitcoin, Recibir Bitcoin y Ver todas las monedas.



![Réception de bitcoins](assets/fr/05.webp)



Pulse "Recibir Bitcoin". Bitcoin Keeper genera una nueva dirección de recepción en formato Bech32 (empezando por bc1...), junto con su código QR. Puede añadir una etiqueta a esta dirección para identificar el origen de los fondos. Comparta la dirección con el remitente mostrando el código QR o copiando la dirección de texto.



La aplicación genera automáticamente una nueva dirección para cada recepción, preservando su privacidad. Utilice "Obtener nuevo Address" para obtener una dirección en blanco si es necesario.



## Gestión de UTXO



Bitcoin Keeper ofrece una visibilidad completa de las UTXO (Salidas de transacciones no gastadas) que componen su saldo. Desde una pantalla wallet, pulse "Ver todas las monedas" para acceder al gestor de rincones.



![Gestion des UTXO](assets/fr/06.webp)



La pantalla "Gestionar monedas" muestra cada UTXO individualmente con su importe y etiqueta. Esta vista le permite rastrear el origen de sus monedas y organizarlas. Puede seleccionar UTXO específicos a través de "Seleccionar para enviar" para enviar con control de monedas, evitando así mezclar monedas de diferentes orígenes.



## Enviar bitcoins



Para enviar, seleccione la cartera de origen y pulse "Enviar Bitcoin". Introduzca la dirección de destino (pegada o escaneada mediante código QR) y, opcionalmente, añada una etiqueta para identificar al destinatario.



![Envoi de bitcoins](assets/fr/07.webp)



La siguiente pantalla le permite introducir el importe que desea enviar. La interfaz muestra su saldo disponible y la conversión en moneda fiduciaria. Seleccione la prioridad de carga: Baja (económica, ~60 minutos), Media o Alta (prioridad). Los gastos estimados en sats/vbyte se muestran en tiempo real. Pulse "Enviar" para continuar.



![Confirmation et envoi](assets/fr/08.webp)



Una pantalla de resumen muestra todos los detalles: wallet origen, dirección de destino, prioridad de la transacción, gastos de red, importe enviado y total. Compruebe cuidadosamente esta información, ya que las transacciones Bitcoin son irreversibles. Pulse "Confirmar y enviar" para enviar la transacción.



Aparece una confirmación de "Envío correcto" con el resumen completo. La transacción es visible en el historial de "Transacciones recientes" con su etiqueta.



## Guarda tus llaves



Hacer una copia de seguridad de la clave de recuperación es un paso fundamental. En la pestaña Más, ve a la sección "Copia de seguridad y recuperación" y haz clic en "Clave de recuperación".



![Sauvegarde de la Recovery Key](assets/fr/09.webp)



La pantalla muestra el estado de sus copias de seguridad. Para verificar su copia de seguridad, la aplicación le pide que confirme una palabra específica de su frase (por ejemplo, la 7ª palabra). Esta verificación garantiza que ha escrito correctamente su frase de recuperación.



Desde "Configuración de la clave de recuperación", puede ver su frase completa a través de "Ver clave de recuperación" y ver la huella digital del firmante de su clave. Guarde su frase de 12 palabras en papel, en un lugar seguro, lejos de la humedad y el fuego. Nunca la guardes en un dispositivo conectado.



## Añadir una llave externa (hardware wallet)



Una de las principales ventajas de Bitcoin Keeper es la integración de monederos hardware. Desde la pestaña Claves, pulsa "Añadir clave" para añadir un nuevo dispositivo de firma.



![Ajout d'une clé hardware](assets/fr/10.webp)



Seleccione "Añadir llave desde un hardware" para conectar un wallet de hardware. La aplicación es compatible con una amplia gama de dispositivos: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner y Specter Solutions.



### Configuración Tapsigner



La Tapsigner es una tarjeta NFC de Coinkite especialmente adaptada al uso móvil. Si quieres saber más, tenemos un tutorial dedicado :



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

Para añadir el Tapsigner, selecciónelo en la lista de monederos hardware.



![Configuration du Tapsigner](assets/fr/11.webp)



Introduzca primero el código PIN de 6-32 dígitos impreso en el reverso de su tarjeta (por defecto en las tarjetas nuevas), o su PIN si ya está configurado. Pulse "Continuar" y, a continuación, acerque su Tapsigner a la parte posterior de su teléfono cuando aparezca "Listo para escanear". La comunicación NFC importa automáticamente la clave pública. A continuación, puede añadir una descripción (por ejemplo, "Tarjeta Métro") para identificar esta clave.



## Crear una cartera multisig



Una vez que hayas configurado tus claves, puedes crear una wallet multifirma combinando varios dispositivos. En la pestaña Monederos, haz clic en "Añadir Wallet".



![Création d'un nouveau wallet](assets/fr/12.webp)



Tiene tres opciones: "Crear Wallet" para una cartera nueva, "Importar Wallet" para restaurar una wallet existente, o "Wallet colaborativa" para una cámara compartida. Seleccione "Crear Wallet" y luego "Bitcoin Wallet".



![Sélection du type de wallet](assets/fr/13.webp)



La siguiente pantalla ofrece diferentes configuraciones: "Tecla única", "2 de 3 multitecla" o "3 de 5 multitecla". Para una multi-sig personalizada, pulse "Seleccionar configuración personalizada". Por ejemplo, elija "1 de 2": se requiere una sola firma de dos llaves posibles.



A continuación, seleccione las llaves que compondrán su Bóveda. En nuestro ejemplo, combinamos la "Llave Móvil" (llave software del teléfono) con la "TAPSIGNER" (Tarjeta Metro). Esta configuración ofrece redundancia: si una de las llaves resulta inaccesible, siempre podrá gastar sus fondos con la otra.



![Finalisation du wallet multisig](assets/fr/14.webp)



Dé un nombre a su wallet (por ejemplo, "Plan de pruebasB"), añada una descripción opcional y marque las teclas seleccionadas. Pulse "Crear su Wallet". Aparecerá un mensaje de confirmación "Wallet creado correctamente", recordándole que debe guardar el archivo de recuperación de wallet.



Su nueva wallet multisig aparece ahora en la pestaña Monederos con la etiqueta "Multillave" y la indicación "1 de 2".



### Guardar archivo de configuración



**A diferencia de una wallet simple, donde la frase de recuperación es suficiente para restaurar el acceso, una wallet multisig también requiere el archivo de configuración que describe la estructura de la caja fuerte (qué claves participan, cuántas firmas se requieren). Sin este archivo, incluso con todas las frases de recuperación, no podrá reconstruir su wallet.



![Export du fichier de configuration](assets/fr/15.webp)



Para exportar este archivo, seleccione su multisig wallet en la pestaña Carteras y, a continuación, pulse el icono Configuración (engranaje) situado en la esquina superior derecha. En "Ajustes Wallet", pulse "Archivo de configuración Wallet". Hay varias opciones de exportación disponibles:





- Exportar PDF**: genera un documento PDF con toda la información de wallet
- Mostrar QR**: muestra un código QR escaneable para importar la configuración a otro dispositivo
- Airdrop / Exportación de archivos**: exporta el archivo a través de las opciones de uso compartido del teléfono
- NFC**: compartir mediante NFC con un dispositivo compatible



Mantenga este archivo de configuración separado de sus frases de recuperación, idealmente en un medio encriptado o impreso. Si pierde su teléfono, este archivo combinado con las frases de recuperación para cada clave participante le permitirá reconstruir su multisig wallet en Bitcoin Keeper o cualquier otro software compatible.



## Buenas prácticas



### Organización de fondos



Estructura tus bitcoins en función de su uso: una wallet Single-Key caliente para gastos corrientes con cantidades limitadas, y una o varias Vaults Multi-Key para ahorros a largo plazo. El etiquetado sistemático de UTXO te ayudará a hacer un seguimiento de la procedencia de tus fondos, lo que resulta especialmente útil para gestionar la confidencialidad y evitar mezclar monedas de distintos orígenes.



Mantén tu teléfono seguro: activa el bloqueo biométrico, realiza actualizaciones del sistema con regularidad y permanece atento a las aplicaciones instaladas. Y mantén Bitcoin Keeper al día con los parches de seguridad.



### Seguridad de las copias de seguridad



Guarde al menos dos copias de cada frase de recuperación en papel, almacenadas en lugares geográficamente separados. Para grandes sumas, considere la posibilidad de grabarlas en metal resistente a catástrofes. No guardes nunca estas frases en un dispositivo conectado a Internet ni las fotografíes.



Para bóvedas multi-sig, guarde también el archivo de configuración (Wallet Recovery File), que contiene las claves públicas participantes y la estructura de la bóveda. Este archivo, combinado con las frases de recuperación de claves, permite reconstruir wallet en cualquier software compatible, como Sparrow o Specter.



## Ventajas y limitaciones



### Destacados





- La aplicación exclusiva Bitcoin reduce la complejidad y el riesgo
- Integración nativa de bóvedas multisig con guía paso a paso
- Compatibilidad ampliada con hardware wallet (Tapsigner, Coldcard, Ledger, Jade, etc.)
- Gestión avanzada de UTXO y control de monedas
- Puede conectarse a un servidor personal Electrum
- Código fuente abierto y auditable



### Limitaciones a tener en cuenta





- Interface principalmente en inglés
- Algunas funciones premium (copia de seguridad en la nube, servidor asistido) requieren una actualización
- La configuración de Multisig requiere formación inicial



## Conclusión



Bitcoin Keeper destaca como solución escalable para gestionar sus bitcoins. Su enfoque progresivo, desde la sencilla wallet caliente hasta las bóvedas multifirma, significa que la seguridad puede actualizarse a medida que cambian las necesidades. La posibilidad de integrar fácilmente monederos de hardware como Tapsigner allana el camino para configuraciones robustas sin excesiva complejidad.



La orientación exclusivamente bitcoin, el código fuente abierto y el respeto por la privacidad la convierten en una opción alineada con los valores fundamentales del ecosistema Bitcoin.



Este tutorial cubre las características esenciales de Bitcoin Keeper en su versión gratuita. La aplicación también ofrece funciones premium (Cloud Backup, Assisted Server Backup, Canary Wallets) que serán objeto de un tutorial dedicado. En una próxima guía, también exploraremos la función de Planificación de Herencias, que le permite preparar la transmisión de sus bitcoins a sus seres queridos, gracias a las Bóvedas Mejoradas y a los documentos de acompañamiento integrados en la aplicación.



## Recursos





- Sitio web oficial: [bitcoinkeeper.app](https://bitcoinkeeper.app)
- Centro de ayuda: [help.bitcoinkeeper.app](https://help.bitcoinkeeper.app)
- Código fuente: [github.com/bithyve/bitcoin-keeper](https://github.com/bithyve/bitcoin-keeper)
- Telegram : [t.me/BitcoinKeeper](https://t.me/BitcoinKeeper)
- Twitter/X: [@bitcoinkeeper_](https://x.com/bitcoinkeeper_)