import seaborn as sb
from matplotlib import pyplot as plt


def plot_purchase_price(dataFrame):
    sb.distplot(dataFrame["Purchase Price"])
    plt.show()


def heat_map(dataFrame):
    data = dataFrame.pivot_table(values="Purchase Price", index="Job", columns="Company")
    sb.heatmap(data)
    plt.show()
