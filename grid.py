from dataclasses import dataclass
from typing import List, Tuple
import random

Vec = List[List[float]]

@dataclass
class SLCAConfig:
    size: int = 6
    leak: float = 0.08
    inhibition: float = 0.12
    noise: float = 0.02
    threshold: float = 0.9

class SLCAGrid:
    def __init__(self, cfg: SLCAConfig):
        self.cfg = cfg
        self.coherent = [[0.0]*cfg.size for _ in range(cfg.size)]
        self.conflicted = [[0.0]*cfg.size for _ in range(cfg.size)]

    def neighbors(self, i: int, j: int) -> List[Tuple[int,int]]:
        offs = [(-1,0),(1,0),(0,-1),(0,1)]
        size = self.cfg.size
        return [(i+di, j+dj) for di,dj in offs if 0 <= i+di < size and 0 <= j+dj < size]

    def step(self, I_coh: Vec, I_con: Vec):
        C, X, cfg = self.coherent, self.conflicted, self.cfg
        def rnd(): return random.uniform(-cfg.noise, cfg.noise)
        newC = [[0.0]*cfg.size for _ in range(cfg.size)]
        newX = [[0.0]*cfg.size for _ in range(cfg.size)]
        for i in range(cfg.size):
            for j in range(cfg.size):
                inhC = sum(X[m][n] for m,n in self.neighbors(i,j)) * cfg.inhibition
                inhX = sum(C[m][n] for m,n in self.neighbors(i,j)) * cfg.inhibition
                c = C[i][j] + I_coh[i][j] - inhC - cfg.leak*C[i][j] + rnd()
                x = X[i][j] + I_con[i][j] - inhX - cfg.leak*X[i][j] + rnd()
                newC[i][j] = max(0.0, c)
                newX[i][j] = max(0.0, x)
        self.coherent, self.conflicted = newC, newX

    def decision(self) -> str:
        avgC = sum(map(sum, self.coherent)) / (self.cfg.size**2)
        avgX = sum(map(sum, self.conflicted)) / (self.cfg.size**2)
        delta = self.cfg.threshold / 10
        if avgC - avgX > delta:
            return "COHERENT"
        elif avgX - avgC > delta:
            return "CONFLICTED"
        return "UNDECIDED"
