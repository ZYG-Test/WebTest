
# 读取txt文件
def read_txt(filename):
    #获取文件地址
    filepath = '../data/'+filename
    #读取文件内容并返回
    with open(filepath,'r',encoding='utf-8') as f:
        return f.readlines()

if __name__ == '__main__':
        read_txt('login.txt')
        print('_________'*10)
        '''使用方法遍历所有数据并转换成列表'''
        arrs =[]
        for data in read_txt('login.txt'):
            arrs.append(tuple(data.strip().split(',')))
        print(arrs[1:])