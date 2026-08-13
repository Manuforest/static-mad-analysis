---
name: analyze-static-mad
description: Analyze static-image MADs through a subject-centered video-understanding core and a mature static-MAD adapter, with provisional AMV and ASMV extensions for explicitly requested experiments. Use when Codex is asked to watch, interpret, explain, compare, review, or technically analyze a 静止系MAD, 静止画MAD, manga MAD, Galgame MAD, image-based AMV, or—on an explicitly provisional basis—a footage-based AMV, ASMV, edited MV, or hybrid fan edit.
---

# Analyze Edited Video

Reconstruct the work as an authored audiovisual system. Use the shared core for subjects, events, time-space, sound, and evidence. Treat static MAD as supported; label AMV and ASMV findings `provisional_extension`.

## Route the analysis

Always read [core-understanding.md](references/core-understanding.md) and [shot-by-shot-analysis.md](references/shot-by-shot-analysis.md), then select the smallest adapter set supported by observable media behavior:

- **Static MAD — supported**: read [type-static-mad.md](references/type-static-mad.md) when still images, manga panels, sprites, typography, crops, masks, compositing, or fabricated camera motion carry the action.
- **AMV — provisional**: read [type-amv.md](references/type-amv.md) only when the user explicitly requests footage-based AMV analysis or experimentation beyond static MAD.
- **ASMV — provisional**: read [type-asmv.md](references/type-asmv.md) only when the user explicitly requests dialogue-led analysis or experimentation.

Load other references only when needed:

- [temporal-relations.md](references/temporal-relations.md) for nonlinear, ambiguous, repeated, mediated, or densely intercut time-space;
- [original-work-context.md](references/original-work-context.md) after the blind pass when the source is identifiable;
- [evidence-schema.md](references/evidence-schema.md) for detailed, auditable, or multi-observer records;
- [montage-grammar.md](references/montage-grammar.md) for symbolic inserts, fabricated composites, graphic matches, typography, or screen mediation;
- [material-economy-and-reveal.md](references/material-economy-and-reveal.md) when limited CGs, panels, sprites, absent viewpoint characters, repeated source images, crop-based withholding, or staged reveals organize the work;
- [text-led-narrative.md](references/text-led-narrative.md) when dialogue, monologue, letters, narration, quotations, or other readable text carries substantial event, causality, psychology, viewpoint, relationship, or emotional development;
- [craft-analysis.md](references/craft-analysis.md) when the user requests technique, critique, comparison, or improvement advice;
- [appreciation-writing.md](references/appreciation-writing.md) when the user requests an appreciation, review, short comment, or other audience-facing evaluative prose;
- [audience-facing-translation.md](references/audience-facing-translation.md) before every user-facing appreciation, 拉片, technical analysis, review, or report;
- [community-reading-framework.md](references/community-reading-framework.md) for static-MAD community vocabulary, arrangement diagnosis, or reception research;
- [qwen-vl.md](references/qwen-vl.md) and [vlm-prompt.md](references/vlm-prompt.md) before external VLM use;
- [failure-modes.md](references/failure-modes.md) for the final audit.

For hybrids, tag claims by mechanism, such as `static_constructed_motion`, `source_footage_action`, `edit_created_relation`, or `recontextualized_speech`. Do not select adapters from the upload title alone.

## Core constraints

- Complete a blind chronological pass before consulting source summaries or creator explanations.
- Complete chronological shot coverage before drafting an interpretation or appreciation. Treat detector output as candidate boundaries, not a finished shot log.
- Ground major claims in timestamped context before and after the relevant moment.
- Track how elements connect to events, responses, relationships, and viewer knowledge across adjacent and repeated passages; do not stop at naming imagery or technique.
- Judge text by its task, readability, timing, emotional progression, and relation to the image. Never infer quality from text quantity alone.
- Judge repeated or limited source material by reveal control, changed context, relational work, and payoff. Never infer weakness from asset quantity or repetition alone.
- Require multiple identity anchors and keep uncertain roles provisional.
- Do not force a protagonist; the subject may be a relationship, group, place, emotion, institution, force, or musical proposition.
- Distinguish playback order from reconstructed chronology and depicted action from edit-constructed motion.
- Treat lyrics and quotations as authored audio material, not automatic speech by the visible person.
- Keep observation, video-grounded inference, original-work context, other external context, and documented creator intent separate.
- Use original-work context to explain editorial transformation, not fidelity, completeness, omitted-information cost, non-source-viewer readability, or competition suitability.

