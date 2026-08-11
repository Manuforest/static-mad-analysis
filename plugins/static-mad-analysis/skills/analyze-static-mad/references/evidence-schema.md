# Evidence schema

Use structured records when practical. Keep observation, inference, external context, and creator intent auditable.

## Type map

```json
{
  "times": [0.0, 32.0],
  "adapters": ["static_mad", "asmv"],
  "adapter_status": {"static_mad": "supported", "asmv": "provisional_extension"},
  "evidence": ["layered still images", "voice bridges organize chapter changes"],
  "confidence": 0.86
}
```

Classify by observable media behavior. A work may change type by interval.

## Evidence levels

- `observation`: directly visible or audible;
- `video_grounded_inference`: supported by adjacent shots or repeated structures;
- `external_context`: obtained outside the analyzed video;
- `documented_author_intent`: explicitly stated by the creator;
- `uncertain`: unresolved or conflicting.

## Observation

```json
{
  "start": 41.0,
  "end": 43.5,
  "level": "observation",
  "description": "A headphone-wearing figure is enclosed by a REC frame.",
  "frame_paths": [],
  "notes": []
}
```

## Entity and roles

```json
{
  "entity_id": "person_b",
  "candidate_identity": null,
  "anchors": [
    {"type": "accessory", "value": "headphones", "times": [41.0, 43.0]},
    {"type": "relation", "value": "framed by REC interface", "times": [43.0]}
  ],
  "roles_by_interval": [
    {"times": [41.0, 48.0], "roles": ["visual_subject", "focalizer", "dramatic_subject"]}
  ],
  "confidence": 0.72,
  "conflicts": []
}
```

When speech leads, add discourse roles separately:

```json
{
  "times": [41.0, 48.0],
  "original_speaker": "person_b",
  "visible_subject": "person_a",
  "assigned_narrator": "uncertain",
  "discourse_subject": "the pair's shared fear of being remembered",
  "implied_addressee": "person_a",
  "editorial_position": "the quotation is reframed as a mutual rather than private fear",
  "confidence": 0.61
}
```

## Chapter

```json
{
  "times": [38.0, 62.0],
  "task": "conflict_and_accumulation",
  "dramatic_question": "Will person_b acknowledge the recorded event?",
  "music_function": "pre_chorus_build",
  "visual_system": ["cold blue", "REC frames", "tight crops"],
  "boundary_evidence": ["instrument change", "focalizer shift"]
}
```

## Event-response-state chain

```json
{
  "event": {"times": [48.0, 50.0], "description": "A recorded image is revealed."},
  "response": {"times": [50.0, 53.0], "description": "The focal subject averts their gaze.", "mode": "visible"},
  "state_change": "The recording shifts from neutral evidence to an avoided memory.",
  "consequence": {"times": [57.0, 60.0], "description": "The REC frame returns as an enclosing border."},
  "level": "video_grounded_inference",
  "counterreading": "The gaze shot may be a non-causal mood insert.",
  "confidence": 0.71
}
```

## Shot relation

```json
{
  "from": [48.0, 50.0],
  "to": [50.0, 53.0],
  "observed": ["eye close-up", "medicine bottle"],
  "candidates": [
    {"type": "symbolic_association", "claim": "Feeling is reframed as diagnosis.", "confidence": 0.82},
    {"type": "physical_continuity", "claim": "The person sees the bottle.", "confidence": 0.28}
  ],
  "needed_evidence": ["shared location cues"]
}
```

## Material transformation

```json
{
  "times": [70.0, 72.0],
  "operations": ["crop", "recolor", "fabricated_composite"],
  "observed_result": "Two figures occupy one continuous room.",
  "proposed_function": "Construct a unified encounter space.",
  "level": "video_grounded_inference",
  "confidence": 0.66
}
```

## Motion provenance

```json
{
  "times": [70.0, 72.0],
  "mechanism": "static_constructed_motion",
  "motion_class": "camera_or_crop_motion",
  "observation": "The crop moves from the hand to the face.",
  "function": "The edit redirects attention from action to response.",
  "literal_character_motion_claimed": false,
  "confidence": 0.91
}
```

For footage-based edits, use `source_footage_action`, `retimed_source_motion`, or `edit_created_relation` as appropriate.

## Expression system

```json
{
  "system_id": "blue_future",
  "carrier": "blue light",
  "appearances": [12.0, 61.0, 94.0],
  "functions_by_appearance": ["distance", "possibility", "accepted future"],
  "fixed_dictionary_rejected": true,
  "confidence": 0.73
}
```

## Interpretation hypothesis

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

- `0.90–1.00`: explicit and repeatedly verified;
- `0.75–0.89`: strong multi-cue inference;
- `0.55–0.74`: leading interpretation with meaningful alternatives;
- `0.35–0.54`: weak but useful possibility;
- below `0.35`: retain in notes unless it resolves a specific ambiguity.

Confidence measures evidence support, not rhetorical importance.
