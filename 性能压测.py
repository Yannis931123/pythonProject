import subprocess
import time

# JMeter脚本的路径和输出文件路径
jmx_files = {
    'group1': 'path/to/script1.jmx',
    'group2': 'path/to/script2.jmx'
}
output_files = {
    'group1': 'path/to/output1.jtl',
    'group2': 'path/to/output2.jtl'
}
html_report_dirs = {
    'group1': 'path/to/report1',
    'group2': 'path/to/report2'
}

# 执行JMeter测试
for group, jmx_file in jmx_files.items():
    output_file = output_files[group]
    html_report_dir = html_report_dirs[group]
    print(f"开始执行{group}的测试")
    subprocess.run(['jmeter', '-n', '-t', jmx_file, '-l', output_file])
    print("生成HTML报告")
    subprocess.run(['jmeter', '-g', output_file, '-o', html_report_dir])
    print(f"{group}测试完成")

# 等待所有测试完成
time.sleep(5)

# 分析结果（这里只是简单打印完成，实际应用中可能需要更复杂的分析逻辑）
print("所有分组测试完成")