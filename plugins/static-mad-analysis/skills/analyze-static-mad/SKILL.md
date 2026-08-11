---
name: analyze-static-mad
description: Analyze static-image MADs through a shared subject-centered video-understanding core and a mature static-MAD adapter, with provisional AMV and ASMV extensions for explicitly requested experiments. Use when Codex is asked to watch, interpret, explain, compare, review, or technically analyze a 静止系MAD, 静止画MAD, manga MAD, Galgame MAD, image-based AMV, or—on an explicitly provisional basis—a footage-based AMV, ASMV, edited MV, or hybrid fan edit.
---

# Analyze Edited Video

Reconstruct the work as an authored audiovisual system. Use one shared understanding core for subjects, events, time-space, sound, and evidence. Treat static-MAD analysis as the current supported path; treat AMV and ASMV handling as provisional extensions whose concepts and coverage may change.

## Select the analysis route

Always read:

- [core-understanding.md](references/core-understanding.md) for the common reasoning model;
- [evidence-schema.md](references/evidence-schema.md) for auditable records;
- [temporal-relations.md](references/temporal-relations.md) for relation classification;
- [failure-modes.md](references/failure-modes.md) before finalizing.

Then select adapters from observable media behavior, not the upload title or community tag:

- **Static MAD / image-based edit — supported**: read [type-static-mad.md](references/type-static-mad.md). Use when still images, manga panels, sprites, typography, crops, masks, compositing, or fabricated camera motion carry the action.
- **AMV / footage-based edit — provisional extension**: read [type-amv.md](references/type-amv.md) only when the user explicitly requests AMV analysis or asks to experiment with the shared core beyond static MAD. Use its concepts as hypotheses, not settled requirements.
- **ASMV / dialogue-led edit — provisional extension**: read [type-asmv.md](references/type-asmv.md) only when the user explicitly requests ASMV analysis or asks to experiment with dialogue-led edits. Use its concepts as hypotheses, not settled requirements.

For a hybrid work, use the smallest adapter set authorized by the request. Tag important claims with the operative mechanism, such as `static_constructed_motion`, `source_footage_action`, `edit_created_relation`, or `recontextualized_speech`. Label every AMV/ASMV adapter finding `provisional_extension`; do not present its terminology or completion checks as a mature standard.

Read [montage-grammar.md](references/montage-grammar.md) when symbolic inserts, repeated images, fabricated composites, typography, graphic matches, intensive compositing, or screens-within-screens materially shape meaning.

Read [craft-analysis.md](references/craft-analysis.md) only when the user requests technique analysis, critique, comparison, or improvement advice. Read [community-reading-framework.md](references/community-reading-framework.md) only for static-MAD community vocabulary and interpretation prompts.

## Shared constraints

- Do not infer plot, identity, intention, or physical motion from an isolated frame.
- Do not equate playback order, source-scene order, and reconstructed story chronology.
- Complete a blind pass before consulting source summaries or creator explanations.
- Require multiple identity anchors; keep uncertain roles provisional.
- Do not force a protagonist. The thematic subject may be a relationship, group, place, emotion, institution, abstract force, or musical proposition.
- Treat lyrics and quoted dialogue as authored audio material, not automatically as literal speech by the visible person.
- Ground major claims in timestamped context before and after the relevant moment.
- Maintain alternative explanations and counterevidence.
- Keep observation, video-grounded inference, external context, and documented author intent separate.

## Workflow

### 1. Establish and classify the analysis surface

Prefer a local video supplied or authorized by the user. For a URL, use an available browser or connector only within the authorized session. Never expose cookies, tokens, or account data.

Record metadata, title, credits, duration, frame rate, resolution, audio, subtitles or lyrics, and available creator notes. Make a type map by interval: still-image construction, continuous footage, dialogue-led construction, or hybrid. Revise the map after inspection. Type detection does not itself authorize the provisional AMV/ASMV extensions.

Store artifacts in a user-approved output directory without overwriting the source.

### 2. Prepare deterministic evidence

Run the bundled preparation workflow:

```powershell
& $python scripts/prepare_analysis.py $video --output-dir $analysisDir --focus 80:100:8
```

This produces metadata, candidate cuts, overview and focus frames, contact sheets, an audio profile, and evidence records. Scene detection is an attention cue, not ground truth.

