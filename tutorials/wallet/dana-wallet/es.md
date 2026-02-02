---
name: Dana Wallet
description: Cartera minimalista para pagos silenciosos (BIP-352)
---

![cover](assets/cover.webp)



La reutilización de direcciones Bitcoin es una de las amenazas más directas a la confidencialidad de los usuarios. Cuando un receptor comparte una misma dirección para recibir múltiples pagos, cualquier observador puede rastrear todas las transacciones asociadas y reconstruir su historial financiero. Este problema afecta especialmente a creadores de contenidos, organizaciones benéficas o activistas que desean mostrar públicamente una dirección de donación sin comprometer su privacidad o la de sus donantes.



Dana Wallet responde a este problema con una solución elegante: Silent Payments. Esta wallet minimalista y de código abierto, lanzada en 2024, genera una dirección estática reutilizable al tiempo que garantiza que cada pago recibido acabe en una dirección distinta de la blockchain. El remitente no necesita interacción previa con el destinatario, y ningún observador externo puede vincular transacciones individuales. En la cadena de bloques, estos pagos parecen transacciones Taproot normales y corrientes.



Dana Wallet está disponible en Mainnet y Signet, pero los desarrolladores aún la consideran experimental y recomiendan no depositar fondos que no estés dispuesto a perder. En este tutorial, utilizaremos la versión Signet para descubrir Silent Payments sin arriesgar fondos reales.



## ¿Qué es Dana Wallet?



### Filosofía y objetivos



Dana Wallet adopta un enfoque "SP-first": wallet genera exclusivamente direcciones de Silent Payments y sólo acepta este tipo de pago. No podrá crear una dirección Bitcoin clásica (legado, SegWit o Taproot estándar) con esta aplicación. Esta restricción deliberada le permite concentrarse plenamente en el aprendizaje del protocolo BIP-352 sin distraerse con otras funciones. La interfaz despejada favorece deliberadamente la facilidad de uso frente a la profusión de opciones, lo que hace que la herramienta sea accesible incluso para los usuarios que no conocen los conceptos de confidencialidad de on-chain.



El proyecto es totalmente de código abierto, desarrollado con Flutter para la interfaz móvil y Rust para la lógica criptográfica interna. Esta arquitectura combina una experiencia de usuario fluida con un rendimiento óptimo para operaciones de exploración intensivas.



### ¿Cómo funcionan los pagos silenciosos?



Los pagos silenciosos (BIP-352) se basan en un sofisticado mecanismo criptográfico que utiliza la clave de curva elíptica Diffie-Hellman Exchange (ECDH). El destinatario genera una dirección estática (que empieza por `sp1...` en mainnet o `tsp1...` en Signet) que consta de dos claves públicas distintas: una clave de exploración ($B_{scan}$) para detectar los pagos entrantes, y una clave de gasto ($B_{spend}$) para gastar los fondos recibidos. Esta separación permite mantener la clave de gasto en el hardware wallet mientras se utiliza la clave de escaneado en un dispositivo conectado.



Cuando un remitente desea efectuar un pago, su wallet combina la suma de las claves privadas de sus entradas con la clave pública de exploración del destinatario para calcular un secreto ECDH compartido. Este secreto genera un "pellizco" criptográfico que, sumado a la clave de gasto del destinatario, crea una dirección Taproot única para esa transacción.



El destinatario puede reproducir este cálculo utilizando su clave de exploración privada y las claves públicas visibles en la transacción (propiedad matemática Diffie-Hellman). Esto le permite detectar y gastar los fondos sin ninguna interacción previa con el remitente.



Este planteamiento ofrece varias ventajas:




- Confidencialidad del destinatario**: cada pago va a parar a una dirección diferente
- Confidencialidad del remitente**: no hay ningún identificador persistente que vincule los pagos
- Sin servidor de terceros**: el protocolo funciona de forma autónoma
- Transacciones indistinguibles**: Los pagos silenciosos parecen transacciones ordinarias de Taproot



El principal inconveniente es el coste del escaneado: el destinatario tiene que analizar cada nueva transacción Taproot para detectar las que van dirigidas a él.



Si desea saber más sobre el funcionamiento técnico de Silent Payments, le recomendamos el curso BTC204 sobre confidencialidad en Bitcoin, que incluye un capítulo dedicado a Silent Payments:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Plataformas compatibles



