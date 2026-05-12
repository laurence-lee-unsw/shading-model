from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from pvmismatch import pvmodule

from .config import FIGURES_DIR, FULL_CELL_AREA, V_BYPASS

SHADE_IRRADIANCE = 0.001  # near-zero to avoid numerical issues at exactly 0


def _save_and_close(fig, filename):
    path = FIGURES_DIR / filename
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    print(f"  saved {path}")
    plt.close(fig)


def _apply_title_and_size(fig, title, ylim):
    fig.set_size_inches(8, 10)
    fig.axes[0].set_ylim(ylim)
    fig.suptitle(title, fontsize=13, y=1.01)


def analyse_full_cell_module():
    mod = pvmodule.PVmodule(
        cell_pos=pvmodule.STD72,
        pvcells=None,
        pvconst=None,
        Vbypass=np.float64(V_BYPASS),
        cellArea=np.float64(FULL_CELL_AREA),
    )

    fig = mod.plotMod()
    _apply_title_and_size(fig, "Full-cell module (72 cells) – unshaded", (0, 8))
    _save_and_close(fig, "full_cell_unshaded.png")

    mod.setSuns([SHADE_IRRADIANCE], cells=[0])
    fig = mod.plotMod()
    _apply_title_and_size(fig, "Full-cell module (72 cells) – 1 cell shaded", (0, 8))
    _save_and_close(fig, "full_cell_shaded.png")


def analyse_half_cell_module():
    half_cell_pos = pvmodule.crosstied_cellpos_pat([24, 24, 24], 2, partial=True)

    mod = pvmodule.PVmodule(
        cell_pos=half_cell_pos,
        pvcells=None,
        pvconst=None,
        Vbypass=np.float64(V_BYPASS),
        cellArea=np.float64(FULL_CELL_AREA / 2),
    )

    fig = mod.plotMod()
    _apply_title_and_size(fig, "Half-cell module (144 cells, 3 zones) – unshaded", (0, 14))
    _save_and_close(fig, "half_cell_unshaded.png")

    mod.setSuns([SHADE_IRRADIANCE], cells=[0])
    fig = mod.plotMod()
    _apply_title_and_size(fig, "Half-cell module (144 cells, 3 zones) – 1 cell shaded", (0, 14))
    _save_and_close(fig, "half_cell_shaded.png")


def run():
    print("  plotting full-cell module IV curves …")
    analyse_full_cell_module()

    print("  plotting half-cell module IV curves …")
    analyse_half_cell_module()


if __name__ == "__main__":
    run()