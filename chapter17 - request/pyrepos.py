import requests
from plotly import offline

# 执行API调用并存储响应。
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers, timeout=10)
print(f"Status code: {r.status_code}")

# 将API响应赋给一个变量。
response_dict = r.json()

# 基本信息
print(response_dict.keys())
print(f"is incomplete? {response_dict['incomplete_results']}")
print(f"total repos: {response_dict['total_count']}")
print(f"return repos: {len(response_dict['items'])}")

# 处理仓库信息
repo_names, star, descriptions = [], [], []
for repo_dict in response_dict['items']:
    # owner
    owner = repo_dict['owner']['login']
    # description
    description = repo_dict['description']
    # repo_url
    url = repo_dict['html_url']
    # hover text
    descriptions.append(f"11Owner: {owner}<br />Description: {description}")
    # stars (y)
    star.append(repo_dict['stargazers_count'])
    # name & link (x)
    repo_names.append(f"<i><a href='{url}'>{repo_dict['name']}</a></i>")
    
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': star,
    'hovertext': descriptions,
    'marker': {
        'color': 'rgb(15, 234, 245)', # 柱体颜色
        'line': { 'width': 1.5, 'color': 'rgb(225, 165, 165)'} # 柱体轮廓
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    }
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