Dana Wallet está disponible como aplicación para Android. El APK puede descargarse a través del repositorio dedicado F-Droid proporcionado por los desarrolladores, a través de Obtainium o directamente desde GitHub. Para los usuarios de Linux, es técnicamente posible compilar la aplicación Flutter para escritorio.



La aplicación no está disponible en iOS ni a través de las tiendas oficiales (Google Play, App Store), lo que refleja su carácter experimental y su orientación a un público técnico.



## Instalación



### Requisitos esenciales



Para instalar Dana Wallet en Android, necesitarás un dispositivo Android con la opción "Orígenes desconocidos" activada en los ajustes de seguridad. No se requiere ninguna cuenta ni registro.



### Añadir depósito F-Cold



El método recomendado es añadir el repositorio F-Droid dedicado de Dana Wallet. Vaya a `fdroid.silentpayments.dev` donde encontrará el enlace al repositorio y un código QR para escanear. El repositorio ofrece actualmente 3 aplicaciones: la versión Mainnet, Desarrollo y Signet.



![Page du dépôt F-Droid Dana Wallet avec QR code et lien](assets/fr/01.webp)



### Instalación a través de F-Droid



Abre la aplicación F-Droid en tu dispositivo Android y, a continuación, accede a Ajustes a través del icono situado en la parte inferior derecha. Selecciona "Repositorios" para gestionar las fuentes de las apps. Pulsa el botón "+" para añadir un nuevo repositorio y, a continuación, escanea el código QR o pega el enlace `https://fdroid.silentpayments.dev/fdroid/repo`. Una vez añadido el repositorio, verás las tres versiones de Dana Wallet disponibles. Selecciona "Dana Wallet - Bookmark" y pulsa "Instalar".



![Ajout du dépôt F-Droid et installation de Dana Wallet - Signet](assets/fr/02.webp)



## Configuración inicial



### Creación de carteras



En el primer lanzamiento, Dana Wallet muestra una pantalla de bienvenida que presenta su misión: "Enviar y recibir donaciones sin intermediarios". Pulsa "Comenzar" para continuar. La siguiente pantalla presenta las tres ventajas principales de la aplicación:




- Donaciones sin esfuerzo**: empiece a recibir donaciones en segundos
- Privacidad por defecto**: sin necesidad de servidores ni infraestructuras complejas
- Experiencia similar a la del correo electrónico**: envíe y reciba bitcoins de forma tan sencilla como un correo electrónico



Puede elegir entre "Restaurar" para restaurar una cartera existente o "Crear nueva wallet" para crear una nueva. Pulse "Crear nueva wallet".



![Premier lancement de Dana Wallet et création du portefeuille](assets/fr/03.webp)



La aplicación genera entonces una frase de recuperación, que debes anotar cuidadosamente en un soporte físico. Incluso para los fondos de prueba sin valor real, adopta buenas prácticas de copia de seguridad.



### Interface y parámetros



Una vez creada la cartera, se accede a la interfaz principal, dividida en dos pestañas: "Transacciones" y "Configuración".



La pestaña **Transacciones** muestra tu saldo de bitcoins (y su conversión a dólares), una lista de transacciones recientes y dos botones de acción: "Pagar" para enviar fondos, y un botón de recepción (icono de descarga).



La pestaña **Configuración** ofrece cuatro opciones:




- Mostrar frase seed**: muestra tu frase de recuperación para que la guardes
- Cambiar moneda fiduciaria**: cambiar la moneda de visualización (USD por defecto)
- Set backend url**: configurar la URL del servidor Blindbit (ver siguiente sección)
- Wipe wallet**: borra completamente la wallet del dispositivo



![Interface principale Transact et menu Settings](assets/fr/04.webp)



### El servidor Blindbit



Dana Wallet utiliza un servidor de indexación llamado **Blindbit** para detectar sus pagos silenciosos. Entender cómo funciona es importante para evaluar el modelo de confianza de la aplicación.



**¿Por qué necesitamos un servidor?



Para detectar un pago silencioso, su wallet debe escanear teóricamente todas las transacciones Taproot de cada bloque y realizar un cálculo criptográfico (ECDH) para cada una de ellas. En un teléfono móvil, esta operación requeriría demasiados cálculos y ancho de banda.



