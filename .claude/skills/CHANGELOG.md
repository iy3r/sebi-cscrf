# Skill Changelog

## 1.0.0

- Three compliance skills: `/ciso` (full workflow), `/ciso-policy` (targeted drafting), `/ciso-assess` (policy evaluation)
- Five specialist agents: analyst, gap-analyst, policy-drafter, reviewer, roadmap-planner
- Entity profiling with deterministic tag resolver (`resolve_entity_tags.py`)
- Task-based gap analysis, policy drafting, and review cycles
- Selective framework loading via `policy-area-map.json`
- Failure envelope contracts for all phases
- Validation suite: `eval_skills.sh` with fixture system, functional contracts, and strict artifact checks
- Skills API evaluation: `eval_skills_api.py` (trigger, functional, full, report modes)
- Packaging for Claude.ai upload: `package_skills.sh`
