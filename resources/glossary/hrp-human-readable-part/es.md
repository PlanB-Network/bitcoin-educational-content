---
term: Hrp (human readable part)

definition: Prefijo legible de las direcciones bech32 que permite identificar el tipo de dirección de Bitcoin.
---
La HRP (Human Readable Part) es un componente de las direcciones de recepción bech32 y bech32m (SegWit v0 y SegWit v1). La HRP se refiere a la parte de la dirección que está específicamente formateada para ser leída e interpretada fácilmente por humanos. Tomemos, por ejemplo, una dirección Bitcoin bech32:

```text
bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwfqx5
```

En esta dirección, la inicial `bc` representa el HRP. Este prefijo permite identificar rápidamente que la cadena de caracteres presentada es una dirección Bitcoin y no otra cosa.