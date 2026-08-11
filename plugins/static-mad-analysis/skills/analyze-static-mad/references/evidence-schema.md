# Evidence schema

Use JSON artifacts when practical. Keep claims auditable.

## Observation

```json
{
  "start": 41.0,
  "end": 43.5,
  "level": "observation",
  "description": "A headphone-wearing figure is enclosed by a REC focus frame.",
  "frame_paths": [],
  "notes": []
}
```

Allowed levels:

- `observation`: directly visible or audible;
- `strong_inference`: multiple independent cues;
- `weak_inference`: plausible but underdetermined;
- `external_fact`: obtained outside the video.

## Entity

```json
{
  "entity_id": "person_b",
  "provisional_name": "person_b",
  "candidate_identity": null,
  "anchors": [
    {"type": "accessory", "value": "headphones", "times": [41.0, 43.0]},
    {"type": "relation", "value": "framed by REC interface", "times": [43.0]}
  ],
  "roles": ["observed_subject"],
  "confidence": 0.72,
  "conflicts": []
}
```

## Shot relation

```json
{
  "from": [48.0, 50.0],
  "to": [50.0, 53.0],
  "observed": ["eye close-up", "medicine bottle"],
  "candidates": [
    {"type": "symbolic_association", "claim": "feeling is reframed as diagnosis", "confidence": 0.82},
    {"type": "physical_continuity", "claim": "the person sees a bottle", "confidence": 0.28}
  ],
  "needed_evidence": ["shared location cues"]
}
```

## Hypothesis

```json
{
  "id": "h1",
  "claim": "The middle section is a memory replay rather than linear present time.",
  "support": [{"times": [0, 8]}, {"times": [100, 106]}],
  "counterevidence": [],
  "alternative": "The repeated space is only a visual bookend.",
  "confidence": 0.68,
  "revisit": [[98, 108]],
  "external_context": []
}
```

## Confidence guide

- 0.90–1.00: explicit and repeatedly verified;
- 0.75–0.89: strong multi-cue inference;
- 0.55–0.74: leading interpretation with meaningful alternatives;
- 0.35–0.54: weak but useful possibility;
- below 0.35: mention only if it explains a specific ambiguity.

Confidence is evidence calibration, not rhetorical emphasis.
