---
term: BIP
---

Acrónimo de "Bitcoin Improvement Proposal" (Propuesta de Mejora de Bitcoin). Una Propuesta de Mejora de Bitcoin (BIP) es un proceso formal para proponer y documentar mejoras y cambios en el protocolo de Bitcoin y sus estándares. Dado que Bitcoin no tiene una entidad central que decida sobre las actualizaciones, los BIP permiten a la comunidad sugerir, discutir e implementar mejoras de manera estructurada y transparente. Cada BIP detalla los objetivos de la mejora propuesta, las justificaciones, los posibles impactos en la compatibilidad, así como las ventajas y desventajas. Los BIP pueden ser escritos por cualquier miembro de la comunidad, pero deben ser aprobados por otros desarrolladores y los editores que mantienen la base de datos de GitHub de Bitcoin Core: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun y Ruben Somsen. Sin embargo, es importante entender que el papel de estas personas en la edición de BIPs no significa que controlen Bitcoin. Si alguien propone una mejora que no es aceptada dentro del marco formal de BIP, aún pueden presentarla directamente a la comunidad de Bitcoin o incluso crear un fork que incluya su modificación. La ventaja del proceso BIP radica en su formalidad y centralización, que facilitan el debate para evitar la división entre los usuarios de Bitcoin, buscando implementar actualizaciones de manera consensuada. Al final, es el principio de mayoría económica el que determina las dinámicas de poder dentro del protocolo.

Los BIP se clasifican en tres categorías principales:
* *BIPs de Seguimiento de Estándares*: Se refieren a modificaciones que afectan directamente a las implementaciones de Bitcoin, como las reglas de validación de transacciones y bloques;
* *BIPs Informativos*: Proporcionan información o recomendaciones sin proponer cambios directos en el protocolo;
* *BIPs de Proceso*: Describen cambios en los procedimientos que rodean a Bitcoin, como los procesos de gobernanza.

Los BIPs de Seguimiento de Estándares e Informativos también se clasifican por "Capa":
* *Capa de Consenso*: Los BIPs en esta capa se refieren a las reglas de consenso de Bitcoin, como modificaciones a las reglas de validación de bloques o transacciones. Estas propuestas pueden ser bifurcaciones suaves (modificaciones compatibles con versiones anteriores) o bifurcaciones duras (modificaciones no compatibles con versiones anteriores). Por ejemplo, los BIPs para SegWit y Taproot pertenecen a esta categoría;
* *Servicios entre Pares*: Esta capa se refiere a la operación de la red de nodos de Bitcoin, es decir, cómo los nodos encuentran y se comunican entre sí en Internet.
* *API/RPC*: Los BIPs de esta capa se refieren a las Interfaces de Programación de Aplicaciones (API) y las Llamadas a Procedimientos Remotos (RPC) que permiten que el software de Bitcoin interactúe con los nodos;
* *Capa de Aplicaciones*: Esta capa pertenece a aplicaciones construidas sobre Bitcoin. Los BIPs en esta categoría suelen tratar con modificaciones a nivel de los estándares de billeteras de Bitcoin.

El proceso de presentación de un BIP comienza con la conceptualización y discusión de la idea en la lista de correo *Bitcoin-dev*. Si la idea es prometedora, el autor redacta un BIP siguiendo un formato específico y lo envía a través de un Pull Request en el repositorio de Core en GitHub. Los editores revisan esta propuesta para verificar que cumpla con todos los criterios. El BIP debe ser técnicamente factible, beneficioso para el protocolo, cumplir con el formato requerido y estar de acuerdo con la filosofía de Bitcoin. Si el BIP cumple con estas condiciones, se integra oficialmente en el repositorio de GitHub de BIPs. Luego se le asigna un número. Este número generalmente es decidido por el editor, a menudo Luke Dashjr, y se asigna de manera lógica: los BIPs que tratan temas similares a menudo reciben números consecutivos.

Los BIPs luego pasan por diferentes estados a lo largo de su ciclo de vida. El estado actual se especifica en el encabezado de cada BIP:
* Borrador: La propuesta aún está en la fase de redacción y debate;
* Propuesto: El BIP se considera completo y listo para ser revisado por la comunidad;
* Diferido: El BIP se pone en espera para más adelante por el campeón o un editor;
* Rechazado: Un BIP se clasifica como rechazado si no ha mostrado actividad durante 3 años. Su autor puede elegir reanudarlo más tarde, lo que permitiría que vuelva al estado de borrador;
* Retirado: El BIP ha sido retirado por su autor;
* Final: El BIP es aceptado y ampliamente implementado en Bitcoin;
* Activo: Solo para los BIPs de proceso, este estado se asigna una vez que se alcanza un cierto consenso;
* Reemplazado / Obsoleto: El BIP ya no es aplicable o ha sido reemplazado por una propuesta más reciente que lo hace innecesario.

![](../../dictionnaire/assets/25.png)

> ► *BIP es el acrónimo de "Bitcoin Improvement Proposal". En francés, se puede traducir como "Proposition d'amélioration de Bitcoin". Sin embargo, la mayoría de los textos en francés usan directamente el acrónimo "BIP" como un sustantivo común, a veces femenino, a veces masculino.*