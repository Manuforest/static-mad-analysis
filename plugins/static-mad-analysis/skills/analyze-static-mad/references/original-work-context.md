# Original-work context and editorial transformation

Use this layer after the blind video pass. Its purpose is to determine how the edit reuses and changes source material, not whether it reproduces the original correctly.

## Three-layer order

Keep these interpretive layers distinct:

1. **Video body**: what the edited audiovisual work establishes through frames, order, sound, text, recurrence, and ending.
2. **Original-work context**: who and what the borrowed material originally depicts, where it belongs, and what changes when the edit reorganizes it.
3. **Creator expression**: what the editor explicitly states in descriptions, notes, interviews, or retrospectives.

Freeze the first layer before researching the next two. Later context may confirm, correct, narrow, complicate, or leave the video reading unchanged; it must not be rewritten as something visible in the blind pass.

## Establish only relevant source facts

Research the minimum source context needed for the edited passages:

- character identities and relationships;
- route, chapter, scene, or episode placement;
- original focalizer, speaker, addressee, and dramatic subject;
- source chronology and whether reused shots originally share a scene;
- the original event-response-state chain around a borrowed moment;
- prior functions of recurring places, objects, gestures, text, or music when reliably documented.

Prefer official material, the work itself, scripts or transcripts, official character and story pages, and creator documentation. Use reliable secondary summaries when primary material is unavailable. Mark fan interpretation as interpretation, not source fact. Record uncertainty when editions, routes, translations, or adaptations differ.

Do not import a full plot summary. Every source fact retained should resolve an identity, temporal, relational, symbolic, or editorial question raised by the video.

## Map editorial operations

Compare the relevant source arrangement with the MAD arrangement. Use operations such as:

- **extraction**: isolate a gesture, expression, place, or line from its original scene;
- **relocation**: place material in a different temporal, emotional, or argumentative position;
- **juxtaposition**: connect materials that were separate in the source;
- **role reassignment**: change the apparent focalizer, speaker, addressee, witness, or dramatic subject;
- **condensation**: make several scenes, routes, or periods function as one progression;
- **expansion**: turn a brief source moment into sustained subjective duration;
- **parallelization**: make different routes, characters, or eras answer one another;
- **counterfactual extension**: propose a continuation or relation not depicted by the source;
- **material transformation**: change meaning through crop, masking, compositing, typography, color, interface, repetition, or sound;
- **thesis reassignment**: use source events to support an editorial proposition that the original scene did not itself state.

For each important operation, record:

`source fact -> edited arrangement -> changed subject/time/relation -> interpretive effect -> confidence`

Example:

```json
{
  "source_fact": "The two images belong to different character routes and do not form one encounter.",
  "edited_arrangement": "The MAD joins them through matched gaze direction and one continuous music phrase.",
  "operation": ["juxtaposition", "parallelization"],
  "changed_relation": "The characters become alternative answers to one shared emotional problem.",
  "level": "original_work_context",
  "confidence": 0.82
}
```

## Test the current interpretation

Ask:

- Does source context identify the video's subjects more securely?
- Does it change an assumed cause, reaction, chronology, speaker, or viewpoint?
- Does the edit preserve the source relation, or construct a new one?
- Does a repeated image carry accumulated meaning from its source scene, meaning created inside the MAD, or both?
- Does the ending close a source arc, combine several arcs, or propose a new continuation?
- Which part of the leading interpretation still stands without source knowledge?

Keep a claim if the video independently supports it. Qualify it as source-dependent when it requires route, character, or scene knowledge. Correct it when source evidence disproves the assumed identity or relation.

## Boundaries

Do not use this layer to judge:

- fidelity or faithfulness to the original;
- completeness of character, plot, causality, or relationship coverage;
- whether omitted source information should have been included;
- readability for viewers unfamiliar with the source;
- whether the interpretation is canonically correct;
- award, ranking, competition, or eligibility suitability.

Analyze transformation rather than compliance. A contradiction with the source may be an intentional counterfactual, symbolic reassignment, or editorial thesis; identify the operation and its evidence before calling it an error.

## Output discipline

Use formulations that preserve provenance:

- `The video alone suggests ...`
- `Original-work context identifies/corrects/adds ...`
- `The edit changes this by ...`
- `The creator's note confirms/narrows/complicates ...`

End with a three-layer synthesis rather than merging all evidence into one seamless plot account.