El servidor de Blindbit resuelve este problema calculando previamente datos intermedios (llamados "tweaks") para todas las transacciones de Taproot. A continuación, su wallet descarga estos tweaks (33 bytes por transacción) y realiza el cálculo final **localmente** para comprobar si un pago le pertenece.



**Preservar la confidencialidad**



A diferencia de un servidor Electrum convencional, en el que revelas tus direcciones, el servidor Blindbit no sabe qué pagos te pertenecen. Proporciona los mismos datos a todos los usuarios, y es su teléfono el que realiza la verificación final. Por lo tanto, se preserva su confidencialidad frente al servidor.



**Servidor por defecto



Dana Wallet utiliza el servidor público `silentpayments.dev/blindbit/signet` (para Signet) o `silentpayments.dev/blindbit/mainnet` (para Mainnet). Puede cambiar esta URL en la configuración si aloja su propio servidor.



**Hospeda tu propio servidor Blindbit**



Para los usuarios que deseen una soberanía total, es posible alojar su propio servidor Blindbit Oracle. Esto requiere :




- Un nodo central Bitcoin completo **sin gancho** (no pruned)
- Instalación de Blindbit Oracle (disponible en GitHub: `setavenger/blindbit-oracle`)
- Aprox. 10 GB de espacio adicional en disco
- Conocimientos técnicos (compilación de Go, configuración del servidor)



Aún no existe ninguna aplicación empaquetada para Umbrel o Start9. De momento, la instalación sigue siendo manual. Se trata de un campo en evolución activa, y es posible que en el futuro surjan soluciones más accesibles.



## Uso diario



### Recepción de fondos



Para recibir bitcoins, pulse el botón de recepción (icono de descarga) de la pantalla principal. Dana Wallet muestra entonces su dirección completa de Silent Payment en el formato `tsp1q...` en Bookmark. La interfaz ofrece varias opciones:




- Mostrar código QR**: muestra el código QR de tu dirección para facilitar el escaneo
- Compartir**: comparte la dirección a través de las aplicaciones de tu teléfono
- Copiar**: copia la dirección en el portapapeles



Como se muestra en la pantalla, puedes compartir esta dirección públicamente en tus redes sociales sin comprometer tu privacidad.



