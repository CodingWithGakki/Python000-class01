# user��-��֪��pyhont�Ƿ�֧�ֽӿ�
class User(object):
    # ��ʼ���û�
    def __init__(self, monetory, quantity):
        # ���ѽ��
        self.monetory = monetory
        # ֧�����
        self.amount = []
        # ��������
        self.quantity = quantity

    # ֧��
    def pay(self):
        pass


# ��ͨ�û�
class CommonUser(User,monetory, quantity):
    # ���캯��
    def __init__(self, monetory, quantity):
        super().__init__(self, monetory, quantity)

    # ��ͨ�û�֧��
    def pay(self):
        if self.monetory < 200:
            self.amount = self.monetory
        else:
            self.amount = self.monetory * 0.9
        return self.amount

# vip�û�
class VipUser(User):
    # ���캯��
    def __init__(self, monetory, quantity):
        super().__init__(self, monetory, quantity)

    # VIP�û�֧��
    def pay(self, instance, owner):
        if self.quantity >= 10:
        self.amount = self.monetory * 0.85
        if self.monetory < 200:
            self.amount = self.monetory
        else:
            self.amount = self.monetory * 0.8
        return self.amount

if __name__ == '__main__':
     user_id = input("����ʱ��ȷ���û����ͣ���ͨ�û�����0��VIP�û�����1:")
     quantity = input("�����������:")
     monetory = input("�������ѽ��:")

     if user_id == 0:
         user CommonUser(monetory,quantity)
     if user_id == 1:
         user VipUser(monetory,quantity)

     user.pay();