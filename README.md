# HTML Slide Builder

給定任何教材，自動生成完整的 **Reveal.js HTML 互動簡報** 並部署至 GitHub Pages。

## ✨ 特色功能
1. 🖼 **AI 背景底圖**（深暗色系霓虹風格）
2. 🎯 **扁平化圖標**（圖標總表 → PIL 裁切 → 亮度去背）
3. 💬 **即時互動元件**（Firebase Firestore 串接文字雲與單選投票）
4. 🔀 **滑桿視覺化演示**（clip-path 揭露前後對比演進）
5. 🚀 **一鍵部署**（自動部署至 GitHub Pages）

## 📁 結構
- `SKILL.md`: 核心指令與工作流程指引
- `references/reveal-template.md`: Reveal.js HTML 模板與 CSS 元件庫
- `references/firebase-config.md`: Firebase 互動元件範例
- `scripts/remove_bg.py`: PIL 圖標透明去背腳本
- `family-activity-writing/`: 實作範例（快樂的家庭活動作文句型學習單簡報）
