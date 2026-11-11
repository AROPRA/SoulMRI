# -*- coding: utf-8 -*-
"""Render the case-4 workflow as a clean PNG: 4 rows, with the fit-by-example loop."""
from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1720, 810
BG = (250, 249, 246)
INK = (40, 40, 40)
MUTED = (110, 110, 110)

FONT = "C:/Windows/Fonts/msyh.ttc"
f_title = ImageFont.truetype(FONT, 26)
f_node = ImageFont.truetype(FONT, 15)
f_sub = ImageFont.truetype(FONT, 12)
f_edge = ImageFont.truetype(FONT, 12)

PAL = {
    "grey":   ((245, 245, 245), (120, 120, 120)),
    "yellow": ((255, 242, 204), (214, 182, 86)),
    "blue":   ((218, 232, 252), (108, 142, 191)),
    "orange": ((255, 230, 204), (215, 155, 0)),
    "purple": ((225, 213, 231), (150, 115, 166)),
    "green":  ((213, 232, 212), (130, 179, 102)),
    "teal":   ((212, 235, 233), (90, 155, 150)),
}

nodes = [
    ("n1", 30, 76, 170, 64, "真人聊天记录", "微信 / QQ / 截图", "grey"),
    ("n2", 240, 76, 190, 64, "够不够？", "先判，不写", "yellow"),
    ("n3", 240, 186, 190, 56, "借 case 3 取材", "记忆 + 提问，逐条标出处", "yellow"),
    ("n4", 480, 76, 180, 64, "Step 0 素材", "条数 · 跨度 · 场合", "blue"),
    ("n5", 700, 76, 190, 64, "Step 1 语言画像", "9 项，过不了全废", "blue"),
    ("n6", 930, 76, 190, 64, "Step 2 三层提问", "先给选项，再要具体事", "blue"),
    ("n7", 30, 296, 200, 64, "Step 3 回应图谱", "求助 · 说TA · 日常 · 告别", "blue"),
    ("n8", 270, 296, 180, 64, "Step 5 写", "行为说明 + 例句", "orange"),
    ("n9", 490, 296, 170, 64, "两道关", "有证据？该说？", "orange"),
    ("n10", 700, 296, 180, 64, "答案不进文件", "删掉成品答案", "orange"),
    ("n11", 920, 296, 200, 64, "两个读者分开", "说明给用户 / 人设给演员", "purple"),
    ("n12", 1160, 296, 210, 64, "开场任务书", "你是谁 · 她不在了 · 推向活人", "purple"),
    ("n13", 30, 506, 210, 64, "硬约束", "热 · 不写诗 · 无时钟 · 不说机器", "purple"),
    ("n14", 280, 506, 190, 64, "感知边界", "时间 · 天色 · 声音 · 方位", "purple"),
    ("n15", 510, 506, 180, 64, "点名活人", "一次一个，随机", "purple"),
    ("n16", 730, 506, 190, 64, "挑该测的", "按这个人、这段关系判断", "green"),
    ("n17", 960, 506, 190, 64, "长对话 10–15 轮", "单问会逼出客服腔", "green"),
    ("n18", 1190, 506, 190, 64, "数四样", "解释 · 提问 · 长度 · 越界", "green"),
    ("n19", 1420, 506, 180, 56, "交付 · 放权", "有一天不需要它", "grey"),
    ("n20", 730, 700, 190, 64, "用户改例句", "「这句应该这么说」", "teal"),
    ("n21", 1000, 700, 190, 64, "多法拟合 3–5 版", "不是改一遍，是各种方法试", "teal"),
    ("n22", 1270, 700, 190, 64, "重测同一句", "还是它自己想出来，才算", "teal"),
]
N = {n[0]: n for n in nodes}

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

def center(cx, cy, text, font, fill=INK):
    bb = d.textbbox((0, 0), text, font=font)
    d.text((cx - (bb[2]-bb[0])/2, cy - (bb[3]-bb[1])/2 - bb[1]), text, font=font, fill=fill)

