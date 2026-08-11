---
name: analyze-static-mad
description: Analyze static-image MAD/AMV/MV videos through human-like multi-pass viewing, adaptive frame sampling, subject and identity tracking, narrative time-space reconstruction, montage analysis, and audio-visual alignment. Use when Codex is asked to watch, interpret, critique, compare, or explain a 静止系MAD, 静止画MAD, manga MAD, edited music video, image-based AMV, or other highly edited narrative video where sparse frames, symbolism, recurring motifs, typography, flash cuts, or non-linear editing carry meaning.
---

# Analyze Static MAD

Treat video understanding as evidence-guided reconstruction, not frame caption aggregation. Separate observation from inference and external source knowledge. Never claim a unique interpretation when the edit remains ambiguous.

## Required resources

Read these before analysis:

- [temporal-relations.md](references/temporal-relations.md) for shot-to-shot time-space classification.
- [evidence-schema.md](references/evidence-schema.md) for entity, relation, hypothesis, and confidence records.

Additionally read:

- [montage-grammar.md](references/montage-grammar.md) for stylized edits, repeated frames, symbolic inserts, graphic matches, typography, or screen-within-screen compositions.
- [static-mad-rubric.md](references/static-mad-rubric.md) only when the user requests critique, scoring, technique analysis, or improvement advice.
- [failure-modes.md](references/failure-modes.md) before forming the final interpretation.

## Core constraints

- Do not infer plot from isolated frames.
- Do not equate playback order with story chronology.
- Do not read a source synopsis before completing a blind video pass.
- Do not identify a character from hairstyle alone. Require at least two independent anchors or mark the identity provisional.
- Do not count inverted, masked, recolored, or reframed versions of one image as separate events without evidence.
- Do not force symbolic inserts into physical space-time.
- Do not treat lyrics as character dialogue unless the edit explicitly attributes them.
- Do not interpret visual density as fast story time by default.
- Ground important claims in timestamped preceding-and-following evidence.
- Preserve competing interpretations and confidence when evidence conflicts.

## Workflow

### 1. Establish the source

Prefer a user-provided local video. For a URL, use an available browser or connector only within the user's authorized session. Never expose cookies or session tokens. Record title, creator, duration, frame rate, resolution, audio availability, subtitles/lyrics, and any creator statement separately from video observations.

Store working artifacts in a user-approved output directory. Do not overwrite the source.

### 2. Prepare deterministic artifacts

Use `scripts/prepare_analysis.py` for the first pass. It creates:

- `manifest.json`: media metadata;
- `shots.json`: candidate cut boundaries, not ground truth;
- `frames/overview`: low-density global frames;
- `frames/focus`: dense samples around candidate cuts and requested intervals;
- `contact_sheets`: timestamped overview sheets;
- `audio/audio_profile.csv`: short-window energy and spectral profile;
- `evidence/`: empty timeline, entity, relation, observation, and hypothesis records.

Example:

```powershell
& $python scripts/prepare_analysis.py $video --output-dir $analysisDir --focus 80:100:8
```

If `python` is unavailable, use a bundled workspace Python. The scripts locate FFmpeg from an explicit argument, `STATIC_MAD_FFMPEG`/`STATIC_MAD_FFPROBE`, or `PATH`. Never assume a machine-specific install directory.

Scene detection is only an attention cue. Flashes, luma changes, ink wipes, and glitch can create false cuts; slow dissolves can hide real semantic boundaries.

### 2a. Optionally use an external video-language model

Use a VLM only as a fallible second observer, never as the evidence ledger. Read [qwen-vl.md](references/qwen-vl.md) before sending video to Qwen. External upload requires the user's authorization and their own API key. Never accept, log, print, or commit an API key as a command-line argument or source-code literal.

Run a cost estimate before every upload:

```powershell
& $python scripts/call_qwen_vl.py $video --prompt-file $prompt --fps 1 --dry-run
```

After the user approves the estimated upload and token budget, rerun with `--send`. The script reads `QWEN_API_KEY` or `DASHSCOPE_API_KEY` from the environment and writes only the response and usage metadata.

Use a 1 fps whole-video pass for provisional chapters and OCR. Use higher density only on short, identified intervals. Never treat higher fps as proof of better reasoning: a VLM may smooth separate edits into invented physical motion. Verify every claimed turn, gaze, gesture, object interaction, or continuous action against timestamped adjacent frames and candidate shot boundaries.

### 3. Blind global pass

Inspect all overview contact sheets in chronological order. Do not consult source plot material yet.

Record only:

- dominant visual systems and their time ranges;
- apparent emotional and audio energy curve;
- recurring people, body parts, objects, text, colors, and interfaces;
- possible chapter boundaries;
- unresolved questions.

Do not write a complete story in this pass. Use provisional labels such as `person_a` and `person_b`.

### 4. Segment semantic chapters

