---
term: FIRMA CIEGA
---

Las firmas ciegas de Chaum son una forma de firma digital donde el emisor de la firma no conoce el contenido del mensaje que está firmando. Sin embargo, la firma puede ser verificada posteriormente con el mensaje original. Esta técnica fue desarrollada por el criptógrafo David Chaum en 1983.

Considera el ejemplo de una empresa que desea autenticar un documento confidencial, como un contrato, sin revelar su contenido. La empresa aplica un proceso de enmascaramiento que transforma criptográficamente el documento original de manera reversible. Este documento modificado se envía a una autoridad de certificación que aplica una firma ciega sin conocer el contenido subyacente. Después de recibir el documento firmado y enmascarado, la empresa desenmascara la firma. El resultado es un documento original autenticado por la firma de la autoridad, sin que la autoridad haya visto nunca el contenido original.

Así, las firmas ciegas de Chaum permiten la certificación de la autenticidad de un documento sin conocer su contenido, asegurando tanto la confidencialidad de los datos del usuario como la integridad del documento firmado.

En Bitcoin, este protocolo se utiliza en sistemas de bancos Chaumianos como una capa adicional (Cashu, Fedimint, etc.), pero especialmente en protocolos de coinjoin Chaumianos, para asegurar que el coordinador no pueda vincular una entrada con una salida.