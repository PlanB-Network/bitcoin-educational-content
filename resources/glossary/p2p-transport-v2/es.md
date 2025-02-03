---
term: TRANSPORTE P2P V2

---
Nueva versión del protocolo de transporte P2P de Bitcoin que incorpora el cifrado oportunista para mejorar la privacidad y seguridad de las comunicaciones entre nodos. Esta mejora pretende resolver varios problemas de la versión básica del protocolo P2P, en particular haciendo que los datos intercambiados sean indistinguibles para un observador pasivo (como un proveedor de servicios de Internet), reduciendo así los riesgos de censura y ataques mediante la detección de patrones específicos en los paquetes de datos.

El cifrado implementado no incluye autenticación para evitar añadir una complejidad innecesaria y no comprometer la naturaleza sin permisos de la conexión de red. No obstante, este nuevo protocolo de transporte P2P ofrece una mayor seguridad contra los ataques pasivos y hace que los ataques activos sean mucho más costosos y detectables (en particular, los ataques MITM). La introducción de un flujo de datos pseudoaleatorio complica la tarea de los atacantes que desean censurar o manipular las comunicaciones.

El Transporte P2P V2 se incluyó como opción (desactivado por defecto) en la versión 26.0 de Bitcoin Core, desplegada en diciembre de 2023. Puede activarse con la opción `v2transport=1` en el archivo de configuración.