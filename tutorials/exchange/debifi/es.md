---
name: Debifi
description: Consigue un préstamo sin custodia garantizado por Bitcoin.
---

![cover](assets/cover.webp)




## Introducción



Durante siglos, el préstamo tradicional ha permitido financiar muchos proyectos. Sin embargo, sigue siendo lento, costoso y poco inclusivo, sobre todo para quienes no tienen acceso a una infraestructura bancaria sólida.



El auge del protocolo Bitcoin inauguró una nueva era financiera, que trajo consigo una serie de retos. Uno de estos retos era cómo obtener liquidez sin verse obligado a vender Bitcoin, perdiendo así la exposición a su potencial de crecimiento



El resultado es **Debifi**, una plataforma que se posiciona como una alternativa moderna a los bancos. El objetivo es claro: hacer que el crédito sea lo más sencillo y transparente posible, combinando las ventajas del sistema financiero tradicional con la libertad que ofrece Bitcoin. El nombre Debifi refleja esta visión: ***Decentralized Bitcoin Finance***, una contracción que ilustra el encuentro de las finanzas descentralizadas y la innovación de la Bitcoin.



Debifi es una plataforma de préstamo sin custodia respaldada por Bitcoin, lo que significa que conservas el control de tus claves privadas. Permite a los usuarios desbloquear liquidez a cambio de sus bitcoins bloqueados como garantía. A diferencia de los préstamos bancarios tradicionales, Debifi utiliza un sistema de custodia multi-firma (3 de 4) y no acepta la rehipotecación de garantías, lo que garantiza una mayor seguridad y transparencia.



En la práctica, esto significa que ni Debifi ni un prestamista individual pueden gastar su BTC sin el acuerdo de tres partes (usted, el prestamista y un tercero de confianza). Esto hace que el sistema sea más seguro: si pides prestado en Debifi, conservas la propiedad de tu Bitcoin hasta que el préstamo haya sido devuelto en su totalidad.



## Ventajas de Debifi



Con Debifi, obtienes préstamos respaldados por Bitcoin que están sobrecolateralizados y garantizados on-chain. Sus fondos permanecen seguros con billeteras multifirma, 2FA y control total sobre su Bitcoin - usted mantiene sus llaves, usted mantiene sus monedas. Pida prestado en una gama de stablecoins u opciones fiat, a tipos competitivos, y liquidez global.



He aquí una rápida comparación entre un préstamo Debifi y un préstamo bancario tradicional:


| Characteristics        | Loan via Debifi                                                        | Traditional Bank Loan                                                       |
| ---------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Accessibility          | ✔️ Open to any Bitcoin holder (even without banking history)           | ❌ Often limited to clients with physical collateral and strong records      |
| Speed of approval      | ✔️ Funds available within minutes or hours                             | ❌ Lengthy process (days or weeks)                                           |
| Required guarantees    | ✔️ Bitcoin used as the sole collateral                                 | ❌ Physical guarantees (property, land, stable income)                       |
| Asset control          | ✔️ You keep exposure to Bitcoin and its upside potential               | ❌ No connection between the loan and your financial assets                  |
| Geographic flexibility | ✔️ Available everywhere (no banking jurisdiction constraints)          | ❌ Restricted to the bank’s jurisdiction                                     |
| Main risk              | ❌ Liquidation risk if BTC price drops too sharply                      | ❌ Risk of asset seizure or negative impact on credit score                  |

Antes de mostrarte paso a paso cómo pedir un préstamo en Debifi, hay algunos puntos que creo que debes saber.




## Definiciones





- Las comisiones de apertura** son gastos únicos que se cobran en el momento de la concesión del préstamo y se calculan como un porcentaje del importe prestado. Estas comisiones cubren los gastos administrativos, operativos y de gestión.





- La garantía** es un activo que se deposita para garantizar un préstamo. En el caso de Debifi, la garantía es Bitcoin (BTC), que el prestatario deposita en la plica Multisig 3/4.





- El sistema Multisig escrow (3/4)** es un mecanismo de depósito seguro en el que los bitcoins de un prestatario se colocan en una dirección multifirma. En concreto, cuatro (4) partes poseen cada una una clave (prestatario, prestamista, Debifi, tercero independiente). Para mover los fondos, se requieren al menos 3 de las 4 firmas.





- Una stablecoin** es una criptomoneda cuyo valor está vinculado a un activo estable (por ejemplo, el dólar estadounidense), lo que evita la volatilidad del Bitcoin. Por ejemplo, 1 USDC siempre vale ~1 USD. Por ejemplo, 1 USDC siempre vale ~$1, ya que está respaldada por reservas fiduciarias.





