from axiom.slca.grid import SLCAGrid, SLCAConfig
import random

def run(size=6, steps=50, seed=42):
    random.seed(seed)
    grid = SLCAGrid(SLCAConfig(size=size))
    for t in range(steps):
        I_coh = [[0.1 if (i==size//2 and j==size//2) else 0.0 for j in range(size)] for i in range(size)]
        I_con = [[0.08 if (i+j+t)%7==0 else 0.0 for j in range(size)] for i in range(size)]
        grid.step(I_coh, I_con)
        if t % 10 == 0:
            print(f"[t={t:02d}] decision={grid.decision()}")
    print(f"[final] decision={grid.decision()}")

if __name__ == "__main__":
    run()
