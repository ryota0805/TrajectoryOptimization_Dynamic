#パラメータ管理class
import numpy as np
import env

class Parameter:
    env_data = env.Env()
    global_N = 30                                                     #系列データの長さ
    N = 30
    M = 5                                                       #設計変数の種類の個数
    
    #初期状態と終端状態
    set_cons = {'initial_x'     :True,                          #境界条件をセットするかどうか
                'terminal_x'    :True, 
                'initial_y'     :True, 
                'terminal_y'    :True, 
                'initial_theta' :True, 
                'terminal_theta':True, 
                'initial_phi'   :False, 
                'terminal_phi'  :False,
                'initial_v'     :False, 
                'terminal_v'    :False}
    
    initial_x = 0                                             #x[m]
    terminal_x = 30                                         #x[m]
    
    initial_y = 0                                              #y[m]
    terminal_y = 0                                              #y[m]

    initial_theta = 0                                          #theta[rad]
    terminal_theta = 0                                          #theta[rad]
    
    initial_phi = 0                                             #phi[rad]
    terminal_phi = 0                                            #phi[rad]
    
    initial_v = 0                                               #v[m/s]
    terminal_v = 0                                              #v[m/s]
    
    #変数の範囲
    x_min = env_data.x_range[0]                                                  #x[m]
    x_max = env_data.x_range[1]                                                  #x[m]
    y_min = env_data.y_range[0]                                                 #y[m]
    y_max = env_data.y_range[1]                                                  #y[m]
    theta_min = -np.pi * 179/ 180                                         #theta[rad]
    theta_max = np.pi *179/180                                          #tehta[rad]
    phi_min = -np.pi/6                                          #phi[rad]
    phi_max = np.pi/6                                           #phi[rad]
    v_min = -2                                                   #v[m/s]
    v_max = 2                                                   #v[m/s]
    
    WayPoint = np.array([[initial_x, initial_y],                #初期パス　[x, y] 
                        [10, 0],
                        [20, 0],
                        [terminal_x, terminal_y]])     



    dt = 1                                                      #刻み幅[s]                                             
    L = 1.5                                                     #前輪と後輪の距離[m]

    #障害物のパラメータ 
    #　(x, y, r)
    #　x　: 円の中心座標
    #　y　: 円の中心座標
    #　r　: 半径 
    obstacle_list = [(10, -1, 3), (20, 1, 3)]                   #障害物のパラメータが格納されたリスト
    
    
    #wallのパラメータ
    wall_thick = 1                                #wallの厚さ
    margin = 2
    
    #robot size
    robot_size = 0.5
