---
term: NVERSION

---
The `nVersion` field in a Bitcoin transaction is used to indicate the version of the transaction format being used. It allows the network to distinguish between different evolutions of the transaction format over time and to apply the corresponding rules. This field has no impact on consensus rules. This means that any value assigned to this field does not result in the transaction being invalidated. However, the `nVersion` field has standardization rules that currently only accept the values of `1` and `2`. For now, this field is only useful for the activation of the `nSequence` field.