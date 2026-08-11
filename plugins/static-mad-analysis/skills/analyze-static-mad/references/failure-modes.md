# Failure modes and research basis

Review this list before final interpretation.

## Evidence and video-understanding failures

- **Language-prior bypass**: infer source plot from title, synopsis, or familiarity instead of video evidence.
- **Uniform-sampling blindness**: miss inserts, action order, text, or match cuts.
- **Identity drift**: merge or rename characters after crop, age, style, polarity, or costume changes.
- **Event multiplication**: treat variants of one source image or memory as separate events.
- **Chronology collapse**: assume adjacent shots share physical time and space.
- **Salience/focalizer confusion**: equate the largest face with the viewpoint subject.
- **Contact-sheet overreach**: infer motion or order from widely spaced thumbnails.
- **VLM continuity hallucination**: smooth cuts, crop changes, and layer animation into physical character action.
- **Single-story lock-in**: write one fluent explanation before testing alternatives.
- **Evidence laundering**: present source knowledge or creator notes as visually inferred.

## Static-MAD interpretation failures

- **Event-only summary**: list incidents without reactions, state changes, or consequences.
- **Author-intent absolutism**: treat a creator statement as the only valid observable effect.
- **Original-work comparison creep**: judge fidelity, completeness, or accessibility against the original when the user requested analysis of the video itself.
- **Fixed-symbol dictionary**: decide that one color/object always means one concept without tracking change.
- **Effect intentionality bias**: assume every repeated effect carries deep meaning.
- **Motion worship**: reward constant movement and overlook meaningful holds or readable stillness.
- **Craft-proxy bias**: use layer count, software, 3D, rendering cost, or visible effort as quality.
- **Template overfit**: impose intro/verse/pre-chorus/chorus functions on a work that uses another structure.
- **Surface-style imitation**: confuse copied gradients, shadows, typography, or transitions with an authored visual language.
- **Music reduction**: equate beat synchronization with narrative or emotional fit.
- **Rhetoric without operation**: use “狂气,” “高级,” “爽,” “意识流,” or “有意境” without observable evidence.

## Research-derived workflow principles

- Use coarse-to-fine temporal search and adaptive sampling.
- Decompose event parsing, grounding, memory, interpretation, and judgment.
- Require timestamped visual evidence and explicit long-video entity memory.
- Keep editing recognition, reasoning, creator intent, and evaluation separate.
- Integrate vision, audio, language, and viewer disclosure at event boundaries.
- Re-probe important temporal answers for consistency.
- Track event-response-state chains and multi-line convergence.
- Analyze visible material treatment without assuming knowledge of its original arrangement.
- Treat global motifs, processing density, and repeated shots as evolving systems.
- Evaluate static MAD with a profile rather than one scalar.

Representative research includes TimeChat, Koala, MoReVQA, NExT-GQA, MA-LMM, ReWind, Re-thinking Temporal Search, VEU-Bench, LongVALE, LongVT, and NarrativeTrack. Community-informed principles come from creator retrospectives, Bilibili columns, and Chinese/Japanese criticism. These sources guide the workflow; they do not replace inspection of the video.
