---
term: REDEEMSCRIPT

---
Un script que define las condiciones específicas que deben cumplir las entradas para desbloquear los fondos asociados a una salida P2SH. En un UTXO P2SH, la `scriptPubKey` contiene el hash del `redeemScript`. Cuando una transacción desea gastar este UTXO como entrada, debe proporcionar el `redeemScript` claro que coincida con el hash contenido en la `scriptPubKey`. El `redeemScript` se proporciona en el `scriptSig` de la entrada, junto con otros elementos necesarios para satisfacer las condiciones del script, como firmas o claves públicas. Esta estructura encapsulada garantiza que los detalles de las condiciones de gasto permanezcan ocultos hasta que los bitcoins se gasten realmente. Se utiliza especialmente para los monederos Legacy P2SH multifirma.