---
name: Bisq Easy Mobile
description: "Un protocolo de comercio entre iguales para nuevos usuarios de bitcoin: sin intermediarios, sin KYC."
---
![cover](assets/cover.webp)


## Introducción


El protocolo comercial [Bisq Easy](https://bisq.network/bisq-easy/) está diseñado para [Bisq 2](https://github.com/bisq-network/bisq2), el sucesor de [Bisq v1](https://github.com/bisq-network/bisq). Bisq 2 soportará múltiples protocolos comerciales, redes de privacidad e identidades. Facilita la compra de Bitcoin sin comisiones comerciales y sin necesidad de depósito de seguridad. Está pensada para los nuevos compradores de Bitcoin que busquen una opción sin necesidad de conocer su identidad y que deseen ser atendidos eficazmente por vendedores con experiencia y conocimientos que estén familiarizados con la plataforma Bisq.


Actualmente, Bisq Easy es el único protocolo comercial para Bisq 2. Se prevén más protocolos comerciales en el futuro. Más información sobre Bisq 2 en este tutorial:


https://planb.academy/tutorials/exchange/peer-to-peer/bisq-v2-c1c6a702-6c16-4101-8b90-62c424017b80

Esta breve guía es un complemento del tutorial anterior sobre la compra de Bitcoin utilizando la aplicación [Bisq Easy Mobile](https://github.com/bisq-network/bisq-mobile) y Lightning.


## 1️⃣ Primeros pasos


Para empezar, descarga Bisq Easy Mobile desde la [página de descarga](https://bisq.network/downloads/). Se recomienda verificar la descarga. Las instrucciones de verificación también están disponibles en la [página de descargas](https://bisq.network/downloads/). Tras la instalación, debes aceptar el "Acuerdo de usuario". A continuación, crea un perfil público compuesto por un `nombre de usuario` y un avatar (representado por un `icono de robot`). Con Bisq Easy, también puedes crear varios perfiles de usuario dentro de un mismo cliente. Tras una breve inicialización, accederás a la "pantalla de inicio". La aplicación destaca material educativo directamente en la página principal. Pulse "Open Trade Guide" para familiarizarse con la información más reciente.


![image](assets/en/01.webp)


La guía de comercio explica todo lo pertinente en sencillos pasos:



- Cómo operar en Bisq Easy
- ¿Cómo funciona el proceso comercial?
- ¿Qué debo saber sobre las normas comerciales?


Otra sección importante es **"¿Hasta qué punto es seguro operar con Bisq Easy?**


![image](assets/en/08.webp)


Marque la casilla "He leído y comprendido" y pulse "Finalizar".


![image](assets/en/02.webp)


## 2️⃣ Haga una copia de seguridad de sus datos


Antes de empezar, vamos a ocuparnos de algunas tareas domésticas y a crear una `copia de seguridad` de su archivo de almacenamiento de datos. Ve a `Más` > `Copia de seguridad y restauración` para guardar tu perfil y tu historial de operaciones. Si pierdes tu dispositivo sin una copia de seguridad, tu reputación y las operaciones en curso serán irrecuperables. Introduzca una `Contraseña` para encriptar su copia de seguridad.


![image](assets/en/11.webp)


## 3️⃣ Ofertas


Desde la pantalla de inicio, hay dos formas de navegar hasta las ofertas. Pulse "Explorar ofertas" en el centro de la pantalla o pulse "Ofertas" en el menú inferior. A continuación, seleccione la divisa con la que desea operar.


![image](assets/en/03.webp)


A diferencia de [Bisq 1](https://planb.academy/en/tutorials/exchange/peer-to-peer/bisq-fe244bfa-dcc4-4522-8ec7-92223373ed04), que requiere una garantía, Bisq Easy se basa únicamente en la reputación del vendedor como garantía. Aunque este enfoque permite a los compradores adquirir Bitcoin por primera vez sin necesidad de poseerlo previamente, deposita un alto grado de confianza en la capacidad del vendedor para entregar Bitcoin tras recibir los pagos en fiat. Por lo tanto, el modelo Bisq Easy security está optimizado sólo para pequeñas cantidades y las operaciones están limitadas a un equivalente de 600 USD por transacción para minimizar el riesgo. En la sección `Offerbook`, seleccione filtros para métodos de pago y liquidación en Lightning o Bitcoin (on-chain).


![image](assets/en/04.webp)


Tras aplicar los "filtros", seleccione una oferta adecuada de un socio comercial de confianza. Aparecerán el método de pago y el tipo de liquidación preseleccionados por el vendedor (`Lightning` o `on-chain`). Asegúrese de que coinciden con sus preferencias antes de continuar. Aquí seleccionamos la opción Rayo ⚡.


![image](assets/en/05.webp)


Revise y confirme los detalles de la operación pulsando en "Confirmar aceptación de oferta". Una ventana emergente le confirmará que ha aceptado la oferta. Pulse Mostrar operación en "Operaciones abiertas". En la sección de Operaciones Abiertas, pegue su `Factura relámpago` y pulse `Enviar al vendedor` para compartirla. Ahora espere los datos de la cuenta de pago del vendedor. Los vendedores pueden tardar en responder. Compruebe periódicamente las actualizaciones en la ventana de chat.


![image](assets/en/06.webp)


Envía un breve saludo en el chat. El vendedor compartirá los detalles del pago cuando se conecte


![image](assets/en/09.webp)


Una vez que haya recibido los datos de pago necesarios del vendedor, proceda a completar el pago. A continuación, pulse el botón "Confirmar que ha realizado el pago" y espere pacientemente el acuse de recibo. ️ ⌛️


Por último, cuando el vendedor confirme la recepción del pago, usted también deberá confirmar la recepción de la Bitcoin. Con esto se completa la compra con Bisq en Modo Fácil. ¡Enhorabuena! Ahora puede pulsar el botón `cerrar la operación`.


![image](assets/en/10.webp)


## 4️⃣ Resolución de litigios en Bisq Fácil


Si algo va mal en su comercio, tanto compradores como vendedores pueden solicitar apoyo de mediación.


**Qué pueden hacer los mediadores:**

- Ayudar a completar con éxito los intercambios

- Verificar pagos en fiat, altcoin y Bitcoin

- Cancelar operaciones cuando sea necesario

- Informar de infracciones graves de las normas a los moderadores para posibles expulsiones de usuarios


**Consecuencias para los vendedores fraudulentos:**

En función de su tipo de reputación:



- Reputación del bono BSQ**: La DAO puede confiscar sus BSQ en bonos
- Cebolla Address Reputación**: Su Bisq 1 dirección de cebolla puede ser prohibido


**Nota importante:** Dado que toda la reputación está ligada a tu perfil de usuario, un baneo desactiva tu reputación por completo.


## 5️⃣ Cree su propia oferta


En lugar de aceptar las ofertas existentes, puedes crear tu propia oferta de compra y dejar que los vendedores acudan a ti. Esta es la opción adecuada si no encuentras ninguna oferta con la prima o las formas de pago adecuadas en el mercado en el que quieres operar, aunque tendrás que esperar a que un vendedor acepte.


En la pantalla "Ofertas", pulse el icono verde "+" de la esquina inferior derecha. A continuación, selecciona "Comprar Bitcoin" y elige tu moneda fiduciaria.


Establezca sus parámetros comerciales:



- Importe fijo o Importe por intervalos**: Elige cuánto quieres gastar.
- Forma de pago**: Seleccione una de las opciones disponibles
- Liquidación**: Elige Rayo ⚡ o ₿ on-chain


Revise sus datos y pulse "Crear oferta". Tu oferta aparecerá en el "Libro de ofertas".


![image](assets/en/07.webp)


*Nota: Como comprador en Bisq Easy, no necesitas reputación: ésta es la principal ventaja. Los vendedores asumen el requisito de reputación y el riesgo, razón por la cual cobran primas. Su oferta sólo tiene que tener un precio lo suficientemente atractivo como para que los vendedores con buena reputación la tengan en cuenta


Una vez publicada, espera en la sección `Libro de ofertas`. Cuando un vendedor acepte tu oferta, recibirás una notificación. Abre la operación en "Operaciones abiertas", donde el vendedor y tú podréis intercambiar vuestros datos de pago. Envía tu dirección Bitcoin o factura Lightning al vendedor. Después de enviar el fiat, confirma el pago. Cuando el vendedor confirme la recepción, liberará los Bitcoin para completar la transacción.


## 🎯 Conclusión


Bisq Easy permite comprar Bitcoin sin garantías, lo que resuelve el clásico problema del huevo y la gallina para los nuevos compradores. La contrapartida es clara: se confía en la reputación del vendedor en lugar de en los fondos bloqueados como garantía. Este enfoque basado en la confianza explica la prima típica del 5-15%, que compensa a los vendedores reputados por su inversión en generar confianza y proporcionar apoyo. Aunque el sistema limita las operaciones a pequeñas cantidades para contener las pérdidas potenciales, siempre hay que ceñirse a los vendedores con una sólida reputación. Para los recién llegados dispuestos a aceptar estas condiciones, Bisq Easy ofrece un punto de entrada fácil a Bitcoin.


## 📚 Bisq Easy Mobile Resources


[Github](https://github.com/bisq-network/bisq-mobile) | [Sitio web ](https://bisq.network/bisq-easy/)| [Wiki](https://bisq.wiki/Bisq_Easy)