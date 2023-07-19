from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

dies_list = []
dice_result = []
frequency = []

def generate_dies(dies_num, dies_sides):
    """生成骰子"""
    for _ in range(dies_num):
        dies_list.append(Die(dies_sides))
    
def roll(num):
    """掷骰子"""
    for _ in range(num):
        result = 0
        for die in dies_list:
            result += die.roll()
        dice_result.append(result)
        
def show_result():
    """展示结果"""
    min_result = len(dies_list)
    max_result = dies_list[0].num_sides * len(dies_list)
    
    x_values= list(range(min_result, max_result+1))
    for side in x_values:
        frequency.append(dice_result.count(side))
    
    # 可视化结果
    data = [Bar(x=x_values, y=frequency)]
    
    # dtick: 刻度间隔
    x_axis_config = {'title': '结果', 'dtick':1}
    y_axis_config = {'title': '结果的频率'}
    my_layout = Layout(title='投掷结果频率', xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename='die.html')

if __name__ == '__main__':
    generate_dies(2, 6)
    roll(10000)
    show_result()