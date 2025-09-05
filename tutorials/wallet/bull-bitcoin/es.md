---
name: Toro Bitcoin Wallet
description: Descubra cómo utilizar la Wallet Bull Bitcoin
---

![cover](assets/cover.webp)



Esta guía le lleva a través de la instalación, configuración y uso de Bull Bitcoin Mobile. Aprenderá a recibir y enviar fondos en las tres redes: onchain, Liquid y Lightning, y a transferir su Bitcoin de una red a otra. Los apéndices proporcionan recursos y contactos, información de fondo y breves explicaciones de conceptos técnicos.



## Introducción



**Bull Bitcoin Mobile**, desarrollado por **[Bull Bitcoin](https://www.bullbitcoin.com/)** ([crear cuenta](https://app.bullbitcoin.com/registration/orangepeel)), es un ** Wallet de Bitcoin autocustodiado**, lo que significa que tiene pleno control sobre sus claves privadas y, por tanto, sobre sus fondos, sin depender de terceros. De código abierto y arraigada en una filosofía Cypherpunk, esta Wallet combina simplicidad, confidencialidad y funciones avanzadas como los intercambios entre redes y la compatibilidad con PayJoin. Te permite gestionar tus bitcoins en tres redes: **Bitcoin onchain**, **Liquid** y **Lightning**, cada una adaptada a usos específicos.



### Contexto de desarrollo



Wallet responde a un reto importante: Las tarifas de la red Bitcoin son inadecuadas para los pequeños pagos, o para abrir pequeños canales Lightning autogestionados. Wallet Bull Bitcoin Mobile ofrece una solución de autocustodia al tiempo que se apoya en las 3 principales redes Bitcoin:





- Red Bitcoin (onchain)**: Ideal para el almacenamiento a medio y largo plazo de UTXOs y transacciones de gran valor, donde las comisiones son proporcionalmente insignificantes.
- Liquid Network**: Diseñado para transacciones rápidas (~2 minutos), más confidenciales (cantidades ocultas) y de bajo coste, perfecto para acumular pequeñas cantidades o proteger su privacidad.
- Red Lightning**: Optimizada para pagos instantáneos y de bajo coste, adecuada para transacciones diarias de valor pequeño o medio.



Con Bull Bitcoin Mobile, por ejemplo, puedes acumular pequeñas cantidades en las carteras **Liquid** o **Lightning** y luego, una vez alcanzada una cantidad significativa, puedes :





- Transferencia a la red onchain para un almacenamiento seguro a medio o largo plazo, con una confidencialidad mejorada con Liquid y/o Lightning en sentido ascendente, y con tarifas onchain para una única transacción



### Evolución continua



Wallet evoluciona constantemente, así que no te sorprendas si encuentras discrepancias entre este tutorial y tu aplicación actualizada.




- Por ejemplo, a partir del 19/07/2025, los botones **"Comprar / Vender / Pagar "** están visibles pero en gris en la aplicación, ya que estas opciones, disponibles en Exchange [bullbitcoin.com](https://app.bullbitcoin.com/registration/orangepeel), pronto se integrarán para una experiencia unificada. Su uso seguirá siendo totalmente opcional. Muchos otros desarrollos están en curso o previstos: gestión multi-Wallet, passphrase, compatibilidad con los monederos hardware...
- En [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49), puede consultar los temas actuales y los próximos desarrollos. Como el proyecto es 100% de código abierto y "construido en público", también puedes enviarnos tus sugerencias y cualquier error que encuentres.




## 1. Requisitos previos



Antes de empezar a utilizar **Bull Bitcoin Mobile**, asegúrese de que dispone de los siguientes elementos:





- Smartphone compatible**: Un dispositivo **iOS** (iPhone o iPad) o **Android**
- Conexión a Internet
- Asegure los soportes de copia de seguridad**: Escribe tu **frase de recuperación** (12 palabras) en papel o metal y guárdala en un lugar seguro.
- Conocimientos básicos**: Una comprensión mínima de los conceptos de Bitcoin (direcciones, transacciones, tasas) es útil, aunque este tutorial explica cada paso para principiantes.



## 2. Instalación





- Descargar la solicitud** :
 - [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&pcampaignid=web_share)** Descargar de la tienda de aplicaciones para dispositivos Android
 - [GitHub](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) Descarga directamente el APK para dispositivos Android**
 - [iOS](https://testflight.apple.com/join/FJbE4JPN)** Descarga a través de TestFlight para dispositivos Apple
 - Compruebe el nombre del promotor (Bull Bitcoin) para evitar solicitudes fraudulentas.
 - Asegúrese de que la versión descargada corresponde a la última versión estable indicada en GitHub.
 - Bull Bitcoin Mobile es **de código abierto**. Para ver el código: [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49)





- Instalar la aplicación




## 3. Configuración inicial



### 3.1 Inicie la aplicación :



La aplicación utiliza una única frase de recuperación de 12 palabras para ambas carteras:




 - seguro Bitcoin' Wallet**: Para transacciones en la red Bitcoin (onchain)
 - instant Payments' Wallet**: Para transacciones instantáneas en las redes Liquid y Lightning



Al abrirlo, se le pedirá que importe una frase de recuperación existente o que cree una nueva Wallet :



![image](assets/fr/02.webp)



### 3.2 Frase de recuperación :



Si desea reutilizar una Wallet existente, haga clic en "**Recuperar Wallet**" y rellene las 12 palabras de su frase de recuperación.



De lo contrario, haga clic en "**Crear nuevo Wallet**" :




- Escriba su frase de recuperación con sumo cuidado. Escríbela en papel o metal y guárdala en un lugar seguro (caja fuerte, ubicación fuera de línea). Esta frase es tu único medio de acceder a tus bitcoins en caso de pérdida de tu dispositivo o de borrado de la aplicación.
- También es importante tener en cuenta que cualquiera con esta frase puede robarte todos tus bitcoins. Nunca los almacenes digitalmente:
 - Sin captura de pantalla
 - Sin copias de seguridad en la nube, correo electrónico o mensajería
 - Sin copiar/pegar (riesgo de guardar en el portapapeles)



*¡*! Este punto es crítico**. Para más ayuda :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 3.3 Asegurar el acceso :





- Vaya a configuración y haga clic en **Código PIN**.
- Establezca un sólido **código PIN** para proteger el acceso a la aplicación.
- Este paso es opcional, pero se recomienda encarecidamente para evitar que cualquier persona con acceso a su teléfono pueda acceder a su Wallet.



![image](assets/fr/03.webp)



### 3.4 Conexión a un nodo personal (opcional):



BullBitcoin Wallet se conecta por defecto a los servidores Electrum: el primero gestionado por Bull Bitcoin y un servidor secundario de Blockstream, ambos se considera que no guardan registros, lo que reduce el riesgo de rastreo.



Para una mayor confidencialidad, puede conectar la aplicación a su propio nodo Bitcoin a través de un servidor Electrum (instrucciones disponibles en [GitHub de BullBitcoin](https://github.com/orgs/SatoshiPortal/projects/49) ).




## 4. Recepción de fondos



Recibir fondos con **Bull Bitcoin Mobile** es sencillo y se adapta a sus necesidades, tanto si utiliza :




  - la red **Bitcoin (onchain)** para su conservación a largo plazo,
  - la red **Liquid** para un Confidential Transactions más rápido,
  - la red **Lightning** para pagos instantáneos de poco valor.



La aplicación genera automáticamente direcciones de recepción Lightning o Invoice, en función de la red seleccionada. A continuación se indica cómo proceder para cada red.



### 4.1. onchain (red Bitcoin)



En la pantalla de inicio, puede :




- o seleccione el **Secure Bitcoin Wallet** y haga clic en "**Recibir "** :



![image](assets/fr/04.webp)





- o haga clic en "**Recibir "** y, a continuación, elija la red **Bitcoin**:



![image](assets/fr/05.webp)



#### 4.1.1. Opción "Sólo copiar o escanear Address" desactivada (por defecto)



![image](assets/fr/06.webp)





- Permite acceder a parámetros avanzados opcionales. Puede especificar :
 - Una **cantidad** en BTC, Sats o fiat.
 - Una **nota personal** que se incluirá en la copia del URI / Código QR.
 - Activación de **PayJoin** (véase el apéndice 3 para más detalles), que mejora la confidencialidad combinando las entradas de remitente y destinatario.





- Ejemplo de URI generado automáticamente** :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=2.1e-7&message=Exemple+de+note&pj=HTTPS%3A%2F%2FPAYJO.IN%2FUJA9LJ6L4CMHY%23RK1QT3YSGFC6PMKRUXND2DSGQMLESTUNH29AY0305XAQ678742CVT5ES+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1RRH8C6Q
```





- Uso**: Copia el URI para compartirlo con el remitente, o deja que escanee el código QR.



#### 4.1.2. Opción "Copiar o escanear sólo Address" activada



![image](assets/fr/07.webp)





- Con la opción **"Copiar o escanear sólo Address"** activada, la aplicación genera un Bitcoin Address simple en formato SegWit (bech32).





- Ejemplo:



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```



Aunque introduzca un importe o una nota, no se incluirán en el código QR ni en la copia de la Address





- Uso**: Copia el Address para compartirlo con el remitente, o deja que escanee el código QR.



#### 4.1.3. Generar un nuevo Address





- ¿Por qué utilizar una Address nueva para cada transacción? Esto **protege su privacidad** impidiendo que varios pagos se vinculen a la misma Address, y limita las posibilidades de seguimiento en la Blockchain.
 - Por defecto, Bull Bitcoin genera automáticamente un Address.** sin utilizar
 - Puede forzar la creación de un nuevo Address haciendo clic en **"Nuevo Address"** en la parte inferior de la pantalla.
 - Todas sus direcciones están vinculadas a su frase seed: no importa cuántas direcciones utilice, su cartera mostrará un único saldo y podrá consolidar automáticamente los fondos cuando se realice un envío.





- Consejo: Utilice siempre el nuevo Address** proporcionado por Bull Bitcoin, a menos que tenga una necesidad específica (por ejemplo, un Address público para recibir donaciones).



### 4.2. Liquid



En la pantalla de inicio, puede :




- o seleccione los **Pagos instantáneos Wallet** y luego haga clic en **"Recibir "** y luego en **"Liquid"** :



![image](assets/fr/08.webp)





- o haga clic en "**Recibir "** y, a continuación, elija la red **Liquid**:



![image](assets/fr/09.webp)



Una vez en la pantalla **"Recibir "**, copie una Liquid Address:





- Sin importe ni nota. Ejemplo:



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```





- O especificando un **importe** (en BTC, Sats o fiat) y/o una **nota personal** que se incluirá en la copia del URI / Código QR. Ejemplo:



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



**Utilizar**: Copia el Address/URI para compartirlo con el remitente, o deja que escanee el código QR.



### 4.3. Rayo



En la pantalla de inicio, puede :




- o seleccione los **Pagos instantáneos Wallet** y, a continuación, haga clic en "**Recibir "** :



![image](assets/fr/10.webp)





- o haga clic en "**Recibir "** y, a continuación, elija la red **Rayo**:



![image](assets/fr/11.webp)



#### 4.3.1. Funcionamiento, límites y ventajas





- Mecanismo**: Bull Bitcoin Wallet es una Wallet que permite realizar y recibir pagos a través de Lightning. Los fondos recibidos a través de Lightning se almacenan en la red **Liquid** (en los pagos instantáneos Wallet) gracias a un intercambio automático a través de **Boltz**. Esto te da la posibilidad de interactuar con Lightning sin tener que gestionar canales de liquidez, permaneciendo en autocustodia.





- Límites:**
 - Una cantidad mínima** de 100 satoshis (a partir del 19/07/2025) al generate la Invoice.
 - Usted paga los gastos**, que se deducirán del importe enviado por el remitente, a diferencia de la recepción con Wallet Lightning native, en la que sólo el remitente paga los gastos de transferencia además del importe enviado. A 19/07/2025, 47 Sats se deducen del importe enviado.





- Ventajas** :
 - Autocustodia**: Sus fondos permanecen bajo su control, almacenados en la Liquid Network.
 - Sin elevadas comisiones onchain**: El almacenamiento en Liquid evita costosos depósitos onchain para abrir su canal Lightning o añadir liquidez. Estas operaciones pueden realizarse más adelante, cuando la cantidad acumulada en Liquid justifique las comisiones.





- Sugerencia:** Si el remitente dispone de Wallet Bull Bitcoin, utilice directamente el Liquid Network para evitar gastos de intercambio



#### 4.3.2. generate Invoice





- Introduzca un **importe** (en BTC, Sats o fiat)





- Añada una **nota personal** que se integrará en la Invoice. Si el remitente paga la Invoice, su Wallet también la incluirá en los detalles de la transacción.





- Validez del Invoice:** El Invoice relámpago es válido durante **12 horas**. Transcurrido este tiempo, caduca y ya no se puede pagar. Deberá generarse una nueva Invoice.





- Uso**: Copia el Invoice para compartirlo con el remitente, o deja que escanee el código QR.




## 5. Envío de fondos



### 5.1. 1. Principio básico



Desde la página de inicio o desde los monederos :



![image](assets/fr/12.webp)



para acceder a la pantalla de envío:



![image](assets/fr/13.webp)



**Bull Bitcoin Mobile** facilita el envío de dinero detectando automáticamente la red (Bitcoin, Liquid o Lightning) en función de la Address o Invoice introducida (copiada o escaneada mediante código QR).



### 5.2. transmisión en cadena (red Bitcoin)



#### 5.2.1. Pantalla de envío



**Acción**: Introducir o escanear un Bitcoin onchain Address





- Si no se ha definido el importe, por ejemplo :



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```





- A continuación, puede elegir en la pantalla de envío :
 - Importe en BTC, sat o fiat. Importe mínimo: 546 satoshis el 22/07/2025.
 - Una nota opcional para identificar la transacción. Solo visible para usted, en los detalles de la transacción.



![image](assets/fr/14.webp)





- Si el importe ya se ha definido, por ejemplo :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



A continuación, accederá directamente a la siguiente pantalla de confirmación.



#### 5.2.2 Pantalla de confirmación



Tómese su tiempo para comprobar todos los parámetros, especialmente el importe, el destino Address y las tasas.


A continuación, puedes ajustar los parámetros:



![image](assets/fr/15.webp)




- Tarifas**: Puede elegir :
  - Se estimará la velocidad de ejecución** de su transacción y las comisiones asociadas
  - Se estimarán las comisiones**, en modo Absoluto (comisiones totales en satoshis) o Relativo (comisiones por byte), y la velocidad de su transacción





- Ajustes avanzados** :





 - Replace-by-fee (RBF)** : Activada por defecto, esta función acelera la transacción mediante el pago de una comisión más elevada (véase el Apéndice 4 para más detalles).





 - Selección manual de UTXO**: Si sus fondos están almacenados en varias direcciones Wallet diferentes, puede seleccionar las direcciones desde las que enviar los fondos. ¿Por qué debería hacerlo? Con la creciente adopción de la Bitcoin, las comisiones de transferencia están aumentando. Enviar desde varias direcciones con pequeñas cantidades es más caro que enviar desde una sola Address, pero hacerlo ahora evita tener que hacerlo más tarde, cuando las comisiones serán aún más altas. Esto se llama **consolidación de UTXO.**



![image](assets/fr/16.webp)





- Envío con PayJoin**: Si la función ha sido activada por el destinatario que suministró el URI, por ejemplo :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



A continuación, Bull Bitcoin Mobile configurará el envío combinando sus UTXOs con los UTXOs del destinatario como entrada, mejorando la confidencialidad (véase el Apéndice 3 para más detalles).



### 5.3. Enviar a Liquid



#### 5.3.1 Pantalla de envío



La red **Liquid** permite transacciones rápidas (~2 minutos gracias a un bloque por minuto), más confidenciales (importes enmascarados) que en la red onchain, y con comisiones muy bajas. Los fondos se retiran de **Instant Payments Wallet**.



**Acción**: Introducir o escanear un Liquid Address





- Si no se ha definido el importe, por ejemplo :



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```



A continuación, puede elegir en la pantalla de envío :




- Cantidad en BTC, sat o fiat. Sin mínimo, 1 Satoshi posible;
- Una nota opcional para identificar la transacción. Solo visible para usted, en los detalles de la transacción.



![image](assets/fr/17.webp)





- Si el importe ya se ha definido, por ejemplo :



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



A continuación, accederá directamente a la siguiente pantalla de confirmación.



#### 5.3.2 Pantalla de confirmación



Tómese su tiempo para comprobar todos los parámetros, especialmente la cantidad y el destino Address.



![image](assets/fr/18.webp)





- Comisiones**: Proporcionales a la complejidad de la transacción, generalmente sobre una base de 0,1 satoshis/vB, es decir, 20-40 satoshis para una transacción sencilla (33 Sats a 22/07/2025).



### 5.4. Enviar a Lightning



#### 5.4.1 Pantalla de envío



La red **Lightning** permite realizar pagos instantáneos y de bajo coste por importes pequeños, ideales para pequeñas transacciones diarias.



**Acción**: Introducir o escanear un Rayo Invoice





- Si escanea una LN-URL Address que le permite establecer la cantidad


Ejemplo: `orangepeel@walletofsatoshi.com`.


a continuación, puede elegir en la pantalla de envío :




 - Importe en BTC, sat o fiat. Importe mínimo de 1000 satoshis el 23/07/2025
 - Una nota opcional para identificar la transacción. Se enviará al destinatario.



![image](assets/fr/19.webp)





- Si escanea una Invoice Lightning que contiene una cantidad definida


Ejemplo:



```
lnbc210n1p58hhk6bullbitcoint4a9jq34dmrmcrursjmw3wjf8elz0nxtdsw9pscqzyssp52jg9dm8vc3xy26er5rc965lxjllhd82je97au7ysvv6lpq7r7shs9q7sqqqqqqqqqqqqqqqqqqqsqqqqqysgqdqqmqz9gxqyjw5qrzjqwryaup9lh50kkranzgcdnn2fgvx390wgj5jd07rwr3vxeje0glclle6wrlm37k39uqqqqlgqqqqqeqqjqnf7w9f2evnzptm2vtdknk7483hsndkl98c4mv2kfe64v5pkq0j6x2dqt9y9wayszv3z33az7c8hkj3yqj9jd7ans7ugq8xv0xefp23gqltph72
```



A continuación, accederá directamente a la siguiente pantalla de confirmación.



Nota: el importe debe ser superior a 21 Sats el 23/07/2025



#### 5.4.2 Funcionamiento, límites y ventajas





- Mecanismo**: Los fondos se extraen de **Pagos Instantáneos Wallet** (Liquid) y se convierten mediante un swap **Liquid → Lightning** con **Boltz**.





- Límites:**
 - Una cantidad mínima** superior a una Wallet Lightning nativa (véase más arriba)
 - Gastos** más Liquid → Intercambio de rayos a través de Boltz





- Ventajas** :
 - Autocustodia**: Sus fondos permanecen bajo su control, almacenados en la Liquid Network, y transferibles a través de Lightning si es necesario
 - Sin altas comisiones onchain**: Almacenar en Liquid te ha ahorrado costosos depósitos onchain para abrir tu canal Lightning o añadir liquidez. Estas operaciones pueden realizarse más adelante, cuando la cantidad acumulada en Liquid justifique las comisiones.





- Consejo:** Si el destinatario dispone de Wallet Bull Bitcoin, utilice directamente el Liquid Network para evitar costes de intercambio



#### 5.3.3 Pantalla de confirmación



Tómese su tiempo para comprobar todos los parámetros, especialmente la cantidad y el destino Address.



![image](assets/fr/20.webp)




## 6. Ver historial



**Bull Bitcoin Mobile** facilita el seguimiento de sus transacciones en las redes **Bitcoin (onchain)**, **Liquid**, y **Lightning**. Se puede acceder al historial de dos maneras, y muestra información detallada para cada tipo de transacción. También puede consultar sus transacciones mediante navegadores de bloques externos.



### 6.1. Historial de acceso





- A través de la pantalla de inicio** :
 - Haga clic en **Bitcoin Wallet** para ver las transacciones **onchain**, o en **Instant Payments Wallet** para las transacciones **Liquid** y **Lightning**.
 - El historial se muestra directamente debajo del total de la cartera, filtrado según el tipo de Wallet seleccionado.



![image](assets/fr/21.webp)





- A través de la página dedicada** :
 - En la pantalla de inicio, pulsa sobre el **símbolo de la historia** (icono del reloj o similar).
 - Acceda a una página que enumera todas las transacciones, con filtros por tipo de acción: **Enviar**, **Recibir**, **Intercambiar**, **PayJoin**, **Vender**, **Comprar** (nota: Vender y Comprar están en desarrollo y no están disponibles en este momento, 20 de julio de 2025).



![image](assets/fr/22.webp)



### 6.2. Detalles de la transacción



Cada transacción muestra información específica en función de la red y del tipo de acción (envío o recepción). Estos son los detalles disponibles para una **transacción onchain** :



![image](assets/fr/23.webp)



### 6.3. Comprobación mediante Block explorer



La lista de exploradores de las redes **Bitcoin onchain**, **Liquid** y **Lightning** figura en el apéndice 4.



Para **Lightning**, las transacciones no son visibles en los navegadores públicos. Comprueba los detalles (incluido el ID de intercambio para Boltz) en la aplicación.




## 7. Ajustes



Se puede acceder a la página de "Configuración" directamente desde la página de inicio de la aplicación Bull Bitcoin, y se utiliza para configurar y gestionar diversos aspectos de la cartera y la experiencia del usuario.



![image](assets/fr/24.webp)





- Wallet Copia de seguridad**: Muestra la frase de recuperación de la cartera para una copia de seguridad segura. Consulte la sección 3. sobre creación de carteras para conocer las mejores prácticas de gestión y almacenamiento de la frase de recuperación.





- Wallet Detalles** :
 - Pubkey**: Clave pública asociada a la Wallet, utilizada para generate Bitcoin direcciones de recepción.
 - Ruta de derivación**: Ruta de derivación utilizada para generate Wallet direcciones de la clave privada.





- Servidor Electrum (Nodo Bitcoin)**: Establece una conexión con un nodo Bitcoin personalizado para transacciones onchain.





- Código PIN**: Active y/o modifique el código de seguridad para proteger el acceso a la aplicación y a las funciones Wallet.





- Moneda**: Elige si quieres mostrar los importes en BTC o Sats, y la moneda fiduciaria por defecto (dólar, euro, etc.).





- Configuración de Auto Swap**: La función _Auto Swap_ le permite automatizar la transferencia de su BTC desde el **Instant Payments Wallet (Liquid)** a su **Bitcoin On-Chain** Wallet, tan pronto como la cantidad alcance un umbral que considere lo suficientemente alto como para justificar la tarifa de transacción.





- Registros**: Registros de actividad visibles, que pueden compartirse con el servicio de asistencia técnica para facilitar la resolución de problemas.





- Acceso a Telegram para asistencia** : Enlace directo al canal oficial de Telegram para asistencia al usuario.





- Acceso a Github** : Enlace al [repositorio Github de Bull Bitcoin](https://github.com/SatoshiPortal) para ver el código de fuente abierta o informar de problemas.




## ANEXOS



### A1. Explicación de PayJoin (P2EP)



![image](assets/fr/25.webp)



**Definición** :




- PayJoin, o **Pay-to-EndPoint (P2EP)**, es una técnica de transacción de Bitcoin que mejora la confidencialidad en la red **onchain**. Combina entradas de remitente y destinatario en una única transacción, lo que dificulta el rastreo de importes y direcciones.



**Operación:**




- En una transacción PayJoin, el emisor y el receptor trabajan juntos a través de un servidor PayJoin compatible para generate una transacción conjunta.
- En lugar de que sólo el emisor aporte entradas (UTXO), el receptor también contribuye con una de sus propias UTXO. Esto difumina la información visible en la Blockchain: en lugar de una única entrada correspondiente al importe real, ahora hay dos entradas, y las salidas no reflejan directamente el importe intercambiado.
- La transacción final se asemeja a una transacción Bitcoin estándar (multientrada/multisalida), pero oculta la cantidad real enviada y los vínculos entre direcciones gracias a una estructura esteganográfica.



**Para uso en Bull Bitcoin Mobile**




- Recepción** (Address Supply): PayJoin está activado por defecto.
- Enviar** : Wallet detecta automáticamente un URI de PayJoin y configura la transacción en consecuencia, por ejemplo:



```
bitcoin:bc1qp2nxbullbticoinzt6tx7x5tlnpzhv37?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F475QR36G3ZCFZ%23...
```




**Beneficios**




- Mayor confidencialidad**: PayJoin invalida la suposición de que todas las entradas de una transacción pertenecen a una única entidad. Con PayJoin, las entradas proceden tanto del emisor como del receptor, lo que rompe esta suposición.
- Enmascaramiento del importe** : El importe real intercambiado no aparece directamente en los resultados. Se calcula como la diferencia entre las UTXO de entrada y salida del destinatario, lo que hace que el análisis sea engañoso.



**Límites**




- PayJoin requiere que el emisor y el receptor utilicen monederos compatibles, de lo contrario se utiliza una transacción onchain estándar.
- La transacción es ligeramente más compleja (más entradas y salidas), lo que se traduce en unos costes ligeramente más elevados.
- Aunque está diseñado para parecerse a una transacción estándar, la heurística avanzada (por ejemplo, salidas ambiguas, servidores PayJoin conocidos) puede hacer sospechar de su uso, aunque sin certeza absoluta.



**Más información:**




- [Glosario](https://planb.network/fr/resources/glossary/payjoin)
- Chapitre [Les transactions PayJoin](https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c/c1e90b95-f709-4574-837b-2ec26b11286f)




### A2. Explicación de Replace-by-fee (RBF)



**Definición**: Replace-by-fee (RBF) es una característica de la red Bitcoin que permite al remitente acelerar la confirmación de una transacción **onchain** aceptando pagar una tarifa más alta.



**Límites** :




- RBF no está disponible para las transacciones Liquid o Lightning.
- La transacción inicial debe marcarse como compatible con RBF cuando se crea, lo que Bull Bitcoin Mobile hace automáticamente a menos que se desactive.



**Más información:**




- [Glosario](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. Buenas prácticas



Para utilizar **Bull Bitcoin Mobile** de forma segura y eficiente, siga estas recomendaciones. Le ayudarán a proteger sus fondos, optimizar sus transacciones y preservar su confidencialidad en las redes **Bitcoin (onchain)**, **Liquid** y **Lightning**.





- Asegura tu frase de recuperación** :
 - Tutorial: [Save your Mnemonic phrase](https://planb.network/fr/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270)
 - Cours [La phrase mnémonique](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8f9340c1-e6dc-5557-a2f2-26c9669987d5)





- Utilizar autenticación segura** :
 - Activar un **PIN fuerte** o **autenticación biométrica** (huella dactilar o reconocimiento facial) para proteger el acceso a la aplicación.
 - Nunca compartas tu PIN ni tus datos biométricos.





- Proteja su intimidad** :
 - generate una nueva Address para cada recepción onchain o Liquid para limitar el rastreo en la Blockchain.
 - Utilice PayJoin cuando esté disponible para aumentar la confidencialidad sobre la cantidad enviada en cadena
 - Para obtener la máxima confidencialidad, conecte su Wallet a su propio nodo Bitcoin a través de un servidor Electrum en lugar de utilizar el nodo público





- Elija la red que mejor se adapte a sus necesidades** :
 - Onchain**: Preferido para custodia a largo plazo o transacciones de gran valor (comisiones insignificantes en relación con el importe).
 - Liquid**: Para transferencias rápidas y económicas con mayor confidencialidad.
 - Relámpago**: Opta por transferencias instantáneas de bajo coste para pequeñas cantidades. Si sois dos usuarios de Wallet Bull Bitcoin, elegid Liquid para evitar las comisiones de intercambio Lightning <> Liquid a través de Boltz.





- Compruebe siempre las direcciones de envío** :
 - Antes de enviar fondos, compruebe cuidadosamente la Address. Los fondos enviados a una Address incorrecta se pierden para siempre. Utiliza copiar/pegar o escanear código QR, nunca copies/modifiques una Address a mano.





- Optimizar los costes** :
 - Para las transacciones onchain, elija las tarifas adecuadas (lenta, media, rápida) en función de la urgencia y la congestión de la red.
 - Utilice Liquid, o Lightning para pequeñas cantidades.
 - Active Replace-by-fee (RBF) (véase el Apéndice 4) para los envíos en cadena si prevé que necesitará acelerar la confirmación.





- Mantener actualizada la aplicación




### A4. Recursos adicionales





- Enlaces oficiales y asistencia:**
 - [staff@bitcoinsupport.com](mailto:staff@bitcoinsupport.com)**, support@bullbitcoin.com : correo electrónico de apoyo
 - [Sitio web oficial de Bull Bitcoin](https://bullbitcoin.com/) :** Información sobre los servicios de Bull Bitcoin, creación de cuenta, acceso a la aplicación
 - [GitHub Bull Bitcoin Mobile](https://github.com/SatoshiPortal/bullbitcoin-mobile) :** Ver código, evolución y hoja de ruta, contribuir al desarrollo...
 - [Cuenta X - Twitter Bull Bitcoin](https://x.com/BullBitcoin_)**
 - Grupo de Telegram** para Wallet móvil: chat de grupo con asistencia, consulta la página "Configuración".





- Exploradores de bloques :**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Rayo: **[1ML (Lightning Network)](https://1ml.com/)**





- Aprendizaje y tutorías:** **[Plan ₿ Network](https://planb.network/)** :
 - Asegurar su frase de recuperación



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** :
 - [Glosario](https://planb.network/resources/glossary/liquid-network)**




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727





- Lightning Network** :
 - [Glosario](https://planb.network/resources/glossary/lightning-network)**




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


### A5. Toro Bitcoin



#### Presentación de la empresa



**[Bull Bitcoin](https://www.bullbitcoin.com/fr)**, es la plataforma no depositaria de Exchange más antigua dedicada exclusivamente a Bitcoin, fundada en 2013 en la Embajada de Bitcoin en Montreal, Canadá. Dirigida por Francis Pouliot, reconocido pionero del ecosistema Bitcoin, la empresa se posiciona como un actor clave en la promoción de la soberanía financiera y la autonomía de los usuarios. Su misión es permitir a las personas recuperar el control de su dinero utilizando Bitcoin como herramienta de libertad y pago, al tiempo que rechaza las monedas fiduciarias y las criptodivisas distintas de Bitcoin.



![image](assets/fr/26.webp)



[Crea tu cuenta](https://app.bullbitcoin.com/registration/orangepeel) con un 0,25% de descuento en compras y ventas de Bitcoin.



#### Valores y filosofía



Bull Bitcoin destaca por sus principios Commitment a Cypherpunk y su ética Bitcoin:





- Enfoque exclusivo en Bitcoin** : La plataforma es fiel a la visión de una moneda descentralizada y resistente a la censura.





- No custodio** : Los usuarios conservan el control total de sus Bitcoins enviando fondos a sus propias carteras.





- Confidencialidad**: Recopilación minimizada de datos personales, con opciones de compra sin KYC para transacciones inferiores a 999 USD. Los datos están protegidos conforme a la normativa (FINTRAC en Canadá, AMF en Francia).





- Transparencia**: Sin comisiones ocultas, los costes están incluidos en el diferencial (la diferencia entre los precios de compra y venta).





- Soberanía financiera**: La bula Bitcoin promueve la independencia de los sistemas bancarios tradicionales y de las instituciones centralizadas.



#### Servicios principales





- Depósito en fiat** : Los usuarios pueden depositar fondos en su cuenta Bull Bitcoin con moneda fiduciaria (CAD, EUR, etc.) mediante transferencia bancaria o efectivo/tarjeta de débito en determinadas oficinas de correos canadienses.





- Adquisición de Bitcoin** : Los usuarios pueden comprar Bitcoin que se envía directamente a su cartera no depositaria, garantizando el control total de sus fondos.





- Compra programada de Bitcoin**: Bull Bitcoin ofrece un servicio de compra recurrente automatizada (DCA - Dollar Cost Averaging) a intervalos regulares, con cargo a su saldo disponible, con transferencia directa de Bitcoins a una Wallet controlada por el usuario, reduciendo el impacto de la volatilidad de los precios.



Tenga en cuenta que una opción llamada "Autocompra" le permite convertir sus fiats en cuanto toquen su saldo de Bitcoin Toro, y enviar sus Bitcoins a su propia Wallet. Esta opción también se puede combinar con una transferencia bancaria periódica programada con su banco para hacer un DCA. Esta opción automatiza tu acumulación de Bitcoin sin tener que abrir nunca la aplicación.






- Comprar Bitcoin a un precio fijo 'Orden Límite'**: Permite comprar Bitcoin a un precio especificado de antemano por el usuario, que se ejecuta automáticamente cuando el precio del índice Bull Bitcoin alcanza o cae por debajo del límite establecido.





- Venta de Bitcoin**: Los usuarios pueden vender sus Bitcoins y recibir los fondos en moneda fiduciaria directamente en su cuenta bancaria mediante transferencia bancaria o SEPA.





- Pagos a terceros**: Bull Bitcoin permite a los usuarios enviar dinero fiduciario a cuentas bancarias desde sus Bitcoins, de forma totalmente transparente para el destinatario.





- Bull Bitcoin Prime**: Bull Bitcoin Prime es un servicio premium para clientes de alto poder adquisitivo y empresas, que ofrece soluciones personalizadas y asistencia premium. Esto incluye el acceso a comisiones reducidas, un gestor de cuenta dedicado y servicios corporativos a medida. Este servicio está dirigido a instituciones, operadores profesionales y clientes corporativos que buscan una experiencia en profundidad y un tratamiento prioritario.





- Wallet móvil**: Bull Bitcoin ofrece una Wallet móvil de código abierto y autocustodia, disponible en Android e iOS, que admite transacciones onchain, Liquid y Lightning Network.





- Apoyo pedagógico**: Guías gratuitas y asesoramiento personalizado para ayudar a los usuarios a crear, asegurar y gestionar sus carteras Bitcoin, reforzando la autonomía financiera.



#### Conformidad y seguridad





- Reglamentación**: Registrado en FINTRAC (Canadá) y AMF (Francia), Bull Bitcoin cumple con los requisitos KYC/AML.





- Seguridad**: Uso de carteras seguras y recomendaciones de almacenamiento offline. Los datos personales se alojan en la infraestructura Bitcoin de Bull, que es 100% autoalojada y no depende de terceros.