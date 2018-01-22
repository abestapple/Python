#__*__ encoding:utf-8 __*__
#打印主菜单
from datebase import Book,db
def showMainmenue():
    print("+------请按指令操作------+")
    print("|------1,借阅书籍--------|")
    print("|------2.归还图书--------|")
    print("|-----3.管理员登录-------|")
    print("*****************************")
def Showcode(code): #展现二级显示页面
    #借书
    if code==1:
        print("+------借阅图书界面-------+")
        print("|------1,输入书名--------|")
        print("|-----2.输入书的编号-----|")
        print("|------3.返回上一级------|")
        print("*****************************")
    #还书
    elif code == 2:
        print("+------归还图书界面-------+")
        print("|------1,输入书名--------|")
        print("|-----2.输入书的编号-----|")
        print("|------3.返回上一级------|")
        print("*****************************")
    #管理员登录
    elif code ==3:
        print("+----1,管理员登录界面----+")
        print("*****************************")
    else:
        print("傻逼,请按指令办事")
        print("*****************************")
        main()
#打印书的信息
def Printbookmessage(id,name,author,type,num):
    print("\n\t书的信息如下：\n\t**************************\n\t编号：%s\n\t书名:%s\n\t作者:%s\n\t类型:%s\n\t库存:%s\n\t**************************"%(id,name,author,type,num))
#从数据库中读取书籍信息，打印在控制台
class Borrowbook(object):
    #通过书籍名字来找
    def Findbyname(self,name):
        book=Book.query.filter(Book.name==name).first()
        id=book.id
        name=name
        author=book.author
        type=book.btype
        num=book.num
        Printbookmessage(id,name,author,type,num)
    #通过书籍的编号来查找
    def Findbyid(self,id):
        book = Book.query.filter(Book.id == id).first()
        id = id
        name = book.name
        author = book.author
        type = book.btype
        num = book.num
        Printbookmessage(id, name, author, type, num)
#和上面的类一样
class Returnbook(object)       :
    def Findbyname(self,name):
        book=Book.query.filter(Book.name==name).first()
        id=book.id
        name=name
        author=book.author
        type=book.btype
        num=book.num
        Printbookmessage(id,name,author,type,num)
    def Findbyid(self,id):
        book = Book.query.filter(Book.id == id).first()
        id = id
        name = book.name
        author = book.author
        type = book.btype
        num = book.num
        Printbookmessage(id, name, author, type, num)
#根据用户的输入指令来输出用户操作结果
class YesorNo(object):
    def borrow(self,b):
        if b==1:
            print("恭喜你借书成功\n")
        else:
            print("借书失败\n")
            main()
    def returnb(self,b):
        if b==1:
            print("恭喜你还书成功\n")
        else:
            print("还书失败\n")
            main()
#对用户指令的判断
def getMessage(ifno):
    if ifno == "YES" or ifno=="yes":
        b = 1
        op = YesorNo()
        op.borrow(b)
    else:
        b = 0
        op = YesorNo()
        op.borrow(b)
#对用户指令的判断
def retgetmessage(ifno):
    if ifno == "YES" or ifno=="yes":
        b = 1
        op = YesorNo()
        op.returnb(b)
    else:
        b = 0
        op = YesorNo()
        op.returnb(b)
def getBorrowcode(borrowcode):
    borrowcode = int(borrowcode)
    if borrowcode == 1:
        bookname = input("请输入书名:\n")
        print("*****************************")
        B = Borrowbook()
        try:
            B.Findbyname(bookname)
            print("\n*****************************")
            ifno = input("你是否要借阅?\n\tYES or NO\n")
            print("\n*****************************")
            getMessage(ifno)
        except:
            print("对不起，查无此书!!\t")
            main()
    elif borrowcode == 2:
        bookid = input("请输入书的编号:\n")
        bookid = int(bookid)
        print("*****************************")
        B = Borrowbook()
        try:
            B.Findbyid(bookid)
            print("\n*****************************")
            ifno = input("你是否要借阅?\n\tYES or NO\n")
            print("\n*****************************")
            getMessage(ifno)
        except:
            print("对不起，查无此书!!\t")
            main()
def getReturncode(returncode):
    returncode = int(returncode)
    if returncode== 1:
        bookname = input("请输入书名:\n")
        print("*****************************")
        B = Returnbook()
        try:
            B.Findbyname(bookname)
            print("\n*****************************")
            ifno = input("你是否要还书?\n\tYES or NO\n")
            print("\n*****************************")
            retgetmessage(ifno)
        except:
            print("对不起，查无此书!!\t")
            main()
    elif returncode == 2:
        bookid = input("请输入书的编号:\n")
        bookid = int(bookid)
        print("*****************************")
        B = Returnbook()
        try:
            B.Findbyid(bookid)
            print("\n*****************************")
            ifno = input("你是否要还书?\n\tYES or NO\n")
            print("\n*****************************")
            retgetmessage(ifno)
        except:
            print("对不起，查无此书!!\t")
            main()
#主函数
def main():
    showMainmenue()
    c=input("输入指令代码:")
    print("*****************************")
    c=int(c)
    Showcode(c)
    if c==1:
        borrowcode=input("请输入借阅书籍的指令:\n")
        getBorrowcode(borrowcode)
    elif c==2:
        returncode=input("请输入归还书籍的指令:\n")
        getReturncode(returncode)
    elif c==3:
        print("\t成功登录!!!")

main()
