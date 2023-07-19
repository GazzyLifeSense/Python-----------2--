import csv
from datetime import datetime
from matplotlib import pyplot as plt

with open('data.csv', 'r', encoding='utf-8') as f:
    dates, tmaxs, tmins = [], [], []
    
    reader = csv.reader(f)
    # 获取表头
    head_row = enumerate(next(reader))
    
    for index, col in head_row:
        print(index, col)
        if(col == 'TMAX'):
            tmax_index = index
        if(col == 'TMIN'):
            tmin_index = index
        if(col == 'DATE'):
            date_index = index

    # 遍历剩余数据部分
    for row in reader:
        date = datetime.strptime(row[date_index], '%Y-%m-%d')
        # 获取最高最低温度
        try:
            tmin = int(row[tmin_index])
            tmax = int(row[tmax_index])
        except ValueError:
            print(f"Missing data for {date}")
        else:
            dates.append(date)
            tmaxs.append(tmax)
            tmins.append(tmin)
            
    fig, ax = plt.subplots()
    # 图表样式设置
    plt.style.use('seaborn')
    ax.set_title("Daily high and low temperatures - 2023", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    ax.set_ylabel("Temperature (F)", fontsize=16)
    # 日期斜体，避免重叠
    fig.autofmt_xdate()
    
    # 绘制
    ax.plot(dates, tmaxs, c='red', alpha=0.5)
    ax.plot(dates, tmins, c='blue', alpha=0.5)
    # 填充绘制区域
    ax.fill_between(dates, tmaxs, tmins, facecolor='blue', alpha=0.1)
    plt.show()
            
    