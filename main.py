from param import Parameter as p
import GenerateInitialPath
import util
import constraints
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as optimize
import objective_function 
import plot
import time
import animation
import dynamic_obstacle
import env

###動的障害物を含む環境下における経路計画

# 計測開始
start_time = time.time()

#初期経路の生成
env_data = env.Env()
initial_path = p.WayPoint
cubicX, cubicY = GenerateInitialPath.cubic_spline_by_waypoint(initial_path)
x, y, theta, phi, v = GenerateInitialPath.generate_initialpath2(cubicX, cubicY)
print(len(x), len(y), len(theta), len(phi), len(v))
thetas, phis, vs = np.array([0.1]*p.N), np.array([0.1]*p.N), np.array([0.1]*p.N)
trajectory_matrix = np.array([x, y, theta, phi, v])
trajectory_vector = util.matrix_to_vector(trajectory_matrix)

#計算結果の保存
x_result, y_result, theta_result = [], [], []

for n in range(p.global_N - 2):
    p.n = n
    
    #目的関数の設定
    func = objective_function.objective_function
    jac_of_objective_function = objective_function.jac_of_objective_function

    #制約条件の設定
    cons = constraints.generate_cons_with_jac()

    #変数の範囲の設定
    bounds = constraints.generate_bounds()

    #オプションの設定
    options = {'maxiter':10000}


    #最適化を実行
    result = optimize.minimize(func, trajectory_vector, method='SLSQP', jac = jac_of_objective_function, constraints=cons, bounds=bounds, options=options)
    
    xs, ys, thetas, phis, vs = util.generate_result(result.x)
    x_result.append(xs)
    y_result.append(ys)
    theta_result.append(thetas)
    
    #最適化結果の表示
    print(result)
    #plot.vis_env()
    #plot.vis_path(trajectory_vector)
    plot.compare_path(trajectory_vector, result.x)
    #plot.compare_history_theta(trajectory_vector, result.x, range_flag = True)
    #plot.compare_history_phi(trajectory_vector, result.x, range_flag = True)
    #plot.compare_history_v(trajectory_vector, result.x, range_flag = True)
    #plot.vis_history_theta(result.x, range_flag=True)
    #plot.vis_history_phi(result.x, range_flag=True)
    #plot.vis_history_v(result.x, range_flag = True)
    #plot.compare_path_rec(trajectory_vector, result.x)
    
    #p.Nと初期状態の更新
    p.N -= 1
    p.initial_x, p.initial_y, p.initial_theta, p.initial_phi, p.initial_v = xs[1], ys[1], thetas[1], phis[1], vs[1]
    p.set_cons['initial_theta'] = False
    
    #WayPointから設計変数の初期値を計算する
    print(len(x), len(y), len(theta), len(phi), len(v))
    thetas, phis, vs = np.array([0.1]*p.N), np.array([0.1]*p.N), np.array([0.1]*p.N)
    trajectory_matrix = np.array([xs[1:], ys[1:], thetas[:], phis[:], vs[:]])
    trajectory_vector = util.matrix_to_vector(trajectory_matrix)

    # 計測終了
    end_time = time.time()

    

# 経過時間を計算
elapsed_time = end_time - start_time
print(f"実行時間: {elapsed_time}秒")
xs, ys, thetas, _, _ = util.generate_result(result.x)
animation.gen_movie(xs, ys, thetas)