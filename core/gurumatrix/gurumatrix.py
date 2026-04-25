"""
GuruMatrix 5D — Dynamic Parametric Tensor
IMIP Framework | Hubstry Deep Tech | PCIHᶟ
DOI: 10.5281/zenodo.19772798

Identity(S, tau) = {G(0), G(1), ..., G(tau)}
Identity is the tensor. The tensor is the memory of the flow.

Five axes:
  i: Ontological category (Aristotelian, 1-10)
  j: Semantic field / knowledge domain (1-10)
  k: Hermeneutic level (1-7)
  t: Temporal regime (1-5)
  l: Target paradigm (1-10)
"""

import numpy as np
import json
import hashlib
from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional
from pathlib import Path

PI = 3.14159265358979

ONTOLOGICAL_CATEGORIES = {
    1: "Substance (ousia)", 2: "Quantity (poson)", 3: "Quality (poion)",
    4: "Relation (pros ti)", 5: "Place (pou)", 6: "Time (pote)",
    7: "Position (keisthai)", 8: "State (echein)",
    9: "Action (poiein)", 10: "Passion (paschein)"
}

KNOWLEDGE_DOMAINS = {
    1: "Formal sciences (logic, mathematics, computation)",
    2: "Natural sciences (physics, chemistry, biology)",
    3: "Human sciences (history, sociology, anthropology)",
    4: "Linguistic sciences (phonology, syntax, semantics)",
    5: "Philosophical sciences (epistemology, ontology, ethics)",
    6: "Theological sciences (comparative religion, mysticism)",
    7: "Technical sciences (engineering, architecture, design)",
    8: "Economic sciences (market, finance, production)",
    9: "Artistic practices (music, dramaturgy, poetry, visual arts)",
    10: "Legal sciences (law, norm, regulation, governance)"
}

HERMENEUTIC_LEVELS = {
    1: "Literal", 2: "Allegorical", 3: "Tropological",
    4: "Anagogical", 5: "Semiotic", 6: "Ontological", 7: "Transcendental"
}

TEMPORAL_REGIMES = {
    1: "Immediate", 2: "Cyclic", 3: "Historical",
    4: "Prospective", 5: "Transcendental"
}

TARGET_PARADIGMS = {
    1: "Scientific", 2: "Artistic", 3: "Entrepreneurial",
    4: "Federal", 5: "Subnational", 6: "International",
    7: "Post-quantum", 8: "Dual-use", 9: "Educational", 10: "Therapeutic"
}


@dataclass
class GuruMatrixCoordinate:
    i: int  # ontological category (1-10)
    j: int  # knowledge domain (1-10)
    k: int  # hermeneutic level (1-7)
    t: int  # temporal regime (1-5)
    l: int  # target paradigm (1-10)

    def to_index(self):
        return (self.i-1, self.j-1, self.k-1, self.t-1, self.l-1)

    def describe(self) -> str:
        return (
            f"i={self.i}:{ONTOLOGICAL_CATEGORIES.get(self.i,'?')} | "
            f"j={self.j}:{KNOWLEDGE_DOMAINS.get(self.j,'?')} | "
            f"k={self.k}:{HERMENEUTIC_LEVELS.get(self.k,'?')} | "
            f"t={self.t}:{TEMPORAL_REGIMES.get(self.t,'?')} | "
            f"l={self.l}:{TARGET_PARADIGMS.get(self.l,'?')}"
        )


@dataclass
class CrossInstanceOperation:
    instance_source: str
    instance_target: str
    coordinate: GuruMatrixCoordinate
    rho_scores: list
    pi_score: float
    timestamp: str = field(
        default_factory=lambda: datetime.utcnow().isoformat())
    successful: bool = True


class GuruMatrix5D:
    """
    5D GuruMatrix — dynamic identity tensor of generative operator S.
    Shape: (10, 10, 7, 5, 10) = 35,000 coordinate positions.
    G(t+1) = G(t) + alpha * learn_from_operation(Ii, Ij, pi_score, rho_scores)
    """

    SHAPE = (10, 10, 7, 5, 10)

    def __init__(self, learning_rate: float = 0.01,
                 persistence_path: Optional[str] = None):
        self.tensor = np.zeros(self.SHAPE, dtype=np.float64)
        self.learning_rate = learning_rate
        self.operation_history = []
        self.persistence_path = persistence_path
        self._delta_log = []
        if persistence_path and Path(persistence_path).exists():
            self.load(persistence_path)

    def learn_from_operation(self, op: CrossInstanceOperation):
        idx = op.coordinate.to_index()
        old = self.tensor[idx]
        delta = self.learning_rate * op.pi_score
        if op.successful:
            self.tensor[idx] = min(1.0, old + delta)
        else:
            self.tensor[idx] = max(0.0, old - delta * 0.5)
        self.operation_history.append(op)
        self._delta_log.append({
            "ts": op.timestamp, "coord": list(idx),
            "old": old, "new": float(self.tensor[idx]), "pi": op.pi_score
        })
        if self.persistence_path:
            self.save(self.persistence_path)

    def pi_convergence(self, f_value: float) -> float:
        """PI(A) = [f(A)]^(1/pi). Converges to 1 for any f(A) > 0."""
        if f_value <= 0:
            return 0.0
        return f_value ** (1.0 / PI)

    def get_weight(self, coord: GuruMatrixCoordinate) -> float:
        return float(self.tensor[coord.to_index()])

    def identity_signature(self) -> dict:
        return {
            "total_operations": len(self.operation_history),
            "non_zero": int(np.count_nonzero(self.tensor)),
            "mean_weight": float(np.mean(self.tensor)),
            "max_weight": float(np.max(self.tensor)),
            "dominant_levels": self._dominant_levels(),
            "tensor_hash": self._hash()
        }

    def _dominant_levels(self) -> list:
        levels = []
        for k in range(7):
            w = float(np.sum(self.tensor[:, :, k, :, :]))
            levels.append({"level": k+1,
                           "name": HERMENEUTIC_LEVELS[k+1], "weight": w})
        return sorted(levels, key=lambda x: x["weight"], reverse=True)[:3]

    def _hash(self) -> str:
        return hashlib.sha256(self.tensor.tobytes()).hexdigest()

    def save(self, path: str):
        Path(path).write_text(json.dumps({
            "tensor": self.tensor.tolist(),
            "learning_rate": self.learning_rate,
            "op_count": len(self.operation_history),
            "hash": self._hash(),
            "saved_at": datetime.utcnow().isoformat()
        }, indent=2))

    def load(self, path: str):
        data = json.loads(Path(path).read_text())
        self.tensor = np.array(data["tensor"])
        self.learning_rate = data.get("learning_rate", self.learning_rate)

    def __repr__(self):
        sig = self.identity_signature()
        return (f"GuruMatrix5D(ops={sig['total_operations']}, "
                f"non_zero={sig['non_zero']}, "
                f"mean={sig['mean_weight']:.4f})")
