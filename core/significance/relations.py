"""
Six Significance Relations rho1-rho6
IMIP Framework | pi*sqrt(f(A)) hexarelational algebra
DOI: 10.5281/zenodo.19772798 (IMIP)
DOI: 10.5281/zenodo.18776462 (pi*sqrt(f(A)) + Quantum Computing)

Chain of implication: rho6 => rho5 => rho4 => rho3 => rho2 => rho1
"""
import math
import numpy as np
from dataclasses import dataclass
from typing import Any, Optional

PHI = (1 + math.sqrt(5)) / 2
PI = math.pi


@dataclass
class SignificanceProfile:
    rho_1: float = 0.0
    rho_2: float = 0.0
    rho_3: float = 0.0
    rho_4: float = 0.0
    rho_5: float = 0.0
    rho_6: float = 0.0

    def as_vector(self) -> np.ndarray:
        return np.array([self.rho_1, self.rho_2, self.rho_3,
                         self.rho_4, self.rho_5, self.rho_6])

    def f_value(self) -> float:
        v = self.as_vector()
        weights = np.array([PHI**k for k in range(6)])
        return math.sqrt(float(np.sum(weights * v**2)))

    def pi_convergence(self) -> float:
        f = self.f_value()
        return f**(1.0/PI) if f > 0 else 0.0

    def is_consistent(self) -> bool:
        v = self.as_vector()
        binary = (v >= 0.5).astype(int)
        for k in range(5, 0, -1):
            if binary[k] == 1:
                for j in range(k):
                    if binary[j] == 0:
                        return False
        return True

    def dominant_relation(self) -> tuple:
        names = ["rho1 Similitude", "rho2 Homology", "rho3 Equivalence",
                 "rho4 Symmetry", "rho5 Equilibrium", "rho6 Compensation"]
        v = self.as_vector()
        for i in range(5, -1, -1):
            if v[i] > 0.1:
                return (i+1, names[i])
        return (0, "None")

    def analogy_type(self) -> str:
        dominant, _ = self.dominant_relation()
        if dominant <= 2:
            return "Heuristic (Firstness)"
        elif dominant <= 4:
            return "Functional (Secondness)"
        else:
            return "Homological (Thirdness)"

    def __repr__(self):
        _, name = self.dominant_relation()
        return (f"SignificanceProfile("
                f"[{self.rho_1:.2f},{self.rho_2:.2f},{self.rho_3:.2f},"
                f"{self.rho_4:.2f},{self.rho_5:.2f},{self.rho_6:.2f}], "
                f"PI={self.pi_convergence():.4f}, dominant={name})")


class SignificanceEvaluator:

    def evaluate_rho1(self, a: Any, b: Any,
                      embeddings: Optional[dict] = None) -> float:
        if embeddings and a in embeddings and b in embeddings:
            va = np.array(embeddings[a])
            vb = np.array(embeddings[b])
            norm = np.linalg.norm(va) * np.linalg.norm(vb)
            return float(np.dot(va, vb)/norm) if norm > 0 else 0.0
        if isinstance(a, str) and isinstance(b, str):
            sa, sb = set(a.lower().split()), set(b.lower().split())
            if not sa or not sb:
                return 0.0
            return len(sa & sb) / len(sa | sb)
        return 0.0

    def evaluate_rho2(self, struct_a: dict, struct_b: dict) -> float:
        if not struct_a or not struct_b:
            return 0.0
        ka, kb = set(struct_a), set(struct_b)
        return len(ka & kb) / len(ka | kb) if ka | kb else 0.0

    def evaluate_rho3(self, func_a, func_b,
                      test_inputs: Optional[list] = None) -> float:
        if not test_inputs:
            return 0.0
        matches = sum(1 for inp in test_inputs
                      if self._safe_eq(func_a, func_b, inp))
        return matches / len(test_inputs)

    def evaluate_rho4(self, func_a, func_b,
                      test_inputs: Optional[list] = None) -> float:
        return (self.evaluate_rho3(func_a, func_b, test_inputs) +
                self.evaluate_rho3(func_b, func_a, test_inputs)) / 2.0

    def evaluate_rho5(self, p_a: np.ndarray,
                      p_b: np.ndarray) -> float:
        if p_a is None or p_b is None:
            return 0.0
        p_a = p_a / (p_a.sum() + 1e-10)
        p_b = p_b / (p_b.sum() + 1e-10)
        kl = float(np.sum(p_a * np.log((p_a+1e-10)/(p_b+1e-10))))
        return max(0.0, 1.0 - abs(kl))

    def evaluate_rho6(self, p_a: np.ndarray, p_b: np.ndarray,
                      p_ab: np.ndarray) -> float:
        """I(A:B) = S(rhoA) + S(rhoB) - S(rhoAB) > 0"""
        if p_a is None or p_b is None or p_ab is None:
            return 0.0
        def H(p):
            p = p / (p.sum() + 1e-10)
            return -np.sum(p * np.log2(p + 1e-10))
        mi = H(p_a) + H(p_b) - H(p_ab)
        return max(0.0, min(1.0, mi / (H(p_a) + H(p_b) + 1e-10)))

    def _safe_eq(self, fa, fb, inp):
        try:
            return fa(inp) == fb(inp)
        except Exception:
            return False
