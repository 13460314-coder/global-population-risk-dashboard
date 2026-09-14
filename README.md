# Global Population & Geopolitical Risk Dashboard

全球人口與伊朗地緣政治風險分析儀表板。

## Project Overview

本專題利用世界人口預測資料與伊朗地緣政治風險資料，建立可公開瀏覽的 RWD Dashboard。

網站內容包含：

- 2024、2030、2050、2100 世界人口預測
- 世界人口趨勢圖
- Python 資料清理與分析結果
- Iran Risk Matrix
- 事實資料與分析推論
- AI 使用與資料驗證方法

## Data Processing

使用 Python 讀取：

`data/raw.txt`

並進行人口資料整理與計算，包括：

- 平均人口
- 各期間成長率
- 2024–2100 CAGR

處理後資料輸出至：

`data/cleaned.json`

Python 程式位於：

`scripts/clean.py`

## Data Source

世界人口資料主要依據：

**United Nations — World Population Prospects 2024**

若不同 AI、新聞或網站提供不同數字，本專題優先參考聯合國官方資料，並確認年份、預測情境及資料單位是否一致。

## AI Usage Statement

本專題使用 AI 協助：

- 規劃網站架構
- 撰寫與檢查 HTML、CSS、JavaScript
- 撰寫 Python 資料處理程式
- 整理地緣政治風險因子
- 協助文字摘要
- 協助建立資料驗證流程

AI 產出的內容不直接視為事實來源，重要數據與地緣政治資訊會另外查證。

## Prompt Examples

網站製作 Prompt 範例：

> 請建立一個 Global Population & Geopolitical Risk Dashboard，包含 2024、2030、2050、2100 世界人口預測、人口圖表、Iran Risk Matrix，並區分事實資料與分析推論。網站需支援手機 RWD。

Python Prompt 範例：

> 請使用 Python 讀取人口原始資料，計算平均值、各期間成長率與 CAGR，並將結果輸出為 JSON。

## Verification Process

資料驗證流程：

1. 使用 AI 協助整理可能的資料與分析方向。
2. 將人口資料與 UN World Population Prospects 2024 官方資料比對。
3. 確認年份、資料單位及預測情境是否一致。
4. 地緣政治資料使用可靠新聞及官方資訊進行交叉確認。
5. 將「可驗證事實」與「分析推論」分開呈現。
6. 若 AI 與官方來源資料不同，以官方原始資料為主要依據。

## AI Bias and Hallucination

地緣政治議題可能受到資料時間點、媒體立場及 AI 訓練資料影響。

為降低 AI 偏誤與幻覺：

- 不直接把 AI 回答當成資料來源
- 優先查證官方或可靠來源
- 使用多個來源交叉確認
- 將事實與推論分開
- 對無法確認的資訊不視為既定事實

## Project Structure

```text
.
├── .github/
│   └── workflows/
├── data/
│   ├── raw.txt
│   └── cleaned.json
├── scripts/
│   └── clean.py
├── index.html
├── notes.md
└── README.md
