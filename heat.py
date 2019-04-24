from matplotlib import pyplot as plt

class Heat():

  def __init__(self, dx, dt, x_end, t_end, coef, b, function_t0):
    self.dx = dx
    self.dt = dt
    self.x_end = x_end
    self.t_end = t_end
    self.coef = coef
    self.b = b
    self.t0 = function_t0

    self.t = []
    self.x = []

    # Allocating memory
    NdataTime = heat_range(self.t, 0., t_end, dt)
    NdataSpace = heat_range(self.x, 0., x_end, dx)

    self.U = []

    for t in range(NdataTime):
      self.U.append([])
      for x in range(NdataSpace):
        self.U[t].append(0.)

    # Initial condition function
    self.U[0] = self.t0(self.x)
    
    self.NdataTime = NdataTime
    self.NdataSpace = NdataSpace


  def heat_solve(self):

    r = self.dt/(self.dx*self.dx)

    for t in range(0, self.NdataTime - 1):

      self.U[t][0] = self.b[0]
      self.U[t][-1] = self.b[1]

      for i in range(1, self.NdataSpace -1):
        self.U[t+1][i] = r*self.U[t][i-1] + (1-2*r)*self.U[t][i] + r*self.U[t][i+1]

    return 0

  def heat_plot(self):

    plt.ion()

    for i in range(1, self.NdataTime,10):
      plt.clf() # Reseting the plot
      plt.plot(self.x, self.U[i]);
      plt.xlim(0, self.x_end)
      plt.ylim(-1.5, 1.5);
      plt.title('Time: {:02.3f}'.format(i*self.dt))

      plt.pause(0.001)
    plt.close()
    return 0

def heat_range(vec, start, end, step):

  n =  int((end - start)/step) + 1
  for i in range(n):
    vec.append(i*step)

  return n
