#!/usr/local/bin/python

from datetime import datetime

def compare_datetime(*args):
    #获取输入
    args = args[0]
    date_time = args[0].strip()
    if date_time == '':
        return
    if len(args) > 1:
        pattern = args[1].strip()
    elif len(args) == 1:
        pattern = '%Y-%m-%d %H:%M'
    try:
        #转换输入为时间戳
        actual = datetime.timestamp(datetime.strptime(date_time, pattern))
    except (ValueError):
        print('Please input correct date time format.')
        return
    #转换当前时间为时间戳
    expect = datetime.timestamp(datetime.strptime(datetime.strftime(datetime.now(), pattern), pattern))
    #输出比较结果
    print(actual == expect)

if __name__ == '__main__':
    while True:
        try:
            actual_time = input("Please input your time, the default format is '%Y-%m-%d %H:%M', if you want to change format, please use ',' to separate:").split(",")
            if actual_time == None or actual_time == '':
                continue
            compare_datetime(actual_time)
        except (KeyboardInterrupt, EOFError):
            try:
                while True:
                    result = 'y'
                    result = input("\nDo you really want to exit ([y]/n)?")
                    if result in ['y', '', None]:
                        result = 'y'
                        break
                    elif result == 'n':
                        break
                    else:
                        continue
                if result == 'y':
                    break
                elif result == 'n':
                    continue
            except (KeyboardInterrupt, EOFError):
                break
