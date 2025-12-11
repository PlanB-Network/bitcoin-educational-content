---
name: Macadamia Wallet
description: wallet móvil de Cashu para pagos anónimos e instantáneos en BTC
---

![cover](assets/cover.webp)



Macadamia Wallet es una wallet para móviles iOS que implementa el protocolo Cashu, un sistema de ecash chaumiano que permite pagos Bitcoin totalmente anónimos. Gracias a las firmas ciegas, ningún observador puede relacionar tus depósitos con tus gastos, lo que ofrece una confidencialidad similar a la del efectivo físico.



En este tutorial, veremos cómo instalar y configurar Macadamia, realizar tus primeras transacciones en Cashu (acuñar, enviar, recibir, fundir) y gestionar múltiples acuñaciones para asegurar tus fondos.



## ¿Qué es la Macadamia Wallet?



### El protocolo Cashu



Cashu utiliza firmas ciegas inventadas por David Chaum: se depositan bitcoins en un servidor "ceca", que emite fichas equivalentes en satoshis. La casa de la moneda firma estos tokens sin ver su contenido, lo que hace imposible vincular un token a un usuario. Los intercambios son off-chain, peer-to-peer, y totalmente opacos - ni siquiera la casa de la moneda puede rastrear quién paga a quién.



Macadamia es una wallet iOS de código abierto desarrollada en Swift/SwiftUI. Funciona sin cuenta ni KYC, tus tokens se almacenan localmente y están protegidos por una frase seed. El código es auditable en GitHub y los tokens son interoperables con otros monederos Cashu (Minibits, Cashu.me).



### Modelo de custodia y compromiso



**Importante**: Cashu opera en un modelo de custodia. Las fichas son promesas de pago (pagarés) respaldadas por las reservas de Bitcoin de la casa de la moneda. Si la casa de la moneda desaparece, tus fichas pierden su valor. Este es el compromiso para la máxima confidencialidad.



Utilice Macadamia como wallet físico: sólo pequeñas cantidades. Reparte tus fondos entre varias mentas para diluir el riesgo.



## Características principales



Macadamia implementa las cuatro operaciones fundamentales del protocolo Cashu. **Mint** convierte tus satoshis en tokens a través de una factura Lightning. **Enviar** te permite enviar tokens de forma gratuita a través de un código QR o un enlace, completamente off-chain. **Recibir** te permite recibir tokens o generate una factura Lightning. **Fundir** paga una factura Lightning destruyendo tus tokens.



wallet soporta la gestión de múltiples mints simultáneamente. Puedes intercambiar fichas entre distintas cecas a través de Lightning.



## Plataformas compatibles



Macadamia solo está disponible en iOS 17 o superior para iPhone y iPad. La aplicación nativa Swift/SwiftUI ofrece una integración óptima con el ecosistema Apple.



El protocolo Cashu garantiza la interoperabilidad entre monederos. Puedes restaurar tu frase seed en otras aplicaciones como Minibits en Android o Nutstash en escritorio.



La versión actual se distribuye a través de TestFlight. Utilice sólo pequeñas cantidades con esta versión beta.



## Instalación



Macadamia está disponible actualmente a través de TestFlight, el programa de pruebas beta de Apple. He aquí cómo instalarla:



### Instalación mediante TestFlight



**Paso 1: Descargar TestFlight**



Si aún no tienes la aplicación TestFlight en tu dispositivo, busca "TestFlight" en la App Store e instálala. TestFlight es la aplicación oficial de Apple para probar versiones beta de aplicaciones iOS.



**Paso 2: Únase al programa beta de Macadamia** (en francés)



