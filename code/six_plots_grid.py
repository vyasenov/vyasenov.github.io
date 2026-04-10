from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats
from sklearn.datasets import load_iris


def main() -> None:
    outpath = Path("files/six-plots-you-should-know-grid.png")
    outpath.parent.mkdir(parents=True, exist_ok=True)

    sns.set_theme(style="whitegrid", context="talk", font_scale=0.9)
    palette = sns.color_palette("Set2", 3)
    species_order = ["setosa", "versicolor", "virginica"]

    # Global title styling
    title_font = {"fontsize": 16, "fontweight": "bold", "pad": 15}
    label_font = {"fontsize": 11}
    tick_size = 10

    iris_bunch = load_iris(as_frame=True)
    iris = iris_bunch.frame.copy()
    iris["species"] = iris["target"].map(dict(enumerate(iris_bunch.target_names)))
    iris = iris.rename(
        columns={
            "sepal length (cm)": "sepal_length",
            "sepal width (cm)": "sepal_width",
            "petal length (cm)": "petal_length",
            "petal width (cm)": "petal_width",
        }
    )

    corr = iris[["sepal_length", "sepal_width", "petal_length", "petal_width"]].corr()

    fig, axes = plt.subplots(3, 2, figsize=(14, 16))
    axes = axes.flatten()

    # Q-Q plot
    (osm, osr), (slope, intercept, _) = stats.probplot(iris["sepal_length"], dist="norm")
    axes[0].scatter(
        osm,
        osr,
        s=30,
        color=palette[0],
        alpha=0.7,
        edgecolor="white",
        linewidth=0.5,
    )
    line_x = np.linspace(osm.min(), osm.max(), 100)
    axes[0].plot(line_x, slope * line_x + intercept, color="#333333", linewidth=1.5, linestyle="--")
    axes[0].set_title("Q-Q Plot", **title_font)
    axes[0].set_xlabel("Theoretical Quantiles", **label_font)
    axes[0].set_ylabel("Sample Quantiles", **label_font)
    axes[0].tick_params(labelsize=tick_size)

    # Violin plot
    sns.violinplot(
        data=iris,
        x="species",
        y="sepal_length",
        order=species_order,
        hue="species",
        palette=palette,
        legend=False,
        inner="box",
        cut=0,
        ax=axes[1],
        linewidth=1.2,
    )
    axes[1].set_title("Violin Plot", **title_font)
    axes[1].set_xlabel("", **label_font)
    axes[1].set_ylabel("Sepal Length", **label_font)
    axes[1].tick_params(labelsize=tick_size)

    # ECDF plot
    for color, species in zip(palette, species_order):
        subset = np.sort(iris.loc[iris["species"] == species, "sepal_length"].to_numpy())
        y = np.arange(1, len(subset) + 1) / len(subset)
        axes[2].step(subset, y, where="post", label=species.title(), color=color, linewidth=2)
    axes[2].set_title("ECDF Plot", **title_font)
    axes[2].set_xlabel("Sepal Length", **label_font)
    axes[2].set_ylabel("Empirical CDF", **label_font)
    axes[2].legend(frameon=False, fontsize=10)
    axes[2].tick_params(labelsize=tick_size)

    # Ridgeline plot
    x_grid = np.linspace(iris["sepal_length"].min() - 0.3, iris["sepal_length"].max() + 0.3, 300)
    offsets = np.array([0.0, 1.0, 2.0])
    for offset, color, species in zip(offsets, palette, species_order):
        subset = iris.loc[iris["species"] == species, "sepal_length"].to_numpy()
        kde = stats.gaussian_kde(subset)
        density = kde(x_grid)
        density = density / density.max() * 0.85
        axes[3].fill_between(x_grid, offset, offset + density, color=color, alpha=0.6)
        axes[3].plot(x_grid, offset + density, color="#444444", linewidth=1)
        axes[3].text(x_grid.min() - 0.05, offset + 0.15, species.title(), ha="right", va="center", fontsize=11, fontweight="bold")
    axes[3].set_title("Ridgeline Plot", **title_font)
    axes[3].set_xlabel("Sepal Length", **label_font)
    axes[3].set_yticks([])
    axes[3].set_ylabel("")
    axes[3].spines["left"].set_visible(False)
    axes[3].tick_params(labelsize=tick_size)

    # Hexbin plot
    hb = axes[4].hexbin(
        iris["sepal_length"],
        iris["petal_length"],
        gridsize=15,
        cmap="YlOrRd",
        edgecolors="#eeeeee",
        linewidths=0.5,
    )
    axes[4].set_title("Hexbin Plot", **title_font)
    axes[4].set_xlabel("Sepal Length", **label_font)
    axes[4].set_ylabel("Petal Length", **label_font)
    axes[4].tick_params(labelsize=tick_size)
    cb = fig.colorbar(hb, ax=axes[4], fraction=0.046, pad=0.04)
    cb.set_label("Count", size=10)
    cb.ax.tick_params(labelsize=9)

    # Corrgram
    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="RdBu_r",
        center=0,
        square=True,
        cbar=False,
        ax=axes[5],
        annot_kws={"size": 12, "weight": "bold"},
    )
    axes[5].set_title("Corrgram", **title_font)
    axes[5].tick_params(labelsize=tick_size)

    #fig.suptitle("Six Plot Types You Should Probably Use More Often", fontsize=22, fontweight="bold", y=0.98)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    fig.savefig(outpath, dpi=250, bbox_inches="tight")
    plt.close(fig)

    print(f"Saved grid plot to {outpath}")


if __name__ == "__main__":
    main()
