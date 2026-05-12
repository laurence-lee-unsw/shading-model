from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from pvmismatch import pvsystem

from .config import FIGURES_DIR, N_MODULES, N_STRINGS, N_SWEEP_POINTS


def build_baseline_system(n_strings=N_STRINGS, n_mods=N_MODULES):
    sys = pvsystem.PVsystem(numberStrs=n_strings, numberMods=n_mods)
    sys.setSuns({0: {0: 1}})
    sys.calcSystem()
    return sys


def sweep_shading(pvsys, pmp_ref, n_points=N_SWEEP_POINTS):
    irr_levels = np.linspace(0.001, 1.0, n_points)
    pmp_values = []

    for irr in irr_levels:
        pvsys.setSuns({0: {0: irr}})
        pvsys.calcSystem()
        pmp_values.append(pvsys.Pmp / pmp_ref * 100)

    shading_pct = (1 - irr_levels) * 100
    return shading_pct, np.array(pmp_values)


def plot_shading_curve(shading_pct, pmp_pct, save=True):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(shading_pct, pmp_pct, color="royalblue", linewidth=3)
    ax.set_title(f"String of {N_MODULES} modules – Pmp vs first-module shading")
    ax.set_xlabel("Shading of first module (%)")
    ax.set_ylabel("Maximum Power Point (%)")
    ax.tick_params(axis="both", direction="in")
    ax.set_xlim([0, 100])
    ax.set_ylim([89, 100])
    ax.grid(False)
    fig.tight_layout()

    if save:
        path = FIGURES_DIR / "string_shading_curve.png"
        fig.savefig(path, dpi=150)
        print(f"  saved {path}")

    return fig


def run():
    print("  building baseline system …")
    pvsys = build_baseline_system()
    pmp_ref = pvsys.Pmp

    print(f"  sweeping {N_SWEEP_POINTS} irradiance levels …")
    shading_pct, pmp_pct = sweep_shading(pvsys, pmp_ref)

    plot_shading_curve(shading_pct, pmp_pct)
    plt.close("all")


if __name__ == "__main__":
    run()