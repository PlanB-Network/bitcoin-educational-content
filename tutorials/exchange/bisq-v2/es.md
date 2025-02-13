---
name: Bisq 2
description: Guía completa para usar Bisq 2 e intercambiar bitcoins P2P
---
![cover](assets/cover.webp)

## Introducción

Los intercambios P2P (peer-to-peer) son esenciales para preservar la confidencialidad y la autonomía financiera de los usuarios. Permiten transacciones directas entre particulares sin necesidad de verificar la identidad, lo que es crucial para quienes valoran la privacidad. Para profundizar en los conceptos teóricos, consulte el curso BTC204:

https://planb.network/courses/btc204
### ¿Qué es Bisq 2?

Bisq 2 es la nueva versión del popular intercambio descentralizado Bisq, lanzado en 2024. A diferencia de su predecesor, Bisq 2 ha sido desarrollado para soportar múltiples protocolos de intercambio, ofreciendo a los usuarios una mayor flexibilidad.

**Principales novedades


- Soporte para múltiples redes de privacidad (Tor, I2P)
- Múltiples identidades para una mayor confidencialidad
- API REST para bots de negociación
- Soporte para múltiples tipos de cartera
- Sistema de roles con depósito obligatorio en BSQ

Esta guía se centra exclusivamente en "Bisq Easy", el único protocolo disponible actualmente. Bisq Easy ha sido diseñado específicamente para los nuevos usuarios de Bitcoin. Este protocolo permite a los usuarios comprar y vender Bitcoins contra monedas fiduciarias en una plataforma descentralizada peer-to-peer. Las transacciones están limitadas al equivalente de 600 USD (con un mínimo de 6 USD), y la seguridad del intercambio se basa en la reputación de los vendedores de BTC. Bisq Easy no cobra comisiones ni exige depósitos de seguridad. Se espera que Bisq Easy sustituya a Bisq 1 en los intercambios de efectivo por debajo de 600 USD (o equivalente).

**Características principales:**


- Aplicación de escritorio multiplataforma
- Varios protocolos de intercambio disponibles
- Red P2P descentralizada
- Enfoque en la confidencialidad (sin KYC, uso de Tor)
- Sin custodia (usted conserva el control de sus fondos)
- Código abierto (AGPL)

### Diferencias con Bisq 1

**Para compradores:**


- No se requiere fianza
- Sin comisiones
- Sin cánones mineros
- Seguridad basada en la reputación del proveedor
- Límites de negociación más bajos (equivalentes a 600 USD)

**Para vendedores:**


- No se requiere fianza
- Construir una reputación
- Posibilidad de quemar BSQ o crear bonos BSQ
- Prima de venta potencialmente más alta (10-15% por encima del mercado)

**Nota importante:** Una vez que el protocolo Bisq Multisig haya sido implementado en Bisq 2, la versión antigua de Bisq podrá ser eliminada. Sin embargo, Bisq 1 seguirá utilizándose como herramienta de gestión para Bisq CAD y para los intercambios BSQ-BTC.

### Proceso de intercambio


- El creador de la oferta define las condiciones del intercambio
- Una vez que los operadores han acordado las condiciones (forma de pago y precio), comienza el intercambio
- El vendedor envía sus datos bancarios al comprador, y el comprador envía su dirección Bitcoin al vendedor
- El comprador realiza el pago en efectivo y lo notifica al vendedor
- Una vez recibido el pago, el vendedor envía los bitcoins a la dirección del comprador
- El intercambio se completa cuando el comprador recibe los bitcoins

### Normas importantes


- Antes de intercambiar los datos de pago, el intercambio puede cancelarse sin justificación
- Tras el intercambio de datos, el incumplimiento de las obligaciones puede acarrear el destierro
- Para las transferencias bancarias, **nunca utilice los términos "Bisq" o "Bitcoin "** en el motivo del pago (esto podría provocar la congelación de los fondos o incluso el bloqueo de la cuenta bancaria del destinatario o del pagador)
- Los operadores deben conectarse al menos una vez al día para seguir el proceso
- En caso de problema, los comerciantes pueden recurrir a los servicios de un mediador

## Instalación y configuración

### 1. Descargar y verificar Bisq 2

![Téléchargement de Bisq 2](assets/fr/01.webp)


