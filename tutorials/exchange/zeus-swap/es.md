---
name: Intercambio Zeus
description: Servicio de intercambio de Bitcoin sin custodia entre On-Chain y Lightning Network
---

![cover](assets/cover.webp)

El ecosistema Bitcoin presenta una dualidad: La red principal (On-Chain) ofrece la máxima seguridad, mientras que Lightning Network permite transacciones instantáneas. Esta arquitectura de dos capas plantea un reto práctico: ¿Cómo transferir fondos de forma eficiente entre estas dos capas sin intermediarios centralizados?

El problema es concreto: Recibes un pago Lightning pero quieres mantenerlo almacenado en Cold, o a la inversa, tienes Bitcoin On-Chain pero necesitas liquidez Lightning. Las soluciones tradicionales implican la apertura/cierre manual de canales Lightning (costoso y técnico) o plataformas centralizadas que requieren KYC.

Zeus Swap resuelve este problema con un servicio de intercambio automatizado y sin custodia. Desarrollado por Zeus LSP, permite convertir Bitcoin On-Chain en satoshis Lightning bidireccionalmente, sin confiar sus fondos a un intermediario. El proceso utiliza contratos atómicos (HTLC) que garantizan que el intercambio se completará o cancelará.

La innovación radica en su sencillez: Uunos pocos clics para realizar intercambios que preservan tu soberanía financiera, sin necesidad de registro ni KYC.

## ¿Qué es Zeus Swap?

Zeus Swap es un servicio de intercambio de liquidez desarrollado por Zeus LSP que permite realizar swaps atómicos entre la red principal de Bitcoin y Lightning Network. Se trata de una infraestructura técnica que utiliza swaps submarinos y swaps inversos para facilitar la conversión bidireccional entre On-Chain BTC y satoshis Lightning, preservando la naturaleza no custodial de la operación.

### Arquitectura técnica

Zeus Swap utiliza la tecnología de intercambio atómico de código abierto Bitcoin/Lightning de Boltz. El protocolo utiliza Hash Time Locked Contracts (HTLC): Contratos que bloquean fondos con dos condiciones de liberación (revelación de un secreto criptográfico o expiración del tiempo).

Para un swap submarino (On-Chain → Lightning), el usuario envía Bitcoin a una dirección que incorpora el Hash de una factura Lightning. Zeus LSP desbloquea estos fondos sólo pagando al Invoice correspondiente, revelando la imagen previa que desbloquea automáticamente el Bitcoin. Este mecanismo garantiza la atomicidad.

Para un intercambio inverso (Lightning → On-Chain), el usuario paga un recibo Lightning desde Zeus LSP, revelando un preimage que permite la liberación de una transacción Bitcoin preparada a la dirección de destino.

Para más información sobre el funcionamiento de la Lightning Network, consulta nuestro curso específico:

https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Modelo de negocio

Zeus LSP actúa como creador de mercado, manteniendo la liquidez de On-Chain y Lightning para honrar los swaps. Para los swaps, Zeus aplica una comisión variable (normalmente del 0,1% al 0,5% en función de la dirección y las condiciones) más la comisión Mining de Bitcoin, mostrada de forma transparente antes de la validación.

Como proveedor de servicios Lightning, Zeus optimiza los costos gracias a su experiencia en apertura de canales a la carta, enrutamiento eficiente y soluciones de liquidez personalizadas.

### Integración

Zeus Wallet integra el servicio de forma nativa, lo que permite realizar intercambios sin salir de Interface Bitcoin/Lightning. Esto elimina la fricción de copiar y pegar entre aplicaciones.

La interfaz web independiente sigue siendo accesible a todos los monederos, lo que garantiza la máxima flexibilidad de uso.

## Características principales

### Canjes bidireccionales

Zeus Swap ofrece dos tipos de intercambio:

**Submarine swaps (On-Chain → Lightning)**: inyecta liquidez Lightning desde tus reservas de Bitcoin, útil para alimentar un nodo móvil Wallet o Lightning sin abrir canales manualmente.

**Cambios inversos (Lightning → On-Chain)**: convertir satoshis Lightning en Bitcoin On-Chain para su almacenamiento a largo plazo, evitando costosos cierres de canales.

### Interfaces de usuario

**Interface web** (swaps.zeuslsp.com): Experiencia simplificada sin registro, proceso guiado con visualización en tiempo real de tasas y estado.

**Integración de Zeus Wallet**: Canjes directos desde la aplicación, gestión automática de facturas y direcciones, eliminando errores de manipulación.

### Seguridad y recuperación

Cada intercambio genera un contrato inteligente único con parámetros inmutables: Hash Lightning, timeout, dirección de reembolso. En caso de fallo, hay una recuperación automática a través de la dirección proporcionada, independientemente de Zeus LSP.

