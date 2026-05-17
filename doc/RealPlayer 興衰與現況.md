# **數位串流基礎設施的先驅與轉型：RealPlayer 及其母公司 RealNetworks 的技術演進、商業興衰與當代重塑**

## **導言：定義網際網路影音傳輸的黎明**

在當今的數位生態系統中，透過網際網路即時串流高畫質影片、隨選視訊（VOD）以及無縫的音訊廣播，已經成為全球網路使用者理所當然的日常體驗。然而，時間回溯至一九九零年代中期，全球資訊網（World Wide Web）的基礎設施仍處於極度原始的階段。當時絕大多數的使用者依賴數據機透過電話線撥接上網，主流連線速率僅有 14.4 kbps 或 28.8 kbps，這意味著下載一首僅數分鐘長的標準音訊檔案，往往需要耗費數十分鐘甚至數小時的等待時間。在這種頻寬極度受限的硬體環境下，要在網際網路上實現即時的多媒體傳輸，幾乎被視為一項不可能達成的工程挑戰。

正是在這一技術瓶頸與歷史轉折點上，RealNetworks 及其旗艦產品 RealPlayer 應運而生，成為了突破物理頻寬限制、開啟「串流媒體（Streaming Media）」時代的真正先驅 1。本研究報告旨在進行詳盡且深度的剖析，全面梳理 RealPlayer 及其母公司 RealNetworks 的前世今生。透過對其早期技術興起、獨佔市場的黃金歲月、商業策略的嚴重失誤、引發廣泛爭議的隱私與軟體膨脹問題，以及近年來公司如何透過私有化重組，將核心技術轉向人工智慧（AI）、企業級安全監控與電信防詐欺領域的完整軌跡進行檢視，本報告將揭示一家曾經壟斷全球數位媒體終端市場的科技霸主，如何因內部管理的侷限與外部技術典範的轉移而失去王座，並最終在企業對企業（B2B）的隱形基礎設施市場中尋求重生的複雜歷程。

## **第一章：串流革命的起源與 Progressive Networks 的誕生**

### **突破撥接時代的傳輸極限**

一九九四年，曾在微軟（Microsoft）任職長達十年的前高階主管 Robert (Rob) Glaser 創立了一家名為 Progressive Networks 的初創企業 2。Glaser 是一位具備前瞻性技術視野的創業者，他最初的商業願景並非單純開發軟體，而是意圖利用互動式多媒體技術，在網際網路上打造一個專注於政治與文化內容的替代性廣播管道 3。在當時，互動式電視（Interactive Television, ITV）的概念在科技圈蔚為風潮，但 Glaser 及其包含 Phil Barrett、Andy Sharpless 與 Stephen Buerkle 在內的創業團隊迅速意識到，與其等待龐大且昂貴的有線電視基礎設施升級，不如從根本上改變網際網路的資料傳輸與播放架構 3。

由於影像傳輸所需的頻寬在當時的技術條件下難以克服，Glaser 決定先從音訊領域著手 5。一九九五年四月三日，Progressive Networks 推出了一項具備破壞性創新的技術產品——RealAudio 1.0 以及其專屬的 RealAudio Player 6。這項技術的核心在於將音訊檔案高度壓縮，並透過網路封包將資料連續不斷地傳送至客戶端，客戶端的播放器在接收到初始封包後即可開始播放，而無需等待整個檔案下載完畢 1。這徹底解決了窄頻時代的播放延遲問題，也是現代串流媒體技術的最早商業化實踐之一 9。

| 早期串流媒體技術對比（1995年前後） | 檔案格式擴展名 | 技術特徵與歷史地位 |
| :---- | :---- | :---- |
| **RealAudio** | .ra,.ram | 由 Progressive Networks 於 1995 年推出，專為低頻寬優化，首創穩定的純音訊即時串流機制 7。 |
| **VivoActive** | .viv | 1995 年推出，採用高度壓縮的專有影像與音訊編解碼器，提供極低畫質但能於早期網路運作的影像串流，現已淘汰 10。 |
| **StreamWorks** | 無固定 | 由 Xing 公司開發，支援基於 MPEG 工具套件的音訊與影像串流，為早期競爭者之一 9。 |
| **Microsoft Tiger** | 無固定 | 微軟早期的影像伺服器技術開發代號，透過將資料切割儲存以利傳輸，為後續 Windows Media 的前身 9。 |

一九九五年九月五日，Progressive Networks 完成了一項歷史性的創舉，他們透過 RealAudio 系統，在網際網路上實現了史上首次體育賽事的即時全球轉播 11。該場賽事為西雅圖水手隊（Seattle Mariners）以六比五擊敗紐約洋基隊（New York Yankees）的美國職棒大聯盟（MLB）比賽 12。儘管受限於頻寬，當時的音質被認為仍不如傳統的無線電廣播，且初期僅能容納數百名聽眾同時連線，但這一事件正式向全球展示了網際網路作為即時媒體傳輸平台的巨大潛力，標誌著串流產業的正式啟動 12。

### **RealNetworks 與 RealPlayer 霸權的確立**

隨著技術的成熟，公司於一九九七年二月推出了名為 RealVideo 的專有影像壓縮格式，該格式最初基於 H.263 標準開發，隨後轉向完全專有的編解碼技術 14。為了提供使用者一體化的媒體播放體驗，早期的 RealAudio Player 被重新命名為 RealPlayer，成為網際網路上首批能夠同時且流暢處理音訊與影像串流的跨平台媒體播放器 1。一九九七年九月，為了迎接口即將到來的首次公開募股（IPO），Progressive Networks 正式更名為 RealNetworks 3。同年十月，公司成功在納斯達克掛牌上市（代號：RNWK），獲得了資本市場的熱烈追捧 3。

RealNetworks 的成功並非僅靠單一軟體，而是建立在強大的底層技術架構與廣泛的業界結盟之上。在技術層面，該公司與網景（Netscape）等企業共同參與制定了即時串流協定（Real-Time Streaming Protocol, RTSP），這項協定至今仍被廣泛應用於多數的安全監控攝影機中 15。在商業策略上，Rob Glaser 帶領公司與其他科技巨頭建立了深度的戰略夥伴關係，例如與微軟合作確保 RealPlayer 與 RealSystem 在 Windows 95 及 Windows NT 環境下的無縫運作，同時也與昇陽電腦（Sun Microsystems）等硬體製造商結盟，確保伺服器端的相容性 4。

這些精準的戰略佈局帶來了使用者基數的爆炸性成長。一九九八年，RealNetworks 影音軟體的註冊使用者達到二千二百萬人；而到了網際網路泡沫達到頂峰的二零零零年，其註冊使用者數量更是飆升至驚人的二億一千五百萬人 11。在那個年代，RealPlayer 實質上成為了每一台個人電腦連接網際網路時不可或缺的基礎配備，確立了其在數位媒體播放市場的絕對壟斷地位。

## **第二章：壓縮極限與亞洲市場的統治者——RMVB 格式的興衰**

在探討 RealPlayer 的歷史軌跡時，其引以為傲的專有媒體封裝與壓縮技術，特別是 RealMedia（.rm）及其衍生格式 RMVB（RealMedia Variable Bitrate），佔據了極其特殊的歷史地位。這項技術不僅展現了 RealNetworks 在編解碼領域的深厚功力，更在亞洲市場形成了長達十年的非對稱性統治，最終又因商業策略的僵化而走向衰亡 14。

