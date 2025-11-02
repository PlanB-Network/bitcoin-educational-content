---
name: SwapMarket
description: Agregador de servicios de intercambio Bitcoin y Lightning
---

![cover](assets/cover.webp)



La transferencia de fondos entre Bitcoin On-Chain y Lightning Network suele requerir o bien la apertura manual de canales Lightning (técnica y costosa), o bien el uso de plataformas de swap centralizadas con KYC. SwapMarket ofrece una alternativa: Trustless swaps atómicos a través de proveedores competitivos, sin KYC.



Innovación: aunque los proveedores son intermediarios, HTLC (*Hash Time Locked Contracts*) garantiza matemáticamente que sus fondos permanecen bajo su control. La agregación de varios proveedores (Boltz, ZEUS Swaps, Eldamar, Middle Way) crea competencia de precios. Interface web de código abierto autoalojable.



## ¿Qué es SwapMarket?



SwapMarket, un agregador de código abierto lanzado en 2024, funciona como comparador de proveedores de swaps Bitcoin/Lightning. El usuario compara al instante las condiciones (comisiones, liquidez, límites) y selecciona el proveedor óptimo.



### Arquitectura técnica



**Frontend del lado del cliente**: aplicación 100% cliente (Fork Boltz Web App) alojada en GitHub Pages. El código se ejecuta en el navegador sin servidor backend. Historial almacenado localmente (cookies/cache). Código fuente público y auditable.



**Descubrimiento de proveedores** : Lista codificada Hard en `src/configs/Mainnet.ts`. Nuevos proveedores añadidos vía Pull Request o email.



**Backends independientes**: Cada proveedor opera su propio backend Boltz. Interface consulta las API en tiempo real para comparar presupuestos al instante.



**HTLC Swaps atómicos**: Los contratos con bloqueo temporal Hash garantizan la atomicidad: o se ejecuta el swap, o cada parte recupera sus fondos. Se elimina matemáticamente el riesgo de contraparte.



### Filosofía



SwapMarket reduce la centralización creando competencia entre proveedores por las comisiones y la liquidez. Sin CSC, código abierto autoalojable, multiplicación de operadores independientes para evitar puntos únicos de fallo.



## Características principales



### Mercado de proveedores



Interface muestra todos los proveedores activos: nombre del proveedor, comisiones aplicadas (porcentuales y/o fijas), importes mínimos/máximos disponibles y tipos de swap admitidos. La aplicación consulta directamente las API de cada proveedor referenciado en el fichero de configuración para obtener cotizaciones en tiempo real. La competencia entre proveedores garantiza unas tarifas óptimas, generalmente en torno al 0,5% para los swaps estándar.



### Canjes bidireccionales



**Swap-in (On-Chain → Lightning)**: Convierte BTC de On-Chain en satoshis de Lightning. Caso de uso: alimentar un Wallet Lightning móvil, obtener capacidad entrante en un nodo o disponer de liquidez instantánea.



**Swap-out (Lightning → On-Chain)**: Convierte satoshis de Lightning en BTC de On-Chain. Caso de uso: volcar Wallet Lightning en Cold storage o reequilibrar la liquidez entre capas.



### Seguridad y recuperación



**Trustless Canjes atómicos: El HTLC garantiza que, o bien el Exchange se completa en su totalidad, o bien cada parte recupera su apuesta. El riesgo de contraparte queda matemáticamente eliminado.



**Mecanismo de canje**: Cada swap tiene una fecha de vencimiento (TIMELOCK). Si el swap falla, los fondos se reembolsan automáticamente tras la expiración. El usuario siempre conserva la opción de reclamar sus bitcoins.



**Claves de recuperación**: SwapMarket te permite exportar claves de recuperación para swaps en curso. En caso de problema, estas claves pueden utilizarse para finalizar o cancelar un intercambio desde cualquier dispositivo.



## Instalación y acceso



### Interface web



SwapMarket no requiere instalación. Se accede a través del navegador visitando https://swapmarket.github.io. Para obtener la máxima confidencialidad, utilice Brave, Firefox con extensiones anti-seguimiento o LibreWolf. Se recomienda Tor Browser para el anonimato en la red.



