#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ��ų�
���ڣ�2020��11��24��

"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����
me=6
# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��
def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��
    if name=="ʯͷ":
      return 0
    if name == "ʷ����":
       return 1
    if name == "ֽ":
        return 2
    if name == "����":
       return 3
    if name == "����":
       return 4

    #��дִ�д���,������ɺ�passɾ��


def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��
    if number==0:
       return "ʯͷ"
    if number==1:
       return "ʷ����"
    if number==2:
       return "ֽ"
    if number==3:
       return "����"
    if number==4:
       return "����"





     #��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    me=name_to_number(player_choice)

    comp_number=random.randrange(0,4)
    a=number_to_name(comp_number)
    print("�������ѡ��Ϊ��",a)
    if me==0 and comp_number==0:
        print("���ͼ��������һ����")
    elif me == 0 and comp_number== 1:
            print("�����Ӯ��")
    elif me == 0 and comp_number == 2:
        print("�����Ӯ��")
    elif me == 0 and comp_number == 3:
        print("��Ӯ��")
    elif me == 0 and comp_number == 4:
        print("��Ӯ��")
    elif me == 1and comp_number == 0:
        print("��Ӯ��")
    elif me == 1 and comp_number == 1:
        print("���ͼ��������һ����")
    elif me == 1 and comp_number == 2:
        print("�����Ӯ��")
    elif me == 1 and comp_number == 3:
        print("�����Ӯ��")
    elif me == 1 and comp_number == 4:
        print("��Ӯ��")
    elif me == 2 and  comp_number== 0:
        print("��Ӯ��")
    elif me == 2 and comp_number == 1:
        print("��Ӯ��")
    elif me == 2 and comp_number == 2:
        print("���ͼ��������һ����")
    elif me == 2 and comp_number == 3:
        print("�����Ӯ��")
    elif me == 2 and comp_number == 4:
        print("�����Ӯ��")
    elif me == 3 and comp_number == 0:
        print("�����Ӯ��")
    elif me == 3 and  comp_number== 1:
        print("��Ӯ��")
    elif me == 3 and comp_number == 2:
        print("��Ӯ��")
    elif me == 3and comp_number == 3:
        print("���ͼ��������һ����")
    elif me == 3 and comp_number == 4:
        print("�����Ӯ��")
    elif me == 4 and comp_number == 0:
        print("�����Ӯ��")
    elif me == 4 and comp_number == 1:
        print("�����Ӯ��")
    elif me == 4 and comp_number == 2:
        print("��Ӯ��")
    elif me == 4 and comp_number == 3:
        print("��Ӯ��")
    elif me == 4 and comp_number == 4:
        print("���ͼ��������һ����")



    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�


     #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


