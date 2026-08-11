---
name: analyze-static-mad
description: Analyze static-image MAD/AMV/MV videos through human-like repeated viewing, adaptive frame sampling, subject and focalizer tracking, event-response narrative reconstruction, material-treatment analysis, montage grammar, music-form alignment, and evidence-calibrated craft interpretation. Use when Codex is asked to watch, interpret, explain, compare, review, or technically analyze a 静止系MAD, 静止画MAD, manga MAD, Galgame MAD, image-based AMV, edited MV, or another highly edited video in which still images, typography, compositing, motifs, flash cuts, or non-linear chronology carry meaning.
---

# Analyze Static MAD

Treat the work as an authored audiovisual construction, not a sequence of frame captions. Reconstruct how events, reactions, music, visual systems, and editing relations cooperate to produce meaning. Preserve ambiguity when the evidence does not determine one reading.

## Read the supporting guidance

Always read:

- [temporal-relations.md](references/temporal-relations.md) for time-space, event-response, and narrative-topology analysis;
- [evidence-schema.md](references/evidence-schema.md) for auditable records;
- [community-reading-framework.md](references/community-reading-framework.md) for static-MAD terminology and interpretation logic;
- [failure-modes.md](references/failure-modes.md) before finalizing.

Read [montage-grammar.md](references/montage-grammar.md) when the work uses symbolic inserts, repeated images, fabricated composites, typography, graphic matches, intensive compositing, or screen-within-screen arrangements.

Read [craft-analysis.md](references/craft-analysis.md) only when the user requests critique, comparison, technique analysis, or improvement advice.

## Epistemic layers

Keep these layers visibly separate throughout the analysis:

1. **Observation** — directly visible or audible evidence.
2. **Video-grounded inference** — an explanation supported by adjacent shots or recurring structures.
3. **External context** — information obtained outside the video; use only when the user explicitly requests contextual comparison or it is necessary for the named task.
4. **Documented author intent** — a claim explicitly made in creator notes, interviews, or project commentary.

Never rewrite layers 3 or 4 as though they were discovered from the video alone.

## Non-negotiable constraints

- Do not infer plot, identity, intention, or physical motion from an isolated frame.
- Do not equate playback order with story chronology.
- Complete a blind pass before consulting a source synopsis or creator explanation.
- Require multiple identity anchors; mark uncertain names and roles provisional.
- Treat recolors, crops, masks, and repeats as possible transformations of one source image rather than new events.
- Do not force symbolic or graphic relations into literal time-space.
- Do not treat lyrics as dialogue without explicit attribution.
- Do not assume more motion, effects, layers, or cuts mean better craft.
- Ground major claims in timestamped context before and after the relevant shot.
- Maintain alternatives and counterevidence instead of polishing uncertainty away.

## Workflow

### 1. Establish the analysis surface

Prefer a local video supplied or authorized by the user. For a URL, use an available browser or connector only within the authorized session. Never expose cookies, tokens, or account data.

Record media metadata, title, credited creator, duration, frame rate, resolution, audio, subtitles or lyrics, and the availability of creator notes. Do not consult creator statements or original-work summaries unless the user requests that context; if used, wait until the blind pass is complete.

Store artifacts in a user-approved output directory without overwriting the source.

### 2. Prepare deterministic evidence

Run `scripts/prepare_analysis.py` for the initial pass:

```powershell
& $python scripts/prepare_analysis.py $video --output-dir $analysisDir --focus 80:100:8
```

The output includes media metadata, candidate cuts, overview frames, dense focus frames, contact sheets, an audio profile, and empty evidence records. Scene detection is an attention cue, not ground truth: flashes may create false cuts and dissolves may hide semantic boundaries.

If Python is unavailable, use a bundled workspace Python. Resolve FFmpeg through an explicit argument, `STATIC_MAD_FFMPEG` / `STATIC_MAD_FFPROBE`, or `PATH`; do not assume a machine-specific location.

### 2a. Optionally use a video-language model

Use a VLM only as a fallible second observer. Read [qwen-vl.md](references/qwen-vl.md) before a Qwen upload and [vlm-prompt.md](references/vlm-prompt.md) before prompting any VLM. External upload requires user authorization and the user's own environment-provided key.

Always estimate cost first:

```powershell
& $python scripts/call_qwen_vl.py $video --prompt-file $prompt --fps 1 --dry-run
```

Use a low-density whole-video pass for provisional chapters and OCR, then increase density only on short uncertain intervals. Verify all claimed gestures, gazes, actions, and spatial continuities against adjacent local frames and cut boundaries.

### 3. Perform a blind global pass

Inspect the overview chronologically without source-plot material. Record:

- dominant visual systems and provisional chapter boundaries;
- emotional and musical energy curves;
- recurring people, objects, body fragments, colors, text, interfaces, and spaces;
- possible focal characters and unresolved identity conflicts;
- apparent changes in information density and processing density;
- questions the edit creates and later answers.

Use labels such as `person_a` and `object_b`. Do not write a complete plot yet.

### 4. Segment chapters by function

Combine candidate cuts with changes in meaning and musical form. A boundary becomes stronger when at least two signals change: focalizer, dramatic question, location logic, color/light, typography, motif behavior, edit density, music phrase, instrumentation, energy, or lyrical function.

Give each chapter a task such as premise-sharing, trigger, development, conflict, accumulation, reversal, release, closure, or aftertaste. Do not force the familiar verse-to-chorus arc when the work deliberately inverts it.

### 5. Establish subjects, entities, and focalization

Track identity with face, clothing, accessory, pose, screen direction, associated object, interaction partner, and adjacent action. Distinguish:

