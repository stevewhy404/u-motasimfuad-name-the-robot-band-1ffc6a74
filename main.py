import os

LINE = "The Roombas — hit single 'Dust in the Wind (And Under the Sofa)'."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/tmp/smoke-robotband-1")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
