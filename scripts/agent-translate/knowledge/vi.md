# Lessons — vi

## 2026-07-03
- Trong SCR403, giữ nguyên `combinator`, `jet`, `gas`, `DAG`, `buffer`, `witness`, `native` và các tên lõi như `iden`, `unit`, `comp`, `pair`, `case`, `take`, `drop`, `injl`, `injr`.
- Dùng thuật ngữ đã có trong `courses/scr403/vi.md`: `kiểu tổng`, `kiểu tích`, `kiểu đơn vị`, `hợp thành tuần tự`, `hợp thành song song`, `phân tích tĩnh`, `cấp phát bộ nhớ động`, `định lý đầy đủ`.
- Dịch `half-adder` là `bộ cộng nửa`; dịch `carry bit` là `bit nhớ`, `sum bit` là `bit tổng`.
- Keep protocol/feature identifiers in English: `Taproot`, `Tapscript`, `Simplicity`, `combinator`, `delegation`, `loop unrolling`. Glossary confirms `Taproot`/`Tapscript` are kept verbatim.
- "recursive covenant" → `khế ước đệ quy` (canonical `resources/glossary/recursive-covenant/vi.md`); the base "covenant" term itself stays English in the glossary.
- Technical verb "commit(ted into)" is kept as `commit` in vi Bitcoin prose (e.g. `được commit vào các địa chỉ Taproot`).
- Gloss dense CS jargon inline with the English kept in parentheses on first use: `điểm bất động (fixed-point)`, `tính chuẩn (standardness)`.
- "unbounded recursion/iteration" → `đệ quy/lặp không giới hạn`.
- For SCR403 Vietnamese, keep Simplicity-specific implementation terms mostly in English as the course does: `combinator`, `jet`, `Bit Machine`, `witness`, `CMR`, `key-spend`, `key-path`, `script path`; translate surrounding prose only.
- Render effect properties consistently with the course: commutative = `giao hoán`, idempotent = `lũy đẳng`, unitary = `đơn vị`.
- For adder quizzes, keep `half-adder`/`full-adder` as technical names, but translate carry/sum bits as `bit nhớ`/`bit tổng`.
- Trong tài liệu Simplicity, giữ nguyên tên hiệu ứng và primitive như `Failure`, `Reader`, `take`, `drop`, `iden`, `jet`, `witness`, `TapLeaf`, `Tapscript`; dịch phần mô tả xung quanh chúng.
- Dịch `combinator` là “tổ hợp tử”; `type system` là “hệ thống kiểu”; `unit type` là “kiểu đơn vị”; `sum/product` trong ngữ cảnh kiểu là “tổng/tích”.
- Với `recursive covenant`, dùng “khế ước đệ quy” theo glossary tiếng Việt, dù mục `covenant` độc lập giữ term là `Covenant`.
- Với thuật ngữ logic, dùng “phép tính sequent”, “tương ứng Curry-Howard”, “phép tính lambda”, “suy diễn tự nhiên”; giữ tên riêng tiếng Anh.
- Giữ `combinator`, `jet`, `witness`, `pruning`, `key-spend`, `x-only`, `batch`, `sighash`, `message digest`, `pubkey` và `cross-input signature aggregation` bằng tiếng Anh trong văn cảnh Simplicity/Bitcoin để tránh lệch thuật ngữ kỹ thuật.
- Dịch tên hiệu ứng `Failure`, `Reader`, `Writer` theo mẫu “hiệu ứng Failure/Reader/Writer”; không Việt hóa tên riêng của hiệu ứng.
- Dịch `sum type`, `product type`, `unit type`, `type inference`, `sequent calculus` lần lượt là “kiểu tổng”, “kiểu tích”, “kiểu đơn vị”, “suy luận kiểu”, “phép tính sequent”.
- Với “Commitment Merkle Root”, giữ cụm tiếng Anh và viết tắt `CMR`; khi nói khái niệm `commitment` độc lập có thể dùng “cam kết”.
