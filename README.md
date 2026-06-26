# githubweekly

## GitHub仓库周榜

访问以下地址查看：

[https://youxiaohanpian.github.io/githubweekly/](https://youxiaohanpian.github.io/githubweekly/)

## 提示词：

推荐高价值的高星项目，优先适合个人，尽量避免重复推荐
检索 GitHub 本周 Trending 中 AI/ML 领域的热门项目，生成中文可视化展示页面。
一、数据获取

- 检索 GitHub Trending（Weekly 维度），筛选 AI/机器学习相关项目（关键词：AI、LLM、图形图像、视频、设计、machine-learning、deep-learning、GPT、agent 等）
- 每个项目提取：项目名、作者、Star 数、本周新增 Star、主要编程语言、仓库 URL
- 对每个项目进行中文解读：
· 一句话概述：项目是什么、解决什么问题
· 核心功能：2-3 个关键能力点
· 适用场景：适合哪类用户、在什么业务场景下使用
二、输出为 HTML 页面
- 所有内容以中文呈现（项目名保留英文原名）
- 设计风格：网页设计为简约风高级配色，无多余装饰，选取一个颜色作为页面的背景主题色，页面背景使用设计敢渐变样式，主题色不重复。
- 布局：卡片列表，每张卡片包含：
· 项目名（可点击跳转至 GitHub 仓库）+ 语言标签 + Star 数与本周增量
· 中文简介：一句话概述
· 核心功能：要点列表
· 适用场景：标签化展示
- 按本周新增 Star 降序排列
- 页面顶部显示数据抓取时间，底部标注数据来源
- 纯静态 HTML/CSS，无外部依赖，可直接浏览器打开



### 以后加新报告只需两步：

1. 把 github-ai-trending-YYYYMMDD.html 放到目录下
2. 运行 python regenerate_index.py → commit → push

