---
name: Aplicación Blockstream - Onchain
description: Instala Blockstream App en tu móvil y gestiona las transacciones onchain
---
![cover](assets/cover.webp)


## 1. Introducción


### 1.1 Objetivo de la tutoría





- Este tutorial explica cómo utilizar la aplicación móvil **Blockstream App** para gestionar una Bitcoin **onchain** Wallet, es decir, transacciones registradas directamente en la Blockchain Bitcoin principal.
- Abarca la instalación, la configuración inicial, la creación de un Software Wallet y las operaciones de recepción y envío de bitcoins.
- Nota: Otros tutoriales en los Apéndices cubren Liquid, Watch-Only y la versión de escritorio.



![image](assets/fr/01.webp)



### 1.2 Destinatarios





- Principiantes**: Usuarios que desean gestionar sus bitcoins con una aplicación móvil intuitiva.
- Usuarios intermedios**: Personas que buscan entender las funcionalidades de onchain y opciones de privacidad como Tor o SPV.



### 1.3. Recordatorios sobre las carteras Hot





- Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: todos los nombres de una aplicación instalada en un smartphone, ordenador o cualquier dispositivo conectado a Internet, que permite gestionar y proteger las claves privadas de un Bitcoin Wallet.
- A diferencia de los **monederos de hardware**, también conocidos como **monederos Cold**, que aíslan las claves fuera de línea, los monederos de software funcionan en un entorno conectado, lo que los hace más vulnerables a los ciberataques.





- Uso recomendado** :
    - Ideal para gestionar cantidades moderadas de Bitcoin, especialmente para transacciones diarias.
    - Adecuada para principiantes o usuarios con recursos limitados, para los que una Hardware Wallet puede parecer superflua.





- Limitaciones**: Menos segura para almacenar grandes fondos o ahorros a largo plazo. En este caso, elige una Hardware Wallet.




## 2. Presentación de la aplicación Blockstream





