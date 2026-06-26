#!/usr/bin/env python3
"""
扫描当前目录下 github-ai-trending-YYYYMMDD.html 文件，
自动重新生成 index.html 的静态报告列表。
"""

import os
import re
import glob
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

WEEKDAY_CN = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

FILENAME_PATTERN = re.compile(r'^github-ai-trending-(\d{4})(\d{2})(\d{2})\.html$')


def parse_date(filename):
    """从文件名解析日期，返回 (datetime, 完整日期字符串, 月, 日)。"""
    m = FILENAME_PATTERN.match(filename)
    if not m:
        return None
    year, month, day = int(m.group(1)), int(m.group(2)), int(m.group(3))
    dt = datetime(year, month, day)
    weekday_str = WEEKDAY_CN[dt.weekday()]
    full_date = f"{dt.year}年{dt.month}月{dt.day}日 {weekday_str}"
    month_str = f"{dt.month}月"
    day_str = str(dt.day)
    return (dt, full_date, month_str, day_str)


def scan_reports():
    """扫描当前目录，返回按日期倒序排列的报告信息列表。"""
    pattern = os.path.join(SCRIPT_DIR, "github-ai-trending-*.html")
    files = glob.glob(pattern)
    reports = []
    for f in files:
        basename = os.path.basename(f)
        # 排除 index.html 自身
        if basename == "index.html":
            continue
        parsed = parse_date(basename)
        if parsed:
            dt, full_date, month_str, day_str = parsed
            reports.append({
                "filename": basename,
                "datetime": dt,
                "full_date": full_date,
                "month_str": month_str,
                "day_str": day_str,
            })
    reports.sort(key=lambda r: r["datetime"], reverse=True)
    return reports


def generate_card(report):
    """生成单个报告卡片的 HTML。"""
    return f"""    <a class="report-card" href="{report['filename']}" target="_blank">
      <div class="date-badge">
        <span class="month">{report['month_str']}</span>
        <span class="day">{report['day_str']}</span>
      </div>
      <div class="report-info">
        <div class="report-title">GitHub AI Trending 周报</div>
        <div class="report-date">{report['full_date']}</div>
      </div>
      <span class="arrow">→</span>
    </a>"""


def regenerate_index(reports, dry_run=False):
    """基于模板重新生成 index.html。"""
    index_path = os.path.join(SCRIPT_DIR, "index.html")

    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 定位 <div class="report-list"> 和对应的 </div>
    list_start = content.find('<div class="report-list">')
    if list_start == -1:
        print("错误：index.html 中未找到 <div class=\"report-list\">")
        return

    # 从 list_start 后找到缩进相同的闭合 </div>
    # report-list 缩进是两个空格
    list_end_marker = content.find("  </div>\n  <footer>", list_start)
    if list_end_marker == -1:
        print("错误：无法定位 report-list 的结束位置")
        return

    # list_start 到行末（包含换行）
    line_end = content.index("\n", list_start) + 1

    header = content[:line_end]
    footer = content[list_end_marker:]

    if reports:
        cards = "\n".join(generate_card(r) for r in reports) + "\n"
    else:
        cards = '    <div class="empty">暂无报告</div>\n'

    new_content = header + cards + footer

    if dry_run:
        print("预览生成内容：")
        print("--- header ---")
        print(repr(header))
        print("--- cards ---")
        print(cards)
        print("--- footer ---")
        print(repr(footer[:200]) + "...")
        return

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"已重新生成 {index_path}")
    print(f"共 {len(reports)} 篇报告")


def main():
    reports = scan_reports()
    print(f"扫描到 {len(reports)} 个报告文件：")
    for r in reports:
        print(f"  {r['filename']} → {r['full_date']}")
    regenerate_index(reports)


if __name__ == "__main__":
    main()
