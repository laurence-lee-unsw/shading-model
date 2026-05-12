# PV Mismatch – Shading Analysis

Simulation scripts using [pvmismatch](https://github.com/SunPower/PVMismatch) to model partial shading effects on PV strings and modules.

## Analyses

| # | Script | Description |
|---|--------|-------------|
| 1 | `scripts/string_shading.py` | Pmp vs shading fraction sweep on a 10-module string |
| 2 | `scripts/iv_curves.py` | System-level IV curves – unshaded vs fully shaded |
| 3 | `scripts/half_cell_comparison.py` | IV curve comparison: standard 72-cell vs 144-half-cell module |

## Layout

```
pv-mismatch/
├── main.py
├── requirements.txt
├── data/
├── figures/
└── scripts/
    ├── config.py
    ├── string_shading.py
    ├── iv_curves.py
    └── half_cell_comparison.py
```

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py              # run all three analyses
python main.py --analysis 1 # string shading sweep only
python main.py --analysis 2 # system IV curves only
python main.py --analysis 3 # half-cell comparison only
```

Scripts can also be run directly:

```bash
python -m scripts.string_shading
```

Figures are written to `figures/`.

## Findings

- **String shading**: shading one module in a 10-module string drops Pmp by ~10 %. Current is unaffected; the loss is entirely a voltage drop driven by bypass diode activation.
- **Half-cell modules**: 144 half-cells across 3 bypass zones means shading a single cell only activates one zone, limiting the power loss to roughly a third of what a standard 72-cell module would see.

## Configuration

Shared parameters (module count, sweep resolution, bypass voltage) are in `scripts/config.py`.
MIT License

Copyright (c) 2026 laurence-lee-unsw

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
