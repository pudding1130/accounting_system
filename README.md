# accounting_system
## 動機
市面上雖然有諸多記帳系統可供選擇，然而現成軟體有以下缺點：
 - 雖功能強大但無法客製化，無法滿足特定情境
 - 隱私、個資問題(資料必須上雲)

## 客製化給自己(?)的記帳系統
預計包含以下功能：
1. 使用者管理：
   - 個別使用者有自己的帳號，預設密碼為`None`但可透過(`.pwd_set()`)自行設定密碼
   - 已設定過密碼的使用者，重設密碼需要事先驗證(待開發)
2. 歷史帳目資料查詢：
   - 使用者擁有自己的資料檔(以csv儲存)，登入時將自動載入歷史紀錄，並告知使用者資料筆數及最後儲存時間
   - 透過`.history`查閱歷史紀錄
   - 已設定密碼的使用者，自動將資料檔加密(待開發)
3. 外幣匯率轉換：
   - 透過外部API查詢當日匯率，紀錄當筆外幣交易等值的台幣金額，目前支援美金(USD)、韓元(KRW)、日幣(JPY)的轉換
   - 增加外幣選項(待開發)
   - 增加虛擬貨幣選項(??)(待開發)
   - 提供使用者自行設定匯率(待開發)
4. 不同帳戶間互動紀錄(待開發)：
   - 以帳戶為單位，開發不同帳戶間的互轉功能
   - 開立子帳戶功能，讓使用者可以用現金、不同銀行帳號做區分
5. 盡量有互動式介面：
   - 雖然目前是以終端機執行，但希望透過回傳的文字讓使用者有互動的感覺(..以及防呆)
  
## 未來目標
1. 讓程式更加簡潔
2. 將csv檔放入local資料庫或上雲(串google sheet API自動更新?)
3. 圖像化使用者介面(GUI)
4. local server建置
5. 視覺化圖表：日報表、月報表、支出與收入分析
