#!/bin/bash
# IMIP Framework — Setup and Push to GitHub
# Run this from INSIDE the imip-framework folder
# Usage: bash setup_and_push.sh

set -e

echo "=== IMIP Framework — GitHub Setup ==="
echo ""

# 1. Init git
git init
git branch -M main

# 2. Add remote
git remote add origin https://github.com/guilherme-machado-ceo/imip-framework.git

# 3. Stage everything
git add .

# 4. Commit
git commit -m "feat: IMIP Framework v1.0

DOI working paper: 10.5281/zenodo.19772798

Modules:
- GuruMatrix 5D with Aristotelian taxonomy and learning
- Six significance relations rho1-rho6 + SignificanceProfile
- Constitutional instance design with Bn (architectural absence)
- DISPATCH_ON_HERMENEUTICS (7 levels)
- Three standard instances (scientific, artistic/Marcabru Aiara, entrepreneurial)
- 35 passing tests
- CITATION.cff with Zenodo DOI integration

Related repos:
- gurudev-lang: DISPATCH_ON_HERMENEUTICS production
- algebra-hexarrelacional: pi*sqrt(f(A)) + GuruMatrix 5D
- qualia-hub-ecosystem: quantum instance hub

Ethical position: IMIP technologies will NOT be licensed
for autonomous AI weapons or citizen surveillance."

# 5. Push
git push -u origin main

echo ""
echo "=== Done! ==="
echo "Repository: https://github.com/guilherme-machado-ceo/imip-framework"
echo "Paper DOI:  https://doi.org/10.5281/zenodo.19772798"
