"""
DISPATCH_ON_HERMENEUTICS
IMIP Framework | GuruDev core instruction
DOI: 10.5281/zenodo.19772798

Produces 7 computationally distinct outputs for a single input token.
Verified in GuruDev MVP: github.com/marcabru-tech/gurudev-lang
Levels 5-7 enable cross-instance operation.
"""
from dataclasses import dataclass
from typing import Optional

LEVELS = {
    1: {"name": "Literal", "op": "direct_syntactic_mapping",
        "anchor": "Peirce: Rheme"},
    2: {"name": "Allegorical", "op": "structural_metaphor_detection",
        "anchor": "Peirce: Dicent"},
    3: {"name": "Tropological", "op": "behavioral_implication_extraction",
        "anchor": "Aristotle: Practical reason"},
    4: {"name": "Anagogical", "op": "systemic_consequence_projection",
        "anchor": "Kant: Regulative idea"},
    5: {"name": "Semiotic", "op": "cross_domain_sign_relation_mapping",
        "anchor": "Peirce: Argument (law)"},
    6: {"name": "Ontological", "op": "category_level_structural_analysis",
        "anchor": "Aristotle: Categories"},
    7: {"name": "Transcendental", "op": "pi_radical_convergence",
        "anchor": "PI(A) = [f(A)]^(1/pi)"}
}


@dataclass
class HermeneuticOutput:
    level: int
    level_name: str
    input_token: str
    interpretation: str
    anchor: str


class DispatchOnHermeneutics:
    """Central instruction of GuruDev. 7 hermeneutic levels."""

    def dispatch(self, token: str,
                 level: Optional[int] = None) -> list:
        levels = [level] if level else list(range(1, 8))
        return [self._level(token, l) for l in levels]

    def _level(self, token: str, l: int) -> HermeneuticOutput:
        cfg = LEVELS[l]
        interps = {
            1: f"[LITERAL] '{token}' -> direct syntactic mapping.",
            2: (f"[ALLEGORICAL] '{token}' as structural metaphor "
                f"pointing beyond immediate referent."),
            3: (f"[TROPOLOGICAL] '{token}' demands behavioral "
                f"reorientation. Practical implication: engage."),
            4: (f"[ANAGOGICAL] '{token}' as regulative ideal — "
                f"systemic consequence projection."),
            5: (f"[SEMIOTIC] '{token}' as cross-domain sign — "
                f"maps sign relations across instance boundaries."),
            6: (f"[ONTOLOGICAL] '{token}' resolved to Aristotelian "
                f"category. Formal ontology: category x domain."),
            7: (f"[TRANSCENDENTAL] '{token}' under PI-radical: "
                f"convergence toward universal significance. "
                f"Cross-instance rho6 candidate.")
        }
        return HermeneuticOutput(
            level=l, level_name=cfg["name"],
            input_token=token,
            interpretation=interps[l],
            anchor=cfg["anchor"]
        )

    def min_level_for_cross_instance(self, pi_score: float) -> int:
        if pi_score >= 0.8: return 7
        elif pi_score >= 0.6: return 6
        elif pi_score >= 0.4: return 5
        elif pi_score >= 0.2: return 3
        else: return 1
