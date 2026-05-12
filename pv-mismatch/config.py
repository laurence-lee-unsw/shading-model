from __future__ import annotations

import argparse
import sys
import time

import scripts.string_shading as string_shading
import scripts.iv_curves as iv_curves
import scripts.half_cell_comparison as half_cell_comparison

ANALYSES: dict[int, tuple[str, object]] = {
    1: ("String shading sweep", string_shading),
    2: ("System IV curves", iv_curves),
    3: ("Half-cell vs full-cell comparison", half_cell_comparison),
}


def run(analyses: list[int]) -> None:
    t0 = time.perf_counter()
    total = len(analyses)

    for i, key in enumerate(analyses, start=1):
        title, module = ANALYSES[key]
        print(f"\n[{i}/{total}] {title}")
        module.run()

    elapsed = time.perf_counter() - t0
    print(f"\nDone in {elapsed:.1f} s. Figures saved to figures/")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run PV mismatch shading analyses.")
    parser.add_argument(
        "--analysis",
        type=int,
        choices=list(ANALYSES.keys()),
        default=None,
        metavar="N",
        help="run only analysis N (default: run all)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    selected = [args.analysis] if args.analysis is not None else list(ANALYSES.keys())
    sys.exit(run(selected))