### **可變位元率帶來的畫質革命**

二零零三年，RealNetworks 正式推出了 RMVB 格式 10。在 RMVB 誕生之前，標準的 RealMedia 容器主要採用固定位元率（Constant Bitrate, CBR）進行編碼，這對於穩定傳輸線上串流雖然有利，但對於本機儲存的高畫質影片而言，卻會導致檔案過大或畫質受損 16。RMVB 的核心技術突破在於導入了可變位元率（Variable Bitrate, VBR）編碼技術，其底層壓縮邏輯與後來普及的 MPEG-4 Part 10（即 H.264，如 x264 編碼器）有相似之處 16。

透過 VBR 技術，編解碼器能夠根據影片畫面的動態複雜度智能地分配資料流量。在處理相對靜止的畫面（如人物對話、靜態風景）時，系統會大幅降低位元率以節省儲存空間；而在處理劇烈運動、爆炸等高動態畫面時，系統則會瞬間提高位元率以確保畫面的清晰度與細節完整性 10。這種優化使得 RMVB 能夠以極小的檔案體積（約每分鐘 5 至 8 MB）提供顯著優於早期 MP4 和 MPEG 格式的畫質 10。

### **亞洲市場的特殊文化現象與統治地位**

RMVB 的技術特性完美契合了二零零零年代初期亞洲市場的特殊網路環境與文化需求。當時，亞洲地區（特別是中國大陸）的寬頻普及率與連線速率遠遠落後於歐美先進國家，然而網民對於盜版電影、日本動畫（Anime）以及歐美電視劇的消費需求卻呈現井噴式的爆發 17。

在這樣的歷史背景下，大量由網民自發組成的「字幕組」成為了海外影視資源在中國傳播的核心樞紐。這些字幕組在獲取高畫質片源（如早期的 AVI 格式）並進行翻譯後，為了適應當時狹窄的網路頻寬，預設將帶有內嵌中文字幕的影片重新壓製成 RMVB 格式，再透過 BitTorrent、eDonkey 及 Gnutella 等點對點（P2P）檔案分享平台進行廣泛散播 16。

因此，RMVB 在亞洲幾乎成為了數位影音、特別是盜版影視資源的代名詞。對於當時的消費者而言，「體積小、有字幕、播放器能播」成為了 RMVB 深入人心的三大理由 20。這種極端的普及度甚至逆向影響了硬體產業，使得當時在中國市場銷售的智慧型電視與多媒體播放盒，都必須宣稱內建支援 RM 甚至 RMVB 格式的硬體解碼，否則便無法在市場上立足 18。

### **商業授權引發的反噬與技術淘汰**

然而，RMVB 的統治地位並未持續到高畫質（HD）時代，其急速的衰弱與最終的消失，深刻揭示了封閉型專有技術在面臨開放標準挑戰時的脆弱性，以及不當商業決策所帶來的毀滅性後果。

RMVB 在亞洲之所以能夠如此普及，很大程度上得益於其早期編解碼器的免費使用特性，以及對盜版生態的被動默許 18。然而，當 RMVB 的市場佔有率達到頂峰，且亞洲地區智慧型電視與網路機上盒市場迎來爆發期時，RealNetworks 的決策層卻選擇了一條短視的變現路徑。這家依靠免費格式起家的公司，組建了龐大的法務團隊，開始向硬體製造商（如早期的中國品牌微鯨、暴風等）以及未經授權支援 RMVB 的第三方播放平台徵收高昂的專利授權費 18。

這一竭澤而漁的策略引發了硬體終端廠商的強烈反彈。包括小米在內的各大主流家電與機上盒品牌，為了避開高昂的權利金，在隨後的韌體與軟體更新中，迅速且徹底地移除了對 RM 及 RMVB 檔案的官方支援 18。儘管部分客服人員私下仍會提供外掛程式供使用者安裝，但從官方層面而言，RMVB 已實質上遭到硬體市場的遺棄 18。

與此同時，全球寬頻與光纖網路基礎設施的快速升級，使得 RMVB 主打的「極小檔案體積」優勢不再具備決定性的吸引力 10。使用者開始追求 720p 甚至 1080p 的高畫質觀影體驗。在技術演進上，H.264 編碼技術與開放原始碼封裝格式 MKV 的成熟，提供了畫質更優異且不受單一公司版權綁架的替代方案 19。MKV 格式強大的外掛字幕支援功能，更直接擊中了亞洲字幕組必須將字幕「硬烙印」在 RMVB 影片上導致畫質劣化的痛點，促使字幕組紛紛放棄 RMVB 轉向 MKV 封裝 20。

此外，在 Linux 和 Unix 平台上，開源社群透過逆向工程將 RMVB 的解碼邏輯整合進 FFmpeg 專案中，使得 MPlayer、xine、Totem 以及跨平台的 VLC media player 等開源播放器，皆能在不依賴官方 RealPlayer 的情況下流暢播放 RMVB 檔案 16。這進一步瓦解了 RealNetworks 對該格式的絕對控制權，最終使 RMVB 成為歷史的陳跡 21。

## **第三章：衰亡的根源——隱私風暴、惡意軟體化與領導力危機**

儘管 RealPlayer 在千禧年初期佔據了統治地位，但其隨後的急劇衰退並非僅僅是因為單一技術的落後或寬頻普及率的改變。深究其因，這是一場由一系列災難性的管理決策、對終端使用者體驗的極度蔑視，以及錯失關鍵歷史機遇所共同構成的系統性崩潰。

### **一九九九年的 GUID 隱私醜聞：信任的首次破裂**

RealPlayer 品牌聲譽下滑的歷史起點，可以精確地追溯至一九九九年爆發的嚴重隱私追蹤醜聞 22。這不僅是公司歷史上的污點，更是早期網際網路產業在缺乏監管環境下，軟體開發商濫用使用者數據的典型案例。

一九九九年底，獨立資訊安全顧問 Richard Smith 在針對 RealNetworks 旗下的音樂管理軟體 RealJukebox 進行程式碼與封包分析時，揭露了一項驚人的事實：該軟體在使用者完全不知情的情況下，秘密為每一位安裝該軟體的使用者分配了一個「全球唯一識別碼」（Global Unique Identifier, GUID） 22。更嚴重的是，軟體不僅追蹤使用者的音樂收聽習慣與播放清單，還會將這些極具個人色彩的行為數據與該 GUID 進行綁定，並透過網路秘密回傳至 RealNetworks 的伺服器 22。

這項發現立刻引發了全美輿論的譁然與隱私權倡議團體的強烈抗議。RealNetworks 隨即面臨了巨大的法律風險與多起集體訴訟。其中，一名名為 Jeffrey Wilens 的使用者在加州高等法院提起了一項高達五億美元的集體訴訟，指控公司的行為違反了該州的不公平商業競爭法；另一名由律師 Jonathan Shub 代表的賓夕法尼亞州使用者，則在聯邦地方法院提起了另一項集體訴訟，控告 RealNetworks 違反了《聯邦電腦欺詐和濫用法》（Computer Fraud and Abuse Act）以及多項州級的隱私保護法案 23。

為了平息這場公關與法律災難，RealNetworks 的營運長 Tom Frank 雖然對外宣稱這些訴訟「毫無根據」，且公司未曾將這些識別碼與任何使用者的真實個人身分直接連結，但公司仍被迫迅速發布了針對 RealJukebox 和 RealPlayer 7 的修補程式，將這些追蹤識別碼全部以零取代 23。儘管在法律層面達成了妥協，但這場風暴徹底破壞了廣大使用者對該品牌的信任基礎，也為其後續被視為「流氓軟體」埋下了伏筆 22。

