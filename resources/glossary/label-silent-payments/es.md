---
term: ETIQUETA (PAGOS SILENCIOSOS)

---
Dentro del protocolo de Pagos Silenciosos, las etiquetas son números enteros que se utilizan para modificar la dirección estática inicial con el fin de crear otras muchas direcciones estáticas. El uso de estas etiquetas permite segregar los pagos enviados a través de Silent Payments, empleando direcciones estáticas diferentes para cada uso, sin aumentar excesivamente la carga operativa para detectar estos pagos (escaneo). Bob utiliza una dirección estática $B$, compuesta por dos claves públicas: $B_{\text{scan}}$ para el escaneo y $B_{\text{spend}}$ para el gasto. El hash de $b_{text{scan}}$ y un entero $m$, multiplicado escalarmente por el punto generador $G$, se añade a la clave pública de gasto $B_{text{spend}}$ para crear una especie de nueva clave pública de gasto $B_m$:

$$ B_m = B_{texto{gasto}} + \text{hash}(b_{text{scan}} \text{ ‖ } m) \cdot G $$

Por ejemplo, la primera clave $B_1$ se obtiene de esta manera:

$$ B_1 = B_{\text{spend}} + \text{hash}(b_{text{scan}} \text{ ‖ } 1) \cdot G $$

La dirección estática publicada por Bob estará ahora compuesta por $B_{texto{escaneado}$ y $B_m$. Por ejemplo, la primera dirección estática con la etiqueta $1$ será:

$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$

Sólo empezamos desde la etiqueta $1$, porque la etiqueta $0$ está reservada para el cambio. Alice, que desea enviar bitcoins a la dirección estática etiquetada proporcionada por Bob, obtendrá la dirección de pago única $P_0$ utilizando el nuevo $B_1$ en lugar de $B_{text{spend}}$:

$$ P_0 = B_1 + \text{hash}(\text{inputHash} \cdot a \cdot B_{text{scan}} \text{ ‖ } 0) \cdot G $$

En realidad, es posible que Alice ni siquiera sepa que Bob tiene una dirección etiquetada, ya que simplemente utiliza la segunda parte de la dirección estática que él proporcionó, que en este caso es el valor $B_1$ en lugar de $B_{text{spend}}$. Para buscar pagos, Bob siempre utilizará el valor de su dirección estática inicial con $B_{text{spend}}$ de esta manera:

$$ P_0 = B_{{texto{gasto}} + \text{hash}(\text{inputHash} \cdot b_{text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$

A continuación, simplemente restará el valor que encuentre para $P_0$ de cada salida una a una. A continuación, comprueba si uno de los resultados de estas restas coincide con el valor de una de las etiquetas que utiliza en su monedero. Si coincide, por ejemplo, para la salida nº 4 con la etiqueta $1$, significa que esta salida es un Pago Silencioso asociado a su dirección estática etiquetada como $B_1$:

$$ Out_4 - P_0 = \text{hash}(b_{text{scan}} \text{ ‖ } 1) \cdot G $$

Esto funciona porque:

$$ B_1 = B_{\text{spend}} + \text{hash}(b_{text{scan}} \text{ ‖ } 1) \cdot G $$

Gracias a este método, Bob puede utilizar multitud de direcciones estáticas (con $B_1$, $B_2$, $B_3$...), todas ellas derivadas de su dirección estática base ($B = B_{text{scan}} \text{ ‖ } B_{text{spend}}$), con el fin de separar adecuadamente los usos.

Sin embargo, esta separación de direcciones estáticas sólo es válida desde el punto de vista de la gestión del monedero personal, pero no permite separar las identidades. Como todas tienen el mismo $B_{\text{scan}}, es muy fácil asociar todas las direcciones estáticas juntas y deducir que pertenecen a una única entidad.