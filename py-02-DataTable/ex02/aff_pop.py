from load_csv import load
import matplotlib.pyplot as plt


def convert_population(value: str) -> float:
    """Convert population string with suffix to float."""
    if value.endswith("M"):
        return float(value[:-1]) * 1_000_000
    elif value.endswith("k"):
        return float(value[:-1]) * 1_000
    elif value.endswith("B"):
        return float(value[:-1]) * 1_000_000_000
    else:
        return float(value)


def main():
    """Load population data and plot Morocco vs Spain (1800-2050)."""
    data = load("population_total.csv")
    if data is None:
        return

    morocco = data[data["country"] == "Morocco"].iloc[0].drop("country")
    morocco = morocco.apply(convert_population)

    morocco.index = morocco.index.astype(int)
    morocco = morocco[morocco.index <= 2050]

    other = data[data["country"] == "Spain"].iloc[0].drop("country")
    other = other.apply(convert_population)

    other.index = other.index.astype(int)
    other = other[other.index <= 2050]

    # Plot
    plt.plot(morocco.index, morocco.values, label="Morocco")
    plt.plot(other.index, other.values, label="Spain")
    plt.title("Population Projections")
    years = data.columns[1:-50:30].astype(int)
    plt.xticks(years)
    plt.xlim(1800, 2050)
    plt.yticks(plt.yticks()[0],
               [f"{int(x / 1_000_000)}M" for x in plt.yticks()[0]])
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
