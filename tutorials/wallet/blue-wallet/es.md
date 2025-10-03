---
name: Blue Wallet

description: Bitcoin Cartera radicalmente sencilla y potente
---
![cover](assets/cover.webp)



Empezar a utilizar Bitcoin parece ser un gran reto para las personas escépticas sobre la sencillez de su uso. Por lo tanto, encontrar las herramientas adecuadas para garantizar esta simplicidad resulta de vital importancia para una mejor adopción de Bitcoin como medio de Exchange y no sólo como depósito de valor.



En este tutorial vamos a echar un vistazo a Blue Wallet, una Bitcoin Wallet sencilla pero muy eficaz que te permite gestionar tus bitcoins personalmente y también crear cooperativas de gestión basadas en [Multisig](https://planb.network/resources/glossary/multisig) (no te preocupes, volveremos a ello).



![Vidéo tutoriel Blue Wallet](https://www.youtube.com/watch?v=UCAtFgkdJtM)



## Primeros pasos con Blue Wallet



Blue Wallet es una Bitcoin Wallet de código abierto que te permite tomar el control de tus bitcoins. Está disponible como aplicación móvil tanto en plataformas Android como iOS. En este tutorial nos basaremos en la versión para Android, sin embargo, todos los procesos que se desarrollarán son igualmente válidos en iOS.



![download](assets/fr/01.webp)



⚠️ Por favor, asegúrese de descargar la aplicación Blue Wallet Bitcoin Wallet en una plataforma oficial para garantizar su autenticidad y proteger sus bitcoins de posibles filtraciones y hackeos.



Una vez instalado, puedes crear un nuevo Wallet y guardar las 12 palabras de recuperación, o importar un Bitcoin Wallet existente. Descubre cómo hacer una copia de seguridad eficiente de tus palabras clave para no perder el acceso a tus bitcoins.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Con Blue Wallet puede crear carteras Bitcoin separadas y dedicadas. Por ejemplo, puedes tener una Wallet para tus ahorros y otra para tus gastos diarios, todo en la misma aplicación.



![home](assets/fr/02.webp)



## Tipos de cartera



En Blue Wallet, encontrará dos tipos de cartera nativos de Bitcoin.



### Cartera Bitcoin



Si está acostumbrado a otras carteras Bitcoin como Phoenix o Aqua, no desentonará en absoluto en Interface con la cartera Bitcoin de Blue Wallet.



https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Bitcoin de Blue Wallet Wallet representa el Wallet estándar en el ecosistema Bitcoin. Puedes gastar bitcoins siempre que estés en posesión de las palabras de recuperación que proporcionarán una firma válida en la red para autenticar que eres el propietario de los bitcoins.



Para crear una cartera Bitcoin, pulse el botón **Añadir ahora**, introduzca el nombre de su cartera y elija el tipo Bitcoin.



![bitcoin-wallet](assets/fr/03.webp)



Cuando hagas clic en la vista previa de tu Bitcoin Wallet, podrás ver tu historial de transacciones y enviar y recibir bitcoins.



⚠️ Todas las transacciones en su Bitcoin Wallet están en la cadena principal del protocolo Bitcoin (Mainnet).





- Recibir bitcoins con la Bitcoin Blue Wallet Wallet es intuitivo. En la parte inferior de tu pantalla, haz clic en el botón **Recibir**. Comparte el código QR o tu Bitcoin Address con tu remitente para que pueda enviarte los bitcoins.



También puede configurar una cantidad predefinida para especificar la cantidad de Bitcoin que desea recibir.



![receive-bitcoin](assets/fr/04.webp)





- En el botón **Enviar**, envía bitcoins a una Bitcoin Address, fijando la cantidad deseada y validando la transacción.



![send-bitcoin](assets/fr/05.webp)



Blue Wallet le permite configurar a su gusto los parámetros de su envío Bitcoin.



Por lo tanto, puede seleccionar el ratio de tarifa de transacción que más le convenga si desea ver su transacción validada rápidamente en un Mempool e incluida en un bloque por los mineros. Dependiendo del ratio que elija, los mineros darán prioridad a su transacción en mayor o menor medida. Obtenga más información en nuestro tutorial sobre el espacio Mempool.



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

![feerate](assets/fr/06.webp)





- Con Blue Wallet, puede añadir varios destinatarios a un mismo envío.



Cuando añada la Bitcoin Address de su primer destinatario, en las opciones, haga clic en **Añadir destinatario**, añada la Bitcoin Address y, a continuación, establezca la cantidad que se enviará a este destinatario, y así sucesivamente. Blue Wallet despachará los bitcoins para múltiples envíos basándose en su única acción.



![add-recipients](assets/fr/07.webp)



Puede eliminar uno o todos los destinatarios haciendo clic en **Eliminar destinatario** y **Eliminar todos los destinatarios** respectivamente.



![remove-recipient](assets/fr/08.webp)





- **Inflar las comisiones**: ¿Has realizado una transacción que está tardando mucho en confirmarse? Activando la inflación de tasas puedes añadir tasas adicionales a tu transacción pendiente para acelerar su confirmación.



![bumping](assets/fr/09.webp)



### Cartera Multisig



El Multisig (multi-firma) Wallet representa un Wallet creado a partir de la agrupación de un cierto número (mínimo 2) de monederos Bitcoin. En este tipo de Wallet, dependiendo de la configuración y el método elegidos, gastar bitcoins se convierte en una acción colectiva y cooperativa.



En Blue Wallet, puede crear carteras multifirma para su asociación, su familia, su empresa. A lo largo de esta sección, exploraremos todos los aspectos de este tipo especial de cartera.



Añada una nueva cartera y seleccione el tipo **Multisig Vault** para crear una cartera multifirma.



![multisig-vault](assets/fr/10.webp)



Defina la configuración de m-de-n en su organización multifirma haciendo clic en **Configuración de bóvedas**.



⚠️ En una configuración m-de-n, **m** representa el número mínimo de firmas necesarias para aprobar una transacción y **n** el número de carteras de su organización.



Asegúrese de definir un número mínimo de firmas (m) para la mayoría de su organización. Por ejemplo, una configuración multifirma 2 de 3 requiere que dos monederos de tu organización firmen la transacción antes de que pueda llevarse a cabo.



❗Definir una configuración m-de-n donde n es igual a m es un gran riesgo. Cuando un miembro pierde el acceso a su Wallet pierdes la autorización para gastar bitcoins en la Wallet.



He aquí algunos ejemplos de configuraciones óptimas para garantizar la seguridad y la accesibilidad a los bitcoins:





- firma múltiple 2-de-3.





- firma múltiple 5-de-7.



![vault-settings](assets/fr/11.webp)



Siga las mejores prácticas seleccionando el formato P2WSH.



❗ **[P2WSH](https://planb.network/resources/glossary/p2wsh) o Pay to Witness Script Hash** es un método de bloqueo que bloquea los bitcoins salientes de tu transacción (Salidas) al Hash de un script personalizado que Blue Wallet configura. La principal ventaja de este tipo de bloqueo es que reduce el tamaño de los datos de la transacción e implícitamente le permite pagar tarifas de transacción más bajas.



Cree o importe cada una de las **n** carteras de su configuración. En nuestro tutorial, utilizaremos una configuración de 2 de 3 multifirmas. Asegúrese de guardar las palabras de recuperación para cada cartera individualmente.



![vault-keys](assets/fr/12.webp)





- Recibir bitcoins



En su página Multisig Wallet, encontrará su historial de transacciones y los botones Recibir y Enviar.



Recibir bitcoins en una Wallet multifirma es el mismo proceso que cuando se está en una Bitcoin estándar.





- **Enviar bitcoins**:



Al gestionar una Wallet con varias firmas, gastar bitcoins se convierte en una acción compuesta, ya sea con otras personas o con una segunda Wallet propia. La firma única de tu Wallet ya no es suficiente. Esto añade una Layer de seguridad a tus bitcoins, porque un individuo malintencionado no podrá gastar esos bitcoins cuando entre en posesión de una sola de tus claves privadas.



Al igual que la cartera estándar Bitcoin de Wallet Azul, puede definir varios destinatarios en la opción **Añadir destinatarios**.



Al validar tu transacción, necesitarás una segunda firma para aprobar el gasto de los bitcoins. Recuerda que estamos en una configuración multifirma 2-de-3.



El segundo firmante de Wallet, si también es usuario, puede firmar la transacción aunque esté fuera de Internet (sin Wi-Fi ni datos móviles) escaneando el código QR de la [transacción parcialmente firmada](https://planb.network/resources/glossary/psbt) que acaba de crear.



![mutisig-send](assets/fr/13.webp)





- Vaya más allá con la **cartera Multi firma**:



En la Interface de su Wallet multifirma, pulse el botón **Gestionar teclas**.



Al olvidar una de las palabras de recuperación de una de las carteras firmantes (**Olvida esta seed...**), notifica a Blue Wallet que borre de su memoria la copia de seguridad de estas palabras. Por lo tanto, habrá realizado una copia de seguridad externa.



![revoke-key](assets/fr/14.webp)



Al realizar esta acción, sólo conservas la clave pública asociada a estas palabras de recuperación.



⚠️ Conservar sólo las claves públicas (XPUB) le permite añadir un nivel adicional de seguridad a su configuración multifirma 2-de-3. De hecho, podría ser perjudicial mantener todas las palabras de recuperación en un solo lugar cuando su teléfono está siendo atacado. Los atacantes con acceso a un solo **VAULT** (palabra clave) que utilices para firmar tus transacciones, no podrán robar tus bitcoins (se requiere un mínimo de 02 firmas) porque las claves públicas no pueden utilizarse para firmar transacciones.



## Más opciones con Blue Wallet



### Mejorar la seguridad de acceso a la cartera



En Ajustes, la opción **Seguridad** le permite definir el uso de una huella dactilar para realizar una transacción, exportar o eliminar su Wallet. Esto autentica a la persona que utiliza tu smartphone.



![biometry](assets/fr/15.webp)



## Activar Lightning Network



Lightning Network ya no es compatible de forma nativa con la aplicación Blue Wallet.



En Configuración > **Configuración Lightning**, puede asociar manualmente su Wallet Lightning cuando ejecute un nodo Lightning Network Daemon (LND). Instala el Hub LND, luego asocia tu Wallet introduciendo el enlace generado por el Hub.



![ln](assets/fr/16.webp)



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

https://planb.network/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Ya has completado el recorrido Blue Wallet, listo para utilizar Bitcoin en toda su sencillez y potencia. Te recomendamos que des el siguiente paso, y descubras cómo puedes aceptar pagos con Bitcoin en tus comercios, gracias a la potencia de Lightning.



https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06