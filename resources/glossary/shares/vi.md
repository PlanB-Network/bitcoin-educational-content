---
term: SHARES
---

Trong bối cảnh của các hồ bơi khai thác (mining pools), một "share" là chỉ số được sử dụng để định lượng đóng góp của từng thợ mỏ cá nhân trong hồ bơi. Thước đo này phục vụ như cơ sở để tính toán phần thưởng mà hồ bơi phân phối lại cho mỗi thợ mỏ. Mỗi share tương ứng với một hash thỏa mãn một mục tiêu khó khăn thấp hơn so với mạng Bitcoin.

Để giải thích bằng một phép ẩn dụ, hãy xem xét một con xúc xắc 20 mặt. Trên Bitcoin, giả sử rằng bằng chứng công việc yêu cầu tung một số nhỏ hơn 3 để xác nhận một khối (tức là, đạt được kết quả 1 hoặc 2). Bây giờ, hãy tưởng tượng rằng trong một hồ bơi khai thác, mục tiêu khó khăn cho một share được đặt ở mức 10. Do đó, đối với một thợ mỏ cá nhân trong hồ bơi, mỗi lần tung xúc xắc mà kết quả nhỏ hơn 10 được tính là một share hợp lệ. Những share này sau đó được thợ mỏ truyền đến hồ bơi, để yêu cầu phần thưởng của họ, ngay cả khi chúng không tương ứng với một kết quả hợp lệ cho một khối trên Bitcoin.

Đối với mỗi hash được tính toán, một thợ mỏ cá nhân trong hồ bơi có thể gặp phải ba kịch bản khác nhau:
* Nếu giá trị hash lớn hơn hoặc bằng mục tiêu khó khăn được hồ bơi đặt cho một share, thì hash này không có ích. Thợ mỏ sau đó thay đổi nonce của họ để thử một hash mới: `hash > share > block`.
* Nếu hash nhỏ hơn mục tiêu khó khăn của share, nhưng lớn hơn hoặc bằng mục tiêu khó khăn của Bitcoin, thì hash này tạo thành một share hợp lệ, tuy nhiên, không đủ để xác nhận một khối. Thợ mỏ có thể gửi hash này cho hồ bơi của họ để yêu cầu phần thưởng liên quan đến share: `share > hash > block`.
* Nếu hash nhỏ hơn mục tiêu khó khăn của mạng Bitcoin, nó được coi là cả một share hợp lệ và một khối hợp lệ. Thợ mỏ truyền hash này cho hồ bơi của họ, mà vội vàng phát sóng nó trên mạng Bitcoin. Hash này cũng được tính là một share hợp lệ cho thợ mỏ: `share > block > hash`.

![](../../dictionnaire/assets/32.png)

Hệ thống share này được sử dụng để ước lượng công việc được thực hiện bởi mỗi thợ mỏ cá nhân trong hồ bơi, mà không cần phải tính toán lại từng hash được tạo ra bởi một thợ mỏ, điều này sẽ hoàn toàn không hiệu quả cho hồ bơi.

Các hồ bơi khai thác điều chỉnh độ khó của shares để cân bằng tải xác minh và đảm bảo rằng mỗi thợ mỏ, dù nhỏ hay lớn, đều gửi shares xấp xỉ mỗi vài giây. Điều này cho phép tính toán chính xác hashrate của mỗi thợ mỏ và phân phối phần thưởng theo phương pháp tính toán bồi thường được chọn (PPS, PPLNS, TIDES...).

> ► *Trong tiếng Pháp, "shares" có thể được dịch là "part".*