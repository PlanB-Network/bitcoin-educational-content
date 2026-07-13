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

## 2026-07-06
- Trong SOC104, giữ `libertarian`, `minarchist/minarchists`, `paleoconservative`, `laissez-faire`, `Federal Reserve` và `fiat` theo cách dùng của course vi; dịch mô tả xung quanh chúng.
- Dịch `non-aggression principle` là `nguyên tắc bất xâm phạm`; `self-ownership` là `quyền tự sở hữu`; `sound money` là `tiền lành mạnh`; `crony capitalism` là `chủ nghĩa tư bản thân hữu`.
- Với centrism, dùng `chủ nghĩa trung dung`, `kỹ trị`, `chủ nghĩa thực dụng`, `lợi ích công`, `thân doanh nghiệp` và `thân thị trường` để khớp `courses/soc104/vi.md`.
- Trong SOC104, dịch `libertarian/libertarianism` là “người/chủ nghĩa tự do cá nhân”, nhưng giữ nguyên `liberal`, `libertarian`, `libertaire`, `libertarianism` khi đoạn đang so sánh khác biệt thuật ngữ xuyên ngôn ngữ.
- Dịch `statism` là “chủ nghĩa nhà nước”; `constructivism` giữ là `constructivism` khi dùng như nhãn triết học, nhưng có thể diễn giải là “trật tự kiến tạo” trong đối lập với “trật tự tự phát”.
- Với glossary Bitcoin trong SOC104: dùng `Tiền mã hóa`, `Ngang hàng (P2P)`, `FOSS`, `Lạm phát`, `Cypherpunks`, `Mật mã học`, `Sách trắng`, `Trường phái Áo` theo frontmatter `term:` của các mục glossary vi.
- Trong SOC104, dùng `chủ nghĩa nhà nước` cho `statism` và `những người theo chủ nghĩa nhà nước` cho `statists`.
- Dùng `chủ nghĩa tự do cá nhân` cho `libertarianism/libertarians` khi cần diễn giải bằng tiếng Việt; giữ `libertarian`, `paleo-libertarian`, `neo-libertarian` và `Libertarian Party` khi chúng là nhãn trào lưu/tổ chức trong bối cảnh Mỹ.
- Dịch `spontaneous order` là `trật tự tự phát`; giữ `laissez-faire`, `New Deal`, `Great Society`, `Big Government` nguyên văn.
- Trong SOC104, giữ `libertarian`, `Cypherpunk(s)`, `mailing list`, `white paper` bằng tiếng Anh theo `courses/soc104/vi.md`; dịch các khái niệm xung quanh như `chủ nghĩa libertarian`, `triết lý libertarian`, `phong trào cypherpunk`.
- Dịch `welfare state` là `nhà nước phúc lợi`, `state money` là `tiền nhà nước`, `market money/currency` là `tiền thị trường/đồng tiền thị trường`, và `fiat money/currency` là `tiền pháp định` theo glossary.
- Dịch `constructivism/anti-constructivism` trong SOC104 là `chủ nghĩa kiến tạo`/`phản kiến tạo`; `spontaneous order` là `trật tự tự phát`.
- Trong ngữ cảnh đạo đức/libertarian của SOC104, dịch `effective property` là `quyền sở hữu hữu hiệu` và `sovereign property` là `quyền sở hữu có chủ quyền`, tránh `tài sản hữu hiệu/chủ quyền`.
- Trong SOC104, tiếp tục dịch `libertarianism` là `chủ nghĩa tự do cá nhân`; `libertarians` là `những người theo chủ nghĩa tự do cá nhân`, theo các quiz vi hiện có.
- Trong ngữ cảnh kinh tế/trợ cấp, dịch `moral hazard` là `rủi ro đạo đức`.
- Dịch `technocratic` là `mang tính kỹ trị`; `centrism/centrist` là `chủ nghĩa trung dung/người trung dung`.
- Trong SOC104, dịch `constructivism` là `chủ nghĩa kiến tạo`, `spontaneous order` là `trật tự tự phát`, và `open/closed society` là `xã hội mở/xã hội đóng`.
- Với cặp `pro-business`/`pro-market`, dùng nhất quán `thân doanh nghiệp`/`thân thị trường` theo các quiz SOC104 đã dịch.
- Trong ngữ cảnh Kant, dịch `state of minority` là `tình trạng chưa trưởng thành` thay vì nghĩa tuổi pháp lý.
- Trong SOC104, giữ nguyên `libertaire(s)` và `libertarian(s)` khi hai thuật ngữ được đối chiếu trực tiếp; tránh dịch cả hai thành “chủ nghĩa tự do” vì sẽ xóa mất sự phân biệt giữa vô chính phủ xã hội chủ nghĩa Pháp và libertarianism.
- Dịch `non-aggression principle` là “nguyên tắc bất xâm phạm”; `defensive violence` là “bạo lực phòng vệ”; `aggressive violence` là “bạo lực xâm lược”.
- Dịch `holism` trong ngữ cảnh triết học xã hội chủ nghĩa là “chủ nghĩa toàn thể”.
- Trong SOC104/Nolan, dịch `libertarianism` là `chủ nghĩa tự do cá nhân (libertarianism)` khi cần phân biệt với `classical liberalism` (`chủ nghĩa tự do cổ điển`); `statism` là `chủ nghĩa nhà nước`.
- Dịch `anarcho-capitalists` là `những người vô chính phủ tư bản` và `minarchists` là `những người theo chủ nghĩa nhà nước tối thiểu`.
- Dùng `biểu đồ Nolan` cho `Nolan diagram` và `hình thoi Nolan` cho `Nolan diamond`; `personal freedoms` là `các quyền tự do cá nhân`, `economic freedoms` là `các quyền tự do kinh tế`.
