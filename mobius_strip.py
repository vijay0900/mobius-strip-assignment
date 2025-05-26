
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class MobiusStrip:
    def __init__(self, R=1.0, w=0.4, n=200):
        self.R = R
        self.w = w
        self.n = n
        self.u = np.linspace(0, 2 * np.pi, n)
        self.v = np.linspace(-w/2, w/2, n)
        self.U, self.V = np.meshgrid(self.u, self.v)
        self.X, self.Y, self.Z = self.compute_mesh()

    def compute_mesh(self):
        U, V, R  = self.U, self.V,self.R
    

        X = (R + V * np.cos(U / 2)) * np.cos(U)
        Y = (R + V * np.cos(U / 2)) * np.sin(U)
        Z = V * np.sin(U / 2)

        return X, Y, Z

    def compute_surface_area(self):
        dx = np.gradient(self.X)
        dy = np.gradient(self.Y)
        dz = np.gradient(self.Z)

        dS = np.sqrt(
            (dy[1] * dz[0] - dz[1] * dy[0])**2 +
            (dz[1] * dx[0] - dx[1] * dz[0])**2 +
            (dx[1] * dy[0] - dy[1] * dx[0])**2
        )

        area = np.sum(dS) * (2 * np.pi / self.n)**2
        return area

    def compute_edge_length(self):
        edge1 = np.array([
            (self.X[-1, i], self.Y[-1, i], self.Z[-1, i]) for i in range(self.n)
        ])
        edge2 = np.array([
            (self.X[0, i], self.Y[0, i], self.Z[0, i]) for i in range(self.n)
        ])

        def arc_length(edge):
            return np.sum(np.linalg.norm(np.diff(edge, axis=0), axis=1))

        return (arc_length(edge1) + arc_length(edge2)) / 2

    def plot(self):
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, cmap='viridis', edgecolor='k', linewidth=0.1)
        ax.set_title('Mobius Strip')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    mobius = MobiusStrip(R=1, w=0.4, n=200)
    mobius.plot()

    area = mobius.compute_surface_area()
    edge = mobius.compute_edge_length()

    print(f"Surface Area ≈ {area:.4f}")
    print(f"Edge Length ≈ {edge:.4f}")
