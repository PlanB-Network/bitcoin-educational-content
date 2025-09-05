---
name : Blitz Wallet


description: La cartera Bitcoin más sencilla.
---
![cover](assets/cover.webp)



La experiencia de usuario es uno de los factores decisivos a la hora de iniciarse con una Wallet. En este tutorial, te presentaremos una Wallet que ha hecho de su experiencia de usuario un factor decisivo: Blitz Wallet te ofrece el monedero Bitcoin más sencillo y uno de los más completos que puedas encontrar.



## ¿Qué es el Blitz Wallet?



Blitz Wallet es un Bitcoin de autocustodia cuyo código fuente está disponible (Open Source), que se centra en tu soberanía y en una experiencia de usuario que facilita su manejo.



[Blitz Wallet](https://blitz-Wallet.com/) es un Wallet móvil disponible en Android (Play Store) e iOS (App Store).



⚠️**IMPORTANTE**: Descargar una Bitcoin Wallet en una plataforma oficial es importante para verificar la autenticidad de la aplicación y, por extensión, reforzar la seguridad de sus fondos.



En este tutorial, nos basaremos en la versión Android de Blitz Wallet, pero todos los procesos presentados a continuación son igualmente válidos en iOS.



![installation](assets/fr/01.webp)



Dado que el Blitz Wallet es una cartera autosuficiente de Bitcoin, puede optar por crear una cartera nueva o importar las palabras de recuperación 12/24 de una cartera que ya tenga.



Aquí, vamos a empezar con la creación de una nueva cartera. Vea a continuación nuestras recomendaciones sobre la copia de seguridad de sus frases de copia de seguridad.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗**IMPORTANTE**: Estas 12 / 24 palabras de recuperación son esenciales para acceder a tus bitcoins. Si las pierdes, ya no estarás autorizado a gastar tus bitcoins.



Ni tus llaves, ni tus bitcoins.




A continuación, crea un código PIN para autenticar el acceso a tu Wallet.



![setup-wallet](assets/fr/02.webp)



## Primeros pasos con Blitz



Operar con Blitz es más intuitivo que con la mayoría de los otros monederos Bitcoin.



En el menú Wallet, tienes un Interface minimalista centrado únicamente en las acciones principales:



### Recibir bitcoins



Para recibir bitcoins en su Blitz Wallet, haga clic en el icono "Flecha hacia abajo", introduzca la cantidad de satoshis que desea recibir y el Wallet creará un Invoice para que lo comparta con su remitente.



⚠️ **NOTA**: Satoshi (o "sat") representa la unidad más pequeña de Bitcoin: 1 Bitcoin = 100.000.000 satoshis



Una de las características especiales de Blitz Wallet es que admite diferentes redes y canales del ecosistema Bitcoin:





- Lightning Network** : Una de las superposiciones de Bitcoin que te permite realizar microtransacciones al instante.





- Bitcoin Mainnet** : La cadena principal del protocolo Bitcoin, adecuada para transacciones de gran valor.





- Liquid Network**: Una cadena paralela a Bitcoin Mainnet desarrollada por BlockStream que utiliza Liquid Bitcoins para realizar operaciones rápidas, Confidential Transactions.



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Por defecto, todas sus transacciones serán en Liquid Network, pero Blitz le permite definir la red en la que desea recibir satoshis haciendo clic en el botón **Elegir formato**.



![receive-sats](assets/fr/03.webp)



### Crear contactos con Blitz



Blitz Wallet te facilita el envío de bitcoins desde su Wallet.



En el menú **Contactos**, puede registrar los nombres de usuario de Blitz o las URL de Lightning con las que más interactúa.



Esto significa que puede enviar satoshis a estas direcciones fácilmente, evitando la fase de escaneado e introducción manual de Address.



![add-contacts](assets/fr/04.webp)



### Enviar bitcoins



Además de los métodos clásicos de envío de Bitcoins (código QR, introducción manual), utilizando los contactos prerregistrados en su Wallet, puede enviar Satss a su destinatario en sólo tres clics.



En el menú **Wallet**, haga clic en el botón "Flecha hacia arriba", elija el método de envío de bitcoins, luego introduzca la cantidad a enviar y proceda a la confirmación.



La cantidad mínima para enviar Bitcoin en Blitz Wallet es actualmente de 1.000 satoshis.



![send-bitcoin](assets/fr/05.webp)



## La tienda Blitz



Además de las operaciones de transferencia Bitcoin, Blitz Wallet le ofrece una tienda en la que puede utilizar sus bitcoins para pagar servicios digitales.





- Acceder a servicios de IA**: Utiliza modelos de inteligencia artificial generativa como: Claude 3-5 sonnet, gpt-4o, gpt-4o-mini gemini-flash-1.5 y pague directamente en bitcoins.



![ia-credits](assets/fr/06.webp)





- Envíe mensajes de texto a cualquier parte del mundo**: En la tienda Blitz, tienes acceso a un servicio GSM que te permite enviar mensajes de texto de forma anónima a cualquier parte del mundo, con facturación directa en Bitcoin.



![sms-credit](assets/fr/07.webp)





- Navegue con total confidencialidad**: Paga una suscripción a WireGuard VPN (Red Privada Virtual) en la tienda Wallet Blitz con tus bitcoins.



![wireguard](assets/fr/08.webp)



https://planb.network/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

https://planb.network/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

## Wallet Blitz entre bastidores: Ir más lejos



Detrás de la sencillez de funcionamiento de Blitz Wallet se esconde una gran potencia y personalización.



Como hemos señalado antes, todos los bitcoins que recibas serán por defecto Liquid Network.



Blitz utiliza microintercambios Liquid Network para presentar su saldo en Satoshi cuando tiene un saldo inferior a 500.000 satoshis.



Este enfoque se justifica por el deseo de facilitar la experiencia inicial y ayudar a los nuevos usuarios a realizar transacciones en Lightning Network con pequeñas cantidades de la forma más sencilla posible.



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Puede ver el desglose de su saldo en el menú **Configuración>Información de saldo**.



![balance](assets/fr/09.webp)



No obstante, Blitz Wallet te ofrece la posibilidad de activar el modo Relámpago, que te abrirá automáticamente un canal de pago cuando alcances un saldo de 500.000 satoshis.



Para activar el modo Relámpago, vaya a **Configuración** y, en la sección **Configuración técnica**, haga clic en la opción **Información del nodo**.



![enable-lightning](assets/fr/10.webp)



Al activar el modo Lightning, una vez cumplida la condición principal (saldo de 500.000 satoshis o 0,005 Bitcoin), podrá realizar transacciones en Lightning Network y ya no tendrá que pasar por Liquid Network de BlockStream.





- Acepte Bitcoin en su tienda** :



La integración de los pagos Bitcoin en las tiendas está aún en fase experimental con Blitz Wallet. Le recomendamos que la utilice con moderación.



En el menú **Configuración>Punto de venta**, puede establecer el identificador único asociado a su tienda y la moneda fiduciaria local en la que desea recibir los pagos.



![pos](assets/fr/11.webp)



Si este tutorial te ha ayudado a familiarizarte con Blitz, estamos seguros de que disfrutarás igual con el tutorial de Muun Wallet. Descubre Muun, un Wallet sencillo tan potente como el Bitcoin.



https://planb.network/tutorials/wallet/mobile/muun-111b56b0-4872-4130-ad2e-e58f8363451d

