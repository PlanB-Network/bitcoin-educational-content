---
name: Blockstream App - Desktop
description: ¿Cómo utilizar tu Hardware Wallet con Blockstream App en un ordenador?
---
![cover](assets/cover.webp)



## 1. Introducción



### 1.1 Objetivo de la tutoría





- Este tutorial explica cómo utilizar la aplicación **Blockstream App** en un ordenador para gestionar una Bitcoin **onchain** Wallet con una **Hardware Wallet**, permitiendo transacciones seguras registradas en la Blockchain Bitcoin principal.
- Abarca la instalación, la configuración inicial, la conexión de un Hardware Wallet y la recepción y el envío de bitcoins onchain.
- Nota: Otros tutoriales en los Apéndices cubren Liquid, Watch-Only y la aplicación móvil.



### 1.2 Destinatarios





- **Principiantes**: Usuarios que deseen gestionar sus bitcoins con un software de escritorio seguro y un Hardware Wallet.
- **Usuarios intermedios**: Personas que buscan entender cómo usar un Hardware Wallet para transacciones onchain y opciones de privacidad como Tor o SPV.



### 1.3. Antecedentes de los monederos electrónicos





- **Hardware Wallet**, **Cold Wallet**: Dispositivo físico que almacena claves privadas offline, ofreciendo un alto nivel de seguridad frente a ciberataques, a diferencia de los monederos **Hot** (monederos software en dispositivos conectados).
- **Uso recomendado**:
    - Ideal para asegurar grandes cantidades o ahorros a largo plazo.
    - Adecuado para usuarios preocupados por la seguridad que desean proteger sus fondos de los riesgos asociados a los dispositivos conectados.
- **Limitaciones**: Requiere software como Blockstream App para ver saldos, direcciones generate y transmitir transacciones firmadas Hardware Wallet.



## 2. Presentación de la aplicación Blockstream





- **Blockstream App** es una aplicación móvil (iOS, Android) y de escritorio para gestionar carteras y activos de Bitcoin en Liquid Network. Adquirida por Blockstream en 2016, se llamaba *GreenAddress*, pasó a llamarse *Blockstream Green* (2019) y ahora se llama *Blockstream app* (2025).
- **Características principales**:
- **Transacciones Onchain** en Blockchain Bitcoin.
    - Transacciones en la red **Liquid** (Sidechain para intercambios rápidos y confidenciales).
- Carteras **Watch-only** para el seguimiento de fondos sin acceso a las claves.
    - Opciones de privacidad: conexión a través de **Tor**, conexión a un **nodo personal** a través de Electrum, o verificación **SPV** para reducir la dependencia de nodos de terceros.
    - Funciones **Replace-by-fee (RBF)** para acelerar las transacciones no confirmadas.
- **Compatibilidad**: Integra monederos hardware como **Blockstream Jade**.
- **Interface**: Intuitivo para principiantes, con opciones avanzadas para expertos.
- **Nota**: Esta guía se centra en el uso de onchain con una Hardware Wallet en la versión de escritorio. Otros tutoriales que se proporcionan como apéndices cubren el uso en la aplicación móvil, para onchain, Liquid y las funciones Watch-Only.



## 3. Instalación y configuración de Blockstream App Desktop



### 3.1. descargar