No es necesario registrarse, enviar un correo electrónico ni verificar la identidad.



### Autoalojamiento (opcional)



Para los usuarios técnicos que deseen eliminar cualquier dependencia del dominio oficial GitHub Pages, SwapMarket puede ejecutarse localmente :



**Via npm** :


```
git clone https://github.com/SwapMarket/swapmarket.github.io.git
cd swapmarket.github.io
npm install
npm run dev
```



**Vía Docker** :


```
docker run -p 3000:80 ghcr.io/swapmarket/swapmarket:latest
```



La aplicación será accesible en `http://localhost:3000`. El autoalojamiento garantiza un control total sobre Interface, elimina el riesgo de censura del dominio oficial y permite auditar el código fuente antes de su ejecución.



### Configuración inicial



**Wallet Lightning**: Asegúrese de que dispone de un Wallet Lightning operativo (Phoenix, Zeus, BlueWallet, etc.). Para los intercambios, pagará una Invoice Lightning. Para los intercambios, pagará un Invoice Lightning.



**Wallet On-Chain**: Para swap-ins, necesitarás una Wallet Bitcoin On-Chain para enviar fondos. Para los swap-outs, prepare una Bitcoin que reciba Address.



**Configuración opcional**: SwapMarket almacena el historial de intercambios y las preferencias en las cookies del navegador. No es necesario crear una cuenta.



## Acceso a la configuración y Rescue Key



Antes de realizar sus primeros canjes, le recomendamos encarecidamente que descargue su **Llave de rescate**. Esta clave de emergencia te permite recuperar tus fondos en caso de problema técnico o pérdida de acceso a tu dispositivo.



### Parámetros de acceso



En la página principal de SwapMarket, haga clic en el icono de engranaje (⚙️) situado en la parte superior derecha de Interface, junto al formulario de intercambio.



![Accès aux paramètres](assets/fr/01.webp)



### Configuración de página



Se abre la página Configuración, que muestra varias opciones de configuración:





- Denominación**: A elegir entre BTC o Sats
- Separador decimal**: Separador decimal (, o .)
- Notificaciones de audio/navegador**: Notificaciones de audio y del navegador
- Clave de recuperación** : Descargar la clave de recuperación
- Registros**: Ver, descargar o eliminar registros



![Page Settings](assets/fr/02.webp)



### Descargar Rescue Key



Haga clic en el botón **Descargar** situado junto a "Rescue Key".



**Puntos importantes** :




- La Rescue Key es una **llave única de emergencia** que sirve para todos sus futuros intercambios
- Guarda esta clave en un lugar **seguro y permanente** (gestor de contraseñas, caja fuerte digital)
- En caso de problema de intercambio (tiempo de espera, fallo técnico), esta clave le permite recuperar sus fondos



## Crear un swap paso a paso



### Intercambio: Rayo → Bitcoin



Este primer ejemplo muestra cómo convertir satoshis de Lightning en bitcoins On-Chain.



**Paso 1: Intercambiar la configuración



En la página principal, seleccione el formulario de intercambio :




- LIGHTNING** (campo superior): Introduzca la cantidad que desea enviar en Sats Lightning (ejemplo: 30.000 Sats)
- Bitcoin** (campo inferior): El importe que recibirá se muestra automáticamente una vez deducidas las tasas (ejemplo: Sats 29.320)



En el campo inferior, pegue su **Bitcoin Address** donde desea recibir los fondos. Compruebe cuidadosamente esta Address.



El proveedor por defecto suele ser Boltz Exchange. Las tarifas de la red y del proveedor se muestran claramente.



![Configuration swap-out](assets/fr/03.webp)



**Paso 2: Selección del proveedor**



Haga clic en el menú desplegable de proveedores (por defecto: "Boltz Exchange") para ver todos los proveedores de liquidez disponibles.



Se abre una ventana modal que muestra una tabla comparativa:




- Estado**: Indicador Green si el proveedor está activo
- Alias**: Nombre del proveedor (Boltz Exchange, Middle Way, Eldamar, ZEUS Swaps)
- Comisión**: Cargos aplicados por el proveedor (generalmente entre el 0,49% y el 0,5%)
- Canje máximo**: Importe máximo aceptado para un swap



Compare las tarifas y los importes máximos y seleccione el proveedor que prefiera.



**Nota**: El Interface de selección de proveedores no muestra los **importes mínimos** de cada proveedor. Esta información sólo aparece en el Interface de creación de intercambios, después de haber seleccionado un proveedor. Los importes mínimos y máximos pueden variar de un proveedor a otro, y pueden cambiar con el tiempo. **Compruebe siempre estos límites en el momento de realizar su swap**: si el importe que desea intercambiar está fuera de los límites de un proveedor, puede seleccionar otro más adecuado para su operación.



![Sélection du provider](assets/fr/04.webp)



**Paso 3: Creación del swap y pago de Lightning**



Haz clic en el botón amarillo **"CREAR SWAP ATÓMICO "**. SwapMarket generate un **Lightning Invoice** (BOLT11) para que usted pueda pagar desde su Wallet Lightning.



La página muestra :




- Identificador de intercambio**: Identificador único de swap (ejemplo: J4ymFIMVR6Hm)
- Estado**: "swap.creado" (swap creado, pendiente de pago)
- Código QR**: Escanéalo con tu Wallet Lightning
- Invoice Lightning**: Cadena de caracteres que comienza por "lnbc" (ejemplo: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)



Pague esta Invoice desde su Wallet Lightning (Phoenix, Zeus, BlueWallet, etc.). Se muestra la cantidad exacta a pagar (ejemplo: 30.000 Sats).



![Paiement Lightning](assets/fr/05.webp)



**Paso 4: Confirmación y aceptación**



Una vez confirmado el pago Lightning, SwapMarket recibe instantáneamente su pago y el proveedor transmite la transacción Bitcoin a su Address.



El estado cambia a **"Invoice.settled "** (Invoice pagado), y aparece un mensaje de confirmación.



Sus On-Chain bitcoins estarán disponibles en cuanto se confirme la transacción (normalmente en unos minutos o unas horas, dependiendo de las Mining tarifas elegidas por el proveedor).



![Confirmation swap-out](assets/fr/06.webp)



Puede hacer clic en **"TRANSACCIÓN DE RECLAMACIÓN ABIERTA "** para ver la transacción Bitcoin en un explorador Blockchain.



### Intercambio: Bitcoin → Rayo



Este segundo ejemplo muestra cómo convertir bitcoins On-Chain en satoshis Lightning.



**Paso 1: Intercambiar la configuración



En la página principal, seleccione el formulario de intercambio :




- Bitcoin** (campo superior): Introduzca el importe que desea enviar en Sats Bitcoin (ejemplo: 63.400 Sats)
- ILUMINACIÓN** (campo inferior): El importe que recibirá se muestra automáticamente una vez deducidas las tasas (ejemplo: 62 884 Sats)



En el campo inferior, pegue un Lightning** Invoice (BOLT11) generado desde su Wallet Lightning, o utilice su LNURL Address si su Wallet lo admite.



![Configuration swap-in](assets/fr/07.webp)



**Paso 2: Comprobación de la clave de rescate**



Tras hacer clic en **"CREAR SWAP ATÓMICO "**, aparece una ventana modal que le pide que verifique su Rescue Key.



![Modal Rescue Key](assets/fr/08.webp)



**Llave de rescate de Boltz**: Como ya ha cargado su clave de recuperación durante la configuración inicial (véase la sección anterior), haga clic en el botón **"VERIFICAR CLAVE EXISTENTE "** para importar la clave que ha guardado.



Seleccione el archivo Rescue Key previamente descargado. Tras una verificación correcta, Interface pasa automáticamente al siguiente paso.



**Paso 3: Bitcoin** depósito Address



SwapMarket genera ahora un **Bitcoin Address** único que contiene el HTLC Contract vinculado a tu Invoice de Lightning.



La página muestra :