- Ir a [bisq.network](https://bisq.network/downloads/)
- Descargue la versión de Bisq 2 correspondiente a su sistema operativo (desplácese hacia abajo en la página)
- Verifique la autenticidad del archivo descargado (muy recomendable). Para obtener una guía detallada sobre la verificación de firmas, consulte el siguiente tutorial:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
### 2. Instalación según su sistema

Sigue los pasos de instalación adecuados para tu sistema operativo. Si encuentra alguna dificultad durante la instalación, puede consultar la guía detallada en la [wiki oficial de Bisq](https://bisq.wiki/Downloading_and_installing).

### 3. Primera puesta en marcha


- Iniciar Bisq 2 y aceptar las condiciones de uso

![Conditions d'utilisation](assets/fr/01.webp)


- Crear un nuevo perfil eligiendo un nombre y un avatar

![Création du profil](assets/fr/02.webp)


- A continuación, accederá al panel principal de la aplicación, donde podrá iniciar Bisq Easy para comprar o vender sus primeros bitcoins

![Page d'accueil de Bisq 2](assets/fr/03.webp)

### 4. Establecer métodos de pago


- Acceda a la sección de cuentas de pago desde el menú principal

![Liste des comptes de paiement](assets/fr/04.webp)


- Añada un nuevo método de pago rellenando la información requerida

![Création d'un nouveau compte de paiement](assets/fr/05.webp)

La configuración previa de los métodos de pago es opcional, pero se recomienda para ahorrar tiempo en las operaciones. También puede configurar sus métodos de pago directamente durante una operación poniéndose en contacto con su socio de intercambio.

### 5. Seguridad de la cuenta

**Copia de seguridad de datos:**

A diferencia de Bisq 1, Bisq 2 no integra actualmente un monedero Bitcoin: por lo tanto, las transacciones se realizan a través de sus propios monederos externos. No obstante, te recomendamos que realices copias de seguridad periódicas de tu carpeta de datos de Bisq 2. Para localizar su carpeta de datos, consulte la [wiki oficial de Bisq](https://bisq.wiki/Backing_up_application_data#Back_up_the_entire_Bisq_data_directory).

**Gestión de la identidad:**

Bisq 2 le permite crear múltiples identidades. Cada identidad puede utilizarse para distintos tipos de transacciones. Sus identidades se almacenan en la carpeta de datos.

## Compra y venta de bitcoins

### Cómo comprar Bitcoins

**Opción 1: Aprovechar una oferta existente**


- En la pantalla principal, seleccione "Bisq Easy", pestaña "Getting started", y haga clic en "Start trade wizard"

![Lancer trade wizard](assets/fr/06.webp)


- Elija "Comprar Bitcoin" y seleccione su moneda

![Sélection achat Bitcoin](assets/fr/07.webp)

![Choix de la devise](assets/fr/08.webp)


- Configure sus métodos de pago preferidos (SEPA, Revolut, etc.)

![Configuration méthodes de paiement](assets/fr/09.webp)


- En este punto, o bien dispone de una lista de ofertas que corresponden a sus criterios anteriores, o bien debe ir al "Libro de ofertas"

![Liste des offres](assets/fr/10.webp)


- En el segundo caso, puede visualizar y filtrar las ofertas mediante los botones situados en la parte superior derecha de la interfaz

![Filtres des offres](assets/fr/11.webp)


- Una vez elegida la oferta, sólo tienes que elegir el método de pago y validar el resumen comercial

![Choix modalités de paiement](assets/fr/12.webp)

![Configuration du trade](assets/fr/13.webp)

![Récapitulatif du trade](assets/fr/14.webp)

**Opción 2: Crea tu propia oferta**


- Seleccione "Bisq Easy" y luego "Offerbook"
- Elija su par de negociación (por ejemplo, BTC/EUR)
- Haga clic en "Crear oferta
- Siga el asistente de creación de ofertas: Defina el importe (fijo o rango)

![Configuration du montant](assets/fr/20.webp)


- Seleccione los métodos de pago aceptados

![Sélection méthodes de paiement](assets/fr/21.webp)


  - Compruebe el resumen y publique la oferta

![Récapitulatif et publication](assets/fr/22.webp)

Una vez iniciado el intercambio :


- Envía tu dirección Bitcoin o factura Lightning al vendedor

![Envoi adresse Bitcoin](assets/fr/15.webp)


- Recibir los datos bancarios del vendedor

![Réception coordonnées bancaires](assets/fr/16.webp)

![Détails coordonnées bancaires](assets/fr/17.webp)


- Realice el pago (sin mencionar "Bisq" o "Bitcoin")
- Notificar el pago al vendedor

![Notification paiement](assets/fr/18.webp)


- Esperar a que lleguen los bitcoins

![Attente réception](assets/fr/19.webp)

### ¿Cómo vender Bitcoins?

El proceso de venta en Bisq 2 sigue una lógica similar al de compra, con los mismos pasos principales pero en orden inverso. Puedes crear tu propia oferta de venta o responder a una oferta de compra existente. Aquí tienes un desglose de las distintas opciones y etapas del proceso:

**Opción 1: Crear una oferta de venta**


- Seleccione "Bisq Easy" y luego "Offerbook"
- Haga clic en "Crear oferta" y elija "Vender Bitcoin"
- Configure su oferta :
 - Seleccione la divisa (EUR, USD, etc.)
 - Elija los métodos de pago aceptados
 - Fije el importe (entre 6 y 600 USD equivalentes)
 - Establezca su precio (fijo o % del mercado)
- Compruebe los detalles y publique la oferta

**Opción 2: Aprovechar una oferta existente**


- Consultar las ofertas en la pestaña "Libro de ofertas
- Filtrar por divisa y forma de pago
- Seleccione la oferta que más le convenga
- Compruebe los detalles y acepte la oferta

**Proceso de venta:**

Una vez iniciado el intercambio :


   - Envía tus datos bancarios al comprador
   - Esperar la dirección Bitcoin del comprador
   - Comprobar que la dirección es válida

Tras la notificación del pago :


   - Comprobar que se ha recibido el pago en su cuenta
   - Confirme que el importe y los datos coinciden
   - Enviar bitcoins a la dirección facilitada
   - Marcar la transacción como completada

Finalización :


   - Esperar la confirmación del comprador
   - Deja tu opinión sobre la transacción
   - Construya su reputación para futuras ventas

**Nota importante:** Como vendedor, debes estar especialmente atento al riesgo de devoluciones. Da preferencia a los métodos de pago seguros y comprueba siempre que se ha recibido el pago antes de enviar bitcoins.

## Buenas prácticas y seguridad

### Consejos de seguridad

**Para compradores:**


- Empezar con pequeñas cantidades
- Compruebe la reputación de los vendedores (puntuación mínima de 30.000)
- Utilice sólo los métodos de pago sugeridos
- Compruebe que el vendedor está activo antes de enviar el pago
- Utilice únicamente los datos bancarios facilitados en el chat de intercambio
- Nunca se comunique fuera de la plataforma Bisq 2
- Conservar el justificante de pago
- No envíe nunca información sensible

**Para vendedores:**


- Cuidado con las cuentas nuevas
- Evite los métodos de pago sensibles a las devoluciones (PayPal, Venmo)
- Comprobar que los datos de la cuenta corresponden al comprador
- Limitar la comunicación al chat Bisq 2
- Abrir una mediación en caso de duda

### Creación de reputación (para vendedores)

Para mejorar su reputación en Bisq como vendedor, realice transacciones con regularidad y mantenga una comunicación profesional con los compradores. Responda rápidamente a las peticiones de los compradores para garantizar una experiencia positiva. También puede crear un vínculo BSQ para mostrar su compromiso con la plataforma. Estas acciones generarán confianza y atraerán a más compradores.

### Resolución de litigios


- Póngase en contacto con su homólogo a través del chat
- Si es necesario, abra un contencioso
- Aporte todas las pruebas solicitadas
- Siga las instrucciones del mediador

### Política de privacidad :


- No requiere registro ni verificación centralizada de identidad
- Todas las conexiones pasan por la red Tor (y pronto por I2P)
- Sin servidor central para almacenar datos
- Los detalles de la transacción sólo son legibles por las partes implicadas

### Protección contra la censura :


- Red P2P totalmente distribuida
- Utilizar la red Tor (y pronto I2P) para resistirse a la censura
- Proyecto de código abierto gestionado por una DAO, sin entidad jurídica centralizada

## Ventajas e inconvenientes

### Ventajas de Bisq 2


- Máxima confidencialidad**: Sin KYC, uso de Tor
- Descentralización**: Sin servidor central
- Seguridad**: Código abierto, sin custodia
- Interfaz intuitiva**: más sencilla que Bisq 1
- Flexibilidad**: Múltiples protocolos de intercambio

### Desventajas de Bisq 2


- Liquidez limitada** (por el momento) :
 - Nuevo protocolo en fase inicial
 - Pocas ofertas de venta disponibles
 - Tiempos de espera potencialmente largos para encontrar un comprador
- Límites de negociación**: Máximo de 600 USD por transacción (con Bisq easy)
- Sólo para ordenadores de sobremesa**: Sin aplicación móvil

## Protocolos futuros

Aunque Bisq Easy es actualmente el único protocolo disponible, se están desarrollando otros protocolos para Bisq 2 :


- Bisq Lightning**: Protocolo de intercambio basado en un sistema de custodia que utiliza criptografía de cómputo multipartito en la red Lightning.
- Bisq MuSig**: Migración del protocolo principal de Bisq 1 a Bisq 2, utilizando un multisig 2 contra 2 con depósitos de seguridad.
- Intercambios BSQ**: Swaps atómicos instantáneos entre BSQ y BTC.
- Liquid Swaps**: Intercambio de activos en la red Liquid (USDT, BTC-L) mediante swaps atómicos.
- Intercambios de Monero**: Intercambios atómicos entre Bitcoin y Monero.
- MuSig líquido**: Versión del protocolo multisig que utiliza L-BTC para reducir costes y aumentar la confidencialidad.
- Intercambios submarinos**: Intercambios entre Bitcoin en la red Lightning y Bitcoin on-chain.
- Intercambios de stablecoin**: Intercambios atómicos entre stablecoins Bitcoin y USD.
- Opciones Multisig**: Creación de opciones de compra y venta P2P con bloqueo de BTC en una transacción multisig en cadena.
- Contratos abiertos multisig**: Permite la creación de contratos condicionales personalizados mediante un sistema multisig 2 contra 3 con arbitraje.

Estos protocolos están actualmente en desarrollo y se integrarán progresivamente en Bisq 2, ofreciendo mayor flexibilidad a los usuarios en función de sus necesidades específicas.

## Recursos útiles


- Página web oficial: [bisq.network](https://bisq.network)
- Documentación: [Bisq Wiki](https://bisq.wiki)
- Soporte técnico: [Foro Bisq](https://bisq.community)
- Código fuente : [GitHub](https://github.com/bisq-network)