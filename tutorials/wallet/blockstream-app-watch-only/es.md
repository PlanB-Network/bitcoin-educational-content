---
name: Blockstream App - Watch-Only
description: ¿Cómo configuro una Watch-only wallet en Blockstream App?
---

![cover](assets/cover.webp)


## 1. Introducción


### 1.1 Objetivo del tutorial





- Este tutorial explica cómo configurar y utilizar la función **Watch-Only** de la aplicación móvil **Blockstream App** para supervisar una Bitcoin Wallet sin acceder a sus claves privadas.
- Abarca la instalación, la configuración inicial, la importación de una clave pública ampliada y su uso para realizar un seguimiento de los saldos y las direcciones de recepción de generate.
- Nota: Otros tutoriales, incluidos en el apéndice, cubren Onchain, Liquid y la versión de escritorio.



### 1.2. Público objetivo





- **Principiantes**: Usuarios que desean supervisar una cartera Bitcoin (a menudo asociada a una Hardware Wallet) a través de una aplicación móvil intuitiva.
- **Usuarios intermedios**: Personas que buscan gestionar carteras de sólo lectura mientras utilizan opciones de privacidad como Tor o SPV.
- **Propietarios de Hardware Wallet**: Para consultar sus saldos y direcciones generate sin conectar su dispositivo.
- **Empresas y comercios**:
 - Realice el seguimiento de sus transacciones con fines contables sin exponer sus claves privadas.
 - Verificar las transacciones recibidas sin introducir sus claves privadas en los sistemas de pago en línea.
 - Permitir a los empleados generate nuevas direcciones de recepción sin tener acceso a las claves privadas.
- **Organizaciones y crowdfunding**: Mostrar el saldo de forma transparente a los donantes sin permitir el acceso a los fondos.



### 1.3. Presentación de Watch-Only



Una **GWatch-Only** Wallet permite controlar las transacciones y el saldo de una Bitcoin Wallet sin tener acceso a las claves privadas. A diferencia de una Wallet convencional, sólo almacena datos públicos, como la **clave pública** extendida (que dio lugar a "**xpub**", luego a "zpub", "ypub", etc.), que le permite obtener direcciones de recepción y seguir el historial de transacciones en la Blockchain Bitcoin. La ausencia de claves privadas imposibilita el desembolso de fondos desde la aplicación, lo que garantiza una mayor seguridad.



![image](assets/fr/10.webp)



**¿Por qué usar una Watch-only wallet?**





- **Seguridad**: Ideal para supervisar una cartera asegurada por un **Hardware Wallet** sin exponer claves privadas en un dispositivo conectado.
- **Comodidad**: Le permite comprobar el saldo y generate nuevas direcciones de destinatarios sin conectar el Hardware Wallet.
- **Confidencialidad**: Compatible con opciones como **Tor** o **SPV** para limitar la dependencia de servidores de terceros.
- **Casos de uso**: Seguimiento de fondos en movimiento, generación de direcciones para recibir pagos o verificación de transacciones sin arriesgar claves privadas.



![image](assets/fr/01.webp)



### 1.4. Claves públicas ampliadas



Una **clave pública extendida** (xpub, ypub, zpub, etc.) es un dato derivado de una Bitcoin Wallet que genera todas las claves públicas hijas y sus direcciones de recepción asociadas, sin dar acceso a las claves privadas.





- Cómo funciona: La clave pública ampliada se genera a partir de la frase seed mediante un proceso determinista (BIP-32). Crea un árbol jerárquico de claves públicas hijas, cada una de las cuales puede convertirse en una Address receptora. Utilizando la misma ruta de derivación (por ejemplo, `m/44'/0'/0'`) que la Wallet vigilada, la Watch-only wallet genera las mismas direcciones, lo que permite hacer un seguimiento de los fondos y crear nuevas direcciones de recepción.



![image](assets/fr/11.webp)





- Tipos de clave pública ampliados
- **xpub**: Se utiliza para las carteras Legacy (direcciones que empiezan por "1", BIP-44) y las carteras Taproot (direcciones que empiezan por "bc1p", BIP-86).
- **ypub**: Diseñado para monederos SegWit compatibles (direcciones que empiezan por "3", BIP-49).
- **zpub**: Asociado a carteras nativas SegWit (direcciones que empiezan por "bc1q", BIP-84).
- **Otros (tpub, upub, vpub, etc.)**: Se utiliza para redes alternativas (como Testnet) o normas específicas. Por ejemplo, tpub es para la red Testnet.





