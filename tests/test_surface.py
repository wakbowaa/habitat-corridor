from pathlib import Path
T=Path('contracts/contract.py').read_text(encoding='utf-8');P=Path('docs/index.html').read_text(encoding='utf-8')
def test_surface():
 for n in ('propose','accept_parcel','observe','get_corridor'):assert 'def '+n in T and n in P
 assert "status:'FINALIZED'" in P and 'id="corridorCanvas"' in P and 'id="parcelRibbon"' in P
