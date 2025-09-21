import os, random, shutil 

random.seed(0)

ROOT = r"datasets/pokemon-1"
src_img = os.path.join(ROOT, "train", "images")
src_lbl = os.path.join(ROOT, "train", "labels")
dst_img = os.path.join(ROOT, "val", "images")
dst_lbl = os.path.join(ROOT, "val", "labels")
os.makedirs(dst_img, exist_ok=True); os.makedirs(dst_lbl, exist_ok=True)

imgs = [f for f in os.listdir(src_img) if f.lower().endswith((".jpg",".png",".jpeg"))]
take = max(1, int(0.2* len(imgs))) # uns 20% das imagens

for f in random.sample(imgs, take):
    base = os.path.splitext(f)[0]
    shutil.move(os.path.join(src_img, f), os.path.join(dst_img, f))
    lbl = base + ".txt"
    if os.path.exists(os.path.join(src_lbl, lbl)):
        shutil.move(os.path.join(src_lbl, lbl), os.path.join(dst_lbl, lbl))

print(f"Movidas {take} imagens para val/")

