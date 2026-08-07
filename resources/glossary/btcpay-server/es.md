---
term: BTCPay Server

definition: Procesador de pagos de código abierto que permite aceptar pagos en bitcoins sin intermediarios.
---

⚠️ **Alerta crítica de seguridad (7 de agosto de 2026):** una vulnerabilidad crítica que afecta a BTCPay Server está siendo explotada activamente y puede provocar la pérdida de fondos. Actualiza tu instancia a la **versión 2.4.2** de inmediato mediante `Admin Dashboard > Server > Maintenance > Update` y luego comprueba que el pie de página muestre `2.4.2`. Si no puedes actualizar de inmediato, apaga tu BTCPay Server. Una vez actualizado, también debes renovar por completo tus macaroons y tu `macaroons.db`, renovar por completo las cadenas de autenticación de cualquier otro backend Lightning y, si generaste una cartera caliente on-chain dentro de BTCPay Server, mover esos fondos y volver a crear la cartera. Los integradores también deben actualizar NBXplorer a la versión 2.6.10. Fuente: [Notas de la versión BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-update-7033a305-8404-4cba-8324-4c7eb679016b
BTCPay Server es un procesador de pagos de código abierto que permite a comerciantes y usuarios aceptar pagos Bitcoin sin depender de terceros para el procesamiento de transacciones. Lanzado en 2017, BTCPay Server ofrece una solución de integración de pagos Bitcoin para sitios de comercio electrónico, con características avanzadas como soporte para monederos de hardware, herramientas de facturación y contabilidad, así como compatibilidad con la red Lightning. Su desarrollo fue iniciado por Nicolas Dorier, en respuesta a las acciones de Bitpay que, según él, había engañado a sus usuarios empujándoles hacia la adopción de SegWit2x, que la compañía consideraba erróneamente como el "verdadero" Bitcoin. Esta oposición se plasmó en un tuit ya famoso de Nicolas Dorier en agosto de 2017:

> "_Es mentira, mi confianza en ti está rota, te haré obsoleto_".
