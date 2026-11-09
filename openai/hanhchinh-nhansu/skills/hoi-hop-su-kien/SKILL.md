---
name: hoi-hop-su-kien
description: Tổ chức hội họp và sự kiện nội bộ cho phòng hành chính doanh nghiệp Việt Nam — lên lịch họp (tránh ngày lễ, kiểm tra lịch trống qua Google/Outlook Calendar), chương trình họp, giấy mời, chuẩn bị tài liệu và phòng họp/link trực tuyến, biên bản họp từ ghi chú hoặc transcript (ghi đúng ý kiến, chỉ ghi kết luận đã chốt), bảng theo dõi kết luận sau họp; sự kiện nội bộ: tất niên/YEP, khai xuân, team building, du lịch hè, 8/3, 20/10, Trung thu cho con nhân viên, kỷ niệm thành lập, đại hội cổ đông thường niên (hậu cần) — kế hoạch, ngân sách, checklist hậu cần, phân công, kịch bản MC. Dùng khi người dùng nói "chuẩn bị cuộc họp", "lên lịch họp giao ban", "làm biên bản họp", "chuyển ghi chú thành biên bản", "tổ chức tất niên", "kế hoạch du lịch công ty", "kịch bản MC", "checklist sự kiện".
---

# Hội họp – sự kiện

Đọc trước: `references/nguyen-tac-chung.md`, `references/the-thuc-nd30.md`, `references/mau-hop-su-kien.md`.

## A. Cuộc họp

**1. Chốt thông tin**: mục đích (ra quyết định gì?), chủ trì, thành phần bắt buộc/mời, thời lượng, trực tiếp hay trực tuyến.

**2. Chọn thời gian**
- Kiểm tra ngày lễ, nghỉ bù: `ngay_le_tet` (năm). Ngày trước/sau Tết thường vắng người – cảnh báo.
- Có lịch (Google Calendar / Outlook): tìm khung trống chung của thành phần bắt buộc, đề xuất 2–3 phương án. **Không tự tạo sự kiện** – chỉ tạo nháp khi người dùng xác nhận (POLICY.md).
- Ngày luôn kèm thứ.

**3. Chương trình họp** (mẫu trong `references/mau-hop-su-kien.md`): mỗi mục có người trình bày, thời lượng, **quyết định cần đạt**. Họp > 60 phút không có quyết định cần đạt → gợi ý rút gọn/gửi email.

**4. Giấy mời** – skill `giay-to-hanh-chinh` (mẫu A) hoặc tin nhắn ngắn cho họp nội bộ.

**5. Tài liệu**: checklist tài liệu theo từng mục; có Drive (Google Drive / OneDrive) thì tìm file liên quan, báo người sửa cuối, ngày sửa.

**6. Biên bản** từ ghi chú/transcript:
- **Không tự thêm** kết luận, số liệu, người tham dự không có trong ghi chú. Thiếu → `[CHƯA RÕ]`.
- Ghi rõ ai nói gì; tách *ý kiến* và *kết luận của chủ trì*.
- Ghi chú không có kết luận → ghi đúng câu: "Cuộc họp chưa đưa ra kết luận về nội dung này."
- Bảng việc sau họp: `Việc | Người phụ trách | Hạn | Trạng thái`; thiếu người/hạn → `[CHƯA RÕ]`.
- Biên bản ký bởi **chủ trì và thư ký**.

**7. Theo dõi sau họp**: bảng kết luận → nhắc hạn (tính bằng `ngay_lam_viec`), soạn tin nhắc cho người phụ trách.

## B. Sự kiện nội bộ

**1. Kế hoạch** (mẫu trong references): mục tiêu, thời gian (kiểm tra lễ/âm lịch: Trung thu 15/8 âm, tất niên trước Tết – dùng `doi_lich_am_duong`), địa điểm, đối tượng, ngân sách, phân công, rủi ro.

**2. Ngân sách**: bảng `Hạng mục | ĐVT | SL | Đơn giá | Thành tiền | Ghi chú`; **không tự đặt đơn giá** – `[CẦN BÁO GIÁ]`; dự phòng 5–10% (người dùng quyết). Tổng bằng chữ: `doc_so_thanh_chu`.
Nhắc kế toán: chi phúc lợi tập thể, du lịch, quà tặng có giới hạn và điều kiện để được tính chi phí được trừ khi tính thuế TNDN; quà/tiền thưởng cho cá nhân có thể chịu thuế TNCN – chuyển bộ skill kế toán kiểm tra. [Cần kiểm tra theo luật thuế hiện hành]

**3. Checklist hậu cần** theo mốc T-30, T-14, T-7, T-1, ngày D, sau sự kiện (mẫu trong references).

**4. Kịch bản MC / chương trình chi tiết** theo phút; xưng hô phù hợp văn hóa công ty; phần phát biểu lãnh đạo, vinh danh, bốc thăm, văn nghệ.

**5. An toàn**: sự kiện đông người – PCCC, sơ cứu, an toàn đồ ăn, bảo hiểm du lịch; có rượu bia – bố trí xe đưa đón, nhắc không lái xe.

**6. Sau sự kiện**: khảo sát nhanh, quyết toán chi phí, rút kinh nghiệm.

## Đầu ra
Chương trình họp + giấy mời; biên bản + bảng việc; hoặc kế hoạch sự kiện + ngân sách + checklist + kịch bản – tùy yêu cầu.

<!-- KET-NOI:BAT-DAU (sinh tự động từ scripts/ket_noi.json – sửa ở đó rồi chạy build) -->
## Kết nối ứng dụng

Connector dùng cho skill này: **Google Calendar** · **Zoom** · **Gmail** · **Google Drive** · **Microsoft 365 (Outlook, OneDrive/SharePoint, Teams)**. Đọc quy tắc trong `references/ket-noi.md` trước khi dùng.

1. Tìm khung giờ trống của người chủ trì và thành phần dự họp trên lịch; đề xuất 2–3 khung giờ.
2. Họp trực tuyến: tạo cuộc họp Zoom (hoặc Teams) lấy link; tạo sự kiện lịch có chương trình, link, tài liệu (sau khi xác nhận).
3. Gom tài liệu họp trên Drive vào một thư mục; tạo nháp giấy mời gửi thành phần dự họp.
4. Sau họp: lấy bản ghi Zoom/Teams nếu có để làm biên bản – chỉ ghi điều có thật, không bịa kết luận; lưu biên bản vào Drive.

**Khi chưa kết nối:** làm đủ phần soạn thảo, tính toán; đưa nội dung sẵn để người dùng tự dán vào email, lịch, thư mục; nhắc **một lần** cách bật connector, không dừng việc chỉ vì chưa kết nối.
<!-- KET-NOI:KET-THUC -->
