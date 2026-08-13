# Shot-by-shot MAD analysis

## Contents

- Pass order and analytical units
- Coverage and enrichment records
- Music as authored structure
- Source and edit contribution
- Pattern synthesis
- Reader-facing 拉片
- Completion gate

Use this module as the internal bridge between deterministic media preparation and interpretation. A few memorable timestamps are not a 拉片. Account for the work chronologically, then select evidence for the final response.

## Pass order

1. **Experience pass**: watch without pausing. Record the initial emotional curve, conspicuous passages, confusion, and aftertaste without importing source knowledge.
2. **Structure pass**: mark functional chapters and musical sections independently. Place a boundary only when supported by observable change.
3. **Boundary pass**: inspect candidate cuts and dense intervals. Confirm, split, merge, or reject machine boundaries.
4. **Coverage pass**: record every analytical shot or justified shot cluster in playback order.
5. **Relation pass**: inspect boundaries, recurrences, sound bridges, and changes in subject, knowledge, energy, and visual momentum.
6. **Synthesis pass**: find repeated rules, developments, ruptures, exceptions, and ending payoffs before forming an editorial thesis.

Do not consult source summaries or creator explanations until the blind shot record is frozen.

## Define analytical units

Treat `shots.json` as candidate segmentation only.

- Use an **analytical shot** when a cut, replacement, major compositional reset, or new audiovisual task creates a distinct unit.
- Keep crop, virtual-camera, layer, mask, or typography development inside one shot when it performs one continuous task; record meaningful phases inside the shot.
- Use a **shot cluster** for very dense flashes or montage bursts that share one rhythmic, graphic, narrative, or emotional task. Record its time span, approximate or verified shot count, density pattern, internal exceptions, and reason for grouping.
- Split a cluster when subject, relation, musical task, or visual rule changes.
- Mark uncertain boundaries rather than manufacturing frame-level precision.

Coverage is complete only when the full playback duration belongs to verified shots, justified clusters, or explicitly marked unresolved intervals.

## Record two levels

Record every unit at **coverage level**:

- shot or cluster identifier;
- start, end, duration, and boundary status;
- visible content and momentary subject;
- music section plus salient beat, phrase, lyric, effect, ambience, or silence;
- primary material or editing operation;
- relation to the preceding unit.

Enrich important, repeated, ambiguous, or structurally decisive units with:

- base-image composition and constructed motion phases;
- audiovisual relation and shot-handoff behavior;
- event, response, state change, viewer-disclosure, or formal task;
- source contribution, MAD contribution, and their combined effect;
- viewer effect stated as an observation-led judgment;
- alternative reading, counterevidence, confidence, and interval to revisit.

When limited source material governs the passage, add the optional asset trail from [material-economy-and-reveal.md](material-economy-and-reveal.md): source-asset identity, visible region, disclosure stage, previous use, newly available information, and later payoff. Do not count a new crop as a new source asset.

When readable text carries the passage, add the optional text trail from [text-led-narrative.md](text-led-narrative.md): text source or voice, addressee, visible subject, narrative or emotional task, new information or state change, reading conditions, image-text relation, musical placement, and changed function on recurrence.

For each important element—color, object, eye, hand, body fragment, title, border, interface, repeated panel, sound, or lyric—continue beyond identification. Record:

`current appearance -> relation to adjacent material -> event or response affected -> relationship or viewer knowledge changed -> later recurrence or consequence`

Do not fill every field mechanically. Use the chain to prevent technique lists and fixed-symbol readings.

Do not enrich every row mechanically. Completeness applies to chronological coverage; depth follows analytical importance.

## Map music as authored structure

Treat audio measurements as private attention cues. Establish sections, phrases, accents, vocal entries, lyric units, instrumental changes, suspensions, releases, sound effects, ambience, and silence by listening in context. Record the heard event and the image's response; do not promote measurement bands or waveform values into musical conclusions.

Classify audiovisual relations without reducing them to beat sync:

- cut or event sync;
- motion or phrase sync;
- section or energy sync;
- lyric or semantic relation;
- dialogue or rhetorical alignment;
- counterpoint, deliberate non-sync, or withheld response.

Record what the image answers and how. A cut landing on a beat is not automatically important; test whether it changes attention, relation, energy, knowledge, atmosphere, or expectation.

## Separate source and edit contribution

For each major judgment, distinguish:

- **source contribution**: depicted pose, expression, action, composition, lighting, performance, location, or source-scene continuity already present;
- **MAD contribution**: selection, excerpt boundary, duration, order, adjacency, reframing, retiming, constructed motion, typography, compositing, treatment, sound bridge, and musical placement;
- **combined effect**: what becomes newly salient, connected, reinterpreted, or felt in this edit.

Do not credit the MAD editor with source animation, drawing, acting, or cinematography unless the edit visibly reconstructs it. Do not deny editorial authorship merely because the underlying image already contains strong expression.

## Synthesize patterns before prose

Look across the record for:

- recurring images whose crop, color, text, duration, or musical position changes;
- privileged images whose partial, full, or recontextualized use controls disclosure;
- text whose voice, task, readability, image relation, or emotional force changes across the work;
- density, scale, motion, and reading-time curves;
- repeated handoff rules involving gaze, direction, shape, color mass, or sound;
- subject-role migration and event-response-state chains;
- prepared versus isolated climaxes;
- deliberate holds, gaps, ruptures, and exceptions;
- an ending that confirms, reverses, or leaves unresolved an earlier proposition.

Generate at least two editorial-thesis hypotheses from these patterns. Selected timestamps in the final response must represent a pattern, development, or consequential exception—not merely the most spectacular frames.

## Publish a reader-facing 拉片

Keep IDs, candidate boundaries, detector scores, sampling details, confidence fields, coverage state, and schema labels in the working record. When the user requests a complete 拉片, translate the verified record into a continuous timeline containing:

- the visible event or material;
- the music, speech, sound, or silence as heard;
- the edit, design, or motion choice that matters;
- the immediate viewing effect and the reason for its placement;
- what the passage inherits from the previous passage, changes in the current event or relationship, and prepares for the next passage when those links are present.

Write the public 拉片 as timestamped prose by default. Let each time range serve as a navigation marker, followed by one or more connected paragraphs. Group very dense flashes when they perform one task and describe the internal pattern in ordinary language. The continuous time ranges demonstrate completeness; do not preface them with detector counts, coverage percentages, or claims about the amount of analysis performed.

For text-led passages, quote only the amount needed to identify the line, then explain what it changes and how the image and music receive it. For material-led passages, describe what becomes visible and why the timing matters instead of exposing asset IDs or recurrence counts.

Do not use a table for a single-work 拉片 unless the user explicitly asks for one or exact repeated-field comparison would otherwise be difficult to follow. Do not divide every passage into fixed “visual / music / technique / meaning” fields. Integrate only the relations that matter locally.

## Completion gate

Before drafting, verify:

- candidate cuts were reviewed rather than accepted literally;
- every interval is covered or marked unresolved;
- dense clusters retain their internal density and exception notes;
- music sections were interpreted beyond energy values;
- major claims separate source and edit contribution;
- the chosen evidence includes context before and after the cited moment;
- important elements have been followed through adjacency, recurrence, event, response, relationship, and changed viewer knowledge where supported;
- the final judgment follows from patterns in the record.
