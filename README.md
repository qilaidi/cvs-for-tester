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

## 3. calculate_str_hex_length.py
### 计算输入字符串的十六进制长度：
#### 将输入字符串转换成GBK编码， 然后转成十六进制，返回有多少个Byte
### 入参：str
- 使用方法：
  打开命令行，在脚本目录执行：
  ```
  python calculate_str_hex_length.py "127.0.0.1"
  ```
  - 返回 9
