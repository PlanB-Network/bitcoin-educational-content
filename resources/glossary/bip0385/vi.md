---
term: BIP0385

definition: Các hàm addr() và raw() để mô tả các tập lệnh đầu ra theo địa chỉ hoặc ở dạng thập lục phân trong các descriptor.
---
Introduces the descriptor functions `addr(ADDR)` and `raw(HEX)`. The `addr(ADDR)` function allows describing an output script using a receiving address, while the `raw(HEX)` function enables specifying an output script using a raw hexadecimal representation of that script. BIP385 was implemented along with all other descriptor-related BIPs (except BIP386) in version 0.17 of Bitcoin Core.