import csv
from datetime import datetime
import os

# 数据存储路径（当前目录下的 accounting.csv）
DATA_FILE = "accounting.csv"


def init_file():
    """初始化CSV文件（若不存在则创建表头）"""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["日期", "金额（元）", "备注"])


def add_record():
    """添加一条记账记录"""
    try:
        # 获取当前日期（格式：2024-05-20）
        date = datetime.now().strftime("%Y-%m-%d")
        # 用户输入金额（需为数字）
        amount = float(input("请输入金额（元）："))
        # 用户输入备注
        note = input("请输入备注（如：早餐/买书）：")

        # 写入CSV文件
        with open(DATA_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([date, amount, note])
        print("记录添加成功！\n")
    except ValueError:
        print("错误：金额需为数字，请重新输入！\n")


def view_records():
    """查看所有记账记录"""
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        print("暂无记账记录！\n")
        return

    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)  # 跳过表头
        print(f"| {headers[0]:<10} | {headers[1]:<8} | {headers[2]:<20} |")
        print("-" * 45)
        for row in reader:
            print(f"| {row[0]:<10} | {row[1]:<8} | {row[2]:<20} |")
    print()  # 空行分隔


def stat_monthly():
    """统计本月消费总额"""
    if not os.path.exists(DATA_FILE):
        print("暂无记录，无法统计！\n")
        return

    current_month = datetime.now().strftime("%Y-%m")
    total = 0.0
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # 跳过表头
        for row in reader:
            if row[0].startswith(current_month):
                total += float(row[1])
    print(f"本月（{current_month}）总消费：{total:.2f} 元\n")


def main():
    """主程序入口（循环显示菜单）"""
    init_file()  # 初始化文件
    while True:
        print("===== 每日记账本 =====")
        print("1. 添加记账记录")
        print("2. 查看所有记录")
        print("3. 统计本月消费")
        print("4. 退出程序")
        choice = input("请输入选项（1-4）：")

        if choice == '1':
            add_record()
        elif choice == '2':
            view_records()
        elif choice == '3':
            stat_monthly()
        elif choice == '4':
            print("已退出，欢迎下次使用！")
            break
        else:
            print("输入错误，请重新选择（1-4）！\n")


if __name__ == "__main__":
    main()