---
name: lich-tuan-thu-hcns
description: Lập lịch tuân thủ và nhắc việc cả năm cho phòng Hành chính – Nhân sự doanh nghiệp Việt Nam — hạn báo cáo tình hình thay đổi lao động (trước 05/6 và 05/12, Mẫu 01/PLI qua Cổng Dịch vụ công → Sở Nội vụ), báo cáo an toàn vệ sinh lao động, quyết toán thuế TNCN (phối hợp kế toán), ngày nghỉ lễ Tết và nghỉ bù, thông báo phương án nghỉ Tết trước 30 ngày, rà hợp đồng lao động sắp hết hạn (báo trước 15 ngày), hết thử việc, xóa kỷ luật, đối thoại định kỳ, khám sức khỏe, huấn luyện ATVSLĐ, gia hạn giấy phép lao động người nước ngoài; xuất file .ics nhập Google Calendar/Outlook có nhắc trước; tạo danh sách việc tháng từ danh sách nhân viên. Dùng khi người dùng nói "lịch nộp báo cáo lao động", "tháng này HCNS phải làm gì", "nhắc hạn hợp đồng sắp hết", "lịch tuân thủ nhân sự năm 2027", "xuất lịch vào Google Calendar", "hạn báo cáo 6 tháng".
---

# Lịch tuân thủ HCNS

Đọc trước: `references/nguyen-tac-chung.md`, `references/quy-dinh-lao-dong-2026.md`.

## 1. Lịch năm
Gọi `lich_tuan_thu_hcns` (`nam`, `nghi_thu_bay`, `xuat_ics` nếu cần file):
- Nghĩa vụ pháp lý (có căn cứ + nhãn tin cậy), ngày nghỉ lễ Tết + nghỉ bù, nhắc việc nội bộ.
- Dòng lệnh: `python3 scripts/cong_cu.py lich_tuan_thu_hcns nam=2027 xuat_ics=lich-hcns-2027.ics`
- Trình bày theo tháng: `Tháng | Ngày | Việc | Loại | Căn cứ`.

## 2. Lịch theo danh sách nhân viên
Người dùng đưa file Excel/CSV (họ tên, ngày vào làm, loại HĐ, ngày hết hạn HĐ, ngày kết thúc thử việc, ngày hết hạn giấy phép lao động, ngày bị kỷ luật...) – hoặc xuất từ `~~HRM`. Tính:

| Mốc | Cách tính | Công cụ |
|---|---|---|
| Thông báo không gia hạn HĐ | Ngày hết hạn − 15 ngày (Điều 45) | `cong_ngay_lich` so_ngay=-15 |
| Quyết định ký HĐ mới khi HĐ hết hạn mà NLĐ vẫn làm | Ngày hết hạn + 30 ngày (khoản 2 Điều 20) | `cong_ngay_lich` |
| Đánh giá kết thúc thử việc | Trước ngày kết thúc thử việc 3–5 ngày làm việc | `ngay_lam_viec` |
| Xóa kỷ luật | Khiển trách +3 tháng; kéo dài nâng lương +6 tháng (Điều 126) | `cong_ngay_lich` |
| Gia hạn giấy phép lao động (người nước ngoài) | Nộp hồ sơ trước khi hết hạn theo thời hạn của nghị định hiện hành | [Cần kiểm tra số ngày] |
| Thâm niên tăng phép năm | Mỗi đủ 5 năm | `phep_nam` |
| Nâng bậc lương | Theo quy chế lương công ty | – |

Rồi gộp vào lịch bằng `su_kien_them` hoặc tạo riêng bằng `tao_file_ics`. Mặc định nhắc trước 7 và 1 ngày; hạn quan trọng nhắc thêm 14 ngày.

## 3. Danh sách việc tháng
Khi người dùng hỏi "tháng này làm gì": lọc lịch năm + mốc từ danh sách nhân viên + việc định kỳ hằng tháng (báo tăng/giảm BHXH, chấm công, tính lương phối hợp kế toán, văn bản đến chưa xử lý từ `tra_cuu_so_van_ban`). Xếp theo hạn.

## Lưu ý
- "Trước ngày 05/6" → hạn cuối là 04/6; nên nộp sớm vài ngày vì cổng dịch vụ công dễ quá tải gần hạn.
- Hạn thuế rơi vào ngày nghỉ được lùi sang ngày làm việc tiếp theo (Luật Quản lý thuế); hạn báo cáo lao động không có quy tắc này → nhắc sớm.
- Sự kiện lịch chỉ được tạo trên `~~calendar` khi người dùng xác nhận (POLICY.md); mặc định giao file .ics để người dùng tự nhập.

## Đầu ra
Lịch năm/tháng dạng bảng · file .ics · danh sách mốc theo từng nhân viên.