**Zeus Swaps Rescue Key**: Durante un swap On-Chain → Lightning, Zeus genera automáticamente una clave de recuperación universal que sustituye a los antiguos archivos de reembolso individuales. Esta clave única funciona en cualquier dispositivo y para todos los swaps creados con ella. Es crucial descargar y guardar esta clave en una ubicación segura para poder recuperar tus fondos en caso de fallo del swap.

### Optimización de la red

Zeus Swap ajusta automáticamente los tiempos de expiración y las tarifas en función de las condiciones de la red. Los usuarios de Zeus se benefician de opciones avanzadas: Elección de LSP, retrasos personalizados, compatibilidad con otros servicios (Boltz).

## Instalación y uso

### Métodos de acceso

**Interfaz web** (swaps.zeuslsp.com): Solución universal compatible con todos los monederos, no requiere instalación, ideal para uso ocasional.

**Aplicación Zeus** (iOS/Android): experiencia integrada que combina Wallet y swaps, apta para usuarios habituales.

Consulta nuestro tutorial sobre Zeus para obtener más información sobre esta completa billetera:

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

### Configuración web

**On-Chain → Lightning**: El proceso comienza configurando el swap en la web interfaz Zeus Swap. El usuario puede utilizar la flecha entre los campos On-Chain y Lightning para invertir la dirección del swap.

![Interface de création de swap](assets/fr/01.webp)

*Interface Zeus Swap: selección de importe (Sats 50.000 → Sats 49.648 después de tasas) con visualización transparente de tasas de red (Sats 302) y servicio Zeus (Sats 50).*

Durante el proceso, Zeus te ofrece descargar la clave de recuperación universal:

![Téléchargement de la Zeus Swaps Rescue Key](assets/fr/02.webp)

*Diálogo de descarga de la clave de rescate de Zeus Swaps: Una clave universal que sustituye a los antiguos archivos de reembolso individuales*

Si ya tienes una clave, Zeus te permite comprobarla:

![Vérification de la clé existante](assets/fr/03.webp)

*Interfaz para comprobar la validez de una clave de rescate Zeus Swaps existente*

Una vez configurado, Zeus genera la dirección de depósito Bitcoin y muestra las instrucciones:

![Adresse de dépôt et instructions](assets/fr/04.webp)

*Página de finalización del canje: Código QR y dirección Bitcoin para el envío de 50.000 Satss, con recordatorio de la fecha de caducidad de 24 horas*

A continuación, el canje espera la confirmación de Bitcoin:

![Attente de confirmation](assets/fr/05.webp)

*Estado "Transacción en Mempool" - a la espera de la confirmación de Bitcoin para finalizar el canje*

Una vez confirmado, el canje se completa automáticamente:

![Swap réussi](assets/fr/06.webp)

*Confirmación de éxito: 49.648 Sats recibidos en Lightning tras deducir los gastos de red y servicio*

### Uso de la aplicación Zeus

**Lightning → On-Chain**: La aplicación Zeus ofrece una experiencia integrada para swaps inversos (Lightning a Bitcoin).

![Navigation vers les swaps dans Zeus](assets/fr/07.webp)

*Pantalla principal de Zeus mostrando los balances de Lightning (69.851 Sats) y On-Chain (38.018 Sats), acceso a los intercambios a través del menú lateral*

![Configuration du swap reverse](assets/fr/08.webp)

*Interfaz de creación de intercambio inverso: 50.000 Sats Lightning → 49.220 Sats On-Chain, con cargos de red (530 Sats) y servicio (250 Sats) claramente visualizados. Los usuarios pueden introducir manualmente una dirección de recepción Bitcoin, o crear una automáticamente desde la billetera Zeus a través del botón "generate On-Chain Address"*

![Finalisation du swap mobile](assets/fr/09.webp)

*Pantallas de finalización: Pantalla de pago Lightning con "PAY THIS Invoice", confirmación del pago Lightning con éxito en 9,96 segundos y extracto de saldo con los 49.162 Sats pendientes de confirmación*

### Vigilancia y seguridad

Cada swap tiene un identificador único con seguimiento en tiempo real. Visualización completa del progreso, alertas automáticas de las fechas de caducidad. Recomendaciones automáticas de carga según las condiciones de la red.

## Ventajas y limitaciones

### Beneficios

- **Sencillez**: Intercambio en unos pocos clics frente a la manipulación manual de canales
- **Sin custodia**: Sin CSC, sin cuenta, los fondos nunca se confían a un tercero
- **Transparencia**: Las comisiones se muestran explícitamente antes de la validación (del 0,1% al 0,5% + minado según las pruebas realizadas por los usuarios - comprueba las comisiones actuales en cada swap)
- **Integración móvil**: Experiencia nativa en Zeus Wallet

### Limitaciones

