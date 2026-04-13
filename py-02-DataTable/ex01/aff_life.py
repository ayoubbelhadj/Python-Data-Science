from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Load life expectancy data from 'life_expectancy_years.csv' and plot
    Morocco's life expectancy over all available years.
    """
    data = load("life_expectancy_years.csv")
    if data is None:
        return

    # Extract the country row
    morocco = data[data["country"] == "Morocco"].iloc[0].drop("country")
    # Convert index to integers
    morocco.index = morocco.index.astype(int)

    # Plot
    plt.plot(morocco.index, morocco.values)
    plt.title("Morocco Life Expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()