If Python is unavailable, use a bundled workspace Python. Resolve FFmpeg through an explicit argument, `STATIC_MAD_FFMPEG` / `STATIC_MAD_FFPROBE`, or `PATH`; do not assume a machine-specific location.

### 2a. Optionally use a video-language model

Use a VLM only as a fallible second observer. Read [qwen-vl.md](references/qwen-vl.md) before a Qwen upload and [vlm-prompt.md](references/vlm-prompt.md) before prompting any VLM. External upload requires user authorization and the user's own environment-provided key.

Estimate cost first:

```powershell
& $python scripts/call_qwen_vl.py $video --prompt-file $prompt --fps 1 --dry-run
```

Use a low-density whole-video pass for provisional chapters and OCR, then increase density only on uncertain intervals. Verify claimed gestures, gazes, actions, speakers, and spatial continuities against local frames, audio, and cut boundaries.

### 3. Run the shared understanding core

Follow [core-understanding.md](references/core-understanding.md):

1. perform a blind global pass;
2. segment functional chapters;
3. establish entities, subject roles, focalization, and—when speech leads—discourse roles;
4. build event-response-state-consequence chains;
5. classify shot relations and reconstruct the six clocks;
6. align image, motion, sound, music, and viewer disclosure;
7. generate and falsify at least two interpretations.

Do not write a polished plot before these records exist.

### 4. Apply the selected adapter

Use each adapter to answer what the common core cannot decide by itself:

- static adapter: distinguish depicted action from crop/layer/mask/typography motion and inspect material reconstruction;
- AMV adapter: distinguish source-scene continuity from relations newly created by selection, omission, juxtaposition, and music;
- ASMV adapter: distinguish speaker, addressee, visible subject, assigned narrator, and the edit's overall discourse position.

Return adapter findings to the shared model: they must clarify subject roles, event chains, time-space, sound-image relations, or the editorial thesis. Do not maintain a separate type-specific story.

### 5. Revisit uncertain intervals adaptively

Increase sampling where identity, action phase, gaze, brief text, speaker attribution, source-scene boundaries, repeated imagery, flash inserts, or audio-visual relations are unstable. Use roughly 4 fps for ordinary inspection, 8–12 fps for dense editing, and original frame rate near suspected inserts or match cuts.

Partition a dense interval into shots before narrating it. Record whether visible change is produced by source action, camera/crop, layers/masks, typography, transition, or remains uncertain.

### 6. Recover and test the editorial thesis

Propose two or three answers to: **what relationship, contradiction, state change, discourse, or idea does this edit organize as important?** Test each across chapters, recurrences, music, sound, and endings. Prefer the account that explains more repeated structures with fewer unsupported assumptions.

### 7. Add external context only when requested

Consult original works, lyrics, creator notes, interviews, or project commentary only after the blind analysis and only when the task calls for them. Report whether each item confirms, weakens, corrects, or merely inspires the video-grounded reading.

### 8. Explain craft through effects

When requested, follow [craft-analysis.md](references/craft-analysis.md):

`timestamped evidence -> operation -> perceptual or narrative effect -> limitation or plausible alternative`

Do not infer effectiveness from popularity, software complexity, source prestige, layer count, or effect count. Give revision advice only when requested.

### 9. Report in layers

Use [report-template.md](assets/report-template.md) for a detailed report. Lead with the main interpretation and confidence, then show the observable timeline, subject map, event chains, time-space, audiovisual organization, adapter-specific findings, alternatives, and optional external-context revision.

## Completion gate

Before finalizing, verify that:

- a type map was inferred from the media, the static adapter was used normally, and provisional adapters were loaded only when explicitly requested;
- identities, focalizers, and speakers use multiple anchors;
- visual, action, focal, dramatic, thematic, and discourse roles are not collapsed;
- key events include reactions and state changes or explicitly mark their absence;
- provisional AMV/ASMV findings are labeled as extensions rather than mature universal rules;
- source-scene causality is distinguished from edit-created relation when the AMV extension is used;
- depicted motion is distinguished from constructed motion where still material is used;
- quoted speech is distinguished from the edit's discourse position when the ASMV extension is used;
- reality, memory, fantasy, symbolism, and playback order are not collapsed;
- music sections, sound bridges, holds, motion amplitude, and reading time are considered;
- dense passages received denser inspection and VLM motion claims were locally verified;
- the leading interpretation includes counterevidence;
- external context and author intent remain separate from blind evidence;
- craft commentary explains mechanisms and effects through timestamped evidence.
