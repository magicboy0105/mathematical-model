#程序文件ti17_3.py
import numpy as np
import pylab as plt

class WaveEquationFD:
    
    def __init__(self, N, D, Mx, My):
        self.N = N; self.D = D
        self.Mx = Mx; self.My = My; self.tend = 6
        self.xmin = 0; self.xmax = 2
        self.ymin = 0; self.ymax = 2
        self.initialization(); self.eqnApprox()
        
    def initialization(self):
        self.dx = (self.xmax - self.xmin)/self.Mx
        self.dy = (self.ymax - self.ymin)/self.My
        self.x = np.arange(self.xmin, self.xmax+self.dx, self.dx)
        self.y = np.arange(self.ymin, self.ymax+self.dy, self.dy)
        #初值条件
        self.u0 = lambda r, s: 0.1*np.sin(np.pi*r)*np.sin(np.pi*s/2)
        self.v0 = lambda a, b: 0
        #边界条件
        self.bxyt = lambda left, right, time: 0  
        self.dt = (self.tend - 0)/self.N
        self.t = np.arange(0, self.tend+self.dt/2, self.dt)
        #确认稳定性条件r < 1
        r = 4*self.D*self.dt**2/(self.dx**2+self.dy**2);
        assert r < 1, "r 大于1!"

    def eqnApprox(self):
        self.rx = self.D*self.dt**2/self.dx**2
        self.ry = self.D*self.dt**2/self.dy**2
        self.rxy1 = 1 - self.rx - self.ry 
        self.rxy2 = self.rxy1*2
        #解矩阵初始化
        self.u = np.zeros((self.Mx+1, self.My+1))
        self.ut = np.zeros((self.Mx+1, self.My+1))
        self.u_1 = self.u.copy()
        #初值条件赋值
        for j in range(1, self.Mx):
            for i in range(1, self.My):
                self.u[i,j] = self.u0(self.x[i], self.y[j])
                self.ut[i,j] = self.v0(self.x[i], self.y[j])
   
    def solve_and_animate(self):
        u_2 = np.zeros((self.Mx+1, self.My+1))
        xx, yy = np.meshgrid(self.x, self.y)
        plt.rc('text', usetex=True); plt.rc('font', size=15)
        ax = plt.axes(projection='3d')
        wframe = None; k = 0; nsteps = self.N
        while k < nsteps:
            if wframe:
                ax.collections.remove(wframe)
            self.t = k*self.dt
            #沿着y轴方向对边界条件赋值
            for i in range(self.My+1):
                self.u[i, 0] = self.bxyt(self.x[0], self.y[i], self.t)
                self.u[i, self.Mx] = self.bxyt(self.x[self.Mx],
                                               self.y[i], self.t)
            for j in range(self.Mx+1):
                self.u[0, j] = self.bxyt(self.x[j], self.y[0], self.t)
                self.u[self.My, j] = self.bxyt(self.x[j],
                                               self.y[self.My], self.t)
            if k == 0:
                for j in range(1, self.My):
                    for i in range(1, self.Mx):
                        self.u[i,j] = (0.5*(self.rx*(self.u_1[i-1,j] +
                            self.u_1[i+1,j])) + 0.5*(self.ry*
                            (self.u_1[i,j-1] + self.u_1[i,j+1])) +
                            self.rxy1*self.u[i,j] + self.dt*self.ut[i,j])
            else:
                for j in range(1, self.My):
                    for i in range(1, self.Mx):
                        self.u[i,j] = (self.rx*(self.u_1[i-1,j] +
                            self.u_1[i+1,j]) + self.ry*(self.u_1[i,j-1] +
                            self.u_1[i,j+1]) + self.rxy2*self.u[i,j] -
                            u_2[i,j])
            u_2 = self.u_1.copy()
            self.u_1 = self.u.copy()
            
            wframe = ax.plot_surface(xx, yy, self.u, cmap='spring')
            ax.set_xlim3d(0, 2.0); ax.set_ylim3d(0, 2.0)
            ax.set_zlim3d(-1.5, 1.5)
            ax.set_xticks([0, 0.5, 1.0, 1.5, 2.0])
            ax.set_yticks([0, 0.5, 1.0, 1.5, 2.0])
            ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_zlabel("$u$")
            plt.pause(0.01); k += 0.5
    
def main():
    simulator = WaveEquationFD(200, 0.25, 50, 50)
    simulator.solve_and_animate(); plt.show()
    
if __name__ == "__main__":
    main()
    