- ID de intercambio**: Identificador único (ejemplo: 1kGmB6JyGqU4)
- Estado** : "Invoice.set" (Invoice fijado, pendiente de pago Bitcoin)
- Código QR**: Bitcoin depósito Address
- Bitcoin** Address: Suele empezar por "bc1p..." (ejemplo: bc1p5mvtwxapjkds...9d4n9f)
- Advertencia en amarillo** : "¡Asegúrese de que su transacción se confirma en un plazo de ~24 horas tras la creación de este swap!"



Este periodo de ~24 horas es el **tiempo de espera** del HTLC Contract. Si su transacción Bitcoin no se confirma dentro de este plazo, el intercambio fallará y tendrá que utilizar su Clave de Rescate para recuperar sus fondos.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Puede copiar el Address haciendo clic en el botón **"Address"**, o escanear el código QR directamente desde su Wallet On-Chain.



**Paso 4: Envío de bitcoins**



Desde su Wallet Bitcoin On-Chain, envíe **exactamente** la cantidad indicada (por ejemplo, 63.400 Sats) a la Address generada.



**Importante**: Utilice tarifas Mining adecuadas para garantizar una confirmación rápida. Si la tarifa es demasiado baja y la transacción permanece en Mempool más allá del tiempo de espera (~24h), el intercambio fallará.



Una vez enviada la transacción, SwapMarket detecta que está en Mempool y muestra :




- Estado** : "transacción.Mempool"
- Mensaje**: "La transacción está en Mempool - Esperando confirmación para completar el intercambio"



![Transaction en mempool](assets/fr/10.webp)



**Paso 5: Confirmación y recepción del Rayo**



En cuanto la transacción Bitcoin recibe su primera confirmación, el proveedor paga automáticamente su Invoice Lightning. Usted recibe al instante los satoshis en su Wallet Lightning.



El estado cambia a **"transacción.reclamación.pendiente "** y, a continuación, se muestra un mensaje de confirmación:



![Confirmation swap-in](assets/fr/11.webp)



Sus satoshis Rayo están disponibles inmediatamente en su Wallet.



## Ventajas y limitaciones



### Beneficios



**Competencia de tarifas**: La agregación de proveedores crea una competencia natural que hace bajar las tarifas (del 0,49% al 0,5%).



**Confidencialidad**: Sin KYC, Interface 100% del lado del cliente (sin transmisión de datos personales), compatible con Tor Browser.



**Sin custodia**: HTLC garantizan matemáticamente el control exclusivo de sus fondos. O el canje tiene éxito, o recuperas tus bitcoins.



**Open-source self-hostable**: código público auditable, desplegable localmente para una máxima resistencia a la censura.



### Limitaciones



**Liquidez limitada**: Número limitado de proveedores activos (Boltz, Eldamar, MiddleWay en función del periodo). Los importes máximos pueden estar limitados.



**Tiempo de expiración**: Tiempo de expiración de 24h a 48h. Si la transacción On-Chain no se confirma antes del vencimiento, se requiere recuperación manual.



**Centralización de Interface**: Aunque autoalojable, el Interface oficial está alojado en GitHub Pages. Si GitHub censura el repositorio, se bloqueará el acceso a través de swapmarket.github.io (solución: autoalojamiento).



**Rastros On-Chain**: Los scripts HTLC son potencialmente identificables mediante análisis avanzados Blockchain.



## Buenas prácticas



### Configuración segura



**Descarga tu Rescue Key**: Antes de realizar su primer intercambio, descargue su Rescue Key desde Ajustes (consulte la sección dedicada más arriba). Esta clave única le servirá para todos sus futuros intercambios y le permitirá recuperar sus fondos en caso de problema.



**Utiliza el Navegador Tor**: Para una máxima confidencialidad, accede a SwapMarket a través de Tor Browser para ocultar tu IP Address.



**Considera el autoalojamiento**: Para los usuarios técnicos, ejecutar su propia instancia de SwapMarket elimina la dependencia del dominio oficial de GitHub Pages.



### Optimización del intercambio



**Vigila Mempool**: Comprueba Mempool.space antes de un intercambio. Elige horas de poca actividad para minimizar los costes de Mining.



