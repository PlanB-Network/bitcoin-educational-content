---
term: BIP72
---

Completa BIP70 y BIP71 definiendo la extensión del URI de Bitcoin (BIP21) con un parámetro adicional `r`. Este parámetro permite incluir un enlace a una solicitud de pago segura firmada por el certificado SSL del comerciante. Cuando un cliente hace clic en este URI extendido, su cartera contacta al servidor del comerciante para solicitar los detalles del pago. Estos detalles se llenan automáticamente en la interfaz de transacción de la cartera, y al cliente se le puede informar que está pagando al propietario del dominio correspondiente al certificado de firma (por ejemplo, "pandul.fr"). Dado que esta mejora está agrupada con BIP70, nunca ha sido ampliamente adoptada.