### **商業模式的異化：被正式標記為「惡意軟體」（Badware）**

隨著技術典範的轉移，Adobe Systems 推出的 Flash 技術在網頁內嵌式影音播放市場迅速崛起，而微軟也將功能日益完善的 Windows Media Player 深度整合進其佔據絕對統治地位的 Windows 作業系統中 25。面臨核心功能逐漸被邊緣化的危機，RealNetworks 未能透過優化核心產品體驗來留住使用者，反而選擇了一條極端榨取剩餘價值的短視道路——採取極度干擾使用者的「膨脹軟體」（Bloatware）與廣告軟體（Adware）策略 25。

這種惡劣的商業實踐在二零零八年受到了權威機構的公開譴責。由哈佛大學法學院伯克曼網際網路與社會中心（Berkman Center for Internet & Society at Harvard Law School）主導的非營利消費者保護組織 StopBadware.org，正式將 RealPlayer 10.5 與當時最新的 RealPlayer 11 標記為「惡意軟體」（Badware） 28。

StopBadware 的報告深入剖析了 RealPlayer 嚴重損害消費者權益的具體行徑。針對 RealPlayer 10.5，報告指出其在終端使用者授權合約（EULA）中使用了極具欺騙性的字眼，將一個純粹用於推送廣告的綑綁軟體包裝為「訊息中心」（Message Center），並在文件中謊稱其功能是為了提供有用的軟體更新 28。當使用者在安裝過程中選擇不向 RealNetworks 註冊個人資訊時，這個廣告推送機制會被預設為強制啟動狀態 28。

針對 RealPlayer 11，問題則更為嚴重。報告指出其安裝程式具備高度的欺騙性，會在使用者不知情且未獲同意的情況下，秘密在電腦底層安裝名為 "Rhapsody Player Engine" 的第三方應用程式 28。更令人詬病的是，當使用者察覺系統變慢而嘗試解除安裝 RealPlayer 時，其解除安裝程式並不會同步移除 Rhapsody Player Engine，且整個過程中從未揭露 RealNetworks 與該綑綁軟體之間的關聯 28。

StopBadware.org 的經理 Maxim Weinstein 對此嚴厲批評：「軟體開發商有責任清晰且毫無歧義地告知使用者將會在他們的電腦上安裝什麼軟體及其具體作用。RealNetworks 剝奪了使用者對其電腦如何被使用的知情選擇權。」 28。

這種強制侵入系統列、頻繁彈出廣告、改變瀏覽器預設設定的行徑，使得 RealPlayer 成為了當年廣大電腦使用者的夢魘。軟體過度消耗系統資源導致的性能低下，使得著名的「正在緩衝...」（BUFFERING...）延遲提示符號，成為了該軟體最為人所詬病的文化代名詞 25。這使得即使其具備一定的技術價值，使用者依然極度厭惡並急於將其從系統中移除 24。

### **領導力危機與錯失的歷史級商業機遇**

RealNetworks 的衰亡除了產品層面的失誤，更深層次的原因在於高階管理層的戰略短視。多數產業觀察家與前高階主管將矛頭指向了創辦人暨執行長 Rob Glaser 25。儘管 Glaser 被公認是一位極具前瞻性的科技先驅，他在早期就準確預見了網路影音與數位音樂的巨大潛力，但他被評斷為一位「更像願景家而非稱職執行長」的領導者 25。

Glaser 的管理風格被前員工形容為過於專橫、好鬥，且極度以自我為中心。他專注於推行自己的願景，卻拒絕傾聽下屬的反饋，並且在多個不同的市場策略之間搖擺不定，導致公司始終無法將資源集中在單一領域做到極致 25。

這種管理缺陷導致 RealNetworks 完美地錯失了其原本應該主導的三次重大歷史機遇：

1. **數位音樂的敗退：** 在數位音樂革命初期，RealNetworks 推出了音樂管理軟體 RealJukebox 與訂閱服務 Rhapsody。然而，由於產品過度臃腫、缺乏與硬體設備的無縫整合，加上隱私醜聞的打擊，最終將這個利潤豐厚的市場拱手讓給了推出 iPod 與 iTunes 簡潔生態系的蘋果公司（Apple） 25。到了二零零九年，Rhapsody 遭遇了嚴重的訂戶流失，單年度流失超過十二萬五千名訂戶，最終不得不被計畫分拆以減輕母公司的財務負擔 25。  
2. **線上影音平台的缺席：** 作為串流影像技術的發明者，RealNetworks 理應成為 Web 2.0 時代影音分享的霸主。然而，他們固守必須下載龐大客戶端軟體的舊思維，忽視了網頁內嵌即開即用的便利性，最終敗給了採用輕量化 Flash 技術的 YouTube 25。  
3. **隨選視訊（VOD）的錯失：** RealNetworks 曾推出名為 SuperPass 的影音隨選訂閱服務，但受限於在內容版權談判上的弱勢，以及未能把握從短片向長篇影集轉型的契機，最終無法與後來崛起的 Netflix 相提並論 25。更糟的是，隨著與 Comcast 合作關係的終止，RealNetworks 的網路廣播訂戶瞬間蒸發了一百一十萬人，僅殘存七萬五千人，徹底退出了主流內容服務市場 25。

## **第四章：法律泥淖中的掙扎——微軟反壟斷案與 RealDVD 的滑鐵盧**

在市場份額不斷被競爭對手蠶食的同時，RealNetworks 試圖利用法律訴訟作為商業競爭的延續。在此過程中，公司經歷了兩場結果截然不同的重大法律戰役：一場為公司帶來了數億美元的無謂意外之財，另一場則由於高層的災難性誤判，給予了公司致命的財務與聲譽打擊。

### **徒勞的勝利：與微軟的世紀反壟斷和解**

早在千禧年初期，隨著微軟將 Windows Media Player 深度綑綁進 Windows 作業系統，RealPlayer 的市佔率受到了毀滅性的衝擊。二零零三年十二月，RealNetworks 正式對微軟提起反壟斷訴訟 26。RealNetworks 指控微軟濫用其在個人電腦作業系統市場的絕對壟斷地位，故意隱瞞或保留關鍵的應用程式介面（API）等技術資訊，阻礙 RealNetworks 開發與系統高度相容的軟體 26。同時，訴狀也指控微軟利用市場力量，迫使電腦硬體製造商（OEM）簽署偏袒 Windows Media Player 而排斥 RealNetworks 產品的授權協議 26。

這場訴訟在經歷了漫長的司法程序與歐洲委員會的介入後，於二零零五年十月迎來了震驚業界的世紀大和解 30。微軟為了終結這項重大反壟斷指控，同意向 RealNetworks 支付總額高達七億六千一百萬美元的天價補償 26。這筆和解金的結構包含：四億六千萬美元的直接現金賠償，以及三億美元的長期合作承諾，用於在微軟的龐大受眾群中推廣 RealNetworks 的音樂訂閱服務與休閒遊戲業務 25。此外，雙方達成協議，微軟將進一步開放 Windows 媒體介面，增強 Windows Media 系統與 RealNetworks 的 Helix 數位版權管理（DRM）系統之間的互通性，確保雙方技術能相互相容 31。

