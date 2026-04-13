from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    """
    Load income (GDP per capita) and life expectancy data, merge them on
    country for the year 1900, and display a scatter plot with
    a logarithmic x-axis.
    """
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life = load("life_expectancy_years.csv")
    if life is None or income is None:
        return

    income_1900 = income[["country", "1900"]]
    life_1900 = life[["country", "1900"]]

    merged = pd.merge(income_1900, life_1900, on="country")
    merged = merged.dropna()

    # Plot
    plt.title("1900")
    plt.scatter(merged["1900_x"], merged["1900_y"])
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.show()


if __name__ == "__main__":
    main()
