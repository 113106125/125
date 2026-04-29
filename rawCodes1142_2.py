import matplotlib.pyplot as plt
import math

# --- 讀取區塊 ---
f = open("example_blast_result.txt", "r")
lines = f.readlines()
f.close()

# 索引對應
identities = [] # Index 2
lengths = []    # Index 3
q_starts = []   # Index 6
q_ends = []     # Index 7
evalues = []    # Index 10
bit_scores = [] # Index 11

for line in lines:
    if line.startswith("#"):
        continue
    
    # 檔案是 Tab 分隔 (Format 7 標準)
    row = line.strip().split("\t") 
    
    # 索引提取
    identities.append(float(row[2]))
    lengths.append(int(row[3]))
    q_starts.append(int(row[6]))
    q_ends.append(int(row[7]))
    
    # 處理 E-value 的 Log 轉換 (注意 Index 10)
    ev = float(row[10])
    log_ev = -math.log10(ev)
    evalues.append(log_ev)
    
    bit_scores.append(float(row[11]))

# --- 繪圖區塊 (四張子圖) ---
# --- 個別繪圖與存檔區塊 ---

# 圖 1: Identity 直方圖
plt.figure(1)
plt.hist(identities, bins=10, color='skyblue')
plt.title("Identity Distribution")
plt.savefig("fig1_identity.png") 
print("Saved Fig 1")

# 圖 2: 顯著性分析散佈圖
plt.figure(2)
plt.scatter(bit_scores, evalues, color='salmon')
plt.title("Significance Analysis")
plt.savefig("fig2_significance.png")
print("Saved Fig 2")

# 圖 3: 長度與一致性
plt.figure(3)
plt.scatter(lengths, identities, color='green')
plt.title("Length vs Identity")
plt.savefig("fig3_length.png")
print("Saved Fig 3")

# 圖 4: 覆蓋圖
plt.figure(4)
for i in range(len(q_starts)):
    plt.plot([q_starts[i], q_ends[i]], [i, i], lw=6)
plt.title("Coverage Map")
plt.savefig("fig4_coverage.png")
print("Saved Fig 4")

# plt.show() # 如果要一次存檔，有時會不需要 show