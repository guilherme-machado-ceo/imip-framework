"""
IMIP Framework — Core Test Suite
DOI: 10.5281/zenodo.19772798
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import pytest
from core.gurumatrix.gurumatrix import (
    GuruMatrix5D, GuruMatrixCoordinate, CrossInstanceOperation
)
from core.significance.relations import SignificanceProfile, SignificanceEvaluator
from core.containment.instance import (
    ConstitutionalBoundary, Instance, TemporalRegime,
    create_scientific_instance, create_artistic_instance,
    create_entrepreneurial_instance
)
from dispatch.hermeneutics import DispatchOnHermeneutics, HermeneuticOutput


# ── GuruMatrix5D ──────────────────────────────────────────────────

def test_gurumatrix_shape():
    gm = GuruMatrix5D()
    assert gm.tensor.shape == (10, 10, 7, 5, 10)

def test_gurumatrix_pi_convergence_one():
    gm = GuruMatrix5D()
    assert abs(gm.pi_convergence(1.0) - 1.0) < 1e-6

def test_gurumatrix_pi_convergence_zero():
    gm = GuruMatrix5D()
    assert gm.pi_convergence(0.0) == 0.0

def test_gurumatrix_pi_convergence_range():
    gm = GuruMatrix5D()
    for v in [0.1, 0.5, 0.9, 2.0]:
        result = gm.pi_convergence(v)
        assert result >= 0.0

def test_gurumatrix_learn_from_operation():
    gm = GuruMatrix5D(learning_rate=0.1)
    coord = GuruMatrixCoordinate(i=1, j=1, k=5, t=2, l=1)
    old = gm.get_weight(coord)
    op = CrossInstanceOperation(
        instance_source="scientific",
        instance_target="artistic",
        coordinate=coord,
        rho_scores=[0.5, 0.4, 0.3, 0.3, 0.2, 0.8],
        pi_score=0.75,
        successful=True
    )
    gm.learn_from_operation(op)
    assert gm.get_weight(coord) > old

def test_gurumatrix_identity_signature():
    gm = GuruMatrix5D()
    sig = gm.identity_signature()
    for key in ["total_operations", "non_zero", "mean_weight",
                "max_weight", "dominant_levels", "tensor_hash"]:
        assert key in sig

def test_gurumatrix_repr():
    gm = GuruMatrix5D()
    assert "GuruMatrix5D" in repr(gm)


# ── SignificanceProfile ───────────────────────────────────────────

def test_profile_vector_length():
    p = SignificanceProfile(0.9, 0.8, 0.7, 0.6, 0.5, 0.4)
    assert len(p.as_vector()) == 6

def test_profile_f_value_nonneg():
    p = SignificanceProfile(0.5, 0.4, 0.3, 0.3, 0.2, 0.1)
    assert p.f_value() >= 0

def test_profile_pi_convergence_range():
    p = SignificanceProfile(0.9, 0.8, 0.7, 0.6, 0.5, 0.4)
    pi = p.pi_convergence()
    assert pi >= 0.0

def test_profile_consistent_valid():
    # Monotonically decreasing: consistent
    p = SignificanceProfile(0.9, 0.8, 0.7, 0.6, 0.5, 0.4)
    assert p.is_consistent() is True

def test_profile_consistent_invalid():
    # rho6=0.9 but rho1=0.1: violates chain
    p = SignificanceProfile(0.1, 0.1, 0.1, 0.1, 0.1, 0.9)
    assert p.is_consistent() is False

def test_profile_dominant_relation():
    p = SignificanceProfile(0.9, 0.8, 0.7, 0.6, 0.5, 0.4)
    n, name = p.dominant_relation()
    assert isinstance(n, int)
    assert isinstance(name, str)

def test_profile_analogy_type():
    valid_types = {
        "Heuristic (Firstness)",
        "Functional (Secondness)",
        "Homological (Thirdness)"
    }
    p = SignificanceProfile(0.9, 0.8, 0.7, 0.6, 0.5, 0.4)
    assert p.analogy_type() in valid_types

def test_profile_zero():
    p = SignificanceProfile()
    assert p.f_value() == 0.0
    assert p.pi_convergence() == 0.0


# ── SignificanceEvaluator ─────────────────────────────────────────

def test_evaluator_rho1_identical():
    ev = SignificanceEvaluator()
    score = ev.evaluate_rho1("semiotics algebra", "semiotics algebra")
    assert score == 1.0

def test_evaluator_rho1_disjoint():
    ev = SignificanceEvaluator()
    score = ev.evaluate_rho1("apple orange", "river mountain")
    assert score == 0.0

def test_evaluator_rho6_emergent():
    ev = SignificanceEvaluator()
    p_a = np.array([0.5, 0.5])
    p_b = np.array([0.5, 0.5])
    p_ab = np.array([0.7, 0.3])
    score = ev.evaluate_rho6(p_a, p_b, p_ab)
    assert score >= 0.0


# ── ConstitutionalBoundary ────────────────────────────────────────

def test_ethical_constraint_weapons():
    b = ConstitutionalBoundary()
    assert b.is_absent(operation="autonomous_weapons") is True

def test_ethical_constraint_surveillance():
    b = ConstitutionalBoundary()
    assert b.is_absent(operation="citizen_surveillance") is True

def test_ethical_constraint_mass():
    b = ConstitutionalBoundary()
    assert b.is_absent(operation="mass_surveillance") is True

def test_allowed_token():
    b = ConstitutionalBoundary()
    assert b.is_absent(operation="formalize", token="theorem") is False


# ── Instance ──────────────────────────────────────────────────────

def test_scientific_instance_creation():
    inst = create_scientific_instance()
    assert inst.name == "Scientific"
    assert len(inst.vocabulary) > 0
    assert inst.temporal_regime == TemporalRegime.CYCLIC

def test_artistic_instance_heteronym():
    inst = create_artistic_instance()
    assert inst.heteronym == "Marcabru Aiara"
    assert inst.name == "Artistic"

def test_entrepreneurial_instance_regime():
    inst = create_entrepreneurial_instance()
    assert inst.temporal_regime == TemporalRegime.PROSPECTIVE

def test_instance_can_process_allowed():
    inst = create_scientific_instance()
    assert inst.can_process(token="theorem", operation="formalize") is True

def test_instance_cannot_process_weapons():
    inst = create_scientific_instance()
    assert inst.can_process(operation="autonomous_weapons") is False

def test_instance_cannot_process_surveillance():
    inst = create_artistic_instance()
    assert inst.can_process(operation="citizen_surveillance") is False

def test_artistic_boundary_compliance():
    inst = create_artistic_instance()
    # compliance report is in Bn for artistic instance
    assert inst.can_process(operation="write_compliance_report") is False


# ── DispatchOnHermeneutics ────────────────────────────────────────

def test_dispatch_returns_seven():
    d = DispatchOnHermeneutics()
    outputs = d.dispatch("semiotics")
    assert len(outputs) == 7

def test_dispatch_all_hermeneutic_output():
    d = DispatchOnHermeneutics()
    outputs = d.dispatch("tensor")
    assert all(isinstance(o, HermeneuticOutput) for o in outputs)

def test_dispatch_distinct_level_names():
    d = DispatchOnHermeneutics()
    outputs = d.dispatch("morpheme")
    names = [o.level_name for o in outputs]
    assert len(set(names)) == 7

def test_dispatch_specific_level():
    d = DispatchOnHermeneutics()
    outputs = d.dispatch("GuruDev", level=7)
    assert len(outputs) == 1
    assert outputs[0].level == 7
    assert outputs[0].level_name == "Transcendental"

def test_dispatch_distinct_interpretations():
    d = DispatchOnHermeneutics()
    outputs = d.dispatch("IMIP")
    interps = [o.interpretation for o in outputs]
    assert len(set(interps)) == 7

def test_dispatch_levels_sequential():
    d = DispatchOnHermeneutics()
    outputs = d.dispatch("PCIHᶟ")
    levels = [o.level for o in outputs]
    assert levels == list(range(1, 8))


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
