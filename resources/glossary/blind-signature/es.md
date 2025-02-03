---
term: FIRMA CIEGA

---
Las firmas ciegas de Chaum son una forma de firma digital en la que el emisor de la firma desconoce el contenido del mensaje que está firmando. Sin embargo, la firma puede verificarse posteriormente con el mensaje original. Esta técnica fue desarrollada por el criptógrafo David Chaum en 1983.

Consideremos el ejemplo de una empresa que desea autenticar un documento confidencial, como un contrato, sin revelar su contenido. La empresa aplica un proceso de enmascaramiento que transforma criptográficamente el documento original de forma reversible. Este documento modificado se envía a una autoridad de certificación que aplica una firma ciega sin conocer el contenido subyacente. Tras recibir el documento firmado enmascarado, la empresa desenmascara la firma. El resultado es un documento original autenticado por la firma de la autoridad, sin que ésta haya visto nunca el contenido original.

Así, las firmas ciegas de Chaum permiten certificar la autenticidad de un documento sin conocer su contenido, garantizando tanto la confidencialidad de los datos del usuario como la integridad del documento firmado.

En Bitcoin, este protocolo se utiliza en sistemas de bancos chaumianos como superposición (Cashu, Fedimint, etc.), pero sobre todo en protocolos de coinjoin chaumianos, para garantizar que el coordinador no pueda vincular una entrada a una salida.