def arrow(p1, p2, color=(90, 90, 90), width=2):
    d.line([p1, p2], fill=color, width=width)
    ang = math.atan2(p2[1]-p1[1], p2[0]-p1[0])
    L, A = 9, 0.42
    for s in (-1, 1):
        d.line([p2, (p2[0]-L*math.cos(ang+s*A), p2[1]-L*math.sin(ang+s*A))], fill=color, width=width)

def poly(points, color=(90, 90, 90), width=2, arrow_head=True):
    for a, b in zip(points, points[1:]):
        d.line([a, b], fill=color, width=width)
    if arrow_head and len(points) >= 2:
        arrow(points[-2], points[-1], color, width)

def label(mid, text, fill=MUTED):
    bb = d.textbbox((0, 0), text, font=f_edge)
    tw, th = bb[2]-bb[0], bb[3]-bb[1]
    d.rectangle([mid[0]-tw/2-3, mid[1]-th/2-2, mid[0]+tw/2+3, mid[1]+th/2+2], fill=BG)
    center(mid[0], mid[1], text, f_edge, fill)

def edge_mid(a, b):
    return ((R(a)[0]+L(b)[0])/2, R(a)[1]-11)

center(W/2, 26, "Case 4 · 从聊天记录到一份能聊的 echo", f_title)
center(W/2, 52, "分诊 → 取证画像 → 写台本 → 演 → 测 → 拟合", f_edge, MUTED)

for nid, x, y, w, h, title, sub, color in nodes:
    fill, stroke = PAL[color]
    d.rounded_rectangle([x, y, x+w, y+h], radius=8, fill=fill, outline=stroke, width=2)
    center(x+w/2, y+h/2 - 8, title, f_node)
    center(x+w/2, y+h/2 + 12, sub, f_sub, MUTED)

def L(nid):
    n = N[nid]; return (n[1], n[2] + n[4]/2)
def R(nid):
    n = N[nid]; return (n[1] + n[3], n[2] + n[4]/2)
def T(nid):
    n = N[nid]; return (n[1] + n[3]/2, n[2])
def B(nid):
    n = N[nid]; return (n[1] + n[3]/2, n[2] + n[4])

# row 1
for a, b in [("n1","n2"), ("n2","n4"), ("n4","n5"), ("n5","n6")]:
    arrow(R(a), L(b))
label(edge_mid("n1","n2"), "")
label(edge_mid("n2","n4"), "够")
label(edge_mid("n4","n5"), "")
label(edge_mid("n5","n6"), "过得了")

# n2 -> n3
poly([B("n2"), (T("n3")[0], T("n3")[1])])
label((T("n3")[0]+30, B("n2")[1]+15), "不够", (180, 70, 70))

# n3 -> n5 : borrow, then return to the profile
poly([R("n3"), (760, R("n3")[1]), (760, B("n5")[1])])
label((600, R("n3")[1]-11), "借完就回来")

# rows 2 and 3
for a, b in [("n7","n8"), ("n8","n9"), ("n9","n10"), ("n10","n11"), ("n11","n12"),
             ("n13","n14"), ("n14","n15"), ("n15","n16"), ("n16","n17"), ("n17","n18"), ("n18","n19")]:
    arrow(R(a), L(b))

# n6 -> n7
poly([R("n6"), (1150, R("n6")[1]), (1150, 262), (130, 262), (130, T("n7")[1])])

# n12 -> n13
poly([R("n12"), (1400, R("n12")[1]), (1400, 470), (135, 470), (135, T("n13")[1])])

# n18 -> n20 : into the fitting loop
poly([B("n18"), (1285, 620), (825, 620), (825, T("n20")[1])])
label((1055, 620), "过了才收工，不过就进环", (90, 155, 150))

arrow(R("n20"), L("n21"))
arrow(R("n21"), L("n22"))

# n22 -> n18 (short diagonal, clear of the delivery box)
poly([(T("n22")[0], T("n22")[1]), (1310, B("n18")[1] + 4)], color=(90, 155, 150))
label((1370, 640), "还不行", (90, 155, 150))

out = r"D:\DAFEIYU\SANDBOX\ABOUT BIRTH\SHIMEN\skill-soul-from-transcript\case4-flow.png"
img.save(out, "PNG")
print(out, img.size)