然而，這場在法庭上的輝煌勝利，卻成為了 RealNetworks 商業營運無能的最終證明。手握超過七億美元的現金與微軟的推廣承諾，RealNetworks 本應擁有足夠的資源進行徹底的轉型與產品創新。但正如產業分析師所指出的，在 Rob Glaser 混亂的領導下，這筆龐大的資金未被投入到任何能夠激起消費者熱情的新產品研發中，反而在公司龐雜、缺乏焦點的多頭馬車營運體系中被白白消耗殆盡 25。

### **逆流而動的災難：RealDVD 的全盤潰敗**

如果說與微軟的和解凸顯了創新能力的喪失，那麼 RealDVD 專案則是一場由高層強行推動、完全逆轉時代潮流的災難性戰略誤判。

二零零八年，當整個科技產業的共識已明確轉向雲端運算與高畫質網路串流（Netflix 已於前一年推出線上串流服務）時，Rob Glaser 卻執意進軍即將沒落的實體光碟備份市場 25。RealNetworks 投入巨資開發了一款名為 "RealDVD" 的軟體，其主要功能是讓使用者能夠將實體 DVD 的內容完美複製並備份至電腦硬碟中 33。配合這項軟體，公司甚至計畫推出一款名為 "Facet" 的硬體播放器，該設備售價約三百美元，可內建儲存約七十部經過複製的數位電影 25。

這一產品直接觸碰了美國電影協會（MPAA）和好萊塢六大傳統片商的核心底線。二零零八年九月，MPAA 迅速針對 RealNetworks 發起版權侵權訴訟 35。MPAA 的核心法律依據在於，RealDVD 軟體的運作機制必須繞過或破壞 DVD 內建的防拷貝加密技術（CSS），這公然違反了美國《數位千禧年版權法》（Digital Millennium Copyright Act, DMCA）中嚴禁開發旨在規避反盜版保護措施之產品的條款 34。

在法庭上，RealNetworks 試圖將此案定調為捍衛消費者權益的聖戰 35。其律師團隊辯稱，消費者既然擁有將合法購買的音樂 CD 擷取至電腦的權利，自然也應享有備份合法購買的實體 DVD 的「合理使用」（Fair Use）權利，並堅稱其軟體並未真正「破解」加密，而是在安全環境下進行轉存 33。

然而，主審此案的聯邦地方法院法官 Marilyn Hall Patel（她正是當年做出關閉著名 P2P 軟體 Napster 歷史性判決的法官）並未被 RealNetworks 的說辭說服 33。在多場被臨時要求封閉以保護商業機密的聽證會中，MPAA 傳喚的安全專家當庭證實，RealDVD 的複製控制機制極其脆弱，只需修改一行程式碼，甚至透過 Real 伺服器的遠端更新，就能輕易解除所有的拷貝限制 34。更致命的是，在交叉詰問中，Rob Glaser 本人被迫承認，使用者確實可以利用 RealDVD 將從影音店「租賃」來的 DVD 製作成未經授權的永久副本 34。這徹底證實了電影製片廠最深層的恐懼——該軟體將促成一個「租借、拷貝、歸還（rent, rip, and return）」的龐大灰色產業鏈 37。

面臨全面敗訴的必然結局，RealNetworks 於二零一零年初選擇全面投降 25。根據雙方達成的永久禁制令與和解協議，RealNetworks 必須立刻停止銷售 RealDVD 及任何類似的產品，徹底終止 Facet 硬體計畫，並被迫全額承擔 MPAA 高達四百五十萬美元的訴訟費用 25。

| 重大法律訴訟事件 | 發生年份 | 核心爭議 | 最終結果與影響 |
| :---- | :---- | :---- | :---- |
| **微軟反壟斷訴訟** | 2003-2005 | 控告微軟綑綁 WMP、隱藏 API 違反競爭。 | 微軟支付 7.61億美元（含 4.6億現金與行銷推廣）；Real 未能妥善利用此資金轉型 25。 |
| **MPAA 版權侵權訴訟** | 2008-2010 | MPAA 指控 RealDVD 繞過加密技術違反《數位千禧年版權法》（DMCA）。 | RealNetworks 全面敗訴，停止開發 RealDVD 與 Facet 硬體，並賠償 MPAA 450萬美元法務費，錯失戰略轉型時機 25。 |

這場法律戰役對 RealNetworks 造成的打擊是毀滅性的。連同龐大的研發成本與法務費用，公司在這項逆勢而為的計畫上蒸發了超過一千萬美元，更為致命的是，他們在這個過程中錯失了投入數位影像串流與行動設備廣告市場的寶貴黃金期 25。

## **第五章：擁抱開源的遲來嘗試——Helix 專案的侷限**

在商業市場與法律戰場雙雙失利的背景下，RealNetworks 曾試圖透過效仿 Mozilla 的開源策略，來延續其底層技術的生命力與影響力。公司啟動了「Helix Community」計畫，這是一個開放的協同開發平台，旨在推廣及擴展 Helix DNA 平台 38。

Helix 專案的架構主要由三個核心組件構成：

1. **Helix DNA Client：** 作為跨平台、多格式媒體播放的底層核心引擎 38。  
2. **Helix Player：** 構建於 Helix DNA Client 之上，專為 Linux、Solaris、Symbian 以及 FreeBSD 等非 Windows/Mac 作業系統開發的開源媒體播放器，這也是後續 RealPlayer Linux 版本的底層基礎 6。  
3. **Helix DNA Producer 與 Server：** 分別用於將媒體檔案編碼壓縮，以及在伺服器端將檔案透過網路串流輸出 38。

在支援格式方面，開源版本的 Helix Player 支援 Ogg Vorbis 音訊、Ogg Theora 影像以及 AVI 格式，並支援 RTSP、RTP 等多種通訊協定，同時在後期的更新中（如第 11 版）加入了對 Alsa 音效驅動與環繞聲的支援 6。

然而，Helix 專案在開源社群中的影響力始終極其有限，最終仍難逃被官方中止的命運 38。其失敗的核心在於 RealNetworks 始終無法真正放棄對核心利潤的控制。儘管 Helix DNA Client 和 Helix Player 以廣泛被接受的 GNU 通用公共授權條款（GPL）發布，但其最具商業價值的核心資產——RDT（Real Data Transport）傳輸協定，以及 RealAudio 與 RealVideo 編解碼器——依然被嚴格限制在專有的二進位商業授權（Helix DNA Technology Binary Research Use License）之下 38。這種「半開源」的態度引起了自由軟體社群的強烈不信任。

與此同時，開源界更傾向於支持完全沒有專利包袱且真正自由的 VLC media player 或 MPlayer 等播放軟體。這些軟體透過集結全球開發者的力量，利用逆向工程技術完美解碼了包括 RMVB 在內的幾乎所有專有格式，這從根本上瓦解了 Helix Player 作為官方 Linux 播放器的存在必要性，也宣告了 RealNetworks 在開源領域的戰略失敗 16。

## **第六章：企業重組與面向 B2B 基礎設施的現代轉型（2020-2026）**

進入二零二零年代，曾經擁有數億終端使用者的 RealNetworks 已經完全褪去了早期網際網路巨頭的光環。早在二零一四年，公司的淨營收已大幅萎縮，陷入嚴重的虧損狀態，員工總數也縮減至一千人左右 3。到了二零二二年，面臨可能因股價低迷而遭那斯達克（NASDAQ）強制下市的嚴峻危機，創辦人 Rob Glaser 最終推動了一項決定性的合併協議，將公司徹底私有化，讓 RealNetworks 退出了公開市場的嚴苛審視 42。