**Compruebe las direcciones**: Para los intercambios, compruebe meticulosamente su Address de recepción. Utilice copiar y pegar y compruebe los 5 primeros y los 5 últimos caracteres.



**Probar con pequeñas cantidades**: Empieza con el mínimo permitido (de 25.000 a 50.000 Sats). Aumenta gradualmente una vez que domines el proceso.



**Documente sus swaps**: Anote la identificación de cada swap, la Address de reembolso y la fecha de caducidad. Esta información facilita el seguimiento y la recuperación en caso de problema técnico.



### Estrategia de uso



**Equilibre su tesorería**: Utiliza SwapMarket para ajustar tu asignación entre On-Chain (ahorro, seguridad a largo plazo) y Lightning (gastos diarios, pagos instantáneos) en función de tus necesidades reales.



**Calcular la rentabilidad**: Para necesidades permanentes de liquidez Lightning, compare el coste acumulado de swaps repetidos frente a la apertura directa de un canal Lightning. SwapMarket destaca para ajustes puntuales, no necesariamente para grandes flujos regulares.



## SwapMarket vs Boltz: ¿Cuál es la diferencia?



### Boltz: Tecnología vs. Servicio



**Boltz es la tecnología de código abierto** (`boltz-backend` en GitHub) que implementa intercambios atómicos a través de HTLC entre Bitcoin, Lightning y Liquid.



**Punto crítico**: Todos los proveedores de SwapMarket (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) despliegan su propia instancia del backend de Boltz. La tecnología subyacente es, por tanto, idéntica. Una vulnerabilidad en el backend Boltz afectaría potencialmente a todos los proveedores, pero la naturaleza de código abierto del sistema permite la auditoría comunitaria.



**Boltz Exchange** es un servicio único operado por el equipo de Boltz, mientras que **SwapMarket** reúne a varios proveedores que utilizan todos la tecnología de Boltz, creando un entorno de precios competitivo.



Consulta nuestros tutoriales de Boltz y Zeus Swap para más detalles:



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.network/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Principales diferencias



| Aspect        | Boltz Exchange           | SwapMarket                                 |
| ------------- | ------------------------ | ------------------------------------------ |
| Nature        | Service unique           | Agrégateur multi-providers                 |
| Providers     | Boltz uniquement         | Boltz, ZEUS, Eldamar, Middle Way           |
| Compétition   | Tarifs fixes             | Compétition libre                          |
| Interface     | boltz.exchange           | swapmarket.github.io (self-hostable)       |
| Sécurité      | Non-custodial (HTLC)     | Non-custodial (HTLC)                       |

**Ventajas de SwapMarket**: Competencia de precios, diversificación de instancias backend, comparación en tiempo real.



**Alternativas tecnológicas** (no compatibles con SwapMarket): Lightning Loop (Lightning Labs), Muun Wallet, NLoop, Breez Wallet. Estas soluciones utilizan sus propias implementaciones de swaps submarinos.



**Recomendación**: Utilizar Boltz Exchange para simplificar o SwapMarket para optimizar los costes mediante la competencia. Ambos son equivalentes en seguridad (HTLC no custodial).



## Conclusión



SwapMarket facilita los intercambios Bitcoin/Lightning agregando múltiples proveedores en un único Interface. La arquitectura HTLC garantiza la naturaleza no custodial de los intercambios, la ausencia de KYC preserva la confidencialidad y el código abierto autoalojable refuerza la resistencia a la censura.



La competencia entre proveedores mejora las tarifas y multiplica las fuentes de liquidez. Para optimizar la gestión de dos Layer (ahorro de On-Chain, gastos de Rayo), SwapMarket es una herramienta práctica que preserva la soberanía financiera y la confidencialidad.



## Recursos



### Documentación oficial




- [SwapMarket - Aplicación web](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [Documentación técnica](https://docs.boltz.Exchange/)
- [Guía de autoalojamiento](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### Proyectos relacionados




- [Boltz Exchange](https://boltz.Exchange) - Servicio de intercambio atómico original
- [ZEUS Swaps](https://zeusln.com) - Proveedor de swaps relámpago