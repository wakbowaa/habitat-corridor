# HABITAT / CORRIDOR

### A spatial pact in four movements

**I — Draw**  
A sponsor identifies a species, orders three to seven parcel records, and assigns one distinct steward per parcel. The records must also live on distinct HTTPS origins.

**II — Consent**  
Each assigned steward accepts exactly their own parcel. The corridor cannot be observed early and no sponsor can impersonate a steward.

**III — Observe**  
GenLayer validators retrieve every parcel record and compare their own structured judgment: are the ordered parcels adjacent and habitat-compatible? The exact source bytes become SHA-256 digests.

**IV — Reveal**  
The ledger says `ACTIVE` only when the chain is connected with no gap indexes. Otherwise it says `FRAGMENTED` and preserves the gaps for repair.

---

### Field kit

| Piece | Location | Purpose |
|---|---|---|
| Primitive | `contracts/contract.py` | consent + spatial consensus |
| Boundary checks | `tests/direct/` | permissions and successful activation |
| Habitat records | `evidence/` | three independently hosted observations |
| Living map | `docs/index.html` | parcel ribbon and animated corridor |
| Receipts | `deployment.json` | exact deployment and live calls |

Run `pytest -q`, then `ruff check contracts tests`. Deploy with `python scripts/deploy.py` using the account-specific StudioNet key in the workspace environment.

This contract does not claim that an LLM owns ecological truth. It makes a narrower guarantee: every validator checks the same frozen parcel set, consensus is explicit, consent is attributable, and the final record is reconstructible.