- **Plazos de caducidad**: 24-48h máximo, fallo si Bitcoin no se confirma a tiempo
- **Límites de importe**: mínimo 25.000 Sats, liquidez Zeus LSP variable según condiciones
- **Rastrea On-Chain**: Scripts HTLC potencialmente identificables por el análisis Blockchain
- **Confirmación requerida**: Mínimo 10 minutos para la validación de Bitcoin

## Buenas prácticas

### Calendario y costes

- Vigilar Mempool.space en momentos de baja congestión
- Prefiere los fines de semana y las horas valle para reducir los costos de minado
- Calcula la rentabilidad: Pequeñas cantidades frente a apertura directa del canal

### Seguridad

- Comprueba cuidadosamente las direcciones de Bitcoin (se recomienda copiar y pegar)
- **Haz una copia de seguridad de la clave de rescate de Zeus Swaps**: Descarga y guarda la clave de recuperación en un lugar seguro
- Documentos: Contract ID, dirección de reembolso, fecha de caducidad
- Utiliza las tasas de minado adecuadas para la confirmación oportuna

### Estrategia de uso

- Equilibra la liquidez de On-Chain/Lightning para adaptarla a tus necesidades
- Zeus Swap para ajustes puntuales, canales directos para necesidades permanentes

## Comparación con otros servicios de swap

### Zeus Swap vs Boltz Exchange

Zeus Swap utiliza la tecnología backend de Boltz, pero introduce algunas mejoras cruciales:

**Beneficios del canje de Zeus**:

- **Interfaz unificado**: Integración nativa en Zeus Wallet vs Interfaz técnica web Boltz
- **API WebSocket**: Aactualizaciones en tiempo real frente al sondeo manual
- **Gestión automatizada**: Facturación automática y gestión de direcciones
- **Soporte móvil**: Optimización sólo para smartphones y ordenadores de sobremesa
- **Documentación Swagger**: API REST completa para desarrolladores

**Boltz sigue siendo ventajoso** para una total independencia y uso con cualquier configuración Bitcoin/Lightning.

Zeus Swap transforma la tecnología probada de Boltz en una experiencia de usuario generalizada, comparable a la diferencia entre un protocolo en bruto y una aplicación fácil de usar.

### Zeus Swap vs Phoenix/Breez (intercambios integrados)

Phoenix y Breez integran funciones de intercambio transparente que ocultan la complejidad técnica al usuario final. Phoenix utiliza un sistema de intercambio automático en el que el usuario no distingue explícitamente entre capas Bitcoin: "envías a una dirección Bitcoin" y la aplicación gestiona el intercambio en segundo plano.

Este enfoque ultrasimplificado se adapta perfectamente a los principiantes, pero limita la comprensión y el control de las operaciones. Zeus Swap adopta una filosofía más educativa: Los usuarios entienden que están intercambiando entre dos capas distintas, desarrollando gradualmente su comprensión del ecosistema de dos capas de Bitcoin.

## Comparación detallada de tasas y límites (2024)

⚠️ **Atención**: Las comisiones pueden variar con el tiempo en función de las condiciones del mercado y de las actualizaciones del servicio. Comprueba siempre las comisiones que aparecen en la interfaz antes de validar un swap.

| Servicio | Submarine Swap (BTC→LN) | Reverse Swap (LN→BTC) | Monto mínimo |
|---------|-------------------------|----------------------|-----------------|
| **Zeus Swap** | ~0.1% + costo de minería | 0.5% + costo de minería | 25 000 sats |
| **Boltz** | 0.2% + costo de minería | 0.5% + costo de minería | 50 000 sats |
| **Phoenix** | Solo tarifas de minería | 0.4% fijo | 10 000 sats |
| **Breez** | 0.25% + cargos de red | 0.5% + costo de minería | 50 000 sats |

Zeus Swap ofrece un equilibrio entre facilidad de uso y control técnico: Más accesible que Boltz, más flexible que Phoenix/Breez, con un estricto enfoque no custodial.

## Conclusión

Zeus Swap representa una innovación significativa en el ecosistema de Bitcoin, resolviendo con elegancia el reto de la interoperabilidad entre la red principal y Lightning Network. Al combinar la solidez criptográfica de los swaps atómicos con una experiencia de usuario accesible, este servicio democratiza la gestión dual Bitcoin-Layer sin comprometer los principios de soberanía financiera.

La arquitectura no custodial de Zeus Swap, heredada de la probada tecnología Boltz, garantiza que tus fondos permanezcan bajo tu control exclusivo durante todo el proceso de intercambio. Este enfoque respeta el espíritu de Bitcoin al tiempo que ofrece al usuario la comodidad necesaria para su adopción generalizada. La transparencia de precios y la ausencia de procesos KYC refuerzan esta propuesta de valor única.

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
