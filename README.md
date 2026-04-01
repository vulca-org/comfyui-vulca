# ComfyUI-VULCA

Cultural art evaluation and Brief-driven creation nodes for ComfyUI. Score any generated image on L1-L5 dimensions across 13 traditions.

## Use Cases

- **Evaluate generated images** — drop any image into VULCA Evaluate, get L1-L5 cultural scores + actionable suggestions
- **Brief-driven creation** — define creative intent, generate concepts, select and refine with cultural feedback
- **Layer decomposition** — split artwork into semantic layers, evaluate each independently
- **Evolution tracking** — see how tradition weights evolve across sessions

## Nodes (11)

| Node | Inputs | Outputs | Description |
|------|--------|---------|-------------|
| **VULCA Brief** | text intent | Brief (JSON) | Create creative brief from natural language |
| **VULCA Concept** | Brief | images (4) | Generate concept variations |
| **VULCA Generate** | Brief | image | Full artwork generation |
| **VULCA Evaluate** | image, tradition | scores (JSON) | L1-L5 cultural evaluation |
| **VULCA Update** | Brief, instruction | Brief (updated) | Natural language Brief modification |
| **VULCA Inpaint** | image, region, instruction | image | Region-based repaint |
| **VULCA Layers Analyze** | image | layers (JSON) | Decompose into semantic layers |
| **VULCA Layers Composite** | layers directory | image | Composite layers back |
| **VULCA Layers Export** | layers directory | PNG directory | Export with manifest |
| **VULCA Evolution** | tradition | weights (JSON) | Current evolved L1-L5 weights |
| **VULCA Traditions** | — | list | Available cultural traditions |

## Installation

```bash
# Option 1: Clone into custom_nodes
cd ComfyUI/custom_nodes/
git clone https://github.com/vulca-org/comfyui-vulca

# Option 2: ComfyUI Manager (search "VULCA")
```

Install dependency:
```bash
pip install vulca>=0.10.0
```

Restart ComfyUI.

## Workflow Examples

### Simple: Evaluate Any Image

```
[Load Image] → [VULCA Evaluate] → [Preview Text]
                 tradition: "chinese_xieyi"
```

### Full: Brief-Driven Creation with Feedback

```
[VULCA Brief]
  intent: "Zen garden at dawn, watercolor style"
       ↓
[VULCA Concept] → select best → [VULCA Generate]
                                       ↓
                                 [VULCA Evaluate]
                                       ↓
                              score < threshold?
                             yes ↓           no ↓
                        [VULCA Update]    [Save Image]
                     "add more warmth"
                             ↓
                        back to Generate
```

### Layer Analysis

```
[Load Image] → [VULCA Layers Analyze] → [VULCA Layers Export]
                                              ↓
                                    PNG directory + manifest.json
```

## Requirements

- Python 3.10+
- `vulca>=0.10.0` ([PyPI](https://pypi.org/project/vulca/))
- ComfyUI (tested with latest stable)

For real VLM evaluation: `export GOOGLE_API_KEY=your-key`. Mock mode works without API keys.

## Citation

```bibtex
@inproceedings{yu2025vulca,
  title={VULCA: A Framework for Culturally-Aware Visual Understanding},
  author={Yu, Haorui},
  booktitle={Findings of EMNLP 2025},
  year={2025}
}
```

## License

Apache-2.0
