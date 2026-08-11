# VLM observation prompt

Adapt this prompt to the clip. Keep observation and inference separate.

```text
Analyze only the visible content of this timestamped video. Do not use source-plot knowledge.

Return:
1. candidate shot boundaries;
2. per-shot subject and stable identity anchors;
3. OCR with timestamps and uncertainty;
4. every visible change labeled as character motion, camera/crop motion, layer/mask motion, typography motion, transition, or uncertain;
5. possible relations between adjacent shots, including alternatives;
6. intervals requiring denser local verification.

Do not smooth cuts into continuous character action. Do not infer a room, object, pose, or expression unless it is visibly supported. Mark uncertainty explicitly.
```