- La relación préstamo-valor (LTV)** de un préstamo determina la cantidad de efectivo que puede pedir prestado como garantía para su Bitcoin. Relación LTV = Importe del préstamo / Importe de la garantía * 100. Por ejemplo, un LTV del 50% significa que el valor del préstamo es igual al 50% del valor de la Bitcoin depositada.




Videotutorial de BTC Sessions :



![Vidéo tutoriel de BTC Sessions](https://youtu.be/02gzg-en8n0)



## Primeros pasos con Debifi



Para empezar a trabajar en Debifi, necesitarás algunos requisitos previos.


### Requisitos previos



Antes de pedir prestado a Debifi, asegúrese de que dispone de los siguientes elementos:





- Bitcoin wallet: donde guardas tu BTC (idealmente no custodiado, por ejemplo Hardware Wallet o un wallet móvil de confianza). Es desde esta wallet desde donde enviarás la garantía Bitcoin a Debifi y recibirás la garantía de vuelta.



Puede utilizar Aqua, una Bitcoin y Liquid wallet que también soporta la gestión de stablecoin USDT en varias redes. O COLDCARD (Mk4 o Q), actualmente el único hardware soportado por Debifi.



https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3



- KYC (*Know Your Customer*): dependiendo de la oferta de préstamo elegida, puede ser necesario un proceso de verificación de identidad. En Debifi, cada oferta indica si se requiere KYC o no. Así que prepárese en consecuencia. KYC se lleva a cabo por terceros proveedores de servicios fiables como Sumsub.



![image](assets/fr/03.webp)





- Aplicación de autenticación de dos factores: Debifi requiere un código Authenticator para cada acción importante. Es una capa extra de seguridad. En este tutorial, usaremos Google Authenticator. Alternativamente, puede utilizar otros como mejor le parezca.



https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc



- Sitio web y aplicación móvil de Debifi: Debifi es a la vez un sitio web y una aplicación móvil, y ambos funcionan en tándem. La aplicación móvil se convierte en una wallet, que almacena tu clave privada y gestiona la firma de los contratos. Además, necesitas utilizar el sitio web para comprometer contratos (una Interface grande te da una visión general de los contratos de préstamo y sus detalles).





- La aplicación móvil Debifi (iOS/Android) es necesaria para contratar préstamos. Debe descargar la aplicación, crear una cuenta y "vincular" su dispositivo (registrar el dispositivo en su cuenta). La aplicación Debifi admite la autenticación de dos factores (2FA) y, sin un smartphone, no podrá confirmar las transacciones en Debifi.



### Crear una cuenta



Visite [el sitio web oficial de Debifi](https://debifi.com/app).



![image](assets/fr/04.webp)



Instala la aplicación según el tipo de smartphone que tengas y ábrela.



![image](assets/fr/05.webp)



![image](assets/fr/06.webp)



Una vez en la aplicación, haz clic en el menú **Configuración**.



![image](assets/fr/07.webp)



A continuación, haga clic en **Iniciar sesión o crear cuenta** para crear una cuenta con su dirección de correo electrónico.



![image](assets/fr/08.webp)



![image](assets/fr/09.webp)



![image](assets/fr/10.webp)



Recibirá un código de verificación por correo electrónico. Copie y pegue este código en la aplicación. A continuación, abre la aplicación Debifi en tu smartphone e identifícate.



![image](assets/fr/11.webp)



### Proteger su cuenta



Por seguridad, Debifi te pedirá que sigas tres pasos.



![image](assets/fr/12.webp)





- En primer lugar, tendrás que establecer un código PIN seguro para acceder más tarde a tu aplicación.



![image](assets/fr/13.webp)





- A continuación, configura la autenticación de dos factores (2FA) para asociar tu dispositivo a tu cuenta mediante el código 2FA.



![image](assets/fr/14.webp)





- Por último, guarde las 12 palabras de su clave privada escribiéndolas en un soporte fiable y guardándolas en un lugar seguro. Esta fase es esencial para recuperar tu cuenta y gestionar tus fondos.



![image](assets/fr/15.webp)





- Para mayor seguridad, puede incluso añadir un passphrase.



![image](assets/fr/16.webp)



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Tenga en cuenta que sólo su smartphone registrado podrá abrir su cuenta (una medida de seguridad adicional).



Una vez completados estos pasos, haga clic en el menú **Ofertas** para ver las ofertas de préstamos disponibles. Al hacer clic en una oferta, te redirige a la página web de Debifi.



![image](assets/fr/17.webp)



### Acceda al sitio web y explore las ofertas de préstamos



Una vez que su dispositivo esté conectado, vaya al [sitio web de Debifi](https://debifi.com/). Inicia sesión para establecer una conexión segura entre la aplicación móvil Debifi y la plataforma web. Esto le facilita la interacción con las ofertas de préstamo disponibles (una visión clara de los detalles de cada oferta) y la gestión de su cuenta.



![image](assets/fr/18.webp)



![image](assets/fr/19.webp)



![image](assets/fr/20.webp)



![image](assets/fr/21.webp)




Tutorial en vídeo sobre cómo iniciar sesión con su cuenta en la plataforma :



![video](https://youtu.be/cUwCfTKDAOo)



## Solicitud de préstamo



La plataforma le pone en contacto con liquidez de calidad institucional y le ofrece una gama de opciones que se adaptan a sus necesidades. Eche un vistazo para saber qué hay disponible. También tiene la flexibilidad de ajustar los parámetros del préstamo en función de su tolerancia al riesgo y su situación financiera.



![image](assets/fr/22.webp)



Las divisas fiat que Debifi ofrece actualmente pueden consultarse en la plataforma.



![image](assets/fr/23.webp)



### Cláusulas contractuales claras y flexibles



Debifi se basa en condiciones de préstamo transparentes y flexibles para satisfacer las necesidades de cada una de las partes (prestamista y prestatario). Las cláusulas clave incluyen :



#### Relación préstamo-valor (LTV)


Los tramos de préstamos Bitcoin suelen ser tres (3):





- Conservador (30% - 40% LTV), que corresponde a un préstamo de bajo riesgo, es ideal para maximizar la seguridad frente a la volatilidad de los precios del Bitcoin;





- Equilibrado (50% LTV) ;





- Agresivo (70% LTV), que ofrece mayor liquidez, pero conlleva un riesgo muy elevado de liquidación durante las fases bajistas del mercado. Para elegir este tramo es imprescindible un seguimiento activo de las condiciones del mercado Bitcoin.



#### Tipos de interés



La fijación de los tipos depende generalmente de la LTV elegida, la duración del préstamo, la volatilidad de las garantías y las evaluaciones de riesgo específicas de la plataforma. Los tipos se mantienen fijos durante toda la duración del préstamo.



#### Plazo del préstamo y flexibilidad de reembolso



Los plazos de amortización son flexibles y están diseñados para adaptarse a las necesidades del prestatario. Los préstamos pueden reembolsarse total o parcialmente en cualquier momento sin comisiones adicionales, siempre que se cumplan los requisitos de garantía. Durante la vigencia del préstamo, los intereses suelen pagarse periódicamente, mientras que el principal se liquida al vencimiento.



#### Derechos de liquidación (Margin calls)



Dada la volatilidad de Bitcoin, los préstamos incluyen una política de ajuste de márgenes claramente definida. Un ajuste de márgenes se produce cuando el LTV aumenta debido a una disminución del valor de la garantía. Debifi notifica al prestatario por correo electrónico y a través de la aplicación, permitiéndole añadir garantías o reembolsar parte del préstamo.


75% LTV - Primera alerta

80% LTV - Segunda alerta

85% LTV - Alerta final

90% LTV - Se liquida la garantía



### Iniciar el proceso de préstamo



Para seleccionar una oferta de préstamo que se adapte a sus necesidades, haga clic en ella para ver sus características.



![image](assets/fr/24.webp)



Puede ver :


1. Nombre de la entidad prestamista ;


2. El importe del préstamo varía;


3. Que recibirá los fondos en USDC Ethereum ;


4. El plazo del préstamo, el tipo de interés y el ratio LTV;


5. Se requiere KYC para esta oferta;


6. Debe introducir el importe exacto que necesita (este importe debe estar dentro de la banda, véase 2);


7. Debe introducirse la dirección Ethereum USDC que se utilizará para recibir los fondos.



Una vez que esté satisfecho con la oferta y haya rellenado la información necesaria, haga clic en "Solicitud Contract".



![image](assets/fr/25.webp)



Volver a la aplicación móvil para ''**Proporcionar clave pública**''.



![image](assets/fr/26.webp)



Pulse '' **Proporcionar clave pública** '', a continuación elija la fuente de la clave pública. El prestamista también tendrá que proporcionar una clave pública.



![image](assets/fr/27.webp)



![image](assets/fr/28.webp)



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



El siguiente paso es firmar el contrato. Todavía en la aplicación móvil, pulsa '' **Firmar Contract** ''



![image](assets/fr/31.webp)



![image](assets/fr/32.webp)



Cuando terminas de firmar el contrato, Debifi crea automáticamente una dirección Bitcoin multifirma única (escrow 3-sur-4) para tu contrato. Mientras tus bitcoins estén en la plica, no podrán utilizarse en ningún otro sitio.



### Depósito de la garantía y recepción de sus fondos



El último paso consiste en depositar su garantía Bitcoin en el sistema de custodia multi-firma. Debifi le muestra la dirección del depósito en garantía (B) y la cantidad de BTC (A) que debe enviar como (garantía + comisión).



![image](assets/fr/33.webp)



También recibirá esta notificación en su aplicación móvil.



![image](assets/fr/34.webp)



En cuanto se confirme su ingreso, el prestamista abonará el importe del préstamo a la dirección de recepción que usted haya indicado, finalizando así la transacción y dándole acceso a los fondos que necesita.



A continuación, recibirá una notificación de Debifi, solicitándole que abone los gastos o comisiones del préstamo para poder avanzar en el estado de su préstamo.



En realidad, una vez creado el contrato, las comisiones del préstamo se deducen automáticamente de la garantía depositada por el prestatario en la dirección de la plica.



Todo lo que tiene que hacer es firmar una transacción que permitirá a Debifi deducir su comisión de la garantía. Por su parte, tu prestamista también tendrá que firmar la transacción de deducción de la comisión, de lo contrario Debifi no podrá recibir su comisión.



![image](assets/fr/35.webp)



Las comisiones de préstamo aplicables son del 1,5-2%, en función de la duración del contrato. La plataforma cobra comisiones solo en Bitcoin.



## Seguimiento de préstamos



Una vez que el préstamo está activo, Debifi le permite seguir su contrato en tiempo real. En la interfaz, encontrará:



- El importe prestado y el plazo restante.
- El ratio LTV (Loan-to-Value) actual, que aumenta cuando el precio del BTC baja y el valor de su garantía disminuye.




Los prestatarios reciben una notificación cuando disminuye el valor de la garantía, y esta información también se muestra en la página de resumen del contrato. Para restablecer la relación préstamo-valor original, el prestatario debe:



- depositar garantías adicionales;
- reembolsar total o parcialmente la deuda.




En caso de aumento del precio de la garantía, el prestatario conserva las plusvalías de la garantía. Sólo debe el importe del préstamo, que está predeterminado y es independiente del precio Bitcoin.




## Reembolso y recuperación de garantías



Al final del plazo acordado (o antes, si lo desea), deberá devolver el préstamo.


En Debifi :





- Vaya a su contrato y haga clic en **Hacer un reembolso**. Introduce el importe total adeudado (principal + intereses).





- Envíe los stablecoins de su wallet a la dirección del prestamista indicada, y vuelva a confirmar el reembolso en la plataforma copiando el **ID** de la transacción de reembolso en la pestaña dedicada. Esto facilita las comprobaciones de Debifi.



Una vez confirmado el pago por el prestamista (y por usted), Debifi le solicitará entonces el **reembolso**. Tu garantía Bitcoin se libera y puedes devolverla desde la plica a tu propia wallet.  No olvides recoger todos tus Bitcoins.



En cuanto reciba sus bitcoins, el contrato de préstamo cambiará a **Contract completado**.



Enhorabuena Has finalizado el proceso.




## Buenas prácticas y seguridad



Sean cuales sean sus objetivos o motivaciones -financiar un proyecto, adquirir una propiedad, comprar bitcoins, etc.-, actúe con mucha cautela antes de pedir un préstamo respaldado por Bitcoin. Tómese su tiempo para evaluar cuidadosamente su decisión, ya que el Bitcoin sigue siendo un activo volátil. **Una caída brusca de su precio podría provocar la liquidación forzosa de tus bitcoins.**



Controle su relación préstamo-garantía (LTV). Establece alertas (precio del BTC, LTV) si es posible. No dejes que tu ratio se acerque al 90%. En caso de duda, aumente la garantía o reembolse anticipadamente.



Controla tus claves. Guarda tu BTC en un wallet seguro (lo ideal es que sea hardware o un wallet de confianza). No establezcas un código PIN relacionado con una fecha importante de tu vida y nunca compartas tu frase de recuperación. En Debifi, tú generate tu clave privada en la aplicación - Debifi no la conoce.



Si es posible, empiece con poco. Para su primer préstamo, pruebe una cantidad modesta para familiarizarse con el proceso.



Utiliza sólo el sitio web oficial de Debifi para estar al día de las novedades de Debifi, y evita los enlaces desconocidos o de suplantación de identidad.  Actualiza la aplicación, protege tu smartphone con un código PIN y elige un Hardware Wallet compatible.



Alternativamente, si usted es un prestamista, este vídeo tutorial le guiará a través del uso de la plataforma Debifi. Desde la selección de prestatarios interesados en su oferta, hasta la provisión de claves públicas, la firma de acuerdos, la transferencia de stablecoins y mucho más.



![video](https://youtu.be/g8iLxwI4xT0)



Ahora ya sabe cómo utilizar la plataforma Debifi para obtener un préstamo.



Te recomiendo que sigas este curso, que profundiza en el Bitcoin, las Stablecoins y su contribución a la soberanía.



https://planb.academy/courses/fdc41e06-ea63-4bf0-a5ac-a0185fe30e46