- **Distinción**: La elección entre xpub, ypub o zpub depende del tipo de Address (legacy, SegWit, Taproot o nested SegWit) y del estándar BIP utilizado por la Wallet. Compruebe el formato requerido por su cartera de fuentes para garantizar la compatibilidad con Blockstream App.





- **Seguridad y confidencialidad**: La clave pública ampliada no es sensible en términos de seguridad, ya que no permite gastar fondos (no hay acceso a las claves privadas). Sin embargo, es sensible en términos de confidencialidad, ya que revela todas las direcciones públicas y el historial de transacciones asociado.



**Recomendación**: Proteja su clave pública extendida como información sensible.



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 1.5. Hot Wallet recordatorio





- **Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: todos los nombres de una aplicación instalada en un smartphone, un ordenador o cualquier dispositivo conectado a Internet, que permite gestionar y proteger las claves privadas de una Bitcoin Wallet.
- A diferencia de los **monederos de hardware**, también conocidos como **monederos Cold**, que aíslan las claves fuera de línea, los monederos de software funcionan en un entorno conectado, lo que los hace más vulnerables a los ciberataques.





- **Uso recomendado**:
    - Ideal para gestionar cantidades moderadas de Bitcoin, especialmente para transacciones diarias.
    - Adecuado para principiantes o usuarios con recursos limitados, para quienes un Hardware Wallet puede parecer superfluo.





- **Limitaciones**: Menos segura para almacenar grandes fondos o ahorros a largo plazo. En este caso, elige una Hardware Wallet.




## 2. Presentación de la aplicación Blockstream





