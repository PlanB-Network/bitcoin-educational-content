---
term: SPREAD (WST)
---

Trong phần mềm Whirlpool Stat Tool, spread là một chỉ số được sử dụng để đo lường độ đồng nhất của quá trình trộn từ góc độ của một mảnh nhất định. Có hai loại spread: tiềm năng và hồi cứu.

Spread tiềm năng được tính toán là tỷ lệ giữa anonset tiềm năng của mảnh của bạn và tổng số mảnh được tạo ra sau Tx0 của bạn. Ví dụ, nếu có 100 mảnh trong pool của bạn và mảnh của bạn có anonset là 70, thì spread tiềm năng của mảnh của bạn là 70%.

Ngược lại, spread hồi cứu là tỷ lệ giữa anonset hồi cứu của mảnh của bạn và tổng số Tx0 được tạo ra trước lần trộn cuối cùng của mảnh của bạn. Do đó, nếu anonset hồi cứu của mảnh của bạn là 95 và có 100 Tx0 trước lần trộn cuối cùng của mảnh của bạn, thì spread hồi cứu của mảnh của bạn là 95%.

Hai chỉ số này được sử dụng để đánh giá hiệu quả của việc trộn mảnh của bạn so với tiềm năng được cung cấp bởi pool. Một spread tiềm năng thấp, như 5%, chỉ ra một khoảng cách lớn cho khả năng cải thiện thông qua các lần trộn bổ sung. Ngược lại, một spread tiềm năng cao, như 97%, có nghĩa là ít anonset bổ sung có thể được thu được với các coinjoin bổ sung.

> ► *Trong tiếng Anh, "spread" có thể được dịch là "tỷ lệ lan truyền" hoặc "tỷ lệ phổ biến".*