---
name: Debifi
description: Consigue un préstamo sin custodia garantizado por Bitcoin.
---

![cover](assets/cover.webp)




## Introducción



Durante siglos, el préstamo tradicional ha permitido financiar muchos proyectos. Sin embargo, sigue siendo lento, costoso y poco inclusivo, sobre todo para quienes no tienen acceso a una infraestructura bancaria sólida.



El auge del protocolo Bitcoin inauguró una nueva era financiera, que trajo consigo una serie de retos. Uno de estos retos era cómo obtener liquidez sin verse obligado a vender Bitcoin, perdiendo así la exposición a su potencial de crecimiento



El resultado es **Debifi**, una plataforma que se posiciona como una alternativa moderna a los bancos. El objetivo es claro: hacer que el crédito sea lo más sencillo y transparente posible, combinando las ventajas del sistema financiero tradicional con la libertad que ofrece Bitcoin. El nombre Debifi refleja esta visión: ***Decentralized Bitcoin Finance***, una contracción que ilustra el encuentro de las finanzas descentralizadas y la innovación de la Bitcoin.



Debifi es una plataforma de préstamo sin custodia respaldada por Bitcoin, lo que significa que usted conserva el control de sus claves privadas. Permite a los usuarios desbloquear liquidez en Exchange por sus bitcoins bloqueados como garantía. A diferencia de los préstamos bancarios tradicionales, Debifi utiliza un sistema de custodia multi-firma (3 de 4) y no acepta hipotecas colaterales, garantizando una mayor seguridad y transparencia.



En la práctica, esto significa que ni Debifi ni un prestamista individual pueden gastar su BTC sin el acuerdo de tres partes (usted, el prestamista y un tercero de confianza). Esto hace que el sistema sea más seguro: si pides un préstamo en Debifi, conservas Ownership de tus Bitcoin hasta que el préstamo se haya devuelto en su totalidad.



## Ventajas de Debifi



Con Debifi, se trata de préstamos colateralizados, seguridad Blockchain (multifirma, 2FA), una selección de stablecoins/líquidos, confidencialidad y control total Bitcoin. Debifi "le permite mantener su dinero" (sus claves, sus monedas), al tiempo que ofrece tasas competitivas y acceso global a préstamos respaldados por BTC.



He aquí una rápida comparación entre un préstamo Debifi y un préstamo bancario tradicional:



| Caractéristiques       | Prêt via Debifi                                                       | Prêt bancaire traditionnel                                                 |
| ---------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Accessibilité          | ✔️ Ouvert à tout détenteur de Bitcoin (même sans historique bancaire) | ❌ Souvent réservé aux clients avec garanties physiques et dossiers solides |
| Vitesse d’obtention    | ✔️ Liquide en quelques minutes/heures                                 | ❌ Processus long (jours ou semaines)                                       |
| Garanties exigées      | ✔️ Collatéral en Bitcoin uniquement                                   | ❌ Garanties physiques (maisons, terrains, revenus stables)                 |
| Contrôle de l’actif    | ✔️ Vous conservez l’exposition au Bitcoin et son potentiel de hausse  | ❌ Vous n’avez aucun lien entre le prêt et vos actifs financiers            |
| Souplesse géographique | ✔️ Disponible partout (sans contrainte géographique bancaire)         | ❌ Limité à la juridiction de la banque                                     |
| Risque principal       | ❌ Risque de liquidation si le prix du BTC chute trop                  | ❌ Risque de saisie de biens ou impact négatif sur la cote de crédit        |

Antes de mostrarte paso a paso cómo pedir un préstamo en Debifi, hay algunos puntos que creo que debes saber.




## Definiciones





- Las comisiones de apertura** son gastos únicos que se cobran en el momento de la concesión del préstamo y se calculan como un porcentaje del importe prestado. Estas comisiones cubren los gastos administrativos, operativos y de gestión.