- **Blockstream App** es una aplicación móvil (iOS, Android) y de escritorio para gestionar carteras y activos de Bitcoin en Liquid Network. Adquirida por [Blockstream](https://blockstream.com/) en 2016, antes se llamaba *Green Address* y después *Blockstream Green*.
- **Características principales**:
- **Transacciones Onchain** en Blockchain Bitcoin.
    - Transacciones en la red **Liquid** (Sidechain para intercambios rápidos y confidenciales).
- Carteras **Watch-only** para el seguimiento de fondos sin acceso a las claves.
    - Opciones de privacidad: conexión a través de **Tor**, conexión a un **nodo personal** a través de Electrum, o verificación **SPV** para reducir la dependencia de nodos de terceros.
    - Funciones **Replace-by-fee (RBF)** para acelerar las transacciones no confirmadas.
- **Compatibilidad**: Integra monederos hardware como **Blockstream Jade**.
- **Interface**: Intuitivo para principiantes, con opciones avanzadas para expertos.
- **Nota**: Esta guía se centra en el uso de Onchain. Otros tutoriales en los Apéndices cubren Onchain, Watch-Only y la versión de escritorio.




## 3. Instalación y configuración de la aplicación Blockstream



### 3.1. descargar





- Para **Android**:
    - Descarga [Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) de Google Play Store.
    - Alternativa: Instalar a través del archivo APK disponible en [GitHub oficial de Blockstream](https://github.com/Blockstream/green_android).
- Para **iOS**:
    - Descarga [Blockstream App](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) de la App Store.
- **Nota**: Asegúrese de descargar de fuentes oficiales para evitar aplicaciones fraudulentas.



### 3.2. configuración inicial





- **Pantalla de inicio**: Cuando se abre por primera vez, la aplicación muestra una pantalla sin Wallet configurada. Las carteras creadas o importadas aparecerán aquí más adelante.



![image](assets/fr/02.webp)





- **Personalizar los ajustes**: Haga clic en "Configuración de la aplicación", ajuste las opciones que aparecen a continuación, haga clic en "Guardar", reinicie la aplicación y cree su cartera.



![image](assets/fr/03.webp)



#### 3.2.1. Privacidad mejorada (solo Android)





- **Función**: Desactiva las capturas de pantalla, oculta las vistas previas de las aplicaciones en el administrador de tareas y bloquea el acceso cuando el teléfono está bloqueado.
- ¿Por qué? Protege sus datos contra el acceso físico no autorizado o malware de captura de pantalla.



#### 3.2.2. Conexión vía Tor





- **Función**: Enruta el tráfico de red a través de **Tor**, una red anónima que cifra tus conexiones.
- ¿Por qué? Oculta tu IP Address y protege tu privacidad, ideal si no confías en tu red (Wi-Fi pública, por ejemplo).
- **Desventaja**: Puede ralentizar la aplicación debido al cifrado.
- **Recomendación**: Active Tor si la confidencialidad es una prioridad, pero pruebe la velocidad de conexión.



#### 3.2.3. Conexión a un nodo personal





- **Función**: Conecta la aplicación a su propio **nodo Bitcoin completo** a través de un **servidor de Electrum**.
- ¿Por qué? Proporciona un control total sobre los datos de Blockchain, eliminando la dependencia de los servidores Blockstream.
- **Requisito**: Un nodo Bitcoin configurado.
- **Recomendación**: Usuarios avanzados que deseen la máxima soberanía.



#### 3.2.4. Verificación SPV





- **Función**: Utiliza **Verificación simplificada de pagos (SPV)** para verificar directamente determinados datos de Blockchain sin necesidad de descargar toda la cadena.
- ¿Por qué? Reduce la dependencia del nodo por defecto de Blockstream, sin dejar de ser ligero para los dispositivos móviles.
- **Desventaja**: Menos seguro que un Full node, ya que depende de nodos de terceros para cierta información.
- **Recomendación**: Active SPV si no puede utilizar un nodo personal, pero prefiere un Full node para una seguridad óptima.





## 4. Creación de una cartera Bitcoin "Watch-only



### 4.1. Recuperar la clave pública extendida



Para configurar una Watch-only wallet, primero debe obtener la clave pública extendida (xpub, ypub, zpub, etc.) de la Wallet que se va a supervisar. Esta información suele estar disponible en la sección de configuración o "Información de Wallet" de su software o Hardware Wallet.





- Ejemplo con Blockstream App: En la pantalla de inicio de Wallet, vaya a "Configuración", luego a "Detalles de Wallet" y copie el archivo zpub :



![image](assets/fr/09.webp)





- Alternativa 1: generate un código QR que contenga la clave pública ampliada para su escaneado en el siguiente paso.
- Alternativa 2: Utilice una output descriptor si su Wallet se la proporciona.



### 4.2. importar Wallet Watch-only





- **Precaución**: Instale su cartera en un entorno privado, sin cámaras ni observadores.
- En la pantalla de inicio, haga clic en "Crear una nueva cartera" y luego en "Empezar" :



![image](assets/fr/04.webp)





- Aparece la siguiente pantalla:



![image](assets/fr/06.webp)






- (1) **"Configurar Wallet móvil "** : Crea una nueva Hot Wallet. Consulta el tutorial "Blockstream App - Onchain" en el apéndice.
- (2) **"Restaurar desde copia de seguridad "**: Importa una cartera existente utilizando una frase Mnemonic (12 o 24 palabras). Precaución: No importe la frase desde un Cold Wallet, ya que quedará expuesta en un dispositivo conectado, invalidando su seguridad.
- (3) **"Watch-Only "**: la opción que nos interesa para este tutorial.





- A continuación, seleccione "**Firma única**" y la red "**Bitcoin**":



![image](assets/fr/12.webp)





- Pegue la clave pública extendida (xpub, ypub, zpub, etc.), escanee el código QR correspondiente o introduzca una output descriptor. Aunque la aplicación especifique "xpub", las claves ypub, zpub, etc. también están autorizadas. A continuación, haga clic en "Conectar":



![image](assets/fr/13.webp)




### 4.3. Uso del Wallet Watch-only



Una vez importada, la Watch-only wallet muestra el saldo total y el historial de transacciones de las direcciones derivadas de la clave pública ampliada. Sólo son visibles las transacciones onchain (se ignoran las transacciones Liquid). Para supervisar una Liquid Wallet, repita la importación seleccionando "Liquid" en el paso anterior.





- **Ver saldo e historial**: desde la pantalla de inicio, consulta el saldo total y el historial de transacciones en cadena:



![image](assets/fr/14.webp)





- generate un Address receptor: Haz clic en "Transact", luego en "Receive", para crear un nuevo Address onchain. Compártelo mediante código QR o copia para recibir fondos:



![image](assets/fr/15.webp)





- **Enviar fondos**: Haga clic en **"Transact"** y, a continuación, en **"Send"**. Puede introducir:
 - El Address del destinatario.
 - El importe de la transacción.
 - Comisiones de transacción.



Sin embargo, como Watch-only wallet no dispone de las claves privadas, no puede enviar fondos directamente. Para firmar la transacción, conecta tus PSBT Hardware Wallet o Exchange escaneando los códigos QR (una opción disponible en la Coldcard Q, por ejemplo).



![image](assets/fr/16.webp)





- **Nota**: Compruebe siempre la Address receptora y los detalles de la transacción para evitar errores. Los fondos enviados a la Address equivocada no se pueden recuperar.




## Apéndices



### A1. Otros tutoriales de Blockstream App





- Uso de la red Onchain :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143



- Uso de la Liquid Network :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Versión de escritorio :



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Claves públicas ampliadas





- Glosario :
 - [Claves públicas ampliadas](https://planb.network/fr/resources/glossary/extended-key)
 - [xpub](https://planb.network/fr/resources/glossary/xpub)
 - [ypub](https://planb.network/fr/resources/glossary/ypub)
 - [zpub](https://planb.network/fr/resources/glossary/zpub)
- Curso :
 - [Les clés publiques étendues](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f)




### A3. Buenas prácticas



Para utilizar **Blockstream App** de forma segura y eficiente, siga estas recomendaciones. Le ayudarán a proteger sus fondos, optimizar sus transacciones y preservar su confidencialidad en las redes **Bitcoin (onchain)**, **Liquid** y **Lightning**.





- **Asegura tu frase de recuperación**:
 - Tutorial: Guardar su frase Mnemonic



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Utilizar autenticación segura**:
 - Activar un **PIN fuerte** o **autenticación biométrica** (huella dactilar o reconocimiento facial) para proteger el acceso a la aplicación.
 - Nunca compartas tu PIN ni tus datos biométricos.





- **Proteja su intimidad**:
 - generate una nueva Address para cada recepción onchain o Liquid para limitar el rastreo en la Blockchain.
 - Active las funciones "Privacidad mejorada", "Tor" y "SPV".
 - Para obtener la máxima confidencialidad, conecte su Wallet a su propio nodo Bitcoin a través de un servidor Electrum en lugar de utilizar el nodo público





- **Elija la red que mejor se adapte a sus necesidades**:
- **Onchain**: Preferido para custodia a largo plazo o transacciones de gran valor (comisiones insignificantes en relación con el importe).
- **Liquid**: Utilícelo para transferencias rápidas y económicas con mayor confidencialidad.
- **Relámpago**: Elija transferencias instantáneas de bajo coste para pequeños importes.





- **Compruebe siempre las direcciones de envío**:
 - Antes de enviar fondos, compruebe cuidadosamente la Address. Los fondos enviados a una Address incorrecta se pierden para siempre. Utiliza copiar/pegar o escanear código QR, nunca copies/modifiques una Address a mano.





- **Optimizar los costes**:
 - Para las transacciones onchain, elija las tarifas adecuadas (lenta, media, rápida) en función de la urgencia y la congestión de la red.
 - Utilice Liquid, o Lightning para pequeñas cantidades.





- Mantener actualizada la aplicación




### A4. Recursos adicionales





- Enlaces oficiales de Blockstream:
- [Sitio web oficial](https://blockstream.com/)
- [Soporte para la aplicación móvil](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): documentación y chat
- [GitHub](https://github.com/Blockstream/green_android)





- Exploradores de bloques :**
 - En cadena: **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Rayo: **[1ML (Lightning Network)](https://1ml.com/)**





- Aprendizaje y tutorías: **[Plan ₿ Network](https://planb.network/)**
  - Asegurar su frase de recuperación



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Liquid Network** :
- [Glosario](https://planb.network/fr/resources/glossary/liquid-network)




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- **Lightning Network**:
- [Glosario](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb