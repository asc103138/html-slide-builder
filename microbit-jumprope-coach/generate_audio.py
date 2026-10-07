import os
import subprocess

EDGE_TTS = "/Users/tunyuan/Library/Python/3.9/bin/edge-tts"
FFMPEG = "/opt/homebrew/bin/ffmpeg"
OUTPUT_DIR = "/Users/tunyuan/anti/html簡報/microbit-jumprope-coach/audio"

scripts = [
    (1, "各位四年級的同學們大家好，我是謝敦元老師！歡迎來到 micro:bit 八人跳繩智慧教練專題課程。今天我們將一起用程式碼與感測器，打造出全校最強的科技運動教練！"),
    (2, "在跳大繩的過程中，大家最常遇到的問題是什麼呢？請拿起平板或手機，在螢幕上的即時文字雲輸入你的觀察與困擾，我們一起來看看全班的答案！"),
    (3, "要做出聰明的智慧教練，我們需要認識 micro:bit 的四大裝備：LED 螢幕、A B 按鈕、加速度感測器，以及內建蜂鳴器。它們就像是教練的眼睛、手腳、平衡神經與嘴巴！"),
    (4, "第 1 週的任務來囉！打開 MakeCode 積木平台，我們要用循序結構，讓 micro:bit 在開機時先顯示微笑，接著滾動播放教練名稱，並順利下載到實體板子上！"),
    (5, "第 2 週我們要來做教練的內建節拍器！穩定的每分鐘 100 拍節奏是成功跳過大繩的關鍵。我們利用重複迴圈，讓蜂鳴器發出規律的嗶嗶聲，引導大家統一步伐。"),
    (6, "這一週的實作挑戰，請同學們幫教練加上起跳倒數音效。按下 A 鍵時，螢幕倒數 3、2、1，並發出起跳提示音，提醒全體隊員做好準備！"),
    (7, "micro:bit 怎麼知道繩子甩過了呢？答案就是它肚子裡的加速度感測器！透過 X、Y、Z 三個軸向的重力變化，當晃動或甩動事件發生時，就能即時觸發程式。"),
    (8, "動手試試看！裝上電池盒，拿著 micro:bit 揮動手臂，模擬甩繩動作。只要感測到晃動，螢幕就會立刻閃爍閃電圖示，確認靈敏度！"),
    (9, "第 4 週是關鍵的計數大腦！什麼是變數呢？變數就像一個貼著名稱的小盒子，開機時裡面是 0，每次甩繩成功，就把它拿出來加 1 再放回去，精準記錄次數。"),
    (10, "現在我們要將變數與按鈕整合！揮動一下數字累加 1，按下 B 鍵則能隨時將數字歸零。請大家實機下載並進行手持連續跳繩測試！"),
    (11, "進入第 5 週的避坑除錯時間！為什麼甩一下數字會狂飆好幾下？因為手臂震顫產生了機械回彈雜訊。我們只要在程式裡加上關鍵的暫停 350 毫秒冷卻時間，就能做到精準防誤判！"),
    (12, "動動腦時間！大家來投票思考一下：如果防誤判的冷卻時間設得太長，例如設成 3 秒鐘，跳繩運動會發生什麼狀況呢？請在螢幕上投下你的神聖一票！"),
    (13, "這週的進階任務是加入條件判斷 if-else！當連續跳滿 10 下時，micro:bit 就會播放勝利歡呼音效並閃爍大愛心，給全隊最高榮譽的激勵！"),
    (14, "第 6 週團隊大連線！我們利用無線電 Radio 功能，將甩繩手上的發送端與場邊裁判的接收端大看板連線，讓全場都能即時看見目前跳了幾下！"),
    (15, "雙機配對大作戰！兩人一組，一人寫發送程式、一人寫接收看板，設定相同的廣播群組頻道，拉開 5 公尺距離測試無線通訊的強大威力！"),
    (16, "第 7 週我們準備下操場實戰！在實測前，務必確實做好創客封裝：用魔鬼氈與束帶將主板和電池盒牢牢固定在握柄上，並加上防撞泡棉保護設備。"),
    (17, "全員通關！恭喜全班同學運用科技教練的精準節奏與穩定計數，成功突破 20 下零失誤的壯舉，展現出無與倫比的團隊默契！"),
    (18, "恭喜大家順利結業！從 0 基礎積木到獨立完成物聯網專題，大家都成了優秀的科技小創客。記得保持好奇心，用程式碼讓校園生活變得更有趣！")
]

os.makedirs(OUTPUT_DIR, exist_ok=True)

# 依據敦元老師男聲頻譜特性微調 (-0.8 半音使聲音更具成年男師沉穩質感)
semitones = -0.8
rate = 2 ** (semitones / 12.0)

for slide_idx, text in scripts:
    raw_mp3 = os.path.join(OUTPUT_DIR, f"temp_{slide_idx}.mp3")
    final_mp3 = os.path.join(OUTPUT_DIR, f"slide_{slide_idx:02d}.mp3")
    
    # 1. 產生高音質中文旁白
    cmd_tts = [
        EDGE_TTS,
        "--voice", "zh-TW-YunJheNeural",
        "--text", text,
        "--write-media", raw_mp3
    ]
    subprocess.run(cmd_tts, check=True)
    
    # 2. 頻譜與語調校正 (asetrate + atempo) 貼合敦元老師音質
    cmd_tune = f"{FFMPEG} -i {raw_mp3} -af asetrate=24000*{rate},atempo={1/rate} {final_mp3} -y"
    subprocess.run(cmd_tune, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if os.path.exists(raw_mp3):
        os.remove(raw_mp3)
        
    print(f"✅ Slide {slide_idx:02d} 語音導覽生成完畢 -> {final_mp3}")

print("🎉 全數 18 頁教學語音導覽生成完成！")