Combine visual cuts with audio phrases and meaning changes. A chapter boundary is stronger when at least two of these change:

- color/light system;
- location or spatial logic;
- focal character;
- music phrase, instrumentation, or energy;
- typography mode;
- recurring motif behavior;
- editing density;
- narrative question.

Do not use equal-duration chapters unless evidence supports them.

### 5. Establish entities and subjects

Maintain an entity ledger using `references/evidence-schema.md`. Track identity across style changes with multiple anchors: face, clothing, accessory, pose, screen direction, associated object, interaction partner, and adjacent action.

For every chapter, distinguish:

1. visual subject — highest salience in the frame;
2. shot subject — what composition and camera motion organize;
3. action subject — who initiates or changes something;
4. focalizer — whose seeing, knowing, memory, or uncertainty structures the sequence;
5. dramatic subject — whose state changes;
6. thematic subject — the person, relationship, idea, or force the work examines.

Allow focalization to shift over time. Do not force the focalizer to be the most visible person.

### 6. Classify shot-to-shot relations

For meaningful adjacent shots, classify the relation using `references/temporal-relations.md`. Start with physical continuity but actively test alternatives such as ellipsis, flashback, viewpoint switch, repeated memory, fantasy, screen mediation, graphic match, symbolic association, contrast, and sound bridge.

Record a relation only after inspecting context on both sides. For a key transition, inspect at least the preceding shot, transition frames, following shot, and later recurrence of either image.

### 7. Revisit suspicious intervals adaptively

Increase temporal resolution when any of these occurs:

- identity becomes ambiguous;
- a hand, gaze, or action may continue across a cut;
- text lasts briefly;
- a frame repeats with altered polarity or crop;
- a flash or black frame may conceal an insert;
- a motif returns after a long interval;
- the proposed time-space relation has low confidence;
- audio and visual boundaries disagree.

Use 4 fps for normal inspection, 8–12 fps for high-change passages, and original frame rate within roughly ±0.5 seconds of suspected insert frames or match cuts. Add explicit intervals with `sample_frames.py --focus START:END:FPS` or rerun `prepare_analysis.py` into a new analysis directory.

Before narrating a dense interval, partition it into shots. For each observed change, label its source as one of: `diegetic_subject_motion`, `camera_or_crop_motion`, `layer_or_mask_motion`, `typography_motion`, `transition`, or `uncertain`. Do not convert a sequence of cuts into character motion merely because the same emotional subject persists.

### 8. Analyze montage as syntax

Use `references/montage-grammar.md`. Ask what meaning is created by adjacency, not only what each frame depicts. Track how later images invade, erase, infect, frame, or reinterpret earlier images.

For repeated images, compare:

- first and later context;
- crop and scale;
- color polarity;
- overlay and masking;
- music position;
- accompanying text;
- whether the repetition changes agency or emotional valence.

### 9. Align audio, lyrics, and edit

Use the audio profile to locate candidate energy changes, then listen to the actual audio when available. Distinguish:

- beat alignment;
- phrase-boundary alignment;
- energy alignment;
- lyric-semantic alignment;
- deliberate counterpoint.

For each important visual change, state which layer it aligns with. A cut on a beat is not automatically a narrative beat.

### 10. Generate and falsify hypotheses

Produce two or three candidate interpretations before selecting a leading one. Each hypothesis must include:

- claim;
- timestamped supporting evidence;
- contradictory or missing evidence;
- alternative explanation;
- confidence;
- a useful interval to revisit.

Prefer the hypothesis that explains more repeated structures with fewer unsupported assumptions. Do not use smooth prose as a substitute for evidence.

### 11. Add external context after blind analysis

Only now consult official source summaries, lyrics, creator notes, or interviews when available. Keep external facts separate. Record whether each item confirms, weakens, or merely inspires an interpretation.

Do not retroactively present source knowledge as something visible in the video.

### 12. Report in layers

Lead with the main interpretation and its confidence. Then present:

1. directly observed timeline;
2. entity and focalization changes;
3. reconstructed time-space model;
4. montage and audio-visual evidence;
5. leading narrative/theme interpretation;
6. alternatives and unresolved ambiguities;
7. source-context revisions;
8. critique or score only when requested.

Use timestamps throughout. Include representative contact sheets or local frame links when they materially support the explanation.

## Analysis completion gate

Before finalizing, verify:

- every named character has adequate identity evidence;
- the main focalizer claim uses at least one shot chain, not a single frame;
- reality, memory, fantasy, and symbolism are not collapsed into one timeline;
- recurring motifs have been compared across appearances;
- major music phrases were considered;
- high-change sections received denser inspection;
- any VLM-generated motion claim was checked against adjacent local frames and shot boundaries;
- external upload and estimated token cost were approved before a VLM call;
- the leading interpretation names counterevidence;
- external knowledge is visibly separated from blind-read evidence;
- claims are labeled as observation, strong inference, weak inference, or external fact.