在私有化之後的重組陣痛期，RealNetworks 進行了根本性的戰略大轉移，將公司僅存的技術資產從競爭激烈的消費者終端（B2C）市場，全面轉移至高門檻的企業級解決方案（B2B）與人工智慧（AI）領域。

### **殘存的消費者遺產：AI 重塑的 RealPlayer 25**

時至今日（以二零二五年及二零二六年為基準），RealPlayer 這一經典品牌依然存在，並已演進至第 25 版 22。然而，其市場定位已經發生了天翻地覆的變化。當代的 RealPlayer 已經徹底放棄了成為「全能型通用媒體播放器」的野心，不再與 YouTube、Netflix 等主流內容平台進行正面競爭，而是巧妙地轉型為這些龐大生態系周邊的「利基型輔助工具」 22。

現代版的 RealPlayer（區分為免費版、Downloader Express、Plus 等付費階層）主打的核心功能，高度聚焦於網路影片的擷取與管理 45。其主要技術特色包括：

1. **高解析度智慧下載（Smart Download）：** 允許使用者透過一鍵操作，從 YouTube、TikTok、Facebook、Instagram 及 Vimeo 等數千個網站，直接下載最高達 8K 解析度的影片。使用者還可自行選擇下載格式，或僅提取 MP3/M4A 音訊，甚至支援切換多語系音軌 44。  
2. **深度平台整合：** 允許使用者直接在軟體內登入 YouTube 帳戶，無縫存取並下載其私有清單、稍後觀看（Watch Later）及已按讚的影片，並支援頻道訂閱的自動下載更新 44。  
3. **AI 驅動的資產管理：** 利用人工智慧自動識別影片中的人物特徵，實現基於人臉識別的影片分類與檢索功能，大幅簡化了海量個人媒體庫的整理工作 46。  
4. **無縫投放與跨裝置同步：** 支援 Chromecast 技術，能將個人電腦或 RealPlayer Mobile 手機端上的內容直接投放至大型電視螢幕，並同步雲端下載內容，結合劇院級的「PLAY NOW」全螢幕播放模式，優化觀影體驗 44。

儘管 RealPlayer 仍維持著一定的活躍度與付費使用者群，但其所能貢獻的營收已無法支撐一家現代科技公司的龐大研發體系。在現今的 RealNetworks 業務版圖中，它更多是作為公司技術傳承的一種象徵性存在 22。

### **從媒體處理到企業級安全：SAFR 電腦視覺平台**

RealNetworks 成功轉型的最關鍵一步，是將其在數位影音處理上積累了超過三十年的核心底層技術，轉化為在人工智慧與電腦視覺領域的重量級產品——SAFR (Secure, Accurate, Facial Recognition) 15。

SAFR 是一個專為企業環境打造的統一臉部識別與電腦視覺生態系統，深度整合了門禁控制、邊緣運算攝影機、行動解決方案以及實體存取控制/影片管理系統（PACS/VMS） 15。為了洗刷過去在 RealPlayer 時代因侵犯隱私而臭名昭著的歷史包袱，SAFR 在架構設計上極度強調「隱私優先」與「演算法準確性」 15。

SAFR 平台的技術優勢在於其專有演算法專為應對「現實環境中的人臉」（faces in the wild，如光線昏暗、遮擋、側臉等複雜情境）而進行訓練，並具備低於 100 毫秒的極速辨識能力 15。根據美國國家標準與技術研究院（NIST）的權威測試，SAFR 的演算法不僅展現出 99.87% 的卓越準確度，更在減少種族與性別偏見（Low bias）的指標上名列前茅，提供了比其他生物辨識解決方案更多元的隱私保護選項 15。

為展現對該業務的絕對信心，創辦人 Rob Glaser 於二零二零年親自斥資一千萬美元，透過私募方式購入公司優先股，專門用於注資 SAFR 的研發與市場拓展 2。二零二四年十月，公司任命 Charisse Jacques 為 SAFR 新任總裁；緊接著在二零二五年四月二十二日，SAFR 迎來了重大的產品里程碑，正式推出了「SAFR Guard」 49。這是一款具備顛覆性的 AI 解決方案，專門針對日益嚴重的實體零售犯罪問題而設計，旨在幫助零售商防範竊盜並同時提升合法顧客的購物體驗，標誌著 RealNetworks 已經徹底在 B2B 實體安全控制與智慧監控市場站穩了腳步 49。

### **KONTXT 平台的崛起與 TransUnion 的歷史性併購 (2026)**

除了視覺領域的 SAFR，RealNetworks 在轉型期間孕育出的最具商業爆發力的資產，體現在其電信與行動網路防護業務上。二零一七年，公司推出了名為 KONTXT 的平台，這是一個建立在自然語言處理與機器學習技術上的通訊基礎設施，最初的業務邏輯是協助全球的電信營運商對龐雜的簡訊流量進行精準的分類與優先順序排列 53。

隨著全球自動語音推銷電話（Robocalls）與電信詐騙問題的日益猖獗，RealNetworks 於二零二一年進一步推出了 KONTXT Voice，專注於利用 AI 即時偵測並在營運商網路層直接攔截這些惡意語音與簡訊 53。鑑於知名市調機構 Jupiter Research 的報告指出，二零二五年全球因行動電話詐騙所造成的經濟損失已高達八百億美元，KONTXT 的這項防詐欺核心技術，迅速引起了尋求強化其安全防護矩陣的企業的高度關注 53。

這項技術最終促成了 RealNetworks 近年來最重要的資本運作。二零二六年二月二日，全球知名的跨國資訊與信用評級巨頭環聯資訊（TransUnion, NYSE: TRU）宣布，已與 RealNetworks 達成最終協議，將收購其旗下的整個行動通訊部門（即包含 KONTXT 平台及其配套的 Metcalf 基礎設施） 49。這項以現金支付的戰略性交易，最終於 **二零二六年四月一日** 宣告正式完成 49。

| 當代核心事業板塊與產品矩陣（截至 2026 年） | 業務性質 | 主要技術應用與產品定位 | 當前營運狀態 |
| :---- | :---- | :---- | :---- |
| **RealPlayer (v25)** | B2C 消費級軟體 | 支援 8K 影片下載、AI 人物分類檢索、跨裝置雲端影音串流與投放 44。 | 作為象徵性產品持續更新，已徹底轉型為利基型的網路影音下載與管理輔助工具 22。 |
| **SAFR / SAFR Guard** | B2B 企業級安全控制 | AI 電腦視覺、NIST 認證高精度即時臉部識別、實體出入控制與邊緣運算整合 15。 | 處於高速增長階段，2025 年 4 月進軍防範零售犯罪與智慧監控市場 49。 |
| **KONTXT (原行動部門)** | B2B 電信通訊基礎設施 | 透過 AI 與自然語言處理進行語音/簡訊分類，防禦惡意機器人呼叫與跨國電信詐欺 53。 | **歷史性轉折：該部門已於 2026 年 4 月 1 日正式被環聯資訊（TransUnion）全面收購** 57。 |
| **GameHouse** | B2C 休閒遊戲發行 | 專注於面向女性受眾的手機遊戲與休閒遊戲發行業務 49。 | 作為 RealNetworks 重組後剩餘投資組合的一部分，維持獨立營運 54。 |

