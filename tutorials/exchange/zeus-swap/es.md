---
name: Intercambio Zeus
description: Servicio Exchange sin custodia entre On-Chain y Lightning Network bitcoins
---

![cover](assets/cover.webp)



El ecosistema Bitcoin presenta una dualidad: la red principal (On-Chain) ofrece la máxima seguridad, mientras que Lightning Network permite transacciones instantáneas. Esta arquitectura de dos Layer plantea un reto práctico: ¿cómo transferir fondos de forma eficiente entre estas dos capas sin intermediarios centralizados?



El problema es concreto: recibes un pago Lightning pero quieres mantenerlo almacenado en Cold, o a la inversa, tienes bitcoins On-Chain pero necesitas liquidez Lightning. Las soluciones tradicionales implican la apertura/cierre manual de canales Lightning (costoso y técnico) o plataformas centralizadas que requieren KYC.



Zeus Swap resuelve este problema con un servicio automatizado y no custodio de Exchange. Desarrollado por Zeus LSP, permite convertir bitcoins On-Chain en satoshis Lightning bidireccionalmente, sin confiar sus fondos a un intermediario. El proceso utiliza contratos atómicos (HTLC) que garantizan que la Exchange se completará o cancelará.



La innovación radica en su sencillez: unos pocos clics para una Exchange que preserva su soberanía financiera, sin necesidad de registro ni KYC.



## ¿Qué es Zeus Swap?



Zeus Swap es un servicio de liquidez de Exchange desarrollado por Zeus LSP que permite realizar swaps atómicos entre la red principal de Bitcoin y Lightning Network. Se trata de una infraestructura técnica que utiliza swaps submarinos y swaps inversos para facilitar la conversión bidireccional entre On-Chain BTC y satoshis Lightning, preservando la naturaleza no custodial de la operación.



### Arquitectura técnica



Zeus Swap utiliza la tecnología de intercambio atómico de código abierto Bitcoin/Lightning de Boltz. El protocolo utiliza Hash Time Locked Contracts (HTLC): contratos que bloquean fondos con dos condiciones de liberación (revelación de un secreto criptográfico o expiración del tiempo).



Para un swap submarino (On-Chain → Lightning), el usuario envía bitcoins a un Address que incorpora el Hash de un Invoice Lightning. Zeus LSP desbloquea estos fondos sólo pagando al Invoice correspondiente, revelando la imagen previa que desbloquea automáticamente los bitcoins. Este mecanismo garantiza la atomicidad.



Para un intercambio inverso (Lightning → On-Chain), el usuario paga un Invoice Lightning desde Zeus LSP, revelando una imagen previa que permite la liberación de una transacción Bitcoin preparada al Address de destino.



Para más información sobre el funcionamiento de la Lightning Network, consulte nuestro curso específico:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Modelo de negocio



Zeus LSP actúa como creador de mercado, manteniendo la liquidez de On-Chain y Lightning para honrar los swaps. Para los swaps, Zeus aplica una comisión variable (normalmente del 0,1% al 0,5% en función de la dirección y las condiciones) más la comisión Mining de Bitcoin, mostrada de forma transparente antes de la validación.



Como proveedor de servicios relámpago, Zeus optimiza los costes gracias a su experiencia en apertura de canales a la carta, enrutamiento eficiente y soluciones de liquidez personalizadas.



### Integración



Zeus Wallet integra el servicio de forma nativa, lo que permite realizar intercambios sin salir de Interface Bitcoin/Lightning. Esto elimina la fricción de copiar y pegar entre aplicaciones.



La web independiente Interface sigue siendo accesible a todos los monederos, lo que garantiza la máxima flexibilidad de uso.



## Características principales



### Canjes bidireccionales



Zeus Swap ofrece dos tipos de Exchange:



**Submarine swaps (On-Chain → Lightning)**: inyecta liquidez Lightning desde tus reservas de Bitcoin, útil para alimentar un nodo móvil Wallet o Lightning sin abrir canales manualmente.



