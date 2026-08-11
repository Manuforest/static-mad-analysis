# Failure modes and research basis

Review this list before final interpretation.

## Failure modes

- Language-prior bypass: inferring the source plot from title, synopsis, or familiarity instead of video evidence.
- Uniform-sampling blindness: missing brief inserts, action order, text, or match cuts.
- Identity drift: renaming or merging characters after style, crop, age, polarity, or location changes.
- Event multiplication: treating graphic variants of one memory as new events.
- Chronology collapse: assuming adjacent shots share physical time and space.
- Salience/focalizer confusion: calling the largest face the viewpoint subject.
- Audio reduction: equating every beat-synchronous cut with narrative synchronization.
- Effect intentionality bias: assuming every repeated effect has deep meaning.
- Single-story lock-in: producing one fluent explanation before testing alternatives.
- Evidence laundering: using external source knowledge and presenting it as visually inferred.
- Contact-sheet overreach: inferring motion or order from widely spaced thumbnails.

## Research-derived design principles

- Use coarse-to-fine temporal search and adaptive frame selection rather than uniform sparse sampling.
- Decompose event parsing, grounding, memory, and reasoning instead of asking for one-pass narration.
- Require timestamped visual grounding for claims.
- Maintain explicit long-video memory for entities and events.
- Treat editing recognition, reasoning, and judgment as distinct tasks.
- Integrate vision, audio, and language at event boundaries.
- Re-probe initial temporal answers for consistency.

Representative sources:

- TimeChat, CVPR 2024: timestamp-aware long-video understanding.
- Koala, CVPR 2024: key-frame-conditioned long-video models.
- MoReVQA, CVPR 2024: modular event parsing, grounding, memory, and reasoning.
- NExT-GQA, CVPR 2024: visually grounded video answers.
- MA-LMM, CVPR 2024 and ReWind, CVPR 2025: memory for long video.
- Re-thinking Temporal Search, CVPR 2025: query-aware coarse-to-fine search.
- VEU-Bench, CVPR 2025: recognition, reasoning, and judgment of editing.
- LongVALE, CVPR 2025: time-aware vision-audio-language events.
- LongVT, CVPR 2026: tool-using agents that browse then revisit video.
- NarrativeTrack, 2026: entity consistency across narrative transitions.

These principles guide workflow design; this skill does not reproduce the papers' learned architectures or benchmark claims.
