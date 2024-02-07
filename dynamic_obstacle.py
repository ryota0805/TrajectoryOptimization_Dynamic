from scipy.interpolate import interp1d
import numpy as np

class DynamicObstacle:
    def __init__(self, n, N):
        self.n = n
        self.N = N
        self.dynamic_obs_data = self.dynamic_obs_data()
        
    def generate_trajectory(self, path):
        x, y = [], []
        for i in range(len(path)):
            x.append(path[i][0])
            y.append(path[i][1])
            
        t = np.linspace(0, 1, len(x))
        
        obstacle_x = interp1d(t, x)
        obstacle_y = interp1d(t, y)
        
        t = np.linspace(0, 1, self.N)
        
        x_list, y_list = obstacle_x(t), obstacle_y(t)
        
        return x_list[self.n], y_list[self.n]
    
    def dynamic_obs_data(self):
        dynamic_obs_path_r = [[[[20, 2], [20, -8]], 1.5]]
        
        dynamic_obs_data = []
        
        for i in range(len(dynamic_obs_path_r)):
            obs_x, obs_y = self.generate_trajectory(dynamic_obs_path_r[i][0])
            dynamic_obs_data.append([obs_x, obs_y, dynamic_obs_path_r[i][1]])
            
        return dynamic_obs_data