透過這次高達數億規模的併購案，TransUnion 能夠將 KONTXT 先進的 AI 簡訊多媒體分析與語音防詐欺技術，深度整合進其龐大且複雜的消費者信用及設備風險（Device Risk）預防體系中，旨在為企業與消費者之間日漸失控的行動通訊渠道重建信任的橋樑 53。

對於 RealNetworks 而言，剝離行動部門不僅為這家私有化公司帶回了極為可觀的現金流動性，在歷史意義上，更象徵著 Rob Glaser 所帶領的工程團隊，已正式從早期與微軟、蘋果爭奪終端消費者眼球的媒體播放器霸主，徹底蛻變為深具底層技術底蘊、服務於企業與跨國機構的隱形基礎設施提供商 57。

## **結論：科技浪潮中的興衰啟示錄**

回顧 RealPlayer 與 RealNetworks 長達三十二年的歷史軌跡，宛如閱讀一部生動且殘酷的全球科技產業盛衰史。作為串流媒體技術無庸置疑的奠基者，Rob Glaser 帶領其技術團隊在網路基礎設施極度貧乏的窄頻年代，突破物理極限，創造了音訊與影像即時傳輸的歷史奇蹟，開啟了人類數位生活的新紀元。

然而，技術的先發優勢與早期的市場壟斷，並未能轉化為長盛不衰的商業帝國。分析其衰弱的深層邏輯，為當代科技企業留下了極具價值的歷史教訓。首先，任何違背終端使用者體驗與基本商業倫理的變現手段，終將遭到市場的嚴厲反噬。一九九九年的 GUID 隱私追蹤醜聞，以及後續將軟體異化為強迫推送廣告的「惡意軟體」策略，為了追求短期的營收數字，徹底犧牲了核心軟體的流暢度與安全性，直接將無數忠實使用者推向了 iTunes 和 Flash 等體驗更佳的競爭對手。

其次，封閉專有系統在開放標準面前存在著絕對的極限。RMVB 格式曾經憑藉技術優勢統治了龐大的亞洲市場，但公司高層試圖利用這種市場支配地位向硬體終端強行收費的貪婪舉動，反而加速了 H.264、MKV 等開放標準與開源播放器的普及，最終導致其引以為傲的技術資產被市場無情淘汰。再者，企業發展最忌諱缺乏明確的戰略聚焦。儘管在與微軟的反壟斷訴訟中獲得了高達七億多美元的資本挹注，RealNetworks 卻在休閒遊戲、甚至逆流而動的硬體備份（RealDVD）等毫無前景的專案上浪費了轉型的黃金窗口，完美錯失了行動互聯網、雲端運算與串流訂閱制帶來的龐大時代紅利。

但值得深思的是，RealNetworks 並未如許多早期的互聯網先驅（例如 Netscape 或 AOL）那般徹底灰飛煙滅。進入二零二零年代中期，透過果斷的私有化退市，並大刀闊斧地進行從 B2C 向 B2B 的戰略轉移，這家老牌科技公司展現出了驚人的組織韌性。二零二六年 TransUnion 對其行動防詐欺部門的歷史性收購，以及 SAFR 臉部識別平台在實體安全與零售防盜市場的持續擴張，強烈證明了這家公司在影像壓縮與資料分析領域所累積的核心演算法架構，依然具備著龐大且真實的商業價值。

綜上所述，今日的 RealNetworks 已不再是那個統治全球個人電腦桌面的媒體播放器霸主，而是隱身於幕後，在人工智慧、企業級安全防護與電信通訊領域默默運作的底層技術引擎。RealPlayer 曾經的王座傳奇雖然早已落幕，但其在一九九五年所開創的「串流」概念，如今早已化為當今數位世界不可或缺的基礎血液，這或許正是一家科技先驅企業所能留下的，最深遠且不朽的歷史遺產。

#### **引用的著作**