- La garantía** es un activo que se deposita para garantizar un préstamo. En el caso de Debifi, la garantía es Bitcoin (BTC), que el prestatario deposita en la plica Multisig 3/4.





- El sistema Multisig escrow (3/4)** es un mecanismo de depósito seguro en el que los bitcoins de un prestatario se colocan en un Address multifirma. En concreto, cuatro (4) partes poseen cada una una clave (prestatario, prestamista, Debifi, tercero independiente). Para mover los fondos, se requieren al menos 3 de las 4 firmas.





- Una stablecoin** es una criptomoneda cuyo valor está vinculado a un activo estable (por ejemplo, el dólar estadounidense), lo que evita la volatilidad del Bitcoin. Por ejemplo, 1 USDC siempre vale ~$1, ya que está respaldada por reservas fiduciarias.





- La relación préstamo-valor (LTV)** de un préstamo determina la cantidad de efectivo que puede pedir prestado como garantía para su Bitcoin. Relación LTV = Importe del préstamo / Importe de la garantía * 100. Por ejemplo, un LTV del 50% significa que el valor del préstamo es igual al 50% del valor de la Bitcoin depositada.




Videotutorial de BTC Sessions :



![Vidéo tutoriel de BTC Sessions](https://youtu.be/02gzg-en8n0)



## Primeros pasos con Debifi



Para empezar a trabajar en Debifi, necesitarás algunos requisitos previos.


### Requisitos previos



Antes de pedir prestado a Debifi, asegúrese de que dispone de los siguientes elementos:





- Bitcoin Wallet: donde guardas tu BTC (idealmente no custodiado, por ejemplo Hardware Wallet o un Wallet móvil de confianza). Es desde esta Wallet desde donde enviarás la garantía Bitcoin a Debifi y recibirás los fondos.





- Stablecoins o fiat: Debifi presta en stablecoins y algunas monedas fiat. Las principales stablecoins utilizadas son USDT y USDC.



Puede utilizar Aqua, una Bitcoin y Liquid Wallet que también soporta la gestión de stablecoin USDT en varias redes. O COLDCARD (Mk4 o Q), actualmente el único hardware soportado por Debifi.



https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3



- KYC (*Know Your Customer*): dependiendo de la oferta de préstamo elegida, puede ser necesario un proceso de verificación de identidad. En Debifi, cada oferta indica si se requiere KYC o no. Así que prepárese en consecuencia. KYC se lleva a cabo por terceros proveedores de servicios fiables como Sumsub.



![image](assets/fr/03.webp)





- Aplicación de autenticación de dos factores: Debifi requiere un código Authenticator para cada acción importante. Es un Layer extra de seguridad. En este tutorial, vamos a utilizar Google Authenticator. Alternativamente, puede utilizar otros como mejor le parezca.



https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc



- Sitio web y aplicación móvil de Debifi: Debifi es a la vez un sitio web y una aplicación móvil, y ambos funcionan en tándem. La aplicación móvil se convierte en una Wallet, que almacena tu clave privada y gestiona la firma de los contratos. Además, tienes que utilizar el sitio web para comprometer contratos (una Interface grande te da una visión general de los contratos de préstamo y sus detalles).





- La aplicación móvil Debifi (iOS/Android) es necesaria para contratar préstamos. Debe descargar la aplicación, crear una cuenta y "vincular" su dispositivo (registrar el dispositivo en su cuenta). La aplicación Debifi admite la autenticación de dos factores (2FA) y, sin un smartphone, no podrá confirmar las transacciones en Debifi.



### Crear una cuenta



Visite [el sitio web oficial de Debifi](https://debifi.com/app).



![image](assets/fr/04.webp)



Instala la aplicación según el tipo de smartphone que tengas y ábrela.



![image](assets/fr/05.webp)



![image](assets/fr/06.webp)



Una vez en la aplicación, haz clic en el menú **Configuración**.



![image](assets/fr/07.webp)



A continuación, haga clic en **Iniciar sesión o crear cuenta** para crear una cuenta con su correo electrónico Address.



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


Los tramos de préstamos de Bitcoin suelen ser tres (3):





- Conservador (20% - 40% LTV), que corresponde a un préstamo de bajo riesgo, es ideal para maximizar la seguridad frente a la volatilidad de los precios del Bitcoin;





- Equilibrado (50% LTV) ;





- Agresivo (70% - 85% LTV), que ofrece mayor liquidez, pero conlleva un riesgo muy elevado de liquidación durante las fases bajistas del mercado. La supervisión activa de las condiciones del mercado Bitcoin es imprescindible a la hora de elegir este tramo.



#### Tipos de interés



La fijación de los tipos depende generalmente de la LTV elegida, la duración del préstamo, la volatilidad de las garantías y las evaluaciones de riesgo específicas de la plataforma. Los tipos se mantienen fijos durante toda la duración del préstamo.



#### Plazo del préstamo y flexibilidad de reembolso



Los plazos de amortización de los préstamos suelen ser flexibles y se adaptan a las necesidades del usuario. Los pagos pueden efectuarse en cualquier momento siempre que se cumplan los requisitos de la garantía. Los pagos de los préstamos suelen consistir en intereses durante la duración del préstamo, y el principal vence al vencimiento.



#### Derechos de liquidación (Margin calls)



Dado que el precio del Bitcoin es volátil, un préstamo responsable incluye en el acuerdo políticas específicas de ajuste de márgenes. Esta política permite avisar al prestatario para que aporte garantías adicionales o reembolse una parte del préstamo.



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


7. Debe introducirse el Ethereum USDC Address que se utilizará para recibir los fondos.



Una vez que esté satisfecho con la oferta y haya rellenado la información necesaria, haga clic en "Solicitud Contract".



![image](assets/fr/25.webp)



Volver a la aplicación móvil para ''**Proporcionar clave pública**''.



![image](assets/fr/26.webp)



Pulse '' **Proporcionar clave pública** '', a continuación, elija la fuente de la clave pública. El prestamista también tendrá que Supply una clave pública.



![image](assets/fr/27.webp)



![image](assets/fr/28.webp)



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



El siguiente paso es firmar la Contract. Todavía en la aplicación móvil, pulse '' **Firmar Contract** ''



![image](assets/fr/31.webp)



![image](assets/fr/32.webp)



Cuando termines de firmar la Contract, Debifi creará automáticamente una Bitcoin Address (escrow 3-sur-4) única multifirma para tu Contract. Mientras tus bitcoins estén en la plica, no podrán utilizarse en ningún otro sitio.



### Depósito de la garantía y recepción de sus fondos



El último paso es depositar su garantía Bitcoin en el sistema de fideicomiso multi-firma. Debifi le muestra entonces el Address en custodia (B) y la cantidad de BTC (A) a enviar como (garantía + comisión).



![image](assets/fr/33.webp)



También recibirá esta notificación en su aplicación móvil.



![image](assets/fr/34.webp)



En cuanto se confirme su depósito, el prestamista abonará el importe del préstamo al Address receptor que usted haya indicado, finalizando así la transacción y dándole acceso a los fondos que necesita.



A continuación, recibirá una notificación de Debifi, solicitándole que abone los gastos o comisiones del préstamo para poder avanzar en el estado de su préstamo.



En realidad, una vez creada la Contract, las comisiones del préstamo se deducen automáticamente de la garantía depositada por el prestatario en la Address de plica.



Todo lo que tiene que hacer es firmar una transacción que permitirá a Debifi deducir su comisión de la garantía. Por su parte, tu prestamista también tendrá que firmar la transacción de deducción de la comisión, de lo contrario Debifi no podrá recibir su comisión.



![image](assets/fr/35.webp)



Las comisiones de préstamo aplicables son del 1,5-2%, en función del plazo de la Contract. La plataforma cobra comisiones solo en Bitcoin.



## Seguimiento de préstamos



Una vez que el préstamo está en marcha, Debifi le permite supervisar su Contract en tiempo real. En Interface, verá :





- El importe prestado y el plazo restante.
- Relación LTV (Loan-to-Value) actual: El LTV aumenta si el precio del BTC baja (ya que tu garantía vale menos). Se establece un umbral de alerta (generalmente el 90%). Si su LTV supera este umbral, existe el riesgo de liquidación forzosa. Debifi le dará 24 horas para reaccionar.



Se informará a los prestatarios de la reducción del precio. Esta información también estará disponible en la página de resumen de Contract. Para restablecer la relación préstamo-valor original de un préstamo, el prestatario debe :





- o depositar una garantía adicional ;
- reembolsar total o parcialmente la deuda.



En caso de aumento del precio de la garantía, el prestatario conserva las plusvalías de la garantía. Sólo debe el importe del préstamo, que está predeterminado y es independiente del precio Bitcoin.




## Reembolso y recuperación de garantías



Al final del plazo acordado (o antes, si lo desea), deberá devolver el préstamo.


En Debifi :





- Vaya a su Contract y haga clic en **Hacer un reembolso**. Introduzca el importe total adeudado (principal + intereses).





- Envíe los stablecoins de su Wallet al Address del prestamista indicado, y vuelva a confirmar el reembolso en la plataforma copiando el **ID** de la transacción de reembolso en la pestaña dedicada. Esto facilita las comprobaciones de Debifi.



Una vez confirmado el pago por el prestamista (y por usted), Debifi le solicitará el **reembolso**. Tu garantía Bitcoin se libera y puedes devolverla desde la plica a tu propia cartera.  No olvides recoger todos tus Bitcoins.



En cuanto reciba sus bitcoins, el préstamo Contract cambiará a **Contract completado**.



Enhorabuena Has finalizado el proceso.




## Buenas prácticas y seguridad



Sean cuales sean sus objetivos o motivaciones -financiar un proyecto, adquirir una propiedad, comprar bitcoins, etc. - sea extremadamente prudente antes de suscribir un préstamo respaldado por Bitcoin. - sea extremadamente prudente antes de suscribir un préstamo respaldado por Bitcoin. Tómese su tiempo para considerar cuidadosamente su decisión, ya que el Bitcoin sigue siendo un activo volátil. **Una caída brusca de su precio podría provocar la liquidación forzosa de sus bitcoins**.



Controla tu relación préstamo-garantía (LTV). Establece alertas (precio del BTC, LTV) si es posible. No dejes que tu ratio se acerque al 90%. En caso de duda, aumente la garantía o reembolse anticipadamente.



Controla tus claves. Guarda tu BTC en una Wallet segura (lo ideal es que sea hardware o una Wallet de confianza). No establezcas un código PIN relacionado con una fecha importante de tu vida y nunca compartas tu frase de recuperación. En Debifi, tú generate tu clave privada en la aplicación - Debifi no la conoce.



Si es posible, empiece con poco. Para su primer préstamo, pruebe una cantidad modesta para familiarizarse con el proceso.



Utiliza sólo el sitio web oficial de Debifi para estar al día de las novedades de Debifi, y evita los enlaces desconocidos o de suplantación de identidad.  Actualiza la aplicación, protege tu smartphone con un código PIN y elige una Hardware Wallet compatible.



Alternativamente, si usted es un prestamista, este vídeo tutorial le guiará a través del uso de la plataforma Debifi. Desde la selección de prestatarios interesados en su oferta, hasta la provisión de claves públicas, la firma de acuerdos, la transferencia de stablecoins y mucho más.



![video](https://youtu.be/g8iLxwI4xT0)



Ahora ya sabe cómo utilizar la plataforma Debifi para obtener un préstamo.



Te recomiendo que sigas este curso, que profundiza en la Bitcoin, las Stablecoins y su contribución a la soberanía.



https://planb.academy/courses/fdc41e06-ea63-4bf0-a5ac-a0185fe30e46