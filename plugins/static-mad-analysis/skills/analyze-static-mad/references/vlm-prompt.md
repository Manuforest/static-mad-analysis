# VLM observation prompt

Adapt this prompt to the clip. Ask for evidence before interpretation.

```text
Analyze only the visible and audible content of this timestamped video. Do not use source-plot knowledge or claim author intent.

Return:
1. candidate shot boundaries and semantic chapter boundaries;
2. per-shot visual subject, action subject, possible focalizer, and stable identity anchors;
3. OCR with timestamp, duration, attribution if visible, and uncertainty;
4. every visible change labeled as diegetic subject motion, camera/crop motion, layer/mask motion, typography motion, transition, or uncertain;
5. candidate event -> response -> state-change chains, including where a reaction is absent or delayed;
6. possible relations between adjacent shots, with at least one alternative for important cuts;
7. recurring colors, objects, borders, text modes, or source images, describing how their function may change across appearances;
8. music-section functions, motion amplitude, holds, and possible reading-time problems;
9. unexplained causal gaps visible within the edit itself;
10. intervals requiring denser local verification.

Do not smooth cuts into continuous action. Do not infer a room, object, pose, expression, chronology, source identity, or motive unless visibly supported. Do not call a visual transformation meaningful without recurrence or contextual evidence. Mark uncertainty explicitly.
```
