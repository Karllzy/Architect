import pickle


class Manger:
    """
    仓储文件管理
    """

    def __init__(self,path=''):
        """
        初始化
        :param path: 指定仓储文件位置
        """
        self.path = path

    def purchase(self, variety, postion, number):
        """
        进货
        :param postion: 砖块位置
        :param number: 砖块数量
        :return:
        """
        try:
            fh = open(self.path, 'rb')
        except IOError:
            print("想的不错")
            fh = open(self.path, 'wb')
        dic = pickle.load(fh)
        fh.close()
        try:
            fh = open(self.path, 'wb')
        except IOError:
            print("想的不错")
            fh = open(self.path, 'wb')
        else:
            print("哇哦")
        info = dic[variety]
        info[0] = postion
        info[2] = number
        dic[variety] = info
        pickle.dump(dic, fh, 3)
        fh.close()

    def withdraw(self, kind):
        """
        取货
        :param kind:种类
        :return:
        """
        fh = open(self.path, 'rb')
        dic = pickle.load(fh)
        fh.close()
        info = dic[kind]
        if info[2] != 0:
            info[2] = info[2] - 1
            dic[kind] = info
        elif kind == '短'and info[2] == 0:
            return False
        elif kind == '厚'and info[2] == 0:
            return False
        else:
            info = dic['长b']
            if info[2] != 0:
                info[2] = info[2] - 1
                dic['长b'] = info
            else:
                info = dic['长c']
                if info[2] != 0:
                    info[2] = info[2] - 1
                    dic['长c'] = info
                else:
                    info = dic['长d']
                    if info[2] != 0:
                        info[2] = info[2] - 1
                        dic['长d'] = info
                    else:
                        info = dic['长e']

                        if info[2] != 0:
                            info[2] = info[2] - 1
                            dic['长e'] = info
                        else:
                            return False

        fh = open(self.path, 'wb')
        pickle.dump(dic, fh, 3)
        fh.close()
        s = info[0][0], info[0][1], info[2]*info[1][2]
        inf = tuple(s)
        print(inf)
        return inf


    def report(self):
        fh = open(self.path, 'rb')
        dic = pickle.load(fh)
        print(dic)



if __name__ == '__main__':
    variety = '短'
    test = Manger("warehouse")
    test.purchase(postion=(10, 10), number=10, variety=variety)
    test.withdraw('长b')
    test.report()