- Vaya al [sitio web oficial](https://blockstream.com/app/) y haga clic en "_Descargar ahora_". Descargue la versión correspondiente a su sistema operativo (Windows, macOS, Linux).
- **Nota**: Asegúrese de descargar desde la fuente oficial para evitar software fraudulento.



### 3.2. configuración inicial





- **Pantalla de inicio**: Cuando se abre por primera vez, la aplicación muestra una pantalla sin Wallet configurado. Las carteras creadas o importadas aparecerán aquí más adelante.



![image](assets/fr/02.webp)





- **Personalizar ajustes**: Haz clic en el icono de configuración de la parte inferior izquierda, ajusta las opciones que aparecen a continuación y sal de Interface para continuar.



![image](assets/fr/03.webp)



#### 3.2.1. Parámetros generales





- En el menú Configuración, haga clic en "**General**".
- **Función**: Cambia el idioma del software y activa funciones experimentales si es necesario.



![image](assets/fr/04.webp)



#### 3.2.2. Conexión vía Tor





- En el menú Configuración, haga clic en "**Red**".
- **Función**: Enruta el tráfico de red a través de **Tor**, una red anónima que cifra tus conexiones.
- **¿Por qué?**: Oculta tu IP Address y protege tu privacidad, ideal si no confías en tu red (Wi-Fi pública, por ejemplo).
- **Desventaja**: Puede ralentizar la aplicación debido al cifrado.
- **Recomendación**: Active Tor si la confidencialidad es una prioridad, pero pruebe la velocidad de conexión.



![image](assets/fr/05.webp)



#### 3.2.3. Conexión a un nodo personal





- En el menú Configuración, haga clic en "**Servidores personalizados y validación**".
- **Función**: Conecta la aplicación a tu propio **nodo Bitcoin completo** a través de un **servidor de Electrum**.
- ¿Por qué? Proporciona un control total sobre los datos de Blockchain, eliminando la dependencia de los servidores Blockstream.
- **Requisito**: Un nodo Bitcoin configurado.
- **Recomendación**: Usuarios avanzados que deseen la máxima soberanía.



![image](assets/fr/06.webp)



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

#### 3.2.4. Verificación SPV





- En el menú Configuración, haga clic en "**Servidores personalizados y validación**".
- **Función**: Utiliza **Verificación Simplificada de Pagos (SPV)** que descarga las cabeceras de bloque y verifica sus transacciones por prueba de inclusión (Merkle), sin almacenar el Blockchain completo.
- ¿Por qué? Reduce la dependencia del nodo por defecto de Blockstream, sin dejar de ser ligero para los dispositivos.
- **Desventaja**: Menos seguro que un Full node, ya que depende de nodos de terceros para cierta información.
- **Recomendación**: Active SPV si no puede utilizar un nodo personal, pero prefiere un Full node para una seguridad óptima.



![image](assets/fr/07.webp)



## 4. Conexión de una Hardware Wallet a Blockstream App



### 4.1. 1. Consideraciones preliminares



#### 4.1.1. Para los usuarios de Ledger





- Blockstream Green sólo admite la aplicación **Bitcoin Legacy** en dispositivos Ledger (Nano S, Nano X).
- Pasos a seguir en **Ledger Live** antes de conectar su dispositivo :


1. Ve a **"Ajustes "** → **"Funciones experimentales "** y activa el **modo desarrollador**.


2. Vaya a **"Mi Ledger"** → **"Catálogo de aplicaciones "** y, a continuación, instale la aplicación **Bitcoin Legacy**


3. Abra la aplicación **Bitcoin Legacy** en su Ledger antes de iniciar Blockstream Green para establecer la conexión.




- **Nota**: Asegúrese de que su Ledger está desbloqueado con su código PIN y que la aplicación Bitcoin Legacy está activa cuando se conecte.



#### 4.1.2 Inicialización de una Hardware Wallet





- Si su Hardware Wallet (Ledger, Trezor o Blockstream Jade) no se ha utilizado nunca (ni con Blockstream Green, ni con otro software como Ledger Live), primero tendrá que inicializarlo. Este paso implica, en un entorno seguro, sin cámaras ni observadores:


1. **Generación de frases seed / Frase Mnemonic** (12, 18 ó 24 palabras): Escríbela cuidadosamente en un papel.


2. **Verificación de la frase seed**: Comprobar la importación de Wallet a partir de las palabras anotadas, por ejemplo, verificando la clave pública ampliada. A realizar antes de enviar fondos a Wallet y asegurar permanentemente la frase seed.


3. **Guardar la frase seed**: Guarda la frase en un soporte físico (papel o metal) y en un lugar seguro. Nunca la almacenes digitalmente (ni capturas de pantalla, ni en la nube, ni por correo electrónico).




- **Importante**: La frase seed es su único medio de recuperar sus fondos si el dispositivo se pierde o funciona mal. Cualquiera con acceso puede robar tus bitcoins.
- **Recursos** para realizar copias de seguridad y comprobar la sentencia seed :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

#### 4.1.3. Configuración para este tutorial :





- Supondremos que la Hardware Wallet ya ha sido inicializada con una frase seed y un código PIN de bloqueo.
- Suponemos que la Hardware Wallet nunca se ha conectado a Blockstream App, lo que requiere la creación de una nueva cuenta. Si la Hardware Wallet ya se ha utilizado con Blockstream App, la cuenta aparecerá automáticamente al abrir la aplicación.



### 4.2. Iniciar conexión





- En la pantalla de inicio, haga clic en "**Configurar una nueva Wallet**", luego valide los términos y condiciones y haga clic en "**Empezar**" :



![image](assets/fr/08.webp)





- Seleccione la opción "**En Hardware Wallet**":



![image](assets/fr/09.webp)





- Si estás utilizando un **Blockstream Jade**, haz clic en el botón correspondiente. De lo contrario, selecciona "**Conectar un dispositivo de hardware diferente**" :



![image](assets/fr/10.webp)





- Conecta tu Hardware Wallet al ordenador mediante USB y selecciónalo en Blockstream App :



![image](assets/fr/22.webp)





- Espere mientras Blockstream App importa la información de su cartera:



![image](assets/fr/23.webp)



### 4.3. 3. Crear una cuenta





- Si tu Hardware Wallet ya se ha utilizado con Blockstream App, tu cuenta aparecerá automáticamente en la Interface tras la importación. De lo contrario, cree una cuenta haciendo clic en "**Crear cuenta**" :



![image](assets/fr/24.webp)





- Elija "**Estándar**" para configurar una cartera Bitcoin clásica:



![image](assets/fr/25.webp)





- Una vez creada su cuenta, podrá acceder a su cartera principal de Interface:



![image](assets/fr/26.webp)





## 5. Uso de la Wallet en cadena con una Hardware Wallet



### 5.1. Recibir bitcoins





- En la pantalla principal de la cartera, haga clic en "**Recibir**" :



![image](assets/fr/27.webp)





- La aplicación muestra un ** Address de recepción en blanco**. Utilizar un Address nuevo para cada recepción mejora su confidencialidad. Haga clic en "**Copiar Address**" para copiar la Address, o deje que el remitente escanee el código QR que se muestra:



![image](assets/fr/12.webp)



**Opciones** :




- (1) Haga clic en las flechas para generate una nueva Address vinculada a su cartera.
- (2) Para solicitar un importe concreto, haga clic en "**Más opciones**" y, a continuación, en "**Solicitar importe**". El QR se actualizará, y el Address se sustituirá por un URI de pago Bitcoin como: `Bitcoin:bc1q...?amount=0.00001`



![image](assets/fr/13.webp)





- (3) Para reutilizar una Address anterior, haga clic en "**Más opciones**" y luego en "**Lista de direcciones**" :



![image](assets/fr/14.webp)





- **Verificación**: Comprueba cuidadosamente el Address compartido para evitar errores o ataques (por ejemplo, que un malware modifique el portapapeles).
- Una vez que la transacción se haya difundido en la red, aparecerá en su Wallet. Espere de 1 a 6 confirmaciones para considerar la transacción inmodificable.



![image](assets/fr/28.webp)



### 5.2. enviar bitcoins





- En la pantalla principal de la cartera, haga clic en "**Enviar**".



![image](assets/fr/29.webp)





- Introduzca los datos:
    - (1) Compruebe que el activo seleccionado es **Bitcoin** (onchain).
    - (2) Introduce el **Address del destinatario** pegándolo o escaneando un código QR con tu webcam.
    - (3) Indique el **importe** a enviar (en BTC, satoshis u otras unidades).




![image](assets/fr/16.webp)





- Seleccione **tarifas de transacción** (opcional) :
 - Elija entre las opciones propuestas (rápido, medio, lento) según la urgencia, con un tiempo estimado de confirmación.
 - Para tarifas personalizadas, ajuste manualmente el número de satoshis por vbyte. Estos se muestran en la pantalla de inicio. Véase también [Mempool.space](https://Mempool.space/).



![image](assets/fr/17.webp)





- **Selección manual de UTXOs** (opcional): Haga clic en "**Selección manual de Coin**" para elegir los UTXO específicos que se utilizarán en la transacción.



![image](assets/fr/18.webp)





- **Verificación preliminar**: Compruebe la Address, el importe y las tasas en la pantalla de resumen y, a continuación, pulse "**Confirmar transacción**". En realidad, la transacción no se liberará a la red hasta que la haya firmado con su Hardware Wallet, que es la única que tiene las claves secretas asociadas a las direcciones de las que se cargarán los UTXO (satoshis).



![image](assets/fr/19.webp)





- **Comprobación final y firma**: Asegúrese de que todos los parámetros de la transacción son correctos **en su pantalla Hardware Wallet** y, a continuación, firme la transacción utilizándola. Un error en Address puede provocar la pérdida irreversible de fondos.





- **Difusión**: Una vez firmada, Blockstream App difunde automáticamente la transacción en la red Bitcoin.



![image](assets/fr/20.webp)





- **Seguimiento**:
 - La transacción aparece en la pantalla de inicio de Wallet como "pendiente" hasta que se confirme.
 - Mientras no se haya confirmado la transacción, puede utilizarse la función **Replace-by-fee (RBF)** para acelerar la confirmación aumentando la comisión (véase el Apéndice).



![image](assets/fr/21.webp)



## Apéndices



### A1. Otros tutoriales de Blockstream





- Uso de la Liquid Network :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Importación y seguimiento de una cartera en "Watch-Only" :



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb



- Uso de la aplicación Blockstream en teléfonos móviles (Hot Wallet) :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

### A2. Explicación de Replace-by-fee (RBF)





- **Definición**: Replace-by-fee (RBF) es una característica de la red Bitcoin que permite al remitente acelerar la confirmación de una transacción **onchain** aumentando la comisión.
- **Límites**:
    - RBF no está disponible para las transacciones Liquid o Lightning.
    - La transacción inicial debe marcarse como compatible con RBF, lo que Blockstream App hace automáticamente.
- Para más información, consulte [nuestro glosario](https://planb.network/resources/glossary/rbf-replacebyfee).



### A3. Buenas prácticas





- **Asegura tu frase de recuperación**:
    - Guarde su frase Hardware Wallet's Mnemonic en un soporte físico (papel, metal) en un lugar seguro.
    - Nunca lo almacenes digitalmente (nube, correo electrónico, captura de pantalla).
    - Tutorial : Guarda tu frase Mnemonic :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Proteja su intimidad**:





    - generate una nueva Address para cada recepción en cadena.
    - Active **Tor** o **SPV** para limitar el seguimiento.
    - Conéctese a su propio nodo Bitcoin a través de Electrum para obtener la máxima soberanía.
- **Compruebe siempre las direcciones de envío**:





    - Compruebe el Address en su pantalla Hardware Wallet antes de firmar.
    - Utilice copiar/pegar o un código QR para evitar errores manuales.
- **Optimizar los costes**:





    - Ajustar las tarifas en función de la urgencia y la congestión de la red (véase [Mempool.space](https://Mempool.space/)).
    - Utiliza Liquid o Lightning para transacciones rápidas y de bajo coste que no requieran seguridad onchain.
- **Actualizar el software**:





    - Mantén tu aplicación Blockstream y el firmware Hardware Wallet actualizados con las últimas funciones y parches de seguridad.



### A4. Recursos adicionales





- **Enlaces oficiales**:
    - [Sitio web oficial](https://blockstream.com/)
    - [Soporte para Blockstream App](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): documentación y chat
    - [GitHub](https://github.com/Blockstream/green_qt)





- **Exploradores de bloques**:
    - Cadena : [Mempool.space](https://Mempool.space/)
    - Liquid : [Información Blockstream](https://blockstream.info/Liquid)
    - Rayo : [1ML (Lightning Network)](https://1ml.com/)





- Asegurar su frase de recuperación:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Liquid Network** :



[Glosario](https://planb.network/fr/resources/glossary/liquid-network)



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727



- **Lightning Network**:



[Glosario](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb