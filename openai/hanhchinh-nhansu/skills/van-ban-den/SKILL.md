---
name: van-ban-den
description: "Quy trình trọn gói: Tiếp nhận văn bản đến – đọc văn bản (ảnh/PDF/email), trích thông tin, đề xuất người xử lý, tính hạn, đăng ký vào sổ văn bản đến."
---

Thông tin cần có từ người dùng: [file/ảnh văn bản đến hoặc nội dung]. Thiếu thông tin quan trọng thì hỏi gọn một lần.


Tiếp nhận văn bản đến: yêu cầu của người dùng

Dùng skill `so-van-ban-di-den`:
1. Trích: cơ quan ban hành, số ký hiệu, ngày, loại, trích yếu, hạn yêu cầu trong văn bản, mức khẩn.
2. Đề xuất bộ phận xử lý theo bảng phân loại; hỏi số ngày làm việc xử lý nếu văn bản không ghi hạn.
3. Hiển thị dòng sẽ ghi vào sổ → chờ xác nhận → `dang_ky_van_ban_den`.
4. Soạn sẵn tin chuyển văn bản cho người xử lý (nháp).