**Cambios inversos (Lightning → On-Chain)**: convertir satoshis Lightning en bitcoins On-Chain para su almacenamiento a largo plazo, evitando costosos cierres de canales.



### Interfaces de usuario



**Interface web** (swaps.zeuslsp.com): experiencia simplificada sin registro, proceso guiado con visualización en tiempo real de tasas y estado.



**Integración de Zeus Wallet**: canjes directos desde la aplicación, gestión automática de facturas y direcciones, eliminando errores de manipulación.



### Seguridad y recuperación



Cada intercambio genera un Contract único con parámetros inmutables: Hash Lightning, timeout, Address de reembolso. En caso de fallo, recuperación automática a través del Address proporcionado, independientemente de Zeus LSP.



**Zeus Swaps Rescue Key**: durante un On-Chain → Lightning swap, Zeus genera automáticamente una clave de recuperación universal que sustituye a los antiguos archivos de reembolso individuales. Esta clave única funciona en cualquier dispositivo y para todos los swaps creados con ella. Es crucial descargar y guardar esta clave en una ubicación segura para poder recuperar tus fondos en caso de fallo del swap.



### Optimización de la red



Zeus Swap ajusta automáticamente los tiempos de expiración y las tarifas Mining en función de las condiciones de la red. Los usuarios de Zeus se benefician de opciones avanzadas: elección de LSP, retrasos personalizados, compatibilidad con otros servicios (Boltz).



## Instalación y uso



### Métodos de acceso



**Interface web** (swaps.zeuslsp.com): solución universal compatible con todos los monederos, no requiere instalación, ideal para uso ocasional.



**Aplicación Zeus** (iOS/Android): experiencia integrada que combina Wallet y swaps, apta para usuarios habituales.



Consulte nuestro tutorial sobre Zeus para obtener más información sobre este completo Wallet :



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

### Configuración web



**On-Chain → Lightning**: El proceso comienza configurando el swap en la web Interface Zeus Swap. El usuario puede utilizar la flecha entre los campos On-Chain y Lightning para invertir la dirección del swap.



![Interface de création de swap](assets/fr/01.webp)



*Interface Zeus Swap: selección de importe (Sats 50.000 → Sats 49.648 después de tasas) con visualización transparente de tasas de red (Sats 302) y servicio Zeus (Sats 50).*



Durante el proceso, Zeus te ofrece descargar la clave de recuperación universal :



![Téléchargement de la Zeus Swaps Rescue Key](assets/fr/02.webp)



*Diálogo de descarga de la clave de rescate de Zeus Swaps: una clave universal que sustituye a los antiguos archivos de reembolso individuales*



Si ya tienes una clave, Zeus te permite comprobarla:



![Vérification de la clé existante](assets/fr/03.webp)



*Interface para comprobar la validez de una clave de rescate Zeus Swaps existente*



Una vez configurado, Zeus genera el depósito Bitcoin Address y muestra las instrucciones :



![Adresse de dépôt et instructions](assets/fr/04.webp)



*Página de finalización del canje: Código QR y Bitcoin Address para el envío de 50.000 Satss, con recordatorio de la fecha de caducidad de 24 horas*



A continuación, el canje espera la confirmación de Bitcoin:



![Attente de confirmation](assets/fr/05.webp)



*Estado "Transacción en Mempool" - a la espera de la confirmación de Bitcoin para finalizar el canje*



Una vez confirmado, el canje se completa automáticamente:



![Swap réussi](assets/fr/06.webp)



*Confirmación de éxito: 49.648 Sats recibidos en Relámpago tras deducir los gastos de red y servicio*



### Uso de la aplicación Zeus



**Rayo → On-Chain**: La aplicación Zeus ofrece una experiencia integrada para swaps inversos (Lightning a Bitcoin).