- Blockstream App** es una aplicación móvil (iOS, Android) y de escritorio para gestionar carteras y activos de Bitcoin en Liquid Network. Adquirida por [Blockstream](https://blockstream.com/) en 2016, antes se llamaba *Green Address* y después *Blockstream Green*.
- Características principales** :
    - Transacciones Onchain** en Blockchain Bitcoin.
    - Transacciones en red **Liquid** (Sidechain para intercambios rápidos y confidenciales).
    - Carteras Watch-only** para el seguimiento de fondos sin acceso a las claves.
    - Opciones de privacidad: conexión a través de **Tor**, conexión a un **nodo personal** a través de Electrum, o verificación **SPV** para reducir la dependencia de nodos de terceros.
    - Funciones **Replace-by-fee (RBF)** para acelerar las transacciones no confirmadas.
- Compatibilidad**: Integra monederos hardware como **Blockstream Jade**.
- Interface**: Intuitivo para principiantes, con opciones avanzadas para expertos.
- Nota**: Esta guía se centra en el uso de onchain. Otros tutoriales en los Apéndices cubren Liquid, Watch-Only y la versión de escritorio.



## 3. Instalación y configuración de la aplicación Blockstream



### 3.1. descargar





- Para Android** :
    - Descarga [Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) de Google Play Store.
    - Alternativa: Instalar a través del archivo APK disponible en [GitHub oficial de Blockstream](https://github.com/Blockstream/green_android).
- Para iOS** :
    - Descarga [Blockstream App](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) de la App Store.
- Nota**: Asegúrese de descargar de fuentes oficiales para evitar aplicaciones fraudulentas.



### 3.2. configuración inicial





- Pantalla de inicio**: Cuando se abre por primera vez, la aplicación muestra una pantalla sin Wallet configurada. Las carteras creadas o importadas aparecerán aquí más adelante.



![image](assets/fr/02.webp)





- Personalizar los ajustes**: Haga clic en "Configuración de la aplicación", ajuste las opciones que aparecen a continuación, haga clic en "Guardar", reinicie la aplicación y cree su cartera.



![image](assets/fr/03.webp)



#### 3.2.1. Privacidad mejorada (solo Android)





- Función**: Desactiva las capturas de pantalla, oculta las vistas previas de las aplicaciones en el administrador de tareas y bloquea el acceso cuando el teléfono está bloqueado.
- ¿Por qué? Protege sus datos contra el acceso físico no autorizado o malware de captura de pantalla.


#### 3.2.2. Conexión vía Tor





- Función**: Enruta el tráfico de red a través de **Tor**, una red anónima que cifra tus conexiones.
- ¿Por qué?**: Oculta tu IP Address y protege tu privacidad, ideal si no confías en tu red (Wi-Fi pública, por ejemplo).
- Desventaja**: Puede ralentizar la aplicación debido al cifrado.
- Recomendación**: Active Tor si la confidencialidad es una prioridad, pero pruebe la velocidad de conexión.


#### 3.2.3. Conexión a un nodo personal





- Función**: Conecta la aplicación a tu propio **nodo Bitcoin completo** a través de un servidor **Electrum**.
- ¿Por qué?**: Proporciona un control total sobre los datos Blockchain, eliminando la dependencia de los servidores Blockstream.
- Requisito**: Un nodo Bitcoin configurado.
- Recomendación**: Usuarios avanzados que buscan la máxima soberanía.


#### 3.2.4. Verificación SPV





- Función**: Utiliza **Verificación simplificada de pagos (SPV)** para verificar directamente determinados datos de Blockchain sin necesidad de descargar toda la cadena.
- ¿Por qué? Reduce la dependencia del nodo por defecto de Blockstream, sin dejar de ser ligero para los dispositivos móviles.
- Desventaja**: Menos seguro que un Full node, ya que depende de nodos de terceros para cierta información.
- Recomendación**: Active SPV si no puede utilizar un nodo personal, pero prefiere un Full node para una seguridad óptima.





## 4. Creación de una cartera Bitcoin onchain



### 4.1. Iniciar la creación





- Precaución**: Instale su cartera en un entorno privado, sin cámaras ni observadores.
- En la pantalla de inicio, haz clic en "Empezar" :



![image](assets/fr/04.webp)





- Si desea gestionar un **Cold Wallet** (Wallet sin conexión): haga clic en **"Conectar Jade "** para utilizar el Blockstream Jade Hardware Wallet u otros monederos Cold compatibles.



![image](assets/fr/05.webp)





- Aparece la siguiente pantalla:



![image](assets/fr/06.webp)





- (1) **"Configurar Wallet móvil "** : Crear una nueva Hot Wallet (Hot Wallet).
- (2) **"Restaurar desde copia de seguridad "**: Importa una cartera existente utilizando una frase Mnemonic (12 o 24 palabras). Precaución: No importe una frase Cold Wallet, ya que quedará expuesta en un dispositivo conectado, invalidando su seguridad.
- (3) **"Watch-Only "**: Importe una cartera existente de sólo lectura, para ver el saldo (por ejemplo, de su Cold Wallet) sin exponer la frase Mnemonic. Consulte el tutorial "Watch Only" en el apéndice.



**En este tutorial**: Pulsa en **"Configurar Wallet Móvil "** para crear un Hot Wallet.


Tu Wallet se crea automáticamente y aparece la página de inicio de Wallet, aquí llamada "Mi Wallet 5":



![image](assets/fr/07.webp)



**Importante**: Blockstream App ha simplificado la creación de una Wallet al no mostrar automáticamente la frase seed de 12 palabras. *Aunque ahora la cartera se crea con un solo clic, corres el riesgo de perder el acceso a tus fondos si no guardas la frase seed*.



### 4.2. Guardar sentencia seed





- En la pantalla de inicio de Wallet, haz clic en la pestaña "Seguridad" y, a continuación, en la indicación "Copia de seguridad" o en el menú "Frase de recuperación":



![image](assets/fr/08.webp)



Aparecerá la frase de 12 palabras seed para que la guarde.





- Escriba su frase de recuperación con sumo cuidado. Escríbela en papel o metal y guárdala en un lugar seguro (ubicación segura y sin conexión). Esta frase es tu único medio de acceder a tus bitcoins en caso de pérdida de tu dispositivo o borrado de la aplicación.
- También es importante tener en cuenta que cualquiera con esta frase puede robarte todos tus bitcoins. Nunca los almacenes digitalmente:
 - Sin captura de pantalla
 - Sin copias de seguridad en la nube, correo electrónico o mensajería
 - Sin copiar/pegar (riesgo de guardar en el portapapeles)



*¡*! Este punto es crítico**. Para más información sobre las copias de seguridad :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3. Confirmar sentencia seed



Antes de enviar fondos a una Address asociada a esta sentencia seed, debe probar el respaldo de sus 12 palabras.



Para ello, anotaremos una referencia, borraremos la Wallet, la restauraremos con la copia de seguridad y comprobaremos que la referencia no ha cambiado.





- En la pantalla de inicio de Wallet, haga clic en la pestaña "Configuración", luego en "Detalles de Wallet", y copie la zPub ([clave pública extendida](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8dcffce1-31bd-5e0b-965b-735f5f9e4602):



![image](assets/fr/09.webp)



Nota: se puede importar una Address zpub a la aplicación Blockstream para la función "Sólo vigilancia" (véase el Apéndice).





- Borre la aplicación, luego restaure la Wallet a través de **"Restaurar desde copia de seguridad "** introduciendo la frase Mnemonic, y compruebe que el zpub no ha cambiado. Si es así, entonces su copia de seguridad es correcta, y puede enviar fondos a la Wallet.





- Para saber más sobre cómo realizar una prueba de recuperación, aquí tienes un tutorial dedicado :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.5. Asegurar el acceso a la aplicación



Bloquee el acceso a la aplicación con un código PIN seguro:




- Desde la pantalla de inicio de Wallet, ve a **"Seguridad "** y luego haz clic en **"PIN "**
- Introduzca y confirme **un código PIN aleatorio de 6 dígitos**.



**Opción biométrica**: Disponible para mayor comodidad, pero menos segura que un código PIN robusto (riesgo de acceso no autorizado, por ejemplo, huella dactilar o escaneado facial durante el sueño).



**Nota**: El PIN asegura el dispositivo, pero sólo la frase seed se puede utilizar para recuperar fondos.





## 5. Uso de la Wallet en cadena



### 5.1. Recibir bitcoins





- Desde la pantalla de inicio de la cartera, haga clic en '"**Transaccionar**" y luego en **"Recibir "**.



![image](assets/fr/10.webp)





- La aplicación muestra un **Address de recepción en blanco** (formato SegWit v0, que empieza por `bc1q...`). El uso de una nueva Address cada vez que recibe Bitcoin mejora su confidencialidad.





- Opciones** :
    - (1) "Bitcoin": haga clic para seleccionar un envío onchain o Liquid, y elija el activo.
    - (2) Haga clic en las flechas para seleccionar otra nueva Address vinculada a esta sentencia seed.
    - (3) También puede elegir una Address de entre las ya utilizadas/mostradas, haciendo clic en los tres puntos de la parte superior derecha y, a continuación, en "Lista de direcciones"
    - (4) Para solicitar un importe concreto, haga clic en los tres puntos de la parte superior derecha, seleccione "Solicitar importe" e introduzca el importe deseado. El QR se actualizará y el Address se sustituirá por un URI de pago Bitcoin.




![image](assets/fr/11.webp)





- Comparta la Address/URI haciendo clic en "**Compartir**", copiando el texto o escaneando el código QR.
- Verificación**: Comprueba en la medida de lo posible el Address compartido con el destinatario para evitar errores o ataques (por ejemplo, que un malware modifique el portapapeles).



### 5.2. enviar bitcoins





- En la pantalla de inicio de la cartera, haga clic en "**Transaccionar**" y luego en **"Enviar "** :



![image](assets/fr/12.webp)





- Introduzca los datos** :
    - (1) Introduzca el **Address del destinatario** pegándolo o escaneando un código QR.
    - (2) Compruebe los activos y la cuenta desde la que se envían los fondos.
    - (3) Indique el **importe** a enviar. Puede elegir la unidad: BTC, satoshis, USD, ...


El importe mínimo (límite de dush) el 03/08/2025 es de 546 Sats.




    - (4) Seleccione **tarifas de transacción** :
        - Elija entre las opciones sugeridas (por ejemplo, rápido, medio, lento) en función de la urgencia, y se mostrará un tiempo aproximado de transferencia.
        - Para tarifas personalizadas, ajuste manualmente el número de Satoshi por vbytes (consulte [Mempool.space](https://Mempool.space/) para conocer las tarifas del mercado).




![image](assets/fr/13.webp)





- Comprueba..:
    - Compruebe el Address, el importe y los gastos en la pantalla de resumen.
    - Un error Address puede provocar una pérdida irreversible de fondos. Cuidado con los programas maliciosos que modifican el portapapeles.



![image](assets/fr/14.webp)





- Confirmación**: Deslice el botón "Enviar" para firmar y distribuir la transacción.
- Seguimiento**: En la pestaña "Transacciones" de Wallet, la transacción aparece como "pendiente" hasta su confirmación (de 1 a 6 confirmaciones):



![image](assets/fr/15.webp)





- Mientras la transacción no haya sido confirmada, la función "Replace by fee" (véase el Apéndice) permite acelerar su tramitación aumentando los gastos de transacción:



![image](assets/fr/16.webp)




## Apéndices



### A1. Otros tutoriales de Blockstream



Uso del Liquid Network



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Importación y seguimiento de un Wallet en modo "Sólo vigilancia



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Versión de sobremesa



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Explicación de Replace-by-fee (RBF)



**Definición**: Replace-by-fee (RBF) es una característica de la red Bitcoin que permite al remitente acelerar la confirmación de una transacción **onchain** aceptando pagar una tarifa más alta.



**Límites** :




- RBF no está disponible para las transacciones Liquid o Lightning.
- La transacción inicial debe marcarse como compatible con RBF cuando se crea, lo que Blockstream App hace automáticamente.



**Más información:**




- [Glosario](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. Buenas prácticas



Para utilizar **Blockstream App** de forma segura y eficiente, siga estas recomendaciones. Le ayudarán a proteger sus fondos, optimizar sus transacciones y preservar su confidencialidad en las redes **Bitcoin (onchain)**, **Liquid** y **Lightning**.





- Asegura tu frase de recuperación** :
 - Tutorial: Cómo guardar su frase Mnemonic



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Utilizar autenticación segura** :
 - Activar un **PIN fuerte** o **autenticación biométrica** (huella dactilar o reconocimiento facial) para proteger el acceso a la aplicación.
 - Nunca compartas tu PIN ni tus datos biométricos.





- Proteja su intimidad** :
 - generate una nueva Address para cada recepción onchain o Liquid para limitar el rastreo en la Blockchain.
 - Active las funciones "Privacidad mejorada", "Tor" y "SPV".
 - Para obtener la máxima confidencialidad, conecte su Wallet a su propio nodo Bitcoin a través de un servidor Electrum en lugar de utilizar el nodo público





- Elija la red que mejor se adapte a sus necesidades** :
 - Onchain**: Preferido para custodia a largo plazo o transacciones de gran valor (comisiones insignificantes en relación con el importe).
 - Liquid**: Utilícelo para transferencias rápidas y económicas con mayor confidencialidad.
 - Relámpago**: Elija transferencias instantáneas de bajo coste para pequeños importes.





- Compruebe siempre las direcciones de envío** :
 - Antes de enviar fondos, compruebe cuidadosamente la Address. Los fondos enviados al Address equivocado se pierden para siempre. Utiliza copiar/pegar o escanear código QR, nunca copies/modifiques una Address a mano.





- Optimizar los costes** :
 - Para las transacciones onchain, elija las tarifas adecuadas (lenta, media, rápida) en función de la urgencia y la congestión de la red.
 - Utilice Liquid, o Lightning para pequeñas cantidades.





- Mantener actualizada la aplicación




### A4. Recursos adicionales





- Enlaces oficiales:**
 - [Sitio web oficial](https://blockstream.com/)**
 - [Soporte para la aplicación móvil](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)** : documentación y chat
 - [GitHub](https://github.com/Blockstream/green_android)**





- Exploradores de bloques :**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Rayo: **[1ML (Lightning Network)](https://1ml.com/)**





- Aprendizaje y tutorías:**[Plan ₿ Network](https://planb.network/)** :
 - Asegurar su frase de recuperación



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** :
 - [Glosario](https://planb.network/fr/resources/glossary/liquid-network)**



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- Lightning Network** :
 - [Glosario](https://planb.network/fr/resources/glossary/lightning-network)**



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb