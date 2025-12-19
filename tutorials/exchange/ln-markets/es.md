---
name: LN Markets
description: Plataforma comercial Bitcoin en Lightning Network
---

![cover](assets/cover.webp)



LN Markets es la primera plataforma de trading de Bitcoin verdaderamente nativa de Lightning, que te permite operar derivados apalancados de Bitcoin directamente desde su wallet Lightning, sin KYC, liquidaciones instantáneas y custodia mínima. Lanzada en 2020, elimina las fricciones de las plataformas tradicionales: Sin verificación de identidad, sin depósitos bloqueados, sin esperar confirmaciones de blockchain. Tu wallet Lightning se convierte en tu cuenta de trading.

## ¿Qué es LN Markets?

LN Markets ofrece **Futuros** (contratos perpetuos con apalancamiento de hasta 100×) y **Opciones** (Call/Put con riesgo limitado a la prima pagada). La plataforma funciona como una capa de agregación de liquidez que consolida múltiples centros de operación para una ejecución óptima sin deslizamiento. Tus fondos sólo están bloqueados durante la duración exacta de tus posiciones activas, y no durante días o semanas como ocurre con una cuenta de custodia tradicional.

### Productos comerciales disponibles

**Futuros (contratos perpetuos)**

Los contratos perpetuos son futuros sin fecha de vencimiento, lo que te permite especular con la tendencia de precios de Bitcoin con apalancamiento. LN Markets ofrece dos modos de gestión de márgenes:

**Modo aislado**: Cada posición tiene su propio margen dedicado. Sólo los fondos asignados a esta posición específica están en riesgo. Si la posición alcanza el precio de liquidación, **sólo se liquida esta posición**, sus otras posiciones y el saldo restante no se ven afectados. Ideal para limitar estrictamente el riesgo por operación.

**Modo cruzado (margen cruzado)**: El margen se reparte entre todas tus posiciones abiertas. El saldo total de tu cuenta sirve como garantía para todas tus posiciones. Si una posición sale mal, el sistema recurre a todo tu saldo disponible para evitar la liquidación. **Riesgo**: Si tu saldo total se agota, todas tus posiciones pueden ser liquidadas simultáneamente. Recomendado sólo para operadores experimentados que busquen maximizar la eficiencia del capital.

**Gestión de puestos**:

- **Posición larga**: Apuestas por la subida del BTC/USD. Si el precio sube, ganas; si baja, pierdes. **Ejemplo**: Bitcoin a $100.000, abres una posición Long con 10.000 sats y apalancamiento 10×. Si Bitcoin sube a 105.000 $ (+5%), tu posición gana un 50% (5% × 10), es decir, ~5.000 sats de beneficio. Si Bitcoin cae a 95.000 $ (-5%), pierde el 50%, es decir, una pérdida de ~5.000 sats.

- **Posición corta**: Apuesta por la caída del par BTC/USD. Si el precio baja, ganas; si sube, pierdes. **Ejemplo**: Bitcoin a $100.000, abres una posición corta con 10.000 sats y apalancamiento 10×. Si Bitcoin cae a 95.000 $ (-5%), tu ganas el 50%, es decir, ~5.000 sats. Si Bitcoin sube a 105.000 $ (+5%), pierdes el 50%.

El apalancamiento (hasta 100×) amplifica proporcionalmente las ganancias y las pérdidas. Un mecanismo de **tasa de financiación** (cargos periódicos cada 8 horas) equilibra las posiciones largas y cortas. Puedes gestionar hasta 100 posiciones de futuros simultáneamente.

**Opciones**

Una opción es como un **boleto de lotería con fecha de caducidad**. Pagas una prima para apostar por la dirección del precio Bitcoin. **Ventaja principal**: Nunca puedes perder más que la prima pagada, no hay liquidación posible.


- **Opción Call (apuesta alcista)**: Apuestas a que Bitcoin subirá por encima del precio de ejercicio antes del vencimiento. Ganas si el precio sube, la pérdida se limita a la prima si el precio baja.


- **Opción de venta (apuesta bajista)**: Apuestas a que Bitcoin caerá por debajo del precio de ejercicio. Ganas si el precio cae, la pérdida se limita a la prima si el precio sube.

- **Straddle (apuesta de volatilidad)**: Compras simultáneamente una opción de compra y una opción de venta. Ganas si Bitcoin se mueve en cualquier dirección, pierdes ambas primas si el precio se mantiene estable.

Límite: 50 posiciones simultáneas. Ideal para iniciarse en el trading apalancado sin miedo a la liquidación.

**sats ↔ sUSD**: Convierte instantáneamente tus satoshis en dólares sintéticos (sUSD) para protegerte de la volatilidad, o viceversa para recuperar la exposición al Bitcoin.

## Acceso a la plataforma y creación de cuentas

### Ir a LN Markets

Ve a [lnmarkets.com](https://lnmarkets.com) y haz clic en "Abrir aplicación".

![Page d'accueil LN Markets](assets/fr/01.webp)

### Crea tu cuenta

La pantalla de bienvenida ofrece varios métodos de conexión:

![Méthodes de connexion](assets/fr/02.webp)

**Opciones disponibles**:

1. **Registrarse con una wallet Lightning** (recomendado): LNURL-auth con Phoenix, Breez, Zeus o BlueWallet

2. **Registrarse con correo electrónico**: Cuenta clásica (limita la experiencia Lightning)

3. **Alby** o **Ledger**: extensiones del navegador

### Conexión a través de Lightning (LNURL-auth)

Haz clic en "Registrarse con una wallet Lightning". Escanea el código QR con tu wallet Lightning:

![QR code LNURL-auth](assets/fr/03.webp)

Tu wallet firma automáticamente una solicitud criptográfica y tu cuenta se crea al instante, sin correo electrónico ni contraseña. Seguridad sólida y anonimato total.

### Configuración inicial

![Configuration post-connexion](assets/fr/04.webp)

**Parámetros disponibles**:

- **Nombre de usuario**: Personaliza tu nombre de usuario
- **Retiros automáticos**: Activa los retiros automáticas a tu wallet tras el cierre de la operación
- **Autenticación de dos factores**: Sseguridad mejorada con 2FA
- **Documentación**: Aacceso a los recursos oficiales

## Conociendo la Interfaz

La interfaz de LN Markets está organizada en varias secciones accesibles desde el menú lateral:

### Cuadro de mandos

![Dashboard](assets/fr/06.webp)

Muestra tu rendimiento por tipo de producto (Futuros Cruzados, Futuros Aislados, Opciones) con P&L, volúmenes negociados y su Address Lightning personal (por ejemplo `pivi@lnmarkets.com`).

### Perfil

![Profil trader](assets/fr/07.webp)

Estadísticas detalladas: Número de operaciones, tipo de operador (SCALPER, etc.), duración media de la posición, desglose Largo/Corto, tasa de ganancias, medias (cantidad, margen, apalancamiento) y estructura de comisiones progresiva en función del volumen.

### Oficios

![Historique des trades](assets/fr/08.webp)

La pestaña Operaciones muestra un historial completo de tus posiciones, con todas las métricas importantes: Fecha de creación, dirección (Larga/Corta), tamaño de la posición (cantidad), margen comprometido, precio de entrada y salida, beneficios/pérdidas realizados (P&L) y comisiones de negociación. Puedes filtrar por tipo de producto (futuros/opciones) y exportar tus datos para análisis externos o contabilidad.

### Ajustes

![Paramètres de la plateforme](assets/fr/05.webp)

La pestaña Configuración ofrece dos pestañas: **Cuenta** e **Interfaz**.

**Pestaña "Cuenta"**:

Gestión de cuentas con campos editables:

- **Nombre de usuario**: Cambia tu nombre de usuario (por ejemplo, "pivi") con el botón "Actualizar"
- **Correo electrónico**: Añade/edita tu dirección de correo electrónico
- **Dirección Bitcoin de depósito**: La dirección Bitcoin que puedes utilizar para depositar fondos on-chain.

**Tres interruptores de configuración**:

- **Aparecer en las clasificaciones**: Elige si quieres aparecer o no en las clasificaciones públicas
- **Utilizar direcciones Taproot**: Utilizar direcciones Bitcoin Taproot para depósitos/retiros on-chain
- **Activar retiradas automáticas**: Activa los retiros automáticos a tu wallet Lightning tras el cierre de la operación

**Migración de cuenta**: Sección que te permite migrar tu cuenta Lightning a la autenticación clásica por email/contraseña.

**Gestión de sesión**: Botón "Borrar sesión y datos locales" para desconectar y limpiar los datos locales del navegador.

**Pestaña Interface**:

Personaliza la experiencia del usuario con siete interruptores:

- **Omitir confirmación de orden**: Desactiva el modo de confirmación antes de la ejecución de la operación (negociación rápida)
- **Mostrar información sobre herramientas**: Muestra información sobre herramientas al pasar el ratón por encima de los elementos
- **Modo privado (enmascara datos sensibles)**: Enmascara importes y datos sensibles en la interfaz (modo privado)
- **Mostrar PL neto en el perfil**: Muestra los beneficios/pérdidas netos en tu perfil público
- **Utilizar iconos de unidades**: Muestra iconos de unidades monetarias (sats, $)
- **Activar notificaciones sonoras**: Activa las notificaciones sonoras para los eventos de negociación
- **Activar notificaciones de escritorio**: Activa las notificaciones de escritorio del sistema operativo

### Wallet

![Wallet](assets/fr/09.webp)

Bitcoin y saldos en USD sintéticos con historial de depósitos, retiross, transferencias cruzadas, swaps, financiación y gestión de direcciones on chain.

### API

![API V3](assets/fr/10.webp)

LN Markets ofrece una completa API REST (V2 y V3) para automatizar completamente tus operaciones a través de scripts o bots. Puedes crear claves API con permisos personalizables (solo lectura, trading, retiradas) directamente desde la interfaz. Los SDK oficiales de TypeScript y Python están disponibles para una fácil integración. La documentación completa de API V3 está disponible en [api.lnmarkets.com/v3](https://api.lnmarkets.com/v3).

## Primer ingreso de fondos

Haz clic en "Ingresar". Hay tres métodos disponibles:

![Modal de dépôt](assets/fr/11.webp)

1. **LNURL**: Escanea el código QR con tu wallet Lightning

2. **Invoice**: Introduce un importe y, a continuación, escanea la factura Lightning

3. **On-Chain**: Depósito Bitcoin on chain

## El trading en la práctica

### Operar con futuros en largo: Apostar al alza

En el panel de control, haz clic en "Futuros" y luego en "Aislados". Haga clic en **"Comprar "** para abrir una posición Larga.

![Interface Futures Long](assets/fr/12.webp)

Haz clic en el icono **calculadora** situado junto al botón "Comprar" para visualizar la calculadora de posiciones:

![Calculateur de position Long](assets/fr/13.webp)


**Ejemplo concreto**:


- **Cantidad**: $100 (tamaño de la posición)
- **Margen comercial**: 12.336 sats (margen comprometido)
- **Apalancamiento**: 7.73× (cada 1% de variación de BTC = 7,73% sobre tu capital)
- **Precio de entrada**: $104,863.5
- **Liquidación**: $92.852 (precio crítico de liquidación automática)
- **Precio de salida**: 110.000 dólares (para el cálculo de beneficios)
- **PL**: 4.492 sats (beneficio si la salida es de 110.000 $)

**Escenarios**:

- **Aumento +4,9%** ($110.000) : +4.492 sats de beneficio (+36,4%)
- **Neutral** ($104.863) : -185 sats (sólo tasas)
- **Abajo -11,5%** ($92.852): liquidación total (-100%)

Haz clic en el botón "Comprar" para confirmar la operación. **Dos casos posibles**:

- **Si dispones de suficiente liquidezen tu cuenta**: Se muestra directamente un modal de confirmación (imagen inferior). Haz clic en "Sí" para ejecutar la operación al instante.

![Confirmation trade Long](assets/fr/14.webp)

- **Si no dispones de suficiente efectivo**: En su lugar aparecerá un código QR Lightning. Escanéalo con tu wallet Lightning para pagar el margen requerido. La operación se abre automáticamente al recibir el pago

### Operar en corto con futuros: Apostar a la baja

Haz clic en **"Vender"** para abrir una posición Corta (Ganarás si el precio cae). Abre la calculadora con el icono de la calculadora para configurar tu posición:

![Calculateur de position Short](assets/fr/15.webp)

Haz clic en "Vender" para confirmar. En cuanto al Largo, **dos casos posibles**:

- **Si dispones de efectivo suficiente**: Mmodo de confirmación directa, haz clic en "Sí"
- **Si no dispones de suficiente efectivo**: Se muestra un código QR Lightning (imagen inferior). Escanéalo con tu wallet Lightning para pagar el margen requerido:

![Paiement Lightning pour Short](assets/fr/16.webp)

Una vez recibido el pago Lightning, tu posición Corta se abre automáticamente. A continuación, puedes gestionarla desde la interfaz de trading.

#### Cerrar una posición

Para cerrar tu posición (Larga o Corta), haz clic en la **pequeña cruz de la esquina inferior derecha** de la interfaz de gestión:

![Interface de clôture](assets/fr/17.webp)

Se muestra un cuadro de diálogo de confirmación para confirmar el cierre de la operación:

![Confirmation clôture](assets/fr/18.webp)

El modal muestra tu P&L (ganancia o pérdida) actual. Haz clic en "Sí" para cerrar. El saldo se añade instantáneamente (beneficio) o se deduce (pérdida) de tu Wallet a través de Lightning.

### Trading Opciones Call: Derecho condicional de compra

Las opciones ofrecen un **riesgo limitado** a la prima pagada, sin posibilidad de liquidación. Una opción de compra te da el derecho (no la obligación) de comprar Bitcoin al precio de ejercicio antes del vencimiento. A diferencia de los futuros, nunca podrás perder más que la prima invertida.

En el panel de control, haz clic en "Opciones" y selecciona la pestaña "Llamada".

![Interface Options Call](assets/fr/19.webp)

Configura tu operación con los siguientes parámetros:

- **Cantidad**: $100 (tamaño de su contrato)
- **Caducidad**: 2025-11-15 (fecha de expiración)
- **Strike**: 96.000 dólares (precio objetivo)

Los demás campos se calculan automáticamente:

- **Margen**: 1.045 sats (prima a pagar, tu inversión)
- **Punto de equilibrio**: $96.923 (precio para recuperar tu apuesta)
- **Delta**: 40 (sensibilidad al precio Bitcoin)

**¿Cómo calcular tu ganancia?**

Tu beneficio depende del precio de Bitcoin al vencimiento. Fórmula: **(Precio BTC - Strike) × Tamaño Contract - Prima pagada**.

**Ejemplos concretos**:

- **Bitcoin a $96.000** (precio actual): Valor intrínseco = 0 $. **Pérdida: -1,045 sats** (pierdes la prima)

- **Bitcoin a $97.000**: Valor intrínseco = (97.000 - 96.000) × 0,00105 BTC = $1,05. Convertido a sats ≈ 2,175 sats. **Ganancia: 2,175 - 1,045 = +1,130 sats** (+108% de ganancia)

- **Bitcoin a $98.000**: Valor intrínseco = $2.000 ≈ 3.224 sats. **Ganancia: +2.179 sats** (+208% de ganancia)

- **Bitcoin a $100.000**: Valor intrínseco = $4.000 ≈ 5.263 sats. **Ganancia: +4.218 sats** (+403% de ganancia)

- **Bitcoin por debajo de 96.000 dólares**: La opción expira sin valor. **Pérdida limitada: -1.045 sats**, sin liquidación posible

Haz clic en "Comprar Call". Aparece un cuadro de diálogo de confirmación:

![Confirmation Call option](assets/fr/20.webp)

Vuelve a pulsar "Comprar Call" para confirmar. La opción aparece en "Opciones en ejecución". Al vencimiento, LN Markets calcula automáticamente el valor intrínseco y ajusta su beneficio/pérdida.

**Nota sobre las opciones de venta**: El funcionamiento es idéntico al de una opción de compra, pero a la inversa. Con una opción de venta, apuestas a que el precio de Bitcoin bajará. Si Bitcoin cae por debajo de tu strike, ganas; si se mantiene por encima, sólo pierdes la prima pagada. El cálculo de las ganancias sigue la misma lógica: **(Strike - Precio BTC) × Tamaño Contract - Prima pagada**.

### Retiro de fondos Lightning

Haz clic en "Retirar":

![Modal de retrait](assets/fr/21.webp)

**Métodos**: LNURL, Invoice, Lightning Address, On-Chain.

**Procedimiento Invoice**:

1. Genera una factura Lightning desde tu wallet

2. Copia la factura (comienza por `lnbc...`)

3. Pégalo en el campo LN Markets

4. Confirma el retiro

5. Tu wallet se acredita en 1-3 segundos

Sin comisiones por retirada de fondos Lightning, sólo costes mínimos de direccionamiento (<0,1% en la práctica).

## Riesgos y buenas prácticas

**Riesgos principales**:

- **Liquidación total**: Un apalancamiento elevado puede acabar con el 100% del margen en cuestión de minutos
- **Servicio experimental**: Fase alfa, incertidumbres tecnológicas
- **Riesgo de contraparte**: La plataforma sigue siendo de contraparte única

**Mejores prácticas**:

1. **Gestión del capital**: Adopta una estrategia de gestión del riesgo adaptada a tu perfil. Por ejemplo: asigna el 5% de tus activos totales a operaciones apalancadas, y arriesga un máximo del 1% de este capital por operación (p. ej.: 1 activo BTC → 5M sats para operar → 50k sats de riesgo máximo por posición)

2. **Systematic stop-loss**: Configura stop-losses para limitar tus pérdidas por operación. Con una regla de riesgo del 1%, por ejemplo, incluso 10 operaciones perdedoras consecutivas representan sólo el 10% de tu capital de trading

3. **Empieza poco a poco**: Prueba primero con unos pocos miles de sats para comprender los mecanismos antes de aplicar tu estrategia de gestión del capital

4. **Retira regularmente tus ganancias**: Asegura tus ganancias en tu wallet principal, dejando sólo en la plataforma el capital de negociación activo

5. **Cuidado con el apalancamiento**: Evita un apalancamiento >20× a menos que seas plenamente consciente de los riesgos de liquidación

**Costes**: Sin comisiones de depósito/retiro Lightning, diferencial ~0,1% por operación (bajando al 0,06% en función del volumen).

## Ventajas y limitaciones

**Ventajas**:

- No custodia (control total excluidos los periodos de trading)
- Sin KYC (anonimato a través de Lightning/Nostr)
- Liquidaciones instantáneas (ingresos/retiros en segundos)
- Ejecución sin deslizamiento con agregación de liquidez
- API público y Nostr de apoyo


**Limitaciones**:

- Servicio alfa (posibles evoluciones)
- Menor liquidez que Binance/Deribit
- Prohibido para residentes en EE.UU

## Conclusión

LN Markets representa una importante evolución de las operaciones de Bitcoin al integrar de forma nativa Lightning Network para devolver el control a los usuarios. Para los bitcoiners expertos que buscan especular sin comprometer su soberanía, es una alternativa única a los intercambios centralizados tradicionales.

La plataforma sigue evolucionando con los futuros lineales USDT y la negociación sin custodia a través de Contratos de Registro Discreto (DLC) en fase de desarrollo. Aplicando buenas prácticas de gestión del riesgo (pequeñas cantidades, stop-loss, retiradas periódicas), LN Markets se convierte en una potente herramienta para explorar el apalancamiento Bitcoin de forma responsable.

Empieza poco a poco, prueba con unos pocos miles de satss y explora gradualmente esta nueva frontera de Lightning Network. ¡Feliz trading soberano ⚡️!

## Recursos

- [Sitio web oficial de LN Markets](https://lnmarkets.com)
- [Documentación](https://docs.lnmarkets.com)