![Navigation vers les swaps dans Zeus](assets/fr/07.webp)



*Pantalla principal de Zeus mostrando los balances de Lightning (69.851 Sats) y On-Chain (38.018 Sats), acceso a los intercambios a través del menú lateral*



![Configuration du swap reverse](assets/fr/08.webp)



*Creación de intercambio inverso Interface: 50.000 Sats Lightning → 49.220 Sats On-Chain, con cargos de red (530 Sats) y servicio (250 Sats) claramente visualizados. Los usuarios pueden introducir manualmente un Bitcoin recibir Address, o generate uno automáticamente desde el Wallet Zeus a través del botón "generate On-Chain Address"*



![Finalisation du swap mobile](assets/fr/09.webp)



*Pantallas de finalización: Pantalla de pago Lightning Invoice con "PAY THIS Invoice", confirmación del pago Lightning con éxito en 9,96 segundos y extracto de saldo con los 49.162 Sats pendientes de confirmación*



### Vigilancia y seguridad



Cada swap tiene un identificador único con seguimiento en tiempo real. Visualización completa del progreso, alertas automáticas de las fechas de caducidad. Recomendaciones automáticas de carga según las condiciones de la red.



## Ventajas y limitaciones



### Beneficios





- Sencillez**: Intercambio en unos pocos clics frente a la manipulación manual de canales
- Sin custodia**: sin CSC, sin cuenta, los fondos nunca se confían a un tercero
- Transparencia**: las comisiones se muestran explícitamente antes de la validación (del 0,1% al 0,5% + minage según las pruebas realizadas por los usuarios - compruebe las comisiones actuales en cada swap)
- Integración móvil**: experiencia nativa en Zeus Wallet



### Limitaciones





- Plazos de caducidad**: 24-48h máximo, fallo si Bitcoin no se confirma a tiempo
- Límites de importe**: mínimo 25.000 Sats, liquidez Zeus LSP variable según condiciones
- Rastrea On-Chain**: Scripts HTLC potencialmente identificables por el análisis Blockchain
- Confirmación requerida**: mínimo 10 minutos para la validación Bitcoin



## Buenas prácticas



### Calendario y costes





- Vigilar Mempool.space en momentos de baja congestión
- Prefiera los fines de semana y las horas valle para reducir los costes de Mining
- Calcular la rentabilidad: pequeñas cantidades frente a apertura directa del canal



### Seguridad





- Compruebe cuidadosamente las direcciones de Bitcoin (se recomienda copiar y pegar)
- Haz una copia de seguridad de la clave de rescate de Zeus Swaps**: descarga y guarda la clave de recuperación en un lugar seguro
- Documento: Contract ID, reembolso Address, fecha de caducidad
- Utilice las tasas Mining adecuadas para la confirmación oportuna



### Estrategia de uso





- Equilibra la liquidez de On-Chain/Lightning para adaptarla a tus necesidades
- Zeus Swap para ajustes puntuales, canales directos para necesidades permanentes



## Comparación con otros servicios de swap



### Zeus Swap vs Boltz Exchange



Zeus Swap utiliza la tecnología backend de Boltz, pero introduce algunas mejoras cruciales:



**Beneficios del canje de Zeus** :




- Interface unificado**: integración nativa en Zeus Wallet vs Interface técnica web Boltz
- API WebSocket**: actualizaciones en tiempo real frente al sondeo manual
- Gestión automatizada**: facturación automática y gestión de Address
- Soporte móvil**: optimización sólo para smartphones y ordenadores de sobremesa
- Documentación Swagger**: API REST completa para desarrolladores



**Boltz sigue siendo ventajoso** para una total independencia y uso con cualquier configuración Bitcoin/Lightning.



Zeus Swap transforma la tecnología probada de Boltz en una experiencia de usuario generalizada, comparable a la diferencia entre un protocolo en bruto y una aplicación fácil de usar.



