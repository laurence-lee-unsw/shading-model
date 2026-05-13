from __future__ import annotations

import matplotlib.pyplot as plt
from pvmismatch import pvsystem

from .config import FIGURES_DIR, N_MODULES, N_STRINGS


def _save_figure(fig, filename):
    path = FIGURES_DIR / filename
    fig.savefig(path, dpi=150)
    print(f"  saved {path}")


def plot_system_iv(pvsys, title, filename):
    pvsys.calcSystem()
    pvsys.plotSys()

    fig = plt.gcf()
    fig.set_size_inches(8, 10)
    fig.suptitle(title, fontsize=13, y=1.01)
    fig.tight_layout()

    _save_figure(fig, filename)
    plt.close(fig)


def run():
    pvsys = pvsystem.PVsystem(numberStrs=N_STRINGS, numberMods=N_MODULES)

    print("  plotting unshaded IV curve …")
    pvsys.setSuns({0: {0: 1}})
    plot_system_iv(pvsys, title="System IV – unshaded (1-sun)", filename="iv_curve_unshaded.png")

    print("  plotting shaded IV curve …")
    pvsys.setSuns({0: {0: 0.01}})
    plot_system_iv(pvsys, title="System IV – module 0 at 1% irradiance", filename="iv_curve_shaded.png")


if __name__ == "__main__":
    run()