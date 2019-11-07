# cvs-for-tester

测试员便利店

# 菜单
## 1. compare_datetime.py
### 命令行交互式的时间比较工具
- 使用方法:
  - python compare_datetime.py 进入命令行交互
  - 传入默认格式的时间与当前系统时间比较，返回Boolean
  ```
  2019-11-07 16:47
  ```
  - 传入时间和时间格式，使用半角逗号分隔，与当前系统时间比较，返回Boolean
  ```
  2019/11/07 16, %Y/%m/%d %H
  ```
  
## 2. compare.py
### 比较工具
- 使用方法：
  ```
  compare(expect_data, actual_data)
  ```
  - expect_data 和 actual_data 目前支持string, list, dict 以及各种嵌套。有其他类型需要请联系我
