from random import choice
from matplotlib import pyplot as plt


class RandomWalk:
    """随机运动坐标类"""
    def __init__(self, num_points=5000) -> None:
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]
      
    @staticmethod
    def get_step():
        """获取步长"""
        direction = choice([-1,1])
        step = choice([1,2,3,4,5,6,7,8])
        return direction * step


def rw_visual():
    """可视化随机运动路径"""
    rw = RandomWalk()
    while len(rw.x_values) < rw.num_points:
        rw.x_values.append(rw.x_values[-1] + rw.get_step())
        rw.y_values.append(rw.y_values[-1] + rw.get_step())
    
    c = range(rw.num_points)
    _, ax = plt.subplots(figsize=(15, 9), dpi=128)
    
    # 样式(绘制所有点)
    plt.style.use('classic')
    
    # c颜色深浅  s点尺寸  cmap颜色  
    ax.scatter(rw.x_values, rw.y_values, c=c, s=5, cmap=plt.cm.Blues, edgecolors='none')
    
    # 起终点突出
    ax.scatter(0, 0, c='green', edgecolors='none', s=20)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=20)
    
    # 模拟花粉运动
    # ax.plot(rw.x_values, rw.y_values, linewidth=1, color='green')
    
    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    
    
rw_visual()