## Workflow

### 1. Establish the surface

Accept a local video or an authorized HTTP/HTTPS video URL. For a public URL that requires local media analysis, run `scripts/fetch_video.py` or pass the URL directly to `scripts/prepare_analysis.py` before asking the user to download it manually. Store acquired media and metadata inside the analysis workspace, never inside the skill directory.

Attempt public access without cookies first. If acquisition fails, report the exact blocker: missing dependency, disabled network, authentication, region restriction, unavailable media, DRM, or insufficient permission. Use `--cookies-from-browser` only after the user explicitly authorizes access to a local browser session. Never print, copy, persist, upload, or expose cookies, tokens, request headers, or account data. Do not bypass access controls.

Record title, credits, duration, frame rate, resolution, audio, subtitles or lyrics, and creator notes. Build an interval type map and revise it after inspection. Store artifacts in a user-approved directory without overwriting the source.

### 2. Prepare evidence

Run the bundled workflow when local analysis is available:

```powershell
& $python scripts/prepare_analysis.py $videoOrUrl --output-dir $analysisDir --focus 80:100:8
```

The command accepts either a local path or an HTTP/HTTPS URL. For a URL, it downloads one authorized video into `$analysisDir/source`, writes `metadata.json` and `download-manifest.json`, resolves the local media path, and continues the normal FFmpeg workflow. If `yt-dlp` is missing and dependency installation is permitted, ask before installing from the skill-local `requirements.txt`; do not send the user away to perform the download manually before an automated public attempt has failed.

For an acquisition-only check or metadata test, run:

```powershell
& $python scripts/fetch_video.py $videoUrl --output-dir "$analysisDir/source" --metadata-only
```

Use coarse-to-fine sampling. Scene detection is an attention cue, not ground truth. Increase density around unstable identity, action phase, gaze, text, source-scene boundaries, flash inserts, match cuts, or sound-image relations. Partition dense intervals into shots before interpreting them.

The prepared `shots.json` is machine evidence. Revise its boundaries into analytical shots or explicitly defined shot clusters in `evidence/shot_reading.jsonl`. Map musical sections manually in `evidence/timeline.json`; audio energy windows do not by themselves establish phrases, climaxes, or semantic alignment.

Use a VLM only as a fallible second observer. Estimate cost before external upload, obtain authorization, and verify motion, identity, text, speaker, and continuity claims locally.

### 3. Complete the shot-by-shot reading

Follow [shot-by-shot-analysis.md](references/shot-by-shot-analysis.md). After the blind global pass, map functional and musical sections, verify or revise candidate boundaries, and account for the full playback duration with shots or justified shot clusters.

Record every shot at coverage level: time, visible content, music or sound position, primary edit operation, and relation to the preceding shot. Enrich important or ambiguous shots with audiovisual relation, editorial function, viewer effect, provenance, alternatives, and confidence. Separate what the source material already supplies from what selection, timing, reframing, compositing, adjacency, and musical placement make newly operative.

Do not draft a polished interpretation or appreciation until chronological coverage exists. A small set of selected timestamps is supporting evidence drawn from the completed shot reading, not a substitute for it.

### 4. Reconstruct the video body

Follow the core in order:

1. perform the blind global pass and segment functional chapters;
2. establish entities, subject roles, and focalization;
3. build event-response-state-consequence chains;
4. classify shot relations and reconstruct relevant clocks;
5. align image, motion, sound, music, and viewer disclosure;
6. generate and falsify at least two editorial-thesis hypotheses.

Do not write a polished plot before these records exist.

### 5. Apply adapters and diagnose arrangement

Use adapters to identify how evidence is produced, then return findings to the shared subject, event, time-space, sound, and thesis model. For static material, distinguish depicted action from crop, layer, mask, typography, transition, and uncertain constructed motion.

When arrangement diagnosis is requested, use the community framework to inspect subject, information, emotional, and visual organization; source-summary compression; relation gaps; tonal continuity; shot handoffs; and audiovisual escalation. Describe mechanisms and viewing effects, not contest fitness.

### 6. Add context in order

After freezing the blind-pass records:

1. use the original work only to establish relevant identities, relationships, scene placement, chronology, viewpoint, and prior motif functions, then map what the edit changes;
2. use creator notes to confirm, correct, narrow, complicate, or inspire—never to erase independently supported effects.

Synthesize three interpretive layers: **video body**, **original-work context**, and **creator expression**.

### 7. Add craft or reception only when relevant

For craft, use:

`timestamped evidence -> operation -> execution qualities -> formal/perceptual/narrative/display function(s) -> limitation or alternative`

Allow graphic, spatial, atmospheric, decorative, structural, and showcase value without inventing narrative justification or splitting craft into separate scoring systems.

Research comments or reviews only when the user requests community reception, provides such material, or asks why a work produced a particular response. Treat reception as auxiliary evidence after video-body analysis, not as a fourth interpretive layer or proof of author intent, technical quality, or award suitability.

### 8. Report and audit

Before drafting any audience-facing response, read [audience-facing-translation.md](references/audience-facing-translation.md). Convert machine evidence and internal taxonomy into verified viewing judgments first. Draft from what a viewer can see, hear, understand, and evaluate. Keep detector output, measurements, sampling details, VLM notes, confidence scores, schema labels, and workflow status private unless the user explicitly requests a method or evidence audit.

Select the output from the user's intent:

- for a detailed, technical, or research-style analysis, use [report-template.md](assets/report-template.md);
- for an appreciation, review, or short comment, read [appreciation-writing.md](references/appreciation-writing.md) and turn the internal shot record into selective, natural prose;
- for an explicit 拉片 or shot-by-shot request, expose a continuous reader-facing timeline in timestamped prose, connecting content and technique to events, responses, relationships, viewer knowledge, and structural placement rather than reproducing the internal shot record;
- for a brief answer, keep the internal evidence discipline but report only the central judgment and strongest supporting passages.

Do not dump the internal shot log into an appreciation. Lead detailed reports with the main interpretation and state only uncertainty that changes how the reader should understand it. Lead appreciations with the most specific viewing judgment rather than a methodology preface.

Before finalizing, verify that:

- identities and subject roles have multiple anchors;
- the full playback duration is covered by verified shots or justified clusters before selected passages are interpreted;
- meaningful events include responses and state changes, or relation gaps are marked;
- playback, story, subjective, music, and disclosure order are not collapsed;
- depicted, source-footage, retimed, crop/layer, transition, and uncertain motion are distinguished where relevant;
- major interpretations have timestamped support, alternatives, and counterevidence;
- original-work facts, creator notes, and reception material retain provenance;
- craft is explained through mechanisms and effects rather than effort, software, layer count, popularity, or narrative usefulness alone;
- appreciation prose remains work-specific, selective, and traceable to the shot reading rather than merely conversational;
- appreciation prose states judgments directly, contains no “不是……而是……” rhetorical reversal or equivalent template, and removes metaphors that would sound affected in ordinary spoken commentary;
- normal audience-facing output contains no detector statistics, sampling details, raw audio measurements, confidence decimals, schema labels, or workflow narration;
- music claims describe audible phrases, accents, entries, releases, holds, and sound-image relations verified by listening rather than treating audio measurements as conclusions;
- appreciation prose preserves the viewer's developing experience when useful, including first impression, later clarification, rewatch, preference, and unresolved response without pretending to be omniscient;
- 拉片 and craft prose follow elements through adjacency, recurrence, narrative consequence, and changed viewer knowledge instead of assigning fixed symbolic meanings or ending at technique names;
- text-led passages identify voice, addressee, new information or state change, reading conditions, and image-text relation where relevant; praise or criticism never rests on text quantity;
- repeated assets are traced as the same source material through crop scope, disclosure stage, changed context, and later payoff rather than counted as separate shots or dismissed as reuse;
- audience-facing structure remains restrained: use continuous prose and timestamped passages by default, avoid tables for single-work analysis, and add headings or lists only when they materially aid navigation;
- the analysis does not become a fidelity, accessibility, ranking, award, or competition judgment.
