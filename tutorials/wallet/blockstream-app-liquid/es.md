---
name: Blockstream App - Liquid
description: Cómo configurar Blockstream App y utilizar Liquid Network
---
![cover](assets/cover.webp)


## 1. Introducción


### 1.1 Objetivo de la tutoría





- Este tutorial explica cómo utilizar la aplicación móvil **Blockstream App** para gestionar una cartera **Bitcoin Liquid**, es decir, transacciones registradas directamente en la cadena lateral Bitcoin "Liquid".
- Cubre la instalación, la configuración inicial, la creación de una Software Wallet, y las operaciones para recibir y enviar bitcoins en Liquid.
- Nota: Otros tutoriales en los Apéndices cubren Onchain, Watch-Only y la versión de escritorio.



### 1.2 Destinatarios





- **Principiantes**: Usuarios que deseen gestionar sus bitcoins con una aplicación móvil intuitiva, integrando la Liquid Network.
- **Usuarios intermedios**: Personas que buscan entender las funcionalidades de onchain y opciones de privacidad como Tor o SPV.



### 1.3 Presentación de Liquid



**Liquid** es un **Sidechain** de Bitcoin, desarrollado por **[Blockstream](https://blockstream.com/Liquid/)**, diseñado para ofrecer mayor velocidad, más Confidential Transactions y funcionalidad avanzada, sin dejar de estar conectado al Blockchain principal Bitcoin.



Una Sidechain es una Blockchain independiente que opera en paralelo con la Bitcoin, utilizando un mecanismo conocido como **two-way peg**. Este sistema bloquea bitcoins en la Blockchain principal para crear **Liquid-Bitcoins (L-BTC)**, tokens que circulan en la Liquid Network manteniendo la paridad de valor con los bitcoins originales. Los fondos pueden devolverse a la Blockchain Bitcoin en cualquier momento.



![image](assets/fr/17.webp)






- (1) **Peg-in**: La federación Liquid bloquea los Bitcoins (BTC) en la Blockchain principal. A cambio, una cantidad equivalente de Liquid-Bitcoins (L-BTC), que garantiza la paridad entre las dos cadenas, se emite en la Blockchain Liquid y se envía al usuario.





- (2) **Transacciones independientes**: Las transacciones pueden ejecutarse simultánea e independientemente en la Blockchain principal (BTC) y en la Sidechain Liquid (L-BTC), en función de las necesidades del usuario.





- (3) **Peg-out**: El usuario envía bitcoins Liquid (L-BTC) a la federación Liquid. La federación desbloquea entonces una cantidad equivalente de bitcoins (BTC) en la Blockchain principal y los transfiere al usuario. La federación desbloquea entonces una cantidad equivalente de bitcoins (BTC) en el Blockchain principal y los transfiere al usuario.



Liquid se basa en una **federación** de participantes de confianza (bolsas, empresas reconocidas de Bitcoin) que gestionan la validación de bloques y el anclaje bilateral. A diferencia de Blockchain Bitcoin, que está descentralizada y depende de los mineros, Liquid es una red **federada**, lo que significa que su seguridad y gobernanza dependen de estos participantes. Aunque esto implica un compromiso en la descentralización, permite un rendimiento optimizado y una funcionalidad avanzada.



![image](assets/fr/18.webp)



##### ¿Por qué Liquid?





- **Rapidez**: Las transacciones en Liquid se confirman en alrededor de **1 minuto**, frente a los 10 minutos o más de las transacciones onchain, gracias a los bloques generados cada minuto por una federación de validadores.
- **Mayor confidencialidad**: Liquid utiliza **Confidential Transactions**, que oculta la cantidad y el tipo de activo transferido, lo que hace que las transacciones sean más privadas (aunque las direcciones siguen siendo visibles).
- **Comisiones bajas**: Las transacciones en Liquid suelen ser menos costosas, lo que las hace ideales para transferencias frecuentes o de pequeñas cantidades.
- **Múltiples activos**: Además de L-BTCs, Liquid admite la emisión de otros activos digitales, como stablecoins o tokens, para su uso en aplicaciones específicas.
- **Casos de uso**: Liquid es especialmente adecuada para intercambios entre plataformas, pagos rápidos o aplicaciones que requieran contratos inteligentes, sin dejar de estar vinculada a la seguridad de Bitcoin.



**Nota: Este tutorial se centra en el uso de Liquid a través de la aplicación Blockstream. Para una comprensión en profundidad de la Liquid Network, encontrará recursos en el apéndice.**



### 1.4. Hot Wallet recordatorio





- **Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: todos los nombres de una aplicación instalada en un smartphone, un ordenador o cualquier dispositivo conectado a Internet, que permite gestionar y proteger las claves privadas de un Bitcoin Wallet.
- A diferencia de los **monederos de hardware**, también conocidos como **monederos Cold**, que aíslan las claves fuera de línea, los monederos de software funcionan en un entorno conectado, lo que los hace más vulnerables a los ciberataques.





- **Uso recomendado**:
    - Ideal para gestionar cantidades moderadas de Bitcoin, especialmente para transacciones diarias.
    - Adecuado para principiantes o usuarios con recursos limitados, para quienes un Hardware Wallet puede parecer superfluo.





- **Limitaciones**: Menos segura para almacenar grandes fondos o ahorros a largo plazo. En este caso, elige una Hardware Wallet.




## 2. Presentación de la aplicación Blockstream





- **Blockstream App** es una aplicación móvil (iOS, Android) y de escritorio para gestionar carteras Bitcoin y activos en Liquid Network. Adquirida por [Blockstream](https://blockstream.com/) en 2016, antes se llamaba *Green Address* y después *Blockstream Green*.
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





- **Función**: Conecta la aplicación a tu propio **nodo Bitcoin completo** a través de un **servidor de Electrum**.
- ¿Por qué? Proporciona un control total sobre los datos Blockchain, eliminando la dependencia de los servidores Blockstream.
- **Requisito**: Un nodo Bitcoin configurado.
- **Recomendación**: Usuarios avanzados que deseen la máxima soberanía.



#### 3.2.4. Verificación SPV





- **Función**: Utiliza **Verificación simplificada de pagos (SPV)** para verificar directamente determinados datos de Blockchain sin necesidad de descargar toda la cadena.
- ¿Por qué? Reduce la dependencia del nodo por defecto de Blockstream, sin dejar de ser ligero para los dispositivos móviles.
- **Desventaja**: Menos seguro que un Full node, ya que depende de nodos de terceros para cierta información.
- **Recomendación**: Active SPV si no puede utilizar un nodo personal, pero prefiere un Full node para una seguridad óptima.





## 4. Creación de una cartera Bitcoin onchain



### 4.1. Iniciar la creación





- **Precaución**: Instale su cartera en un entorno privado, sin cámaras ni observadores.
- En la pantalla de inicio, haz clic en "Empezar" :



![image](assets/fr/04.webp)





- Si desea gestionar un **Cold Wallet** (Wallet sin conexión): haga clic en **"Conectar Jade "** para utilizar el Blockstream Jade Hardware Wallet u otros monederos Cold compatibles.



![image](assets/fr/05.webp)






- Aparece la siguiente pantalla:



![image](assets/fr/06.webp)






- (1) **"Configurar Wallet móvil "** : Crear un nuevo Hot Wallet (Hot Wallet).
- (2) **"Restaurar desde copia de seguridad "**: Importa una cartera existente utilizando una frase Mnemonic (12 o 24 palabras). Atención: No importe la frase desde una Cold Wallet, ya que quedará expuesta en un dispositivo conectado, invalidando su seguridad.
- (3) **"Watch-Only "**: Importe una cartera existente de sólo lectura, para ver el saldo (por ejemplo, de su Cold Wallet) sin exponer la frase Mnemonic. Consulte el tutorial "Watch Only" en el apéndice.



**En este tutorial**: Haga clic en **"Configurar Wallet móvil "** para crear un Hot Wallet.


Tu Wallet se crea automáticamente y aparece la página de inicio de Wallet, aquí llamada "Mi Wallet 5":



![image](assets/fr/07.webp)



**Importante**: Blockstream App ha simplificado la creación de una Wallet al no mostrar automáticamente la frase seed de 12 palabras. *Aunque ahora la cartera se crea con un solo clic, corres el riesgo de perder el acceso a tus fondos si no guardas la frase seed*.



### 4.2. Guardar frase seed





- En la pantalla de inicio de Wallet, haz clic en la pestaña "Seguridad" y, a continuación, en la indicación "Copia de seguridad" o en el menú "Frase de recuperación":



![image](assets/fr/08.webp)



Aparecerá la frase de 12 palabras seed para que la guardes.





- Escriba su frase de recuperación con sumo cuidado. Escríbela en papel o metal y guárdala en un lugar seguro (ubicación segura y sin conexión). Esta frase es tu único medio de acceder a tus bitcoins en caso de pérdida de tu dispositivo o borrado de la aplicación.
- También es importante tener en cuenta que cualquiera con esta frase puede robarte todos tus bitcoins. Nunca los almacenes digitalmente:
 - Sin captura de pantalla
 - Sin copias de seguridad en la nube, correo electrónico o mensajería
 - Sin copiar/pegar (riesgo de guardar en el portapapeles)



**¡!** Este punto es crítico. Para más información sobre las copias de seguridad:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3. Comprobar frase seed



Antes de enviar fondos a una Address asociada a esta frase seed, debe probar el respaldo de sus 12 palabras.


Para ello, anotaremos una referencia, borraremos el Wallet, lo restauraremos con la copia de seguridad y comprobaremos que la referencia no ha cambiado.





- En la pantalla de inicio de Wallet, haz clic en la pestaña "Configuración", luego en "Detalles de Wallet" y copia la zPub ([clave pública extendida](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f):



![image](assets/fr/09.webp)



Nota: se puede importar una Address zpub a la aplicación Blockstream para la función "Sólo vigilancia" (véase el Apéndice).





- Borre la aplicación, luego restaure la Wallet a través de **"Restaurar desde copia de seguridad "** introduciendo la frase Mnemonic, y compruebe que el zpub no ha cambiado. Si es así, entonces su copia de seguridad es correcta, y usted puede enviar fondos a la Wallet.





- Para saber más sobre cómo realizar una prueba de recuperación, aquí tienes un tutorial dedicado :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.4. Asegurar el acceso a la aplicación



Bloquee el acceso a la aplicación con un código PIN seguro:




- Desde la pantalla de inicio de Wallet, ve a **"Seguridad "** y luego haz clic en **"PIN "**
- Introduzca y confirme **un código PIN aleatorio de 6 dígitos**.



**Opción biométrica**: Disponible para mayor comodidad, pero menos segura que un código PIN robusto (riesgo de acceso no autorizado, por ejemplo, huella dactilar o escaneado facial durante el sueño).



**Nota**: El PIN asegura el dispositivo, pero sólo la frase seed se puede utilizar para recuperar los fondos.





## 5. Utilización de la Liquid Wallet



### 5.1. Recibir bitcoins "L-BTC



Para recibir Liquid-Bitcoins (L-BTC), existen varias opciones. Puedes pedirle a alguien que te envíe algunos directamente compartiendo un Liquid que reciba Address, lo que se detalla a continuación.



Alternativamente, Exchange sus bitcoins onchain o a través de la Lightning Network para L-BTC utilizando [un puente como Boltz](https://boltz.Exchange/): introduzca su Liquid recibiendo Address, realice el pago como prefiera y reciba su L-BTC.





- Desde la pantalla de inicio de la cartera, haga clic en '"**Transaccionar**" y luego en **"Recibir "**.



![image](assets/fr/19.webp)





- Por defecto, la aplicación muestra un **recibo Address, onchain** en blanco (formato SegWit v0, empezando por `bc1q...`). Haga clic en "Bitcoin" para seleccionar **Liquid Bitcoin** :



![image](assets/fr/20.webp)





- **Opciones**:
 - (1) Haga clic en las flechas para seleccionar otro nuevo Address vinculado a esta sentencia seed.
    - (2) También puede elegir una Address de entre las ya utilizadas/mostradas, haciendo clic en los tres puntos de la parte superior derecha y, a continuación, en "Lista de direcciones"
    - (3) Para solicitar un importe específico, haga clic en los tres puntos de la parte superior derecha, seleccione "Solicitar importe" e introduzca el importe deseado. El QR se actualizará y el Address se sustituirá por un URI de pago Bitcoin.



![image](assets/fr/21.webp)





- Comparta la Address/URI haciendo clic en "**Compartir**", copiando el texto o escaneando el código QR.
- **Verificación**: Comprueba en la medida de lo posible el Address compartido con el destinatario para evitar errores o ataques (por ejemplo, que un malware modifique el portapapeles).



### 5.2. enviar bitcoins





- En la pantalla de inicio de la cartera, haga clic en "**Transaccionar**" y luego en **"Enviar "** :



![image](assets/fr/22.webp)





- Introduzca los datos:
    - (1) Introduzca el **Address del destinatario** pegándolo o escaneando un código QR.
    - (2) Compruebe los activos y la cuenta desde la que se envían los fondos.
    - (3) Indique el **importe** a enviar. Puede elegir la unidad: L-BTC, L-satoshis, USD, ...



![image](assets/fr/23.webp)





- Comprueba..:
    - Compruebe la Address, el importe y los gastos en la pantalla de resumen.
    - Un error Address puede provocar una pérdida irreversible de fondos. Cuidado con los programas maliciosos que modifican el portapapeles.



![image](assets/fr/24.webp)





- **Confirmación**: Deslice el botón "Enviar" para firmar y distribuir la transacción.
- **Seguimiento**: En la pestaña "Transacciones" de Wallet, la transacción aparece como "Sin confirmar", luego como "Confirmada" y después como "Completada":



![image](assets/fr/25.webp)





- El tiempo entre 2 bloques es de 1 minuto en Liquid, por lo que la transacción se confirma y completa rápidamente.




## Apéndices



### A1. Otros tutoriales de Blockstream App



Uso de la red Onchain



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

Importación y seguimiento de una Wallet en modo "Sólo vigilancia



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Versión de sobremesa



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da



### A2. Buenas prácticas



Para utilizar **Blockstream App** de forma segura y eficiente, siga estas recomendaciones. Le ayudarán a proteger sus fondos, optimizar sus transacciones y preservar su confidencialidad en las redes **Bitcoin (onchain)**, **Liquid** y **Lightning**.





- **Asegura tu frase de recuperación**:
 - Tutorial: Cómo guardar su frase Mnemonic



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Utilizar autenticación segura**:
 - Activar un **PIN fuerte** o **autenticación biométrica** (huella dactilar o reconocimiento facial) para proteger el acceso a la aplicación.
 - Nunca compartas tu PIN ni tus datos biométricos.





- **Proteja su intimidad**:
 - generate una nueva Address para cada recepción en cadena o Liquid para limitar el rastreo en la Blockchain.
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




### A3. Recursos adicionales





- **Enlaces oficiales:**
- [Sitio web oficial](https://blockstream.com/)
- [Soporte para la aplicación móvil](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): documentación y chat
- [GitHub](https://github.com/Blockstream/green_android)





- Exploradores de bloques :**
 - on chain : **[Mempool.space](https://Mempool.space/)**
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