### Zeus Swap vs Phoenix/Breez (intercambios integrados)



Phoenix y Breez integran funciones de intercambio transparente que ocultan la complejidad técnica al usuario final. Phoenix utiliza un sistema de intercambio automático en el que el usuario no distingue explícitamente entre capas Bitcoin: "envía a una Bitcoin Address" y la aplicación gestiona el intercambio en segundo plano.



Este enfoque ultrasimplificado se adapta perfectamente a los principiantes, pero limita la comprensión y el control de las operaciones. Zeus Swap adopta una filosofía más educativa: los usuarios entienden que están intercambiando entre dos capas distintas, desarrollando gradualmente su comprensión del ecosistema de dos Layer Bitcoin.



## Comparación detallada de tasas y límites (2024)



⚠️ **Atención**: Las comisiones pueden variar con el tiempo en función de las condiciones del mercado y de las actualizaciones del servicio. Compruebe siempre las comisiones que aparecen en Interface antes de validar un swap.



| Service | Submarine Swap (BTC→LN) | Reverse Swap (LN→BTC) | Montant minimum |
|---------|-------------------------|----------------------|-----------------|
| **Zeus Swap** | ~0.1% + frais minage | 0.5% + frais minage | 25 000 sats |
| **Boltz** | 0.2% + frais minage | 0.5% + frais minage | 50 000 sats |
| **Phoenix** | Frais minage uniquement | 0.4% fixe | 10 000 sats |
| **Breez** | 0.25% + frais réseau | 0.5% + frais minage | 50 000 sats |

Zeus Swap ofrece un equilibrio entre facilidad de uso y control técnico: más accesible que Boltz, más flexible que Phoenix/Breez, con un estricto enfoque no custodial.



## Conclusión



Zeus Swap representa una innovación significativa en el ecosistema de Bitcoin, resolviendo con elegancia el reto de la interoperabilidad entre la red principal y Lightning Network. Al combinar la solidez criptográfica de los swaps atómicos con una experiencia de usuario accesible, este servicio democratiza la gestión dual Bitcoin-Layer sin comprometer los principios de soberanía financiera.



La arquitectura no custodial de Zeus Swap, heredada de la probada tecnología Boltz, garantiza que sus fondos permanezcan bajo su control exclusivo durante todo el proceso de intercambio. Este enfoque respeta el espíritu de la Bitcoin al tiempo que ofrece al usuario la comodidad necesaria para su adopción generalizada. La transparencia de precios y la ausencia de procesos KYC refuerzan esta propuesta de valor única.



Para el usuario moderno de Bitcoin, Zeus Swap es una herramienta estratégica para optimizar la distribución de liquidez según las necesidades: Almacenamiento seguro de On-Chain para ahorros a largo plazo, disponibilidad de Lightning para gastos diarios y microtransacciones. Esta flexibilidad transforma la gestión de Bitcoin de una limitación técnica en una ventaja competitiva.



La evolución futura de Zeus Swap, respaldada por el experimentado equipo de Zeus LSP y la comunidad de código abierto Boltz, promete mejoras continuas en términos de costes, tiempos de procesamiento y experiencia del usuario. Este servicio forma parte de una tendencia más amplia hacia la maduración de la infraestructura Bitcoin, en la que la sofisticación técnica se vuelve transparente para el usuario final.



## Recursos



### Documentación oficial




- [Zeus Swap - Portal web](https://swaps.zeuslsp.com)
- [Zeus Wallet - Aplicación móvil](https://zeusln.app)
- [Blog Zeus - Anuncios y tutoriales](https://blog.zeusln.com)
- [Documentación técnica de Zeus](https://docs.zeusln.app)



### Comunidad y apoyo




- [Twitter Zeus (@zeusln)](https://twitter.com/zeusln)
- [Telegrama Zeus](https://t.me/ZeusLN)
- [GitHub Zeus](https://github.com/ZeusLN)