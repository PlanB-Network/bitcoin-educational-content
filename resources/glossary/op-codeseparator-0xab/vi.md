---
term: OP_CODESEPARATOR (0XAB)

definition: Mã vận hành phân đoạn một tập lệnh để cho phép các chữ ký độc lập cho mỗi phần.
---
Modifies the current output script, indicating that only the operations following this opcode will be considered in the verification of the signatures for the corresponding inputs. This allows for segmenting a complex script into multiple parts, where each segment can be signed independently.