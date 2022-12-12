from numpy import ndarray as Array
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Qt5Agg")
plt.style.use("ggplot")

class VizShower:
    def __init__(self, seconds: float):
        self.fig, self.ax = plt.subplots()
        self.seconds = seconds

    def add_data(self, X: Array, y: Array) -> "VizShower":
        self.ax.scatter(X[:, 0], X[:, 1], c=y)
        self.ax.set_xlabel("$x_1$")
        self.ax.set_ylabel("$x_2$")
        return self

    def show(self) -> "VizShower":
        self.fig.show()
        plt.pause(self.seconds)
        plt.close()
        return self