1. RealNetworks CEO Rob Glaser on the History of Streaming Media, 檢索日期：5月 17, 2026， [https://blog.real.com/realnetworks-ceo-rob-glaser-on-the-history-of-streaming-media/](https://blog.real.com/realnetworks-ceo-rob-glaser-on-the-history-of-streaming-media/)  
2. Rob Glaser \- Wikipedia, 檢索日期：5月 17, 2026， [https://en.wikipedia.org/wiki/Rob\_Glaser](https://en.wikipedia.org/wiki/Rob_Glaser)  
3. RealNetworks \- Wikipedia, 檢索日期：5月 17, 2026， [https://en.wikipedia.org/wiki/RealNetworks](https://en.wikipedia.org/wiki/RealNetworks)  
4. RealNetworks \- Suresh Kotha, 檢索日期：5月 17, 2026， [https://sureshkotha.wordpress.com/wp-content/uploads/2018/05/realnetworks1.pdf](https://sureshkotha.wordpress.com/wp-content/uploads/2018/05/realnetworks1.pdf)  
5. Internet Radio History: The Real Networks Years \- Radio Survivor, 檢索日期：5月 17, 2026， [https://www.radiosurvivor.com/2018/12/internet-radio-history-the-real-networks-years/](https://www.radiosurvivor.com/2018/12/internet-radio-history-the-real-networks-years/)  
6. RealPlayer \- Wikipedia, 檢索日期：5月 17, 2026， [https://en.wikipedia.org/wiki/RealPlayer](https://en.wikipedia.org/wiki/RealPlayer)  
7. RealAudio \- Wikipedia, 檢索日期：5月 17, 2026， [https://en.wikipedia.org/wiki/RealAudio](https://en.wikipedia.org/wiki/RealAudio)  
8. The RealAudio Player, developed by RealNetworks, was introduced April 3rd, 1995\. It was a groundbreaking innovation, allowing users to stream audio over the internet for the first time. : r/90s \- Reddit, 檢索日期：5月 17, 2026， [https://www.reddit.com/r/90s/comments/1jqjo6z/the\_realaudio\_player\_developed\_by\_realnetworks/](https://www.reddit.com/r/90s/comments/1jqjo6z/the_realaudio_player_developed_by_realnetworks/)  
9. The Early History Of The Streaming Media Industry and The Battle Between Microsoft & Real, 檢索日期：5月 17, 2026， [https://www.streamingmediablog.com/2016/03/history-of-the-streaming-media-industry.html](https://www.streamingmediablog.com/2016/03/history-of-the-streaming-media-industry.html)  
10. Video File Formats: Finding the Best Video Format For You \- Vodpod, 檢索日期：5月 17, 2026， [https://www.vodpod.com/video/file-formats/](https://www.vodpod.com/video/file-formats/)  
11. History of RealNetworks, Inc. – FundingUniverse, 檢索日期：5月 17, 2026， [https://www.fundinguniverse.com/company-histories/realnetworks-inc-history/](https://www.fundinguniverse.com/company-histories/realnetworks-inc-history/)  
12. Realnetworks | 25 years of streaming, 檢索日期：5月 17, 2026， [https://25yearsofstreaming.com/](https://25yearsofstreaming.com/)  
13. 1995: The Beginning of Internet Baseball Broadcasts, 檢索日期：5月 17, 2026， [https://miscbaseball.wordpress.com/2012/09/10/1995-the-beginning-of-internet-baseball-broadcasts/](https://miscbaseball.wordpress.com/2012/09/10/1995-the-beginning-of-internet-baseball-broadcasts/)  
14. RealVideo \- Wikipedia, 檢索日期：5月 17, 2026， [https://en.wikipedia.org/wiki/RealVideo](https://en.wikipedia.org/wiki/RealVideo)  
15. SAFR Biometric Access Control / Unified Facial Recognition Ecosystem, 檢索日期：5月 17, 2026， [https://safr.com/](https://safr.com/)  
16. RMVB \- Wikipedia, 檢索日期：5月 17, 2026， [https://en.wikipedia.org/wiki/RMVB](https://en.wikipedia.org/wiki/RMVB)  
17. What Is a RMVB File and How to Recover Deleted RMVB \- Disk Drill, 檢索日期：5月 17, 2026， [https://www.cleverfiles.com/howto/recover-deleted-rmvb.html](https://www.cleverfiles.com/howto/recover-deleted-rmvb.html)  
18. Why Did the RMVB Format Disappear? The Simple Reason \- szyunze, 檢索日期：5月 17, 2026， [https://www.szyunze.com/why-did-the-rmvb-format-disappear-the-simple-reason/](https://www.szyunze.com/why-did-the-rmvb-format-disappear-the-simple-reason/)  
19. Why is MKV so popular? : r/DataHoarder \- Reddit, 檢索日期：5月 17, 2026， [https://www.reddit.com/r/DataHoarder/comments/115hpba/why\_is\_mkv\_so\_popular/](https://www.reddit.com/r/DataHoarder/comments/115hpba/why_is_mkv_so_popular/)  
20. \[轉載\] 本該被淘汰的RM及RMVB \- 數碼廣播 \- HKEPC, 檢索日期：5月 17, 2026， [https://www.hkepc.com/forum/viewthread.php?fid=116\&tid=1618923\&page=1](https://www.hkepc.com/forum/viewthread.php?fid=116&tid=1618923&page=1)  
21. RMVB已死MP3也要淘汰？谈近年离我们远去的技术-太平洋电脑网 \- 软件, 檢索日期：5月 17, 2026， [https://pcedu.pconline.com.cn/868/8687800\_all.html](https://pcedu.pconline.com.cn/868/8687800_all.html)  
22. Remember RealPlayer? The iconic '90s media player you thought was dead \- MakeUseOf, 檢索日期：5月 17, 2026， [https://www.makeuseof.com/realplayer-iconic-90s-media-player-was-dead/](https://www.makeuseof.com/realplayer-iconic-90s-media-player-was-dead/)  
23. RealNetworks faced with second privacy suit \- CNET, 檢索日期：5月 17, 2026， [https://www.cnet.com/tech/tech-industry/realnetworks-faced-with-second-privacy-suit/](https://www.cnet.com/tech/tech-industry/realnetworks-faced-with-second-privacy-suit/)  
24. Realnetworks Realplayer in 1999 was sued for what is common practice today \- Reddit, 檢索日期：5月 17, 2026， [https://www.reddit.com/r/privacy/comments/4i00se/realnetworks\_realplayer\_in\_1999\_was\_sued\_for\_what/](https://www.reddit.com/r/privacy/comments/4i00se/realnetworks_realplayer_in_1999_was_sued_for_what/)  
25. RealNetworks: A tale of opportunities missed \- CNET, 檢索日期：5月 17, 2026， [https://www.cnet.com/culture/realnetworks-a-tale-of-opportunities-missed/](https://www.cnet.com/culture/realnetworks-a-tale-of-opportunities-missed/)  
26. Real deal ends Microsoft's US legal battle \- The Guardian, 檢索日期：5月 17, 2026， [https://www.theguardian.com/technology/2005/oct/12/news.microsoft](https://www.theguardian.com/technology/2005/oct/12/news.microsoft)  
27. 'Potential virus' warning when downloading or updating RealPlayer \- SUPPORT, 檢索日期：5月 17, 2026， [https://customer.real.com/hc/en-us/articles/204040343--Potential-virus-warning-when-downloading-or-updating-RealPlayer](https://customer.real.com/hc/en-us/articles/204040343--Potential-virus-warning-when-downloading-or-updating-RealPlayer)  
28. StopBadware.org Labels RealPlayer Software as Badware ..., 檢索日期：5月 17, 2026， [https://cyber.harvard.edu/newsroom/Stopbadware\_Labels\_RealPlayer\_Software\_as\_Badware](https://cyber.harvard.edu/newsroom/Stopbadware_Labels_RealPlayer_Software_as_Badware)  
29. StopBadware finds RealPlayer serving up more than audio/video \- iTnews, 檢索日期：5月 17, 2026， [https://www.itnews.com.au/news/stopbadware-finds-realplayer-serving-up-more-than-audio-video-102643](https://www.itnews.com.au/news/stopbadware-finds-realplayer-serving-up-more-than-audio-video-102643)  
30. RealNetworks in Settling "Antitrust Case of Century" with Microsoft \- Cleary Gottlieb, 檢索日期：5月 17, 2026， [https://www.clearygottlieb.com/news-and-insights/news-listing/realnetworks-in-settling-antitrust-case-of-century-with-microsoft55](https://www.clearygottlieb.com/news-and-insights/news-listing/realnetworks-in-settling-antitrust-case-of-century-with-microsoft55)  
31. Microsoft, Real Settle Antitrust Lawsuit \- Los Angeles Times, 檢索日期：5月 17, 2026， [https://www.latimes.com/archives/la-xpm-2005-oct-12-fi-micro12-story.html](https://www.latimes.com/archives/la-xpm-2005-oct-12-fi-micro12-story.html)  
32. Microsoft and RealNetworks Resolve Antitrust Case and Announce Digital Music and Games Partnership \- Source, 檢索日期：5月 17, 2026， [https://news.microsoft.com/source/2005/10/11/microsoft-and-realnetworks-resolve-antitrust-case-and-announce-digital-music-and-games-partnership/](https://news.microsoft.com/source/2005/10/11/microsoft-and-realnetworks-resolve-antitrust-case-and-announce-digital-music-and-games-partnership/)  
33. RealNetworks surrenders in RealDVD case \- CNET, 檢索日期：5月 17, 2026， [https://www.cnet.com/culture/realnetworks-surrenders-in-realdvd-case/](https://www.cnet.com/culture/realnetworks-surrenders-in-realdvd-case/)  
34. Week in review: RealDVD takes the stand \- CNET, 檢索日期：5月 17, 2026， [https://www.cnet.com/tech/services-and-software/week-in-review-realdvd-takes-the-stand/](https://www.cnet.com/tech/services-and-software/week-in-review-realdvd-takes-the-stand/)  
35. RealNetworks appeals to public in RealDVD fight \- CNET, 檢索日期：5月 17, 2026， [https://www.cnet.com/tech/services-and-software/realnetworks-appeals-to-public-in-realdvd-fight/](https://www.cnet.com/tech/services-and-software/realnetworks-appeals-to-public-in-realdvd-fight/)  
36. RealDVD case centers on copy questions \- CNET, 檢索日期：5月 17, 2026， [https://www.cnet.com/tech/services-and-software/realdvd-case-centers-on-copy-questions/](https://www.cnet.com/tech/services-and-software/realdvd-case-centers-on-copy-questions/)  
37. MPAA to request injunction against RealDVD \- CNET, 檢索日期：5月 17, 2026， [https://www.cnet.com/tech/services-and-software/mpaa-to-request-injunction-against-realdvd/](https://www.cnet.com/tech/services-and-software/mpaa-to-request-injunction-against-realdvd/)  
38. Helix (multimedia project) \- Wikipedia, 檢索日期：5月 17, 2026， [https://en.wikipedia.org/wiki/Helix\_(multimedia\_project)](https://en.wikipedia.org/wiki/Helix_\(multimedia_project\))  
39. Helix \- Debian Wiki, 檢索日期：5月 17, 2026， [https://wiki.debian.org/Helix](https://wiki.debian.org/Helix)  
40. Realplayer and Helix Player 11 for Linux, 檢索日期：5月 17, 2026， [http://www.linux-magazine.com/Online/News/Realplayer-and-Helix-Player-11-for-Linux](http://www.linux-magazine.com/Online/News/Realplayer-and-Helix-Player-11-for-Linux)  
41. Open Source Licenses \- SUPPORT \- RealPlayer, 檢索日期：5月 17, 2026， [https://customer.real.com/hc/en-us/articles/204043733-Open-Source-Licenses](https://customer.real.com/hc/en-us/articles/204043733-Open-Source-Licenses)  
42. RealNetworks and Founder, Chairman and CEO Rob Glaser Announce Definitive Merger Agreement, 檢索日期：5月 17, 2026， [https://realnetworks.com/press/releases/2022/realnetworks-and-founder-chairman-and-ceo-rob-glaser-announce-definitive-merger](https://realnetworks.com/press/releases/2022/realnetworks-and-founder-chairman-and-ceo-rob-glaser-announce-definitive-merger)  
43. Facing NASDAQ delisting, RealNetworks CEO Rob Glaser makes bid to take company private \- GeekWire, 檢索日期：5月 17, 2026， [https://www.geekwire.com/2022/facing-nasdaq-delisting-realnetworks-ceo-rob-glaser-makes-bid-to-take-company-private/](https://www.geekwire.com/2022/facing-nasdaq-delisting-realnetworks-ceo-rob-glaser-makes-bid-to-take-company-private/)  
44. Home to the video player and downloader, RealPlayer from RealNetworks, 檢索日期：5月 17, 2026， [https://www.real.com/](https://www.real.com/)  
45. Installing RealPlayer 25 \- SUPPORT, 檢索日期：5月 17, 2026， [https://customer.real.com/hc/en-us/articles/8504428306587-Installing-RealPlayer-25](https://customer.real.com/hc/en-us/articles/8504428306587-Installing-RealPlayer-25)  
46. RealPlayer® PC features, 檢索日期：5月 17, 2026， [https://www.real.com/realplayer](https://www.real.com/realplayer)  
47. Where are my paid features? \- SUPPORT \- RealPlayer, 檢索日期：5月 17, 2026， [https://customer.real.com/hc/en-us/articles/8504529913499-Where-are-my-paid-features](https://customer.real.com/hc/en-us/articles/8504529913499-Where-are-my-paid-features)  
48. Installing RealPlayer 22 \- SUPPORT, 檢索日期：5月 17, 2026， [https://customer.real.com/hc/en-us/articles/26977777292059-Installing-RealPlayer-22](https://customer.real.com/hc/en-us/articles/26977777292059-Installing-RealPlayer-22)  
49. RealNetworks |, 檢索日期：5月 17, 2026， [https://realnetworks.com/](https://realnetworks.com/)  
50. SAFR Launches SAFR Guard – A Game Changing AI-based Solution to Prevent Retail Crime and Improve the Shopping Experience | RealNetworks, 檢索日期：5月 17, 2026， [https://realnetworks.com/press/releases/2025/safr-launches-safr-guard-%E2%80%93-game-changing-ai-based-solution-prevent-retail-crime](https://realnetworks.com/press/releases/2025/safr-launches-safr-guard-%E2%80%93-game-changing-ai-based-solution-prevent-retail-crime)  
51. RealNetworks CEO Rob Glaser to Invest $10 Million into the Company, 檢索日期：5月 17, 2026， [https://realnetworks.com/press/releases/2020/realnetworks-ceo-rob-glaser-invest-10-million-company](https://realnetworks.com/press/releases/2020/realnetworks-ceo-rob-glaser-invest-10-million-company)  
52. 2025 Press Releases \- RealNetworks |, 檢索日期：5月 17, 2026， [https://realnetworks.com/press/releases/2025](https://realnetworks.com/press/releases/2025)  
53. TransUnion's Real Networks Deal Focuses on Robocall Blocking \- Dark Reading, 檢索日期：5月 17, 2026， [https://www.darkreading.com/cyber-risk/transunion-s-real-networks-deal-focuses-on-robocall-blocking](https://www.darkreading.com/cyber-risk/transunion-s-real-networks-deal-focuses-on-robocall-blocking)  
54. TransUnion Announces Definitive Agreement to Acquire Mobile Division of RealNetworks to Enhance Voice and Messaging Solutions, 檢索日期：5月 17, 2026， [https://newsroom.transunion.com/transunion-announces-definitive-agreement-to-acquire-mobile-division-of-realnetworks-to-enhance-voice-and-messaging-solutions/](https://newsroom.transunion.com/transunion-announces-definitive-agreement-to-acquire-mobile-division-of-realnetworks-to-enhance-voice-and-messaging-solutions/)  
55. TransUnion looks to bring trust back to mobile communications channels | MarTech, 檢索日期：5月 17, 2026， [https://martech.org/transunion-looks-to-bring-trust-back-to-mobile-communications-channels/](https://martech.org/transunion-looks-to-bring-trust-back-to-mobile-communications-channels/)  
56. TransUnion Announces Definitive Agreement to Acquire Mobile Division of RealNetworks to Enhance Voice and Messaging Solutions, 檢索日期：5月 17, 2026， [https://realnetworks.com/press/releases/2026/transunion-announces-definitive-agreement-acquire-mobile-division-realnetworks](https://realnetworks.com/press/releases/2026/transunion-announces-definitive-agreement-acquire-mobile-division-realnetworks)  
57. TransUnion Completes Acquisition of the Mobile Division of RealNetworks, 檢索日期：5月 17, 2026， [https://newsroom.transunion.com/transunion-completes-acquisition-of-the-mobile-division-of-realnetworks/](https://newsroom.transunion.com/transunion-completes-acquisition-of-the-mobile-division-of-realnetworks/)  
58. TransUnion Completes Acquisition of the Mobile Division of RealNetworks \- GlobeNewswire, 檢索日期：5月 17, 2026， [https://www.globenewswire.com/news-release/2026/04/01/3266981/0/en/transunion-completes-acquisition-of-the-mobile-division-of-realnetworks.html](https://www.globenewswire.com/news-release/2026/04/01/3266981/0/en/transunion-completes-acquisition-of-the-mobile-division-of-realnetworks.html)  
59. TransUnion Completes Acquisition of the Mobile Division of RealNetworks, 檢索日期：5月 17, 2026， [https://realnetworks.com/press/releases/2026/transunion-completes-acquisition-mobile-division-realnetworks](https://realnetworks.com/press/releases/2026/transunion-completes-acquisition-mobile-division-realnetworks)  
60. TransUnion Completes Acquisition of the Mobile Division of RealNetworks | BIIA.com, 檢索日期：5月 17, 2026， [https://www.biia.com/transunion-completes-acquisition-of-the-mobile-division-of-realnetworks/](https://www.biia.com/transunion-completes-acquisition-of-the-mobile-division-of-realnetworks/)