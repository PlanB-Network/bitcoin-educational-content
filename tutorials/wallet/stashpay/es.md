---
name: StashPay
description: La Bitcoin Wallet minimalista para todos
---

![cover](assets/cover.webp)



La experiencia del usuario es un factor clave en la adopción de soluciones de Bitcoin en todo el mundo. Ofrecer una experiencia fluida, sencilla y técnicamente libre de trabas es la prioridad de muchos monederos y plataformas Exchange. En este sentido, StashPay destaca por su enfoque minimalista, al tiempo que demuestra la potencia de Lightning Network.



En este tutorial, echaremos un vistazo a esta cartera para descubrir cómo funciona y por qué es ideal para pequeñas empresas o autónomos.



## Primeros pasos con StashPay



StashPay es una Wallet de autocustodia Lightning reconocida principalmente por su experiencia de usuario minimalista y centrada en el usuario.  Con esta Wallet, no necesitas ningún conocimiento técnico para recibir y enviar tus primeros satoshis.



StashPay es un proyecto de código abierto desarrollado en React Native y tiene como objetivo resolver el problema de las altas comisiones de transacción incluso con transacciones en la cadena principal del protocolo Bitcoin. Está disponible como aplicación móvil en plataformas Android e iOS a través de enlaces de descarga presentes en el [sitio web](https://stashpay.me/).



![introduce](assets/fr/01.webp)



Es importante descargar la aplicación para Android desde la página web, ya que no está disponible en Google Play Store.


Cuando finalice la descarga, concede los permisos necesarios para poder instalar la aplicación en tu teléfono Android.



Una vez instalada la aplicación, StashPay creará una Bitcoin Wallet inicial para usted la primera vez que la abra. Antes de cualquier transacción, le recomendamos que haga una copia de seguridad de este Wallet. A continuación, encontrará todas nuestras directrices para asegurarse de que sus frases de recuperación tienen una copia de seguridad adecuada.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Acceda a la configuración de StashPay haciendo clic en el icono "Configuración" y, a continuación, en la opción **Crear copia de seguridad**. A continuación, autorice la visualización de frases de recuperación. No copie sus frases de recuperación en el portapapeles de su teléfono, ya que pueden ser accesibles para otras aplicaciones fraudulentas instaladas en su móvil.



![backup](assets/fr/02.webp)



También puede recuperar una Bitcoin Wallet que ya esté utilizando haciendo clic en la opción **Recuperar Wallet** e insertando sus 12 o 24 palabras de recuperación.



### Recibe tus primeros satoshis en StashPay



En la pantalla de inicio, haga clic en el botón **Recibir** y establezca una cantidad superior a la especificada en rojo. En nuestro caso, no podemos recibir menos de 0,11 USD con el Wallet de StashPay.



![receive](assets/fr/03.webp)



Una vez definido el importe, puede hacer clic en el botón **Crear Invoice** y, a continuación, escanear o copiar el Invoice para enviarlo a su remitente satoshis.



![receive_sats](assets/fr/04.webp)



Puede consultar su historial de transacciones haciendo clic en el icono "reloj" de la página de inicio.



![network_fee](assets/fr/05.webp)



Se habrá dado cuenta de que para recibir satoshis tendrá que pagar una cuota de red. Estas comisiones se deducirán de los satoshis que vaya a recibir. Esto se debe a que StashPay es un Wallet basado en el Breez Development Kit. Para recibir satoshis con la implementación sin nodos Lightning del Kit, Breez cobrará al cliente (StashPay en nuestro caso) `0,25% + 40 satoshis`. Más información en nuestro tutorial de Misty Breez.



https://planb.network/tutorials/wallet/mobile/misty-breez-738ced2a-0764-4d7f-a150-ec0ce84a9d25

### Envía bitcoins con StashPay



Enviar bitcoins con StashPay es bastante intuitivo gracias a la minimalista Interface. En la pantalla de inicio, haz clic en el botón **Enviar**. Escanea el código QR o pega el Address al que deseas enviar satoshis. StashPay detectará automáticamente la cadena de protocolo Bitcoin a la que desea enviar bitcoins.



![send](assets/fr/06.webp)



Como StashPay es un Wallet basado en el Kit de Desarrollo de Breez, se beneficia de una interesante ventaja: el envío de bitcoins en la cadena principal a bajo coste. Breez utiliza el servicio Boltz para realizar transacciones entre las distintas cadenas del protocolo Bitcoin, lo que permite a los clientes que implementan el Kit de Desarrollo beneficiarse de este servicio directamente en su aplicación.



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

Sin embargo, Breez SDK impone una cantidad mínima a partir de la cual se pueden enviar bitcoins a un Address de la cadena principal.



![onchain](assets/fr/07.webp)



También puedes enviar bitcoins utilizando el Address Lightning de tu destinatario. Revisa los detalles de la transacción y confírmalos haciendo clic en el botón **Enviar**.



![confirm](assets/fr/08.webp)



## Más configuraciones



En los ajustes de StashPay, puede ajustar las configuraciones para personalizar el uso de Wallet.



StashPay le permite Exchange satoshis basado en la moneda local de su elección. Haga clic en la opción **Monedas** y, a continuación, busque su moneda en la lista de +113 monedas que ofrece StashPay.



![currencies](assets/fr/09.webp)



En el menú **Opciones de recepción**, encontrarás todos los ajustes para recibir bitcoins con StashPay. Por ejemplo, al seleccionar **Elige Lightning u Onchain**, habilita tu Wallet para recibir bitcoins de la cadena principal.



![receive-onchain](assets/fr/10.webp)



La opción **Escanear direcciones OnChain** te permite refrescar el saldo de tu Wallet comprobando todos los UTXOs (bitcoins que aún no has gastado) vinculados a tus distintas direcciones.



![rescan](assets/fr/11.webp)



El menú **Exportar registro** enumera todas las acciones de las infraestructuras Breez y Boltz relativas a sus transacciones e intercambios atómicos entre las distintas cadenas de protocolos Bitcoin.



![export](assets/fr/12.webp)



Acabas de familiarizarte con la minimalista Bitcoin Wallet de StashPay. Si te ha resultado útil este tutorial, te recomendamos nuestro tutorial sobre cómo empezar con Bitcoin y ganar tus primeros bitcoins.



https://planb.network/courses/obtenir-ses-premiers-bitcoins-f3e3843d-1a1d-450c-96d6-d7232158b81f