Una vez instalado TestFlight, sigue este enlace de invitación desde tu iPhone o iPad: [https://testflight.apple.com/join/RMU6PaRu](https://testflight.apple.com/join/RMU6PaRu)



El enlace abrirá automáticamente TestFlight y le ofrecerá instalar Macadamia Wallet. Toca "Aceptar" y luego "Instalar" para iniciar la descarga. La aplicación pesa unos diez megabytes y tarda unos segundos en instalarse.



![Installation TestFlight](assets/fr/01.webp)



### Información importante sobre las versiones beta



Macadamia se encuentra aún en fase de desarrollo activo. Las versiones TestFlight se actualizan con frecuencia y pueden introducir nuevas funciones o corregir errores. Sin embargo, como ocurre con cualquier versión beta, pueden producirse fallos de funcionamiento. **Le recomendamos encarecidamente que utilice sólo pequeñas cantidades**, que acepte que podrían perderse en caso de problema técnico.



Macadamia no recoge ningún dato del usuario según la política de privacidad mostrada. Asegúrese de comprobar que el desarrollador es cypherbase UG al instalar.



## Configuración inicial



En el primer lanzamiento, Macadamia genera una frase BIP-39 de 12 palabras. Anótalas en un lugar seguro, nunca como captura de pantalla. Estas palabras te permiten recrear tu wallet y gastar tus fichas.



![Configuration initiale](assets/fr/02.webp)



Siga los cuatro pasos: bienvenida, aceptar condiciones, guardar frase seed y confirmación final.



![Interface principale](assets/fr/03.webp)



Una vez finalizada la configuración, Macadamia presenta tres pestañas principales. **Wallet** muestra su saldo y el historial de transacciones. **Mints** le permite gestionar sus servidores Cashu. **Configuración** da acceso a la configuración y a su frase seed.



![Ajout d'un mint](assets/fr/04.webp)



Ahora necesitas configurar una ceca, es decir, un servidor Cashu que emitirá tus tokens. Vaya a la pestaña "Casas de la Moneda", pulse "Añadir nueva URL de Casa de la Moneda" e introduzca la dirección de la casa de la moneda elegida (por ejemplo, mint.cubabitcoin.org). Echa un vistazo a bitcoinmints.com o cashu.space para encontrar cecas públicas de buena reputación. Valida sólo las cecas cuya reputación hayas comprobado, ya que tendrán la custodia de tus satoshis.



## Uso diario



### Creación de nuevas fichas (Mint)



Para alimentar su wallet Macadamia con ecash, debe realizar una operación "Mint" (para crear fichas). Toque "Recibir" y elija la opción "Rayo". Introduzca la cantidad deseada (por ejemplo, 1000 sats), seleccione la menta que desea utilizar y, a continuación, generate la factura Lightning.



![Opération Mint](assets/fr/05.webp)



Pague la factura Lightning generada con su wallet habitual (Phoenix, Zeus, BlueWallet).



![Confirmation Mint](assets/fr/06.webp)



Las fichas Cashu aparecen instantáneamente en tu saldo tras el pago.



### Enviar fichas



Para enviar fichas Cashu a otro usuario, toque el botón "Enviar" en la pantalla principal y seleccione "Ecash". Introduzca la cantidad a enviar (por ejemplo, 50 sats) y añada una nota descriptiva si es necesario.



![Envoi Ecash](assets/fr/07.webp)



Comparte el código QR o el texto generado a través de iMessage, Signal o Telegram. El destinatario reclama los fondos al instante y de forma gratuita.



### Recibir fichas



Para recibir fichas Cashu enviadas por otro usuario, toca "Recibir" y luego selecciona "Ecash". Escanea el código QR token o pega el enlace token que has recibido.



![Réception Ecash](assets/fr/08.webp)



Toque "Redeem" para reclamar token.



### Pagos relámpago (fusión)



Para pagar una factura Lightning con tus fichas Cashu, toca "Enviar" y selecciona "Lightning". Pega una factura BOLT11 que desees pagar.



![Paiement Lightning](assets/fr/11.webp)



La casa de la moneda destruye tus tokens y ejecuta el pago Lightning. Así puedes pagar cualquier servicio Lightning preservando tu anonimato.



### Intercambiar mentas



Cuando recibe fichas de una fábrica de moneda que no ha configurado, Macadamia le ofrece varias opciones para gestionar estas fichas.



![Swap inter-mints](assets/fr/09.webp)



Añade la nueva ceca o intercambia los tokens con una ceca existente. El canje utiliza Lightning como puente para transferir tus fondos de forma anónima.



### Gestión avanzada de varias mentas



Macadamia ofrece sofisticadas herramientas para gestionar varias mentas simultáneamente y asignar estratégicamente sus fondos.



![Gestion multi-mints](assets/fr/10.webp)



"Distribuir fondos" distribuye automáticamente su saldo según porcentajes (por ejemplo, 50/50). "Transferir" permite realizar transferencias manuales entre cecas para diversificar sus riesgos.



## Ventajas y limitaciones



**Destacados** :





- Máxima confidencialidad**: Transacciones imposibles de rastrear, incluso por la casa de la moneda. Sin metadatos blockchain, intercambios peer-to-peer sin rastro.
- Rápido y gratuito**: Transferencias instantáneas y gratuitas en un céntimo, ideales para micropagos.
- Interoperabilidad**: fichas Cashu estandarizadas para su uso con otros monederos compatibles (Minibits, Nutstash).
- Sencillez**: Interface iOS nativo es accesible para principiantes sin dejar de ser auditable (código abierto).



**Limitaciones** :





- Modelo de custodia**: se requiere la confianza de una fábrica de moneda. Si una ceca desaparece, tus fichas pierden su valor.
- sólo iOS**: No hay versión para Android/escritorio. La interoperabilidad de Cashu permite el acceso a través de otros monederos, pero la experiencia óptima sigue siendo iOS.
- Dependencia de Mint**: Mint offline = incapaz de realizar transacciones que requieran su intervención (Mint, Melt).
- Tecnología emergente** : Desarrollo activo, posibles errores, normas en evolución.



## Buenas prácticas





- Diversifique sus caramelos de menta**: Reparta sus fichas entre varias casas de la moneda de buena reputación para diluir el riesgo.
- Limite las cantidades**: Utilice Macadamia como wallet físico para pagos diarios, no como caja fuerte.
- Asegura tu seed**: Guarde su frase de 12 palabras en papel en un lugar seguro. Prueba la restauración de vez en cuando.
- Comprueba las mentas**: Consulta cashu.space y los foros de la comunidad antes de añadir un mint. Elige aquellos con un buen tiempo de actividad y una reputación sólida.
- VPN o Tor**: Oculta tu IP con VPN/Tor para maximizar la privacidad en la red.
- Únete a la comunidad**: Grupos de Telegram/Discord Cashu para actualizaciones, recomendaciones de mentas y mejores prácticas.



## Conclusión



Macadamia Wallet aporta las propiedades del efectivo físico a la Bitcoin digital. Al combinar las firmas ciegas Chaum y Lightning, ofrece una solución elegante para la confidencialidad transaccional. Su interfaz nativa para iOS hace accesible una sofisticada tecnología criptográfica sin dejar de ser de código abierto e interoperable con el ecosistema Cashu.



El modelo de custodia exige vigilancia y buenas prácticas de seguridad. Utilizado correctamente, Macadamia se convierte en una herramienta inestimable para los pagos cotidianos que requieren anonimato, complementando a los monederos no custodiados para el ahorro.



## Recursos



### Documentación oficial




- Sitio web oficial: [macadamia.cash](https://macadamia.cash)
- Preguntas frecuentes sobre la macadamia: [macadamia.cash/faq](https://macadamia.cash/faq)
- Código fuente GitHub: [github.com/zeugmaster/macadamia](https://github.com/zeugmaster/macadamia)



### Documentación sobre Cashu




- Documentación técnica: [docs.cashu.space](https://docs.cashu.space)
- Lista de cecas públicas: [bitcoinmints.com](https://bitcoinmints.com)
- Sitio web oficial del protocolo: [cashu.space](https://cashu.space)



### Comunidad




- Telegrama del grupo Cashu: [t.me/cashu_ecash](https://t.me/cashu_ecash)