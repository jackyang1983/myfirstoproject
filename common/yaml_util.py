import yaml

class YamlUtil:
    def __init__(self,yaml_file):
        """
        通过init方法把yaml文件读入到类

        :param yaml_file:
        """
        self.yaml_file = yaml_file

    def read_yaml(self):
        """
        读取yaml文件，降yaml文件反序列化，就是将我们的yaml文件转换成dict格式
        :return:
        """
        with open(self.yaml_file,encoding='utf-8') as f:
            value = yaml.load(f,Loader=yaml.FullLoader)
            print(value)
            print(type(value))
            return value


if __name__ == '__main__':
    YamlUtil('../data/test_uilogin.yaml').read_yaml()