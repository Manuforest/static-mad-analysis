# Audience-facing translation

## Contents

- Internal aids, viewing judgments, and reader expression
- Verification and hidden internal aids
- Translation examples and heard music
- Technical explanation
- Output modes and structural restraint
- Final reader audit

Use this module before every user-facing appreciation, 拉片, technical analysis, review, or report. Keep analytical rigor in the working record and write the final response from verified viewing judgments.

## Keep three layers separate

1. **Internal aids**: sampled frames, contact sheets, candidate cuts, audio measurements, detector thresholds, VLM observations, confidence scores, coverage state, and provenance tags.
2. **Viewing judgment**: musical entry or release, rhythmic acceleration, a held expression, a sudden reduction in motion, a change of attention, a readable technical operation, or a changed relation between passages.
3. **Reader-facing expression**: what happens, how it feels or reads, how the edit achieves it, and why its placement matters.

Move through all three layers. Draft the response from layers 2 and 3. Do not paraphrase machine artifacts into prose.

## Use tools as prompts for verification

- Let audio measurements point to intervals worth listening to. Establish phrases, accents, vocal entries, instrumental changes, suspensions, releases, and silence by listening in context.
- Let candidate cuts point to boundaries worth watching. Describe verified cuts, flashes, replacements, holds, and transitions as experienced in playback.
- Let sampling and VLM output point to details worth rechecking. Establish motion, identity, continuity, text, and gaze from adequate local context.
- Let confidence and provenance fields discipline claims internally. Express only meaningful uncertainty in ordinary language.

Never use a measurement as a substitute for a musical, visual, or emotional judgment.

## Hide internal aids by default

Exclude the following from normal output:

- RMS, dBFS, spectral centroid, energy bands, thresholds, and waveform statistics;
- candidate-cut counts, detector scores, sampling FPS, frame counts, model names, token estimates, and VLM output;
- confidence decimals, coverage percentages, boundary-review status, internal IDs, and schema labels;
- workflow narration such as “after blind viewing,” “automatic detection shows,” or “the model verified the whole video.”

Reveal these only when the user explicitly requests methodology, evidence auditing, reproducibility, or tool diagnostics. Put them in a separate method appendix so they do not interrupt the reading of the work.

Technical media facts such as duration, resolution, frame rate, or codec belong in the response only when they answer the request or affect a visible result.

## Keep acquisition limits attached to the copy

Separate the finished work from the platform transcode, downloaded file, sampled frame, screenshot, OCR result, and any enlargement used during analysis. A low-resolution copy can support broad composition, order, rhythm, and large text while leaving small typography, edges, texture, compression, and fine compositing unresolved.

When a limitation affects a claim, state it once and reserve that claim: “当前取得的公开下载副本为 480p，其中的小字号文字无法可靠辨认；这一限制不计入作品评价。” Do not describe the work itself as illegible, rough, compressed, or lacking detail until a sufficiently faithful source confirms it. Upscaling and sharpening can aid inspection but do not restore missing evidence.

## Translate internal findings

| Internal aid or label | Reader-facing judgment |
|---|---|
| audio level rises | the drums and vocal push forward here; the passage feels more urgent |
| level stays similar across sections | the music keeps its drive while the edit creates contrast by reducing color and motion |
| dense candidate boundaries | a run of flashes and short replacements speeds up the transition |
| long detected duration | the edit holds on the expression long enough for the line to settle |
| `subject_role_migration` | attention gradually moves from the group to this character's response |
| `graphic_match` | the cut keeps the eye in the same screen position, so the new image arrives cleanly |
| low confidence | the finished image suggests this treatment, though the exact construction cannot be confirmed |
| high text density with adequate hold | the image settles and gives the thought time to unfold |
| repeated asset with expanded crop | the earlier view withheld the other person; the wider return now makes the exchange legible |
| repeated line under changed context | the same words return after the relationship has changed, so they now read as an answer rather than a promise |

Keep useful timestamps and durations when they help the reader locate or feel a decision. Explain the perceptual consequence instead of presenting the number as proof.

## Write music as it is heard

Prefer phrases a viewer or editor would naturally use:

- the vocal enters or drops out;
- the drums become busier or pull back;
- the phrase reaches its release;
- a cut lands on the downbeat;
- several movements follow one musical phrase;
- the picture holds through the beat;
- the lyric and image briefly answer each other;
- the music continues while the image suddenly becomes still;
- the ending lets the sound fall away.

Use technical musical terminology only when it is audible, relevant, and understood well enough to apply accurately.

## Preserve useful technical explanation

For craft analysis, write:

`visible result -> editing or design operation -> viewing effect -> role in the passage`

Add a plausible implementation only when the user asks about technique and the inference helps. Phrase it naturally: “The character appears to have been separated from the panel and placed into a shared layout.” Do not guess software, plugins, project structure, layer count, labor, or production time.

Internal mechanism labels may guide reasoning. Replace them in normal prose with concrete operations and effects. A specialist term may remain when it is standard, useful, and explained by the visible example.

## Match the output mode

- **Appreciation**: write as an attentive viewer whose understanding can develop. Present selected moments, first impressions, later clarification, rewatch, preferences, and enough craft to make them specific. Prefer continuous paragraphs without headings.
- **Complete 拉片**: keep a continuous timeline in timestamped prose with `time -> content -> audiovisual or technical choice -> connection to adjacent or recurring elements -> event, relationship, information, and placement`. The time ranges demonstrate coverage; do not report coverage statistics.
- **Technical and arrangement analysis**: emphasize visible operations, execution, rhythm, handoffs, development, narrative connection, and payoff. Keep implementation uncertainty brief. Organize around decisive passages rather than a fixed craft taxonomy.
- **Method audit**: expose tools, measurements, sampling, confidence, and verification only because the user explicitly requested them.

## Keep structure subordinate to the reading

Use continuous prose by default. A short appreciation normally needs no headings, bullets, table, executive summary, or closing recap. A complete 拉片 normally needs timestamped passage labels and paragraphs, not a multi-column table. A technical analysis may use a few descriptive headings when the work has clear movements that benefit from navigation.

Use a table only when the user asks for one, when comparing multiple works or versions, or when many exact repeated-field mappings would be harder to verify in prose. Do not create categories simply because the internal analysis has categories. Vary paragraph length according to the importance of the passage and avoid ending every section with a miniature thesis.

When text or limited material is central, keep the tracking machinery hidden. Describe whose words the viewer follows, what becomes understandable, what an image initially withholds, and how a return changes its force. Do not report character counts, reading-speed estimates, asset counts, crop labels, or disclosure-state names unless the user requests a method audit.

## Final reader audit

Before returning the response, ask:

- Is this sentence about the work or about how the model analyzed the work?
- Could an attentive viewer say it after watching the passage?
- Does every number clarify a viewing decision?
- Has audio been interpreted by listening rather than inferred from measurements alone?
- Does each technical term explain something visible or audible?
- Can an internal taxonomy be replaced with plain language without losing precision?
- Did the user explicitly request any methodology that remains in the response?
- Does the structure help the reader follow this work, or does it display the analysis framework?
- Can a heading, list, table, summary, or repeated conclusion be removed without losing clarity?

Delete sentences whose main purpose is to prove that analysis work was performed.
