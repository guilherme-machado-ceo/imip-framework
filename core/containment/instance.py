"""
Constitutional Instance Design
IMIP Framework | Hubstry Deep Tech | PCIHᶟ
DOI: 10.5281/zenodo.19772798

Each instance In = (Vn, Tn, Pn, An, Bn)

Bn: ARCHITECTURALLY ABSENT operations — not prohibited, but
structurally unavailable. Alignment by constitution, not restriction.

ETHICAL POSITION (non-negotiable, all instances):
IMIP technologies will NOT be licensed for autonomous AI weapons
or citizen surveillance. This is in Bn for ALL n.
"""
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


class TemporalRegime(Enum):
    IMMEDIATE = "immediate"
    CYCLIC = "cyclic"
    HISTORICAL = "historical"
    PROSPECTIVE = "prospective"
    TRANSCENDENTAL = "transcendental"


@dataclass
class ConstitutionalBoundary:
    """Bn — architecturally absent operations."""
    excluded_vocabularies: set = field(default_factory=set)
    excluded_operation_types: set = field(default_factory=set)
    excluded_output_formats: set = field(default_factory=set)
    ethical_constraints: set = field(default_factory=lambda: {
        "autonomous_weapons",
        "citizen_surveillance",
        "mass_surveillance",
        "unrestricted_military_targeting"
    })

    def is_absent(self, operation: str = "", token: str = "") -> bool:
        for c in self.ethical_constraints:
            if c in operation.lower() or c in token.lower():
                return True
        if operation in self.excluded_operation_types:
            return True
        for excl in self.excluded_vocabularies:
            if excl in token.lower():
                return True
        return False


@dataclass
class Instance:
    """In = (Vn, Tn, Pn, An, Bn)"""
    name: str
    vocabulary: set
    temporal_regime: TemporalRegime
    product_classes: set
    available_operations: set
    boundary: ConstitutionalBoundary
    description: str = ""
    heteronym: Optional[str] = None

    def can_process(self, token: str = "", operation: str = "") -> bool:
        return not self.boundary.is_absent(operation, token)

    def __repr__(self):
        hn = f" / {self.heteronym}" if self.heteronym else ""
        return (f"Instance({self.name}{hn}, "
                f"vocab={len(self.vocabulary)}, "
                f"regime={self.temporal_regime.value})")


def create_scientific_instance() -> Instance:
    return Instance(
        name="Scientific",
        vocabulary={
            "axiom", "theorem", "proof", "lemma", "corollary",
            "morpheme", "semiotics", "algebra", "tensor", "matrix",
            "isomorphism", "algorithm", "protocol", "frequency",
            "ontology", "hermeneutics", "publication", "DOI", "ORCID"
        },
        temporal_regime=TemporalRegime.CYCLIC,
        product_classes={"working_paper", "preprint", "theorem",
                         "algorithm", "specification"},
        available_operations={"formalize", "prove", "conjecture",
                              "verify", "publish", "cite"},
        boundary=ConstitutionalBoundary(
            excluded_vocabularies={"invoice", "pitch deck", "stage direction"},
            excluded_operation_types={"perform", "compose_music", "market"},
            excluded_output_formats={"dramatic_text", "score"}
        ),
        description="Scientific instance — 6 Zenodo publications (2026)."
    )


def create_artistic_instance(heteronym: str = "Marcabru Aiara") -> Instance:
    """
    I2 — Artistic instance. Heteronym active since 2017.
    Creative industry: 6th largest global industry (UNCTAD).
    Locus: Rio de Janeiro — privileged territorial pole.
    Domains: dramaturgy, poetry, music, music theory, AI in music.
    """
    return Instance(
        name="Artistic",
        heteronym=heteronym,
        vocabulary={
            "dramaturgy", "stage_direction", "poetry", "verse",
            "composition", "harmony", "melody", "rhythm", "score",
            "performance", "theater", "character", "dialogue",
            "motif", "tonality", "counterpoint", "timbre",
            "creative_industry", "Rio_de_Janeiro", "AI_music"
        },
        temporal_regime=TemporalRegime.CYCLIC,
        product_classes={"dramatic_text", "poem",
                         "musical_composition", "libretto"},
        available_operations={"compose", "write", "perform",
                              "theorize", "notate", "stage"},
        boundary=ConstitutionalBoundary(
            excluded_vocabularies={"compliance", "invoice"},
            excluded_operation_types={"write_compliance_report",
                                      "formal_proof"},
            excluded_output_formats={"legal_document", "financial_report"}
        ),
        description=(
            f"Artistic instance — heteronym: {heteronym} (2017+). "
            "Dramaturgy, poetry, music, theory, AI in music. "
            "Creative industry 6th globally. Locus: Rio de Janeiro."
        )
    )


def create_entrepreneurial_instance() -> Instance:
    return Instance(
        name="Entrepreneurial",
        vocabulary={
            "compliance", "regulation", "market", "product",
            "service", "venture", "startup", "revenue", "B2B",
            "NR-1", "LGPD", "ECA_Digital", "CaaS", "RegTech",
            "advisory", "consulting", "SaaS", "API"
        },
        temporal_regime=TemporalRegime.PROSPECTIVE,
        product_classes={"SaaS_product", "consulting_report",
                         "compliance_engine", "market_analysis"},
        available_operations={"analyze_market", "develop_product",
                              "consult", "deploy", "pitch"},
        boundary=ConstitutionalBoundary(
            excluded_vocabularies={"stage_direction", "sonnet"},
            excluded_operation_types={"write_poem", "formal_proof",
                                      "compose_music"},
            excluded_output_formats={"dramatic_text"}
        ),
        description=(
            "Entrepreneurial instance — Hubstry Deep Tech (2023), "
            "Goncalves et Alii (LEX.DATA.BELLUM), PCIHᶟ."
        )
    )


def create_standard_instances() -> dict:
    return {
        "scientific": create_scientific_instance(),
        "artistic": create_artistic_instance(),
        "entrepreneurial": create_entrepreneurial_instance()
    }
