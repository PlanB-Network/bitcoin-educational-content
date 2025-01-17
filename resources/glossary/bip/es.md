---
term: PIF

---
Acrónimo de "Propuesta de Mejora Bitcoin" Una Propuesta de Mejora Bitcoin (BIP) es un proceso formal para proponer y documentar mejoras y cambios en el protocolo Bitcoin y sus estándares. Dado que Bitcoin no tiene una entidad central que decida sobre las actualizaciones, las BIPs permiten a la comunidad sugerir, discutir e implementar mejoras de forma estructurada y transparente. Cada BIP detalla los objetivos de la mejora propuesta, las justificaciones, los impactos potenciales en la compatibilidad, así como las ventajas y desventajas. Los BIPs pueden ser escritos por cualquier miembro de la comunidad, pero deben ser aprobados por otros desarrolladores y los editores que mantienen la base de datos Bitcoin Core GitHub: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun y Ruben Somsen. Sin embargo, es importante entender que el papel de estas personas en la edición de los PIF no significa que controlen Bitcoin. Si alguien propone una mejora que no es aceptada dentro del marco formal del BIP, aún puede presentarla directamente a la comunidad Bitcoin o incluso crear una bifurcación que incluya su modificación. La ventaja del proceso BIP reside en su formalidad y centralización, que facilitan el debate para evitar la división entre los usuarios de Bitcoin, buscando implementar actualizaciones de forma consensuada. Al final, es el principio de mayoría económica el que determina la dinámica de poder dentro del protocolo.

Los PIF se clasifican en tres categorías principales:


- PIF de la vía estándar*: Se refieren a modificaciones que afectan directamente a las implementaciones de Bitcoin, como las reglas de validación de transacciones y bloques;
- PIF informativos*: Proporcionan información o recomendaciones sin proponer cambios directos en el protocolo;
- Proceso de los PIF*: Describir los cambios en los procedimientos en torno a Bitcoin, como los procesos de gobernanza.

Los PIF normalizados e informativos también se clasifican por "niveles":


- Capa de Consenso*: Los BIPs en esta capa conciernen a las reglas de consenso de Bitcoin, tales como modificaciones a las reglas de validación de bloques o transacciones. Estas propuestas pueden ser soft forks (modificaciones compatibles con versiones anteriores) o hard forks (modificaciones no compatibles con versiones anteriores). Por ejemplo, los BIPs para SegWit y Taproot pertenecen a esta categoría;
- Servicios de pares*: Esta capa se refiere al funcionamiento de la red de nodos Bitcoin, es decir, cómo los nodos se encuentran y se comunican entre sí en Internet.
- API/RPC*: Los BIP de esta capa se refieren a las interfaces de programación de aplicaciones (API) y las llamadas a procedimientos remotos (RPC) que permiten al software de Bitcoin interactuar con los nodos;
- Capa de aplicaciones*: Esta capa pertenece a las aplicaciones construidas sobre Bitcoin. Los BIP de esta categoría suelen tratar modificaciones a nivel de los estándares de los monederos Bitcoin.

El proceso de presentación de un BIP comienza con la conceptualización y discusión de la idea en la lista de correo *Bitcoin-dev*. Si la idea es prometedora, el autor redacta un BIP siguiendo un formato específico y lo envía a través de una Pull Request en el repositorio GitHub del Core. Los editores revisan esta propuesta para comprobar que cumple todos los criterios. El BIP debe ser técnicamente factible, beneficioso para el protocolo, cumplir con el formato requerido y estar de acuerdo con la filosofía de Bitcoin. Si el BIP cumple estas condiciones, se integra oficialmente en el repositorio GitHub de BIPs. Entonces se le asigna un número. Este número lo decide generalmente el editor, a menudo Luke Dashjr, y se asigna de forma lógica: Los BIP que tratan temas similares suelen recibir números consecutivos.

Los PIF pasan por diferentes estados a lo largo de su ciclo de vida. El estado actual se especifica en la cabecera de cada PIF:


- Borrador: La propuesta está aún en fase de redacción y debate;
- Propuesto: El PIF se considera completo y listo para su revisión por la comunidad;
- Aplazado: El campeón o un redactor dejan en suspenso el PIF para más adelante;
- Rechazado: Un PIF se clasifica como rechazado si no ha mostrado actividad durante 3 años. Su autor puede optar por reanudarlo más adelante, lo que le permitiría volver al estado de proyecto;
- Retirado: El PIF ha sido retirado por su autor;
- Final: El BIP está aceptado y ampliamente implantado en Bitcoin;
- Activo: Sólo para los PIF de proceso, este estado se asigna una vez alcanzado un determinado consenso;
- Sustituido / Obsoleto: El PIF ya no es aplicable o ha sido sustituido por una propuesta más reciente que lo hace innecesario.

![](../../dictionnaire/assets/25.webp)

> ► *BIP es el acrónimo de "Propuesta de Mejora de Bitcoin". En francés, puede traducirse como "Proposition d'amélioration de Bitcoin". Sin embargo, la mayoría de los textos franceses utilizan directamente el acrónimo "BIP" como un sustantivo común, a veces femenino, a veces masculino.*