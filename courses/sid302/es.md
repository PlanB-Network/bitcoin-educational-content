---
name: Liquid Bootcamp Essentials
goal: Conozca a fondo los proyectos Liquid Network y Elements, y aprenda a implantar soluciones avanzadas en transacciones confidenciales, tokenización y arquitectura de red descentralizada.
objectives: 

  - Comprender los fundamentos de la arquitectura Liquid y su relación con Bitcoin.
  - Aprenda a configurar y utilizar los nodos Liquid con el software Elements.
  - Explorar el uso de transacciones confidenciales y emisión de activos en la Liquid Network.
  - Comprender los aspectos empresariales y técnicos del Liquid para su aplicación en los mercados de capitales.

---

# Introducción a la red Liquid


Embárquese en un viaje educativo diseñado para proporcionar una comprensión profunda del proyecto Liquid Network y Elements. Este bootcamp combina teoría y práctica para enseñarle los fundamentos técnicos, arquitectónicos y empresariales necesarios para implantar y aprovechar las capacidades de Liquid. Desde transacciones confidenciales hasta diseño de ecosistemas, este curso es ideal para quienes buscan ampliar sus conocimientos sobre herramientas avanzadas dentro del ecosistema de Bitcoin.


Con presentaciones a cargo de expertos del sector, el curso abarca temas como la arquitectura de Liquid, aplicaciones de tokenización, conceptos técnicos de Elements y casos de uso innovadores como el SDK de Breez. Diseñado para ser accesible a principiantes y usuarios intermedios, el curso también ofrece valor a los desarrolladores experimentados que buscan dominar Liquid como plataforma para optimizar sus proyectos.

+++

# Introducción


<partId>9f8a83d5-27e0-4e6d-af12-6cd6eb667291</partId>


## Resumen del curso


<chapterId>3192ee7d-255b-4c4f-ba18-e08c5ab98577</chapterId>


Bienvenido al Liquid Bootcamp, una formación integral diseñada para dotarle de los conocimientos y habilidades necesarios para aprovechar eficazmente el proyecto Liquid Network y Elements. Este curso ofrece una exploración exhaustiva de las características distintivas de Liquid, incluida Confidential Transactions, la emisión de activos y su arquitectura de red federada, al tiempo que introduce los conceptos fundamentales de Elements, el software que impulsa Liquid.


A lo largo del campamento de entrenamiento, explorará las aplicaciones prácticas de la Liquid Network, desde la configuración y el funcionamiento de los nodos hasta la comprensión de su uso en los mercados de capitales y la tokenización de la Bitcoin. Con presentaciones de expertos del sector, también obtendrá información sobre temas avanzados como los HTLC, el SDK de Breez y el proyecto Blockstream AMP.


Este bootcamp se realizó originalmente como un evento presencial, siguiendo un programa estructurado (como se muestra en la imagen) diseñado para sesiones en directo. Sin embargo, para esta adaptación del curso, el contenido se ha reorganizado para adaptarlo mejor a un formato en línea y facilitar la comprensión del alumno. El nuevo orden garantiza una progresión lógica desde los conceptos básicos hasta los temas más avanzados y técnicos, maximizando así la experiencia de aprendizaje.


Esta jornada está estructurada para dar cabida a participantes con distintos niveles de experiencia, ofreciendo una mezcla de conocimientos teóricos y experiencia práctica. Al final de este campamento de entrenamiento, conocerá a fondo la arquitectura de Liquid, su integración con Bitcoin y cómo utilizar sus innovadoras funciones para crear y optimizar soluciones financieras.


Sumérgete en el mundo de la cadena lateral Liquid y libera todo su potencial ahora mismo

# Fundamentos


<partId>6dd86449-c0f7-4e51-9252-5f135cf019df</partId>


## Liquid Arquitectura


<chapterId>4bca9c70-d54d-4e9a-b2db-17c3a6fa655b</chapterId>


:::video id=ff6899d2-b47f-4c3d-983d-3bd66d2be59d:::

### Arquitectura y modelo de consenso de Liquid Network


Liquid Network es una cadena lateral federada construida sobre la base de código de Elements, diseñada para ampliar las capacidades de Bitcoin al tiempo que se apoya en su seguridad fundamental. A diferencia de [Proof-of-Work](https://planb.academy/resources/glossary/proof-of-work) de Bitcoin, Liquid opera en un modelo de [Consenso](https://planb.academy/resources/glossary/consensus) Federado. El mantenimiento de la red corre a cargo de un grupo de miembros distribuidos por todo el mundo, entre los que se cuentan bolsas, mesas de contratación y proveedores de infraestructuras. De entre estos miembros, se seleccionan quince "funcionarios" para actuar como firmantes de [bloques](https://planb.academy/resources/glossary/block).


Estos funcionarios producen bloques de forma determinista, con un nuevo bloque generado cada minuto. Esta sincronización precisa contrasta con los intervalos probabilísticos de diez minutos de Bitcoin. Para que un bloque sea válido, necesita la firma de al menos 11 de los 15 funcionarios (un umbral de dos tercios más uno). Este mecanismo dota a Liquid de "finalidad de dos bloques", lo que significa que una vez que una [transacción](https://planb.academy/resources/glossary/transaction-tx) tiene dos confirmaciones (aproximadamente dos minutos), es matemáticamente imposible reorganizar la cadena. Esta velocidad y certidumbre son fundamentales para el arbitraje, la negociación automatizada y la rápida liquidación entre bolsas.


La federación es dinámica. Mediante el protocolo de federación dinámica (Dynafed), la red puede rotar a los funcionarios o actualizar los parámetros sin necesidad de un [fork](https://planb.academy/resources/glossary/fork) duro. Esto permite que el sistema evolucione y sustituya hardware o miembros sin problemas, manteniendo un funcionamiento continuo.


### Confidential Transactions y Gestión de Activos


Una característica definitoria de Liquid es su compatibilidad nativa con Confidential Transactions (CT) y múltiples activos. En la cadena principal de Bitcoin, todos los detalles de la transacción (remitente, destinatario e importe) son públicos. En Liquid, la TC utiliza compromisos criptográficos para ocultar el tipo de activo y el importe del libro mayor público, al tiempo que permite a la red verificar que la transacción es válida (es decir, que no se ha producido [inflación](https://planb.academy/resources/glossary/inflation)). Sólo los participantes que poseen las claves de ocultación pueden ver los valores específicos, lo que ofrece un nivel de privacidad comercial esencial para las instituciones que mueven grandes posiciones.


Liquid trata todos los activos como ciudadanos "nativos" de la [blockchain](https://planb.academy/resources/glossary/blockchain). Esto incluye Liquid Bitcoin (LBTC), stablecoins como USDT y tokens de seguridad. Emitir un activo no requiere complejos contratos inteligentes; es una función básica del protocolo.


#### Activos regulados y AMP

Para los activos que requieren conformidad, como los tokens de seguridad, Liquid emplea la Plataforma de Gestión de Activos (AMP) de Blockstream. Esto introduce una capa de permisos en la que las transacciones requieren una segunda firma de un servidor de autorización. Esto permite a los emisores hacer cumplir las normas -como las listas blancas o los requisitos KYC- a un nivel granular, combinando la eficiencia de una cadena de bloques con los controles reglamentarios de las finanzas tradicionales.


### La infraestructura bidireccional Peg y Security


La conexión entre Liquid y Bitcoin se mantiene a través de una conexión bidireccional. Para conectarse, el usuario envía Bitcoin a una dirección generada en mainchain. Estos fondos se bloquean durante 102 confirmaciones (aproximadamente 17 horas) para eliminar los riesgos de reorganización. Estos fondos se bloquean durante 102 confirmaciones (aproximadamente 17 horas) para eliminar los riesgos de reorganización. Una vez confirmados, se acuña una cantidad equivalente de LBTC en la cadena lateral Liquid.


El proceso de "peg-out" permite a los usuarios canjear LBTC por Bitcoin. Para ello es necesario quemar LBTC y obtener una autorización criptográfica de la federación. Para evitar robos, los "peg-outs" están estrictamente controlados por Claves de Autorización de Peg-out (PAK) en poder de los miembros de la federación. Además, los fondos pueden intercambiarse instantáneamente a través de proveedores externos como SideSwap, evitando el retraso en la liquidación para una liquidez más rápida.


#### Módulos de seguridad de hardware (HSM)

La seguridad se aplica estrictamente a través del hardware. Los funcionarios no guardan [claves privadas](https://planb.academy/resources/glossary/private-key) en servidores estándar, sino que utilizan módulos de seguridad de hardware (HSM). Estos dispositivos están separados de la lógica del servidor anfitrión y programados con reglas estrictas. Por ejemplo, un HSM se negará a firmar un bloque si su altura no es mayor que la del anterior, impidiendo así la reescritura del historial. Este modelo de seguridad "adversarial" supone que el servidor anfitrión podría verse comprometido, lo que garantiza que las claves permanezcan seguras incluso si se vulnera la ubicación física.


## Fundamentos de Elements


<chapterId>1e9cfbed-108e-4067-afb9-4cf950cb43d3</chapterId>


:::video id=5652dcb2-4303-484c-8be5-d98063b39c1c:::

### Elements: Los cimientos de Liquid


Elements es una plataforma de blockchain de código abierto derivada del código base de Bitcoin Core. Amplía la funcionalidad de Bitcoin al permitir cadenas de bloques independientes de las cadenas laterales que pueden transferir activos a y desde Bitcoin. Mientras que Bitcoin Core alimenta la red Bitcoin, Elements es el motor de software detrás de Liquid Network y otras sidechains personalizadas.


La relación es directa: Liquid es una "instancia" específica de una cadena lateral Elements, configurada para su uso en producción con un modelo de consenso federado. Los desarrolladores familiarizados con Bitcoin encontrarán Elements intuitivo, ya que conserva la misma interfaz RPC (Remote Procedure Call) y estructura de línea de comandos (`elements-cli`, `elements-d`, `elements-qt`). La diferencia clave radica en la configuración: establecer `chain=liquidv1` conecta un [nodo](https://planb.academy/resources/glossary/node) a la red principal Liquid, mientras que `chain=elementsregtest` pone en marcha un entorno local de pruebas de regresión donde los desarrolladores pueden generate bloques al instante y probar sin dependencias externas.


#### Emisión de activos

Una característica destacada de Elements es la emisión nativa de activos. A diferencia de Ethereum, donde los tokens son complejos contratos inteligentes, los activos en Elements son ciudadanos de primera clase creados a través de un simple comando RPC (`issueasset`).


- Identificadores únicos:** Cada activo recibe un ID hexadecimal único de 64 caracteres.
- Tokens de reemisión:** Los emisores pueden crear opcionalmente tokens de reemisión, que otorgan al titular el derecho a acuñar más del activo más adelante (útil para stablecoins o tokens de seguridad).
- Registro de Activos:** Dado que los ID hexadecimales no son legibles, el Registro de Activos de Blockstream asigna estos ID a nombres y tickers (por ejemplo, "USDT"), de forma similar a un DNS para activos.


### Privacidad a través de Confidential Transactions


Elements aborda una de las principales limitaciones de las blockchains públicas: la falta de privacidad comercial. En Bitcoin, el importe de cada transacción es visible para todo el mundo. Elements introduce **Confidential Transactions (CT)**, que oculta criptográficamente el importe y el tipo de activo al tiempo que permite a la red verificar la validez de la transacción.


Esto se consigue utilizando **Compromisos de Pedersen** y **Pruebas de Rango**.


- Los Compromisos Pedersen** sustituyen la cantidad visible por un compromiso criptográfico. Debido al cifrado homomórfico, los validadores pueden comprobar que *Compromisos de entrada = Compromisos de salida + Tasas* sin ver nunca los valores reales.
- Las pruebas de rango** evitan que un usuario cree dinero de la nada (por ejemplo, utilizando números negativos) demostrando matemáticamente que el valor oculto es un número entero positivo dentro de un rango válido.


Para un observador externo, una transacción confidencial muestra entradas y salidas válidas, pero oculta *qué* se está enviando y *cuánto*. Sólo el emisor y el receptor (que poseen las claves de ocultación) pueden ver los datos en texto claro.


### Desarrollo y flujo de trabajo de RPC


La interacción con un nodo Elements se realiza principalmente a través de su interfaz JSON-RPC. Esto permite a las aplicaciones escritas en Python, JavaScript o Go comunicarse con la cadena de bloques. Esto permite a las aplicaciones escritas en Python, JavaScript o Go comunicarse con la cadena de bloques.



- Configuración:** Un desarrollador suele empezar en modo `regtest`. Esto permite la generación instantánea de bloques (`generateblock`) para confirmar transacciones inmediatamente, evitando el tiempo de bloque de 1 minuto de la red en vivo.
- Comandos:** Están disponibles comandos estándar de Bitcoin como `getblockchaininfo`, junto con comandos específicos de Elements como `dumpblindingkey` (para auditar CTs) o `pegin` (para mover BTC a la sidechain).
- Alias:** Para gestionar múltiples nodos (por ejemplo, un "emisor" y un "receptor" para pruebas), los desarrolladores suelen utilizar alias de shell como `e1-cli` y `e2-cli` que apuntan a diferentes directorios de datos, simulando una red [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p) en una única máquina.


Esta arquitectura permite a los desarrolladores crear sofisticadas aplicaciones financieras -como plataformas de valores o pasarelas de pago privadas- utilizando las sólidas y familiares herramientas del ecosistema Bitcoin.


## Conexión de capas Bitcoin


<chapterId>3ff2df4a-8995-4d5e-9b8a-cd114880e666</chapterId>


:::video id=31368c02-b979-44d7-b217-ceed96c7ca5c:::

### Infraestructura Cross-Layer y HTLCs


El ecosistema Bitcoin ha evolucionado hasta convertirse en una arquitectura multicapa, en la que Mainchain proporciona liquidación, Lightning ofrece velocidad y Liquid permite capacidades avanzadas de activos. Mover valor entre estas capas sin intermediarios centralizados requiere una primitiva criptográfica sin confianza: la [Hash](https://planb.academy/resources/glossary/hash-function) Time Locked Contract ([HTLC](https://planb.academy/resources/glossary/htlc)).


Un HTLC crea un [canal de pago](https://planb.academy/resources/glossary/payment-channel) condicional que enlaza sistemas independientes de forma atómica. Funciona mediante dos restricciones principales: un **bloqueo de hash** y un **bloqueo de tiempo**.


- La cerradura Hash:** Los fondos pueden gastarse inmediatamente si el receptor revela una "preimagen" secreta que coincida con un hash criptográfico específico.
- El bloqueo temporal:** Si el receptor no revela el secreto en un plazo determinado (altura del bloque), el emisor original puede reclamar los fondos.


Esta estructura de doble ruta garantiza la seguridad. En un intercambio entre capas, se utiliza la misma clave hash en ambas redes. Cuando el receptor revela el secreto para reclamar fondos en una capa (por ejemplo, Liquid), ese secreto se hace visible para el remitente, que puede utilizarlo para reclamar los fondos recíprocos en la otra capa (por ejemplo, Lightning). Esta vinculación criptográfica garantiza que el intercambio se complete con éxito para ambas partes o fracase para ambas, eliminando el riesgo de que una parte pierda fondos mientras la otra los gana.


### Actualización de Taproot y MuSig2


Las HTLC heredadas ([SegWit](https://planb.academy/resources/glossary/segwit) v0) funcionaban bien, pero adolecían de inconvenientes de privacidad y eficiencia. Requerían publicar toda la lógica del [script](https://planb.academy/resources/glossary/script) on-chain, lo que hacía que las transacciones de intercambio fueran fácilmente identificables para los analistas de blockchain y más caras debido a su tamaño de datos. La introducción de [Taproot](https://planb.academy/resources/glossary/taproot) (SegWit v1) y el protocolo MuSig2 ha revolucionado esta arquitectura.


Taproot permite la **Agregación de claves** a través de MuSig2. En lugar de revelar un complejo script con múltiples [claves públicas](https://planb.academy/resources/glossary/public-key), MuSig2 permite a los participantes del intercambio combinar sus claves en una única clave pública agregada.


- Si ambas partes están de acuerdo con el intercambio (el "camino feliz"), firman conjuntamente la transacción. Para la red, esto parece idéntico a un pago estándar con una sola firma. Consume un espacio de bloque mínimo y no revela absolutamente ninguna información sobre las condiciones del canje.
- Si una de las partes no responde o es maliciosa, sólo entonces se revela el script subyacente (que contiene los bloqueos de hash/tiempo). Esto se organiza en un [árbol de Merkle](https://planb.academy/resources/glossary/merkle-tree), permitiendo a la parte honesta exponer sólo la rama específica necesaria para recuperar los fondos, manteniendo el resto de la lógica del contrato oculta.


### Aplicación práctica: Liquid-Cambios relámpago


En la práctica, estos protocolos permiten un intercambio fluido entre las capas de Bitcoin. Un intercambio típico de Liquid a Lightning comienza cuando un cliente solicita un intercambio a un proveedor de servicios. El cliente proporciona una [factura Lightning](https://planb.academy/resources/glossary/invoice-lightning), y el proveedor bloquea el Bitcoin equivalente de Liquid (L-BTC) en una dirección HTLC habilitada para Taproot.


La atomicidad se hace efectiva cuando se liquida el pago. Para reclamar el L-BTC, el proveedor de servicios debe tener la preimagen. La preimagen sólo se obtiene cuando se paga correctamente la factura Lightning del cliente. En el momento en que se finaliza el pago Lightning, se revela la preimagen, lo que permite al proveedor desbloquear los fondos Liquid.


#### Abstracción Wallet y gestión UTXO

Para los usuarios finales, esta complejidad es totalmente abstracta. Los [monederos](https://planb.academy/resources/glossary/wallet) modernos como Aqua gestionan los procesos de generación de claves, creación de facturas y firma en segundo plano. El usuario simplemente "paga" una factura Lightning utilizando su saldo de Liquid. Entre bastidores, el servicio gestiona la consolidación de [UTXO](https://planb.academy/resources/glossary/utxo), barriendo periódicamente las salidas pequeñas, no reclamadas o reembolsadas para mantener la eficiencia de wallet y minimizar el impacto de las tarifas durante los periodos de mucho tráfico.


## Visión general de Liquid Network


<chapterId>1968db03-2364-46c0-9670-9e9844289ca1</chapterId>


:::video id=0bac0a62-90f2-41da-ac7c-330c0604bc61:::

### Liquid Network Arquitectura y consenso


Liquid Network funciona como una cadena lateral federada basada en el código **Elements**. Mientras que Elements -una fork de Bitcoin Core- proporciona la base de software, Liquid es la implementación de la red de producción. A diferencia de Proof-of-Work de Bitcoin, que depende de la competitiva [mining](https://planb.academy/resources/glossary/mining), Liquid utiliza un modelo de **consenso federado**.


El mantenimiento de la red corre a cargo de quince "funcionarios" distribuidos por todo el mundo Estas entidades operan servidores especializados que desempeñan dos funciones críticas:

1.  **Producción de bloques:** Los funcionarios se turnan para crear bloques en un programa determinista de rotación, generando un nuevo bloque exactamente cada minuto.

2.  **Firma de bloques:** Para que un bloque sea válido, debe estar firmado por al menos 11 de los 15 funcionarios.


Este umbral de 11 de 15 garantiza que la red pueda tolerar el fallo de hasta cuatro nodos sin detenerse. La principal ventaja de este compromiso es la **finalidad determinista**. Mientras que Bitcoin se basa en probabilidades, Liquid logra la certeza de la liquidación después de dos bloques (aproximadamente dos minutos). Una vez que un bloque tiene una única confirmación encima, la cadena no puede reorganizarse, lo que la hace muy eficaz para el arbitraje y la liquidación rápida.


### Confidential Transactions y activos autóctonos


La característica que define a Liquid es el uso por defecto de **Confidential Transactions (CT)**. En la Bitcoin mainchain, el remitente, el destinatario y el importe son públicos. Liquid mejora esta situación al ocultar criptográficamente el importe y el tipo de activo, dejando visibles las direcciones del remitente y el destinatario para su verificación.


Para garantizar que un usuario no pueda imprimir dinero (por ejemplo, enviando cantidades negativas), Liquid emplea **Compromisos de Pedersen** y **Pruebas de Rango**. Estas primitivas criptográficas permiten a la red verificar que *Entradas = Salidas + Tasas* y que todos los valores son enteros positivos, sin revelar nunca los números concretos al libro mayor público. Sólo los participantes que posean las claves cegadoras pueden ver los datos descifrados.


#### Emisión de activos

Liquid trata todos los activos como "nativos" Ya se trate de Liquid Bitcoin (L-BTC), una stablecoin como USDT, o un token de seguridad, todos comparten la misma arquitectura. Emitir un activo no requiere contratos inteligentes, sólo una simple llamada RPC.


- Activos no regulados:** Pueden ser emitidos sin permiso por cualquier persona.
- Activos regulados:** Utilizando la Plataforma de Gestión de Activos (AMP) de Blockstream, los emisores pueden aplicar las normas de cumplimiento (como KYC/AML) exigiendo una segunda firma de un servidor de autorización antes de poder mover un activo.


### La clavija bidireccional y la federación dinámica


El puente entre Bitcoin y Liquid es el **Peg bidireccional**. Permite a los usuarios mover BTC a la cadena lateral (Peg-in) y de vuelta a la mainchain (Peg-out).


**El proceso Peg-in:**

Esto es sin permiso. Un usuario envía BTC a una dirección controlada por la federación. Para protegerse de las reorganizaciones de la blockchain Bitcoin, estos fondos deben esperar **102 confirmaciones** (aprox. 17 horas) antes de que se acuñe el L-BTC equivalente en la sidechain.


**El proceso de Peg-out:**

Para volver a Bitcoin, se quema L-BTC. Sin embargo, para evitar el robo de las reservas subyacentes de Bitcoin, las salidas no están totalmente automatizadas. Requieren la autorización de un miembro que posea una **clave de autorización de salida (PAK)**. Los propios fondos del Bitcoin están protegidos en un wallet multifirma de 11 de 15, con claves guardadas en módulos de seguridad de hardware (HSM) que están aislados de los servidores principales de los funcionarios.


**Federación Dinámica (Dynafed):**

Para garantizar su longevidad, Liquid emplea Dynafed, un protocolo que permite a la red rotar a los funcionarios o actualizar los parámetros sin necesidad de una fork dura. Si hay que sustituir a un funcionario, la red emite una transacción de transición. Tras un periodo de solapamiento de dos semanas, la nueva configuración toma el relevo, lo que permite a la federación evolucionar sin problemas y mantener un tiempo de actividad continuo.


## Ecosistema y mercados de capitales


<chapterId>5f4c0e50-b435-4b6c-b8b7-c55cc1a35431</chapterId>


:::video id=07e0b82f-2d60-4eb3-9b5d-2ccb7ad06e8a:::

### Liquid Network: Estrategia empresarial y ecosistema


Liquid es más que una cadena lateral técnica; es una capa de infraestructura centrada en el negocio y diseñada para gestionar los complejos requisitos de los mercados de capitales que Bitcoin mainchain no pueden soportar de forma eficiente. Mientras que [Lightning Network](https://planb.academy/resources/glossary/lightning-network) está optimizada para pagos de alta frecuencia y bajo valor, Liquid se centra en transferencias de alto valor, emisión de activos y liquidación entre intercambios.


El ecosistema está impulsado por la **Liquid Federation**, un consorcio de unas 73 empresas que incluye bolsas, mesas de negociación y proveedores de infraestructuras. Este modelo de colaboración es un reflejo de las cámaras de compensación financieras tradicionales, pero funciona con mayor transparencia y tiempos de liquidación significativamente reducidos (2 minutos frente a T+2 días).


### La tokenización de los activos del mundo real (RWA)


El principal argumento comercial de Liquid es la "tokenización", que representa el valor del mundo real (acciones, bonos, contratos mining) como fichas digitales en la cadena de bloques. Esto ofrece tres ventajas principales:

1.  **Mercados globales 24 horas al día, 7 días a la semana:** Eliminación de horarios bancarios y restricciones geográficas.

2.  **Eficiencia operativa:** Eliminación de errores de conciliación mediante un libro mayor compartido e inmutable.

3.  **Liquidación atómica:** Reducción del riesgo de contraparte garantizando que la entrega se produce simultáneamente con el pago.


#### Activos regulados y AMP

La mayoría de los activos institucionales no pueden negociarse sin permisos debido a requisitos legales. La **plataforma de gestión de activos (AMP)** es el estándar técnico que hace cumplir estas normas.


- Listas blancas:** Los emisores pueden restringir la tenencia y la negociación a las direcciones verificadas por KYC.
- Control Multisig:** Las acciones de cumplimiento (como la congelación de fondos robados o la reemisión de tokens perdidos) se gestionan mediante autorización multifirma, lo que garantiza que ningún empleado pueda actuar unilateralmente.


Esta infraestructura ya está en funcionamiento. Plataformas como **Stalker** ofrecen servicios de tokenización de extremo a extremo en Europa, mientras que **Sideswap** actúa como bolsa descentralizada y wallet no custodiada, permitiendo la negociación entre pares de activos como el **Blockstream Mining Note (BMN)** y las acciones tokenizadas de MicroStrategy (CMSTR).


### Éxito en el mundo real: El caso Mayfell


La prueba más convincente de la utilidad de Liquid procede de **Mayfell** en México. En un mercado en el que la financiación tradicional se basa en pagarés en papel, propensos a pérdidas, fraudes y lentitud de procesamiento, Mayfell trasladó toda la infraestructura a Liquid.



- Escala:** Más de 25.000 pagarés emitidos, que representan **más de 1.500 millones de dólares** en valor.
- Privacidad:** Utilizando Confidential Transactions de Liquid, los importes de los préstamos sólo son visibles para el prestamista y el prestatario, lo que preserva la privacidad comercial al tiempo que permite a los auditores verificar la integridad del libro mayor.
- Impacto:** Al conectar a los prestamistas no bancarios con los mercados globales de capital a través de blockchain, Mayfell redujo los costos y amplió el acceso al crédito para las pymes mexicanas, demostrando que la propuesta de valor de Liquid se extiende mucho más allá del comercio especulativo.


### Posicionamiento estratégico frente a otras cadenas


Liquid compite en un mercado saturado de plataformas de tokenización (Ethereum, Solana, etc.), pero cuenta con claras ventajas estratégicas:


- Claridad normativa:** Liquid utiliza Bitcoin (L-BTC) como activo nativo. No tiene un token pre-minado ni una ICO, evitando los riesgos de "valor no registrado" que plagan otras blockchains L1.
- Estabilidad:** A diferencia del modelo de cuenta de Ethereum, en el que las transacciones fallidas siguen quemando comisiones de gas, el modelo UTXO de Liquid es determinista y fiable para datos financieros de misión crítica.
- Privacidad:** La confidencialidad por defecto es un requisito para la mayoría de las instituciones financieras, una característica que Liquid ofrece de forma nativa y que las cadenas públicas luchan por implementar sin complejos complementos.


Para los desarrolladores, este ecosistema ofrece una clara oportunidad: crear las herramientas (cuadros de mando, monederos, integraciones de cumplimiento) que tiendan un puente entre las finanzas tradicionales y la capa de liquidación segura de Bitcoin.


## Blockstream AMP


<chapterId>4f21a0a7-0dc0-44cf-8a3a-d9e2f8a3f05f</chapterId>


:::video id=f00822b4-dc1a-46ff-adfc-ff7c97a0024d:::

### Blockstream AMP: Control de activos autorizado en Liquid


Blockstream AMP (Asset Management Platform) sirve como una capa de infraestructura crítica en la Liquid Network, diseñada específicamente para los emisores de valores digitales regulados y stablecoins. Mientras que Liquid proporciona una capa base sin permisos con emisión nativa de activos, las entidades reguladas a menudo requieren una supervisión estricta y capacidades de cumplimiento. AMP salva esta brecha introduciendo una capa de control con permisos sobre activos específicos sin sacrificar los beneficios de privacidad de Confidential Transactions de Liquid.


La principal propuesta de valor de la plataforma se basa en dos capacidades principales: la visibilidad completa del emisor y la autorización de las transacciones. A diferencia de los activos Liquid estándar, en los que los importes y los tipos son blinded para todos menos para los participantes, los activos AMP permiten al emisor mantener una pista de auditoría completamente unblinded transparente. Esta transparencia es esencial para los informes reglamentarios y las auditorías internas. Además, AMP aplica un estricto modelo de autorización mediante un mecanismo de cofirmación. Cada transferencia de un activo AMP requiere una firma del servidor AMP. Esto permite a los emisores aplicar normas complejas, como la congelación de cuentas, la creación de listas blancas de inversores acreditados o la imposición de límites a las transferencias, actuando de hecho como un guardián centralizado dentro de una red descentralizada.


#### Compromisos operativos

Esta arquitectura introduce contrapartidas específicas. El sistema depende de la disponibilidad del servidor AMP; si el servidor actúa como cofirmante y se desconecta, la liquidez de los activos se detiene. Además, aunque se mantiene la privacidad de usuario a usuario, los inversores deben aceptar que el emisor tenga plena visibilidad de sus tenencias. Este modelo es ideal para los tokens de seguridad que cumplen las normas, pero inadecuado para las [criptomonedas](https://planb.academy/resources/glossary/cryptocurrency) resistentes a la censura.


### Evolución de la arquitectura y vías de integración


El ecosistema AMP se encuentra actualmente en transición desde su primera iteración a una arquitectura "Versión 2" más flexible e interoperable. El sistema anterior exigía a los emisores mantener nodos Elements totalmente sincronizados y obligaba a los desarrolladores a depender en gran medida del SDK Green monolítico. Aunque funcional, esto creaba grandes barreras técnicas de entrada y limitaba las opciones de wallet.


La arquitectura de nueva generación simplifica fundamentalmente estos requisitos trasladando la complejidad al servidor. En este nuevo modelo, el servidor de AMP se encarga del trabajo pesado de la construcción de transacciones, la selección de UTXO y el cálculo de comisiones. Presenta al emisor una transacción Elements parcialmente firmada (PSET) que sólo requiere una firma. Este enfoque de "servidor inteligente, wallet tonto" elimina la necesidad de que los emisores ejecuten nodos completos y permite el uso de monederos de hardware y configuraciones estándar multifirma para la gestión de tesorería.


Para los desarrolladores, esta evolución significa alejarse de los SDK propietarios y acercarse a los descriptores estándar y los flujos de trabajo PSET. Ahora, los monederos pueden registrar descriptores multifirma en el servidor de AMP para establecer derechos de autorización. Esto alinea el desarrollo de AMP con los estándares más amplios Bitcoin wallet, haciendo la integración accesible a cualquier aplicación capaz de manejar los formatos PSBT/PSET. Se anima a los desarrolladores a que utilicen herramientas como el Liquid Wallet Kit (LWK), compatible con estas arquitecturas modernas basadas en descriptores, para garantizar que sus aplicaciones estén preparadas para el futuro con los nuevos estándares de AMP.


### El ecosistema Liquid Wallet y la confidencialidad


La creación de aplicaciones en Liquid requiere navegar por una pila más compleja que el desarrollo estándar en Bitcoin debido a características como los activos nativos y Confidential Transactions. El ecosistema se apoya en una arquitectura por capas: las bibliotecas de bajo nivel como `secp256k1-zkp` gestionan las primitivas criptográficas, mientras que los conjuntos de herramientas de alto nivel gestionan la lógica de wallet.


Históricamente, el Kit de Desarrollo Green (GDK) proporcionaba una solución completa pero rígida. La alternativa moderna es el Kit Liquid Wallet (LWK), que ofrece un enfoque modular. El LWK separa los problemas en distintas cajas, gestionando los descriptores, la firma y la comunicación de hardware de forma independiente, lo que ofrece a los desarrolladores la flexibilidad necesaria para crear soluciones personalizadas sin la sobrecarga de una biblioteca monolítica.


#### Manipulación Confidential Transactions

El reto más destacado de este ecosistema es la gestión del ciclo de vida del cegado. En Liquid, los resultados de las transacciones se cifran mediante el intercambio de claves de curva elíptica Diffie-Hellman (ECDH). El remitente utiliza la clave pública del receptor para cifrar las cantidades y tipos de activos, generando una prueba de alcance que verifica la validez de la transacción sin revelar los valores.


Para que una wallet funcione, debe invertir con éxito este proceso. Cuando una wallet detecta una transacción entrante, intenta desencriptar la salida utilizando su clave de desencriptación privada. Si el secreto compartido coincide, la wallet puede descifrar el valor y añadirlo al saldo del usuario. Este proceso es intensivo desde el punto de vista informático y requiere una gestión precisa de los factores de cegamiento para garantizar que las transacciones estén matemáticamente equilibradas, una complejidad que herramientas como LWK pretenden eliminar para el desarrollador.


# Técnico


<partId>53629f58-b9e0-4a10-8ab2-d51b047414f8</partId>

<chapterId>f1fdf2b0-4b6a-4ba7-812c-7586dcb36713</chapterId>


## SDK Breez - Sin nodos


<chapterId>fb77442c-3d1e-427e-b2f5-16668ce4c643</chapterId>


:::video id=1a6289b5-fdae-4320-b5b1-41925150108c:::

### Introducción al SDK de Breez Liquid


El SDK de Breez Liquid es un conjunto de herramientas autocustodiado y de código abierto diseñado para tender un puente entre Liquid Network y el ecosistema más amplio de Bitcoin. Su misión principal es abstraer las complejidades de la gestión de nodos y los intercambios atómicos de Lightning Network, permitiendo a los desarrolladores crear aplicaciones financieras sin fricciones.


Construida con una filosofía "mobile-first", la lógica central está escrita en Rust por rendimiento y seguridad, pero utiliza UniFFI (Unified Foreign Function Interface) para proporcionar bindings nativos para Kotlin, Swift, Python, C#, Dart y Flutter. Esto garantiza que los desarrolladores puedan integrar la funcionalidad Bitcoin en su entorno preferido sin gestionar operaciones criptográficas de bajo nivel.


**Tipos de transacción admitidos:**

El SDK funciona con Liquid como "base de operaciones" Destaca en tres operaciones específicas:

1.  **Liquid-a-Liquid:** Transferencias directas on-chain.

2.  **Liquid-a-Lightning:** Pago de facturas Lightning utilizando fondos Liquid.

3.  **Liquid-a-Bitcoin:** Intercambio de fondos directamente a la Bitcoin mainchain.


*Nota: El SDK no admite transacciones directas de Lightning a Lightning ni de Bitcoin a Bitcoin. Es una herramienta estrictamente centrada en Liquid. Es estrictamente una herramienta centrada en Liquid.*


### Arquitecturas de pago: Swaps submarinos


Para lograr la interoperabilidad entre Liquid, Lightning y Bitcoin sin custodios centralizados, Breez se basa en **Submarine Swaps**. Se trata de operaciones atómicas en las que una transacción se completa con éxito en ambas redes o falla en ambas, lo que garantiza que los fondos nunca se pierdan en tránsito.


#### Lightning Send (Intercambio de submarinos)

Cuando un usuario paga una factura Lightning, el SDK emite una transacción de "bloqueo" en la Liquid Network. Esto pone los fondos en custodia. El proveedor del swap (Boltz) lo detecta, paga la factura Lightning y, a continuación, utiliza la imagen previa del pago (el recibo criptográfico) para reclamar los fondos bloqueados de Liquid.


#### Recepción relámpago (intercambio submarino inverso)

La recepción de Lightning es el proceso inverso. El usuario genera una factura y el proveedor de swaps bloquea los fondos en la Lightning Network. El SDK supervisa este proceso a través de WebSockets. Una vez confirmado el bloqueo, el SDK ejecuta automáticamente una transacción de reclamación para mover los fondos equivalentes a la Liquid wallet del usuario.


#### Cadena cruzada Bitcoin

Para las transferencias de Liquid a Bitcoin, la arquitectura utiliza un mecanismo de "doble intercambio". Las transacciones de bloqueo se realizan simultáneamente en ambas cadenas. El remitente reclama fondos en Bitcoin, mientras que el receptor lo hace en Liquid. Esto permite una transferencia sin confianza, sin depender de federated peg-outs ni de intercambios centralizados.


### Desarrollador Interface y gestión automatizada


El SDK Breez simplifica la experiencia del desarrollador condensando los complejos flujos financieros en un proceso estandarizado de tres pasos: **Conectar, Preparar y Ejecutar**.


1.  **Connect:** Inicializa la wallet, se sincroniza con la blockchain usando el Liquid Wallet Kit (LWK), y establece conexiones WebSocket para monitorización en tiempo real.

2.  **Preparar:** Antes de comprometer los fondos, este paso calcula y devuelve todas las comisiones de red y costes de intercambio asociados, permitiendo que la interfaz de usuario presente un total claro al usuario.

3.  **Ejecutar:** Este paso construye la transacción, la difunde e inicia el intercambio.


#### Mecanismos de seguridad automatizados

Una de las funciones más importantes del SDK es la **gestión automatizada de reembolsos**. En caso de fallo de la red o de que la contraparte no coopere, los fondos podrían quedar teóricamente atrapados en un contrato bloqueado en el tiempo. El SDK abstrae por completo la lógica de recuperación. Supervisa el estado de cada swap; si un swap falla o expira, el SDK construye y transmite automáticamente la transacción de reembolso para devolver los fondos a la wallet del usuario.


Además, el SDK se encarga de la **Resolución de metadatos**. Fusiona los datos de intercambio off-chain (proporcionados por el intercambiador Boltz) con el historial de transacciones on-chain. Esto garantiza que el historial de transacciones del usuario sea legible para el ser humano, mostrando los detalles de la factura y el contexto de pago en lugar de sólo hashes de transacciones hexadecimales en bruto.


# Sección final


<partId>7ec65e6b-6e63-41b6-92ea-6a13bc77c3ff</partId>


## Opiniones y valoraciones


<chapterId>e5f6348c-e207-40ae-8fef-6a068a6bf741</chapterId>


<isCourseReview>true</isCourseReview>

## Examen final


<chapterId>b13c4aa8-ced6-11f0-8515-afd3f381a001</chapterId>

<isCourseExam>true</isCourseExam>

## Conclusión


<chapterId>e30a5587-d74b-4360-87fb-bbf3de1b0ba8</chapterId>

<isCourseConclusion>true</isCourseConclusion>