![Affichage de l'adresse de réception Silent Payment](assets/fr/05.webp)



Para obtener sus primeros fondos de prueba en Signet, utilice el grifo dedicado de Silent Payments accesible en `silentpayments.dev/faucet/signet`. Copie su dirección `tsp1...`, péguela en el campo del grifo y valide la solicitud. Espera a que se extraiga un bloque (unos 10 minutos en Signet).



### Enviar un pago



Para enviar fondos, pulse el botón "Pagar" de la pantalla principal. Aparecerá la pantalla "Elegir destinatario(s)" con tres opciones para especificar el destinatario:




- Introducir manualmente la información de pago
- Pegar desde el portapapeles**: pegar una dirección desde el portapapeles
- Escanear código QR**: escanear un código QR que contenga la dirección



Una vez validada la dirección del destinatario, la pantalla "Introducir importe" le permite introducir el importe a enviar en satoshis. Su saldo disponible se muestra como referencia. Pulse "Pasar a la selección de tarifas" para continuar.



![Envoi d'un paiement : sélection du destinataire et du montant](assets/fr/06.webp)



La siguiente pantalla muestra tres niveles de tarifas, en función de la urgencia requerida:




- Rápido** (10-30 minutos): tarifas más elevadas para la confirmación rápida
- Normal** (30-60 minutos): costes moderados
- Lento** (más de 1 hora): tarifa mínima para transacciones no urgentes



Tras seleccionar el nivel de comisión, la pantalla de confirmación "¿Listo para enviar?" resume todos los detalles: dirección de destino, importe, tiempo estimado y comisión de transacción. Compruebe detenidamente esta información y, a continuación, pulse "Enviar" para enviar la transacción.



Una vez enviada, la transacción aparece en su historial con el estado "Sin confirmar" hasta que se incluya en un bloqueo. Su saldo se actualiza en consecuencia.



![Sélection des frais, confirmation et transaction envoyée](assets/fr/07.webp)



## Ventajas y limitaciones



### Destacados





- Pedagógico**: interfaz simplificada centrada en el aprendizaje Pagos silenciosos
- Bidireccional**: admite tanto el envío como la recepción, a diferencia de otras carteras
- Código abierto**: código totalmente auditable en GitHub
- Faucet** dedicado: facilita la obtención de financiación para pruebas
- Sin cuenta**: no es necesario registrarse ni introducir datos personales



### Limitaciones a tener en cuenta





- Experimental**: software no auditado, utilizar con precaución en Mainnet
- Plataforma limitada**: principalmente Android, sin versión iOS
- Funcionalidad reducida**: sin control de monedas, sin subcuentas, sin Lightning
- Exploración intensiva**: la detección de pagos consume muchos recursos



## Buenas prácticas



### Seguridad seed



Incluso para las pruebas de Signet con fondos sin valor, trata tu frase de recuperación con seriedad. Utilice la opción "Mostrar frase de seed" en la configuración para escribirla cuidadosamente. Como cuestión de buena práctica, mantén carteras completamente separadas para Signet y Mainnet: nunca utilices una seed creada para pruebas en una wallet destinada a recibir fondos reales.



### Advertencia sobre el estado experimental



Dana Wallet sigue siendo considerada experimental por sus desarrolladores. Como dicen claramente: "No utilices fondos que no estés dispuesto a perder". Para aprender, opta por la versión Signet. Si utilizas la versión Mainnet, limítate a las cantidades de token.



### Copia de seguridad y restauración



La recuperación de fondos de Pagos Silenciosos requiere una wallet compatible con el protocolo BIP-352. Una wallet estándar no puede escanear la blockchain para recuperar sus Pagos Silenciosos UTXO. Mantenga Dana Wallet instalado o utilice la opción "Restaurar" en el primer lanzamiento para recuperar un wallet existente.



## Comparación con BIP-47 y PayJoin



| Critère | Silent Payments (BIP-352) | BIP-47 PayNyms | PayJoin (BIP-78) |
|---------|---------------------------|----------------|------------------|
| Adresse statique | Oui (`sp1...`) | Oui (code de paiement) | Non |
| Interaction requise | Aucune | Transaction de notification initiale | À chaque paiement |
| Empreinte on-chain | Aucune (transactions normales) | OP_RETURN visible | Transaction modifiée |
| Scan côté receveur | Intensif (chaque bloc) | Léger (après notification) | Aucun |
| Confidentialité expéditeur | Excellente | Limitée (lien après notification) | Bonne (brouillage) |

Los pagos silenciosos eliminan la transacción de notificación BIP-47 a costa de un escaneado más caro. PayJoin resuelve un problema diferente (correlación de entrada) y puede combinarse con los Pagos Silenciosos.



## Conclusión



Dana Wallet es una valiosa herramienta educativa para aprender sobre los pagos silenciosos en un entorno sin riesgos. Su enfoque minimalista le permite comprender los mecanismos fundamentales del protocolo BIP-352 sin distraerse con características secundarias. Experimentando con Signet, desarrollará una comprensión práctica de esta prometedora tecnología para la confidencialidad de las transacciones Bitcoin.



Los pagos silenciosos representan un importante paso adelante en la conciliación de la facilidad de uso y el respeto a la privacidad. El entusiasmo de la comunidad y las primeras integraciones en varios monederos (Cake Wallet, BitBox02, BlueWallet para el envío) apuntan a un futuro en el que publicar una dirección de donación ya no comprometerá la privacidad financiera de su propietario.



## Recursos



### Documentación oficial




- Repositorio GitHub de Dana Wallet: https://github.com/cygnet3/danawallet
- F-Cold depósito: https://fdroid.silentpayments.dev
- Sitio de la comunidad de Pagos Silenciosos: https://silentpayments.xyz
- Especificación BIP-352: https://bips.dev/352



### Herramientas de prueba Signet




- Faucet Pagos silenciosos: https://silentpayments.dev/faucet/signet
- Explorador Signet Mempool: https://mempool.space/signet



### Servidor Blindbit (autoalojado)




- Oráculo Blindbit (GitHub): https://github.com/setavenger/blindbit-oracle