1. visual subject — highest frame salience;
2. shot subject — what composition and camera treatment organize;
3. action subject — who initiates a change;
4. focalizer — whose seeing, knowing, memory, or uncertainty structures the sequence;
5. dramatic subject — whose state changes;
6. thematic subject — the relationship, idea, person, or force under examination.

Allow these roles to diverge and shift.

### 6. Build event-response-state chains

For each narratively important event, inspect what follows. Record:

`event -> subject response -> state or relationship change -> next consequence`

A response may be facial, gestural, spatial, typographic, musical, symbolic, or an intentional absence. If the edit jumps from incident to incident without showing or implying response, mark a possible causal gap rather than inventing one.

Classify the broader topology as single-thread transformation, dual-thread relational development, multi-thread convergence, episodic accumulation, or deliberately fragmented/associative construction. Use [temporal-relations.md](references/temporal-relations.md).

### 7. Reconstruct time and space

Classify meaningful shot relations before constructing chronology. Test physical continuity against ellipsis, flashback, anticipation, viewpoint change, repeated memory, fantasy, screen mediation, graphic match, symbolic association, contrast, and sound bridge.

Maintain playback, shot, story, subjective, music, and viewer-disclosure time separately. For important transitions, inspect the preceding shot, transition frames, following shot, and later recurrence.

### 8. Revisit uncertain intervals adaptively

Increase sampling when identity is unstable, a hand or gaze may continue across a cut, text is brief, a frame repeats with altered treatment, a flash may hide an insert, a motif returns, audio and visual boundaries disagree, or the proposed relation has low confidence.

Use roughly 4 fps for normal inspection, 8–12 fps for dense editing, and original frame rate near suspected inserts or match cuts. Partition a dense interval into shots before narrating it. Label visible change as `diegetic_subject_motion`, `camera_or_crop_motion`, `layer_or_mask_motion`, `typography_motion`, `transition`, or `uncertain`.

### 9. Recover the editorial thesis and material logic

Infer two or three provisional answers to: **what relationship, contradiction, state change, or idea does this edit organize as important?** Test them against the whole work.

Record visible material treatment as selection/crop, separation/redraw, compositing/reconstruction, fabricated composite, external asset, treatment-only, or uncertain. Do not infer fidelity to, deviation from, or completeness relative to the original work unless the user explicitly asks for an original-work comparison and supplies or authorizes appropriate context.

### 10. Analyze montage and global expression systems

Use [montage-grammar.md](references/montage-grammar.md). Read adjacency as syntax and track systems across the entire work:

- recurring colors, objects, borders, line treatments, text modes, screens, or spaces;
- how their meaning changes rather than assigning a fixed symbol dictionary;
- how a repeated source image is recontextualized;
- whether processing density distinguishes past/present, intimacy/distance, control/disorder, or another state;
- whether effects serve revelation, concealment, fragmentation, contamination, transition, or decoration.

Inspect the base composition before praising animation. Separate single-frame hierarchy from what movement adds.

### 11. Align music, motion, and reading time

Distinguish beat, phrase, energy, lyric-semantic, structural, and contrapuntal alignment. For each major passage, ask:

- what narrative task the musical section performs;
- whether motion amplitude and easing fit the musical and emotional state;
- whether a hold allows expression or text to be read;
- whether cutting the song damages accumulation or release;
- whether dynamic/static contrast creates emphasis;
- whether visual-change density and semantic density diverge.

A beat-synchronous cut is not automatically a narrative beat.

### 12. Generate and falsify interpretations

Produce at least two candidate interpretations. Each must include a claim, timestamped support, counterevidence, alternative explanation, confidence, and a useful interval to revisit. Prefer the explanation that accounts for more repeated structures with fewer unsupported assumptions.

### 13. Add external context only when requested

If the user requests comparison with the original work, lyrics, creator notes, interviews, or project commentary, consult them only after the blind analysis. Record whether each external item confirms, weakens, corrects, or merely inspires the video-grounded reading.

Do not treat creator intent as the only valid audience experience. Report meaningful gaps between observable effect, plausible interpretation, and documented intention.

### 14. Explain craft through effects

When critique or technique analysis is requested, use [craft-analysis.md](references/craft-analysis.md). Explain each important choice as `evidence -> operation -> perceptual or narrative effect -> limitation/alternative`. Analyze narrative organization, emotion, subject/focalization, composition, animation, compositing, music/edit structure, visual design, atmosphere, and finish as interacting mechanisms rather than isolated checkboxes.

Do not infer effectiveness from popularity, software complexity, layer count, or the number of effects. Give improvement advice only when requested, and tie it to timestamped evidence and the work's own apparent aims.

### 15. Report in layers

Use [report-template.md](assets/report-template.md) when a detailed report is requested. Lead with the main interpretation and confidence, then present the observable timeline, event-response chains, focalization, time-space reconstruction, material treatment, expression systems, music/motion design, alternatives, optional external-context revisions, and craft analysis.

Use timestamps and representative frames wherever they materially support the argument.

## Completion gate

Before finalizing, verify that:

- identities and focalizer claims use multiple anchors and shot chains;
- key events include their reactions or an explicit note that the reaction is absent;
- narrative topology and major state changes are stated;
- reality, memory, fantasy, symbolism, and playback order are not collapsed;
- recurring motifs are compared across appearances rather than decoded once;
- material treatment is described without unsupported claims about the original work;
- music sections, holds, motion amplitude, and reading time are considered;
- dense passages received denser inspection;
- VLM motion claims were locally verified;
- every external upload passed authorization and cost gating;
- the leading interpretation includes counterevidence;
- author intent and source knowledge remain separate from blind evidence;
- craft commentary explains how choices function instead of assigning category fitness;
- important claims are labeled observation, video-grounded inference, external context, or documented author intent.
