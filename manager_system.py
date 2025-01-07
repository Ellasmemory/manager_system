import os
import pickle
# import base64
# import requests

global In_to_library
In_to_library = 0
global state
state = 0

#端口选择
def status():
    print("----------端口选择------------")
    print("1、客户端")
    print("2、管理员端")
    print("3、退出")
    status_choice = input("请选择：")
    if status_choice == "1":
        client.run()
        global state 
        state = 1
    elif status_choice == "2":
        manager.run()
        state = 2
    elif status_choice == "3":
        exit()
    else:
        print("输入有误，请重新输入。")
        status()

#书
class Book:
    def __init__(self, book_id, book_type, name, price):
        self.book_id = book_id
        self.book_type = book_type
        self.name = name
        self.price = price

    def __str__(self):
        return f"ID: {self.book_id}, Type: {self.book_type}, Name: {self.name}, Price: {self.price}"
    
#用户登陆界面
class Client:
    def __init__(self, data_file="Client_dict.txt"):
        self.data_file = data_file
        self.Client_info = []
        self.load_Client_info()
    #加载用户信息
    def load_Client_info(self):
        """加载用户信息"""
        if os.path.exists(self.data_file) and os.path.getsize(self.data_file) > 0:
            with open(self.data_file, 'rb') as file:
                try:
                    self.Client_info = pickle.load(file)
                except EOFError:
                    self.Cilent_info = []  # 如果文件为空或格式有误
        else:
            self.Client_info = []
    #登陆界面
    def log(self):
        """展示登录菜单"""
        print("-----------欢迎来到用户登陆界面------------")
        print("1、登陆")
        print("2、注册")
        print("3、退出")
    #用户登陆
    def sign_in(self):
        """用户登录"""
        user_name = input("请输入您的用户名(按enter退出):")
        if user_name == "":
            return
        password = input("请输入您的密码:")
        # 登录检查用户信息，确保 Managers_info 中存的是字典
        for user in self.Client_info:
            if isinstance(user, dict) and user.get('username') == user_name and user.get('password') == password:
                print("登陆成功！")
                global In_to_library
                In_to_library = 1
                return  # 登录成功后直接返回，不需要继续执行
        print("用户名或密码错误，请重新输入！")
        input("请按enter")
        self.sign_in()  # 重新尝试登录

    def sign_up(self):
        """用户注册"""
        user_name = input("请输入你想要的用户名:")
        # 检查用户名是否已存在
        for user in self.Client_info:
            if user['username'] == user_name:
                print("用户名已存在，请选择其他用户名！")
                input("请按enter")
                return
        password = input("设置一个密码: ")
        Client_info = {"username": user_name, "password": password}
        self.Client_info.append(Client_info)
        with open(self.data_file, mode="wb") as f1:
            pickle.dump(self.Client_info, f1)  # 将所有用户信息保存到文件
        print("注册成功！")

    def run(self):
        while True:
            self.log()
            choice = input("请选择：")
            if choice == "1":
                self.sign_in()
                if In_to_library == 1:
                    break
            elif choice == "2":
                self.sign_up()
            elif choice == "3":
                print("感谢你的使用，下次再见")
                exit()
            else:
                print("输入有误，请重新输入。")

#管理员登陆界面
class Manager:
    def __init__(self, data_file="Manager_dict.txt"):
        self.data_file = data_file
        self.Manager_info = []
        self.load_Manager_info()

    def load_Manager_info(self):
        """加载用户信息"""
        if os.path.exists(self.data_file) and os.path.getsize(self.data_file) > 0:
            with open(self.data_file, 'rb') as file:
                try:
                    self.Manager_info = pickle.load(file)
                except EOFError:
                    self.Manager_info = []  # 如果文件为空或格式有误
        else:
            self.Manager_info = []

    def log(self):
        """展示登录菜单"""
        print("-----------欢迎来到管理员登陆界面------------")
        print("1、登陆")
        print("2、退出")

    def sign_in(self):
        """用户登录"""
        user_name = input("请输入您的用户名(按enter退出):")
        if user_name == "":
            return
        password = input("请输入您的密码:")
        # 登录检查用户信息，确保 Managers_info 中存的是字典
        for user in self.Manager_info:
            if isinstance(user, dict) and user.get('username') == user_name and user.get('password') == password:
                print("登陆成功！")
                global In_to_library
                In_to_library = 1
                return  # 登录成功后直接返回，不需要继续执行
        print("用户名或密码错误，请重新输入！")
        input("请按enter")
        self.sign_in()  # 重新尝试登录

    #创建管理员的时候会用上！！！
    # def sign_up(self):
    #     """用户注册"""
    #     user_name = input("请输入你想要的用户名:")
    #     # 检查用户名是否已存在
    #     for user in self.Manager_info:
    #         if user['username'] == user_name:
    #             print("用户名已存在，请选择其他用户名！")
    #             input("请按enter")
    #             return
    #     password = input("设置一个密码: ")
    #     Manager_info = {"username": user_name, "password": password}
    #     self.Manager_info.append(Manager_info)
    #     with open(self.data_file, mode="wb") as f1:
    #         pickle.dump(self.Manager_info, f1)  # 将所有用户信息保存到文件
    #     print("注册成功！")

    def run(self):
        """运行系统"""
        while True:
            self.log()
            choice = input("请选择：")
            if choice == '1':
                self.sign_in()
                if In_to_library == 1:
                    break
            elif choice == '2':
                print("感谢您的使用，再见！")
                exit()
            #注册管理员的时候开启
            # elif choice == '3':
            #     self.sign_up()
            #     exit()
            else:
                print("输入有误，请重新输入！")
                input("请按enter")

class Manager_Library_System:
    def __init__(self, data_file="librarys.data"):
        self.data_file = data_file
        self.books = []
        self.load_books()

    def load_books(self):
        if os.path.exists(self.data_file) and os.path.getsize(self.data_file) > 0:
            with open(self.data_file, 'rb') as file:
                self.books = pickle.load(file)
        else:
            self.books = []
    def save_books(self):
        with open(self.data_file, 'wb') as file:
            pickle.dump(self.books, file)

    def add_book(self, book):
        if any(b.name == book.name for b in self.books):
            print("\u274c 相同名字的书籍已经存在！")
        else:
            self.books.append(book)
            print("\u2705 图书添加完成！")

    def delete_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print("\u2705 图书更新完成！")
                return
        print("\u274c 找不到该书籍！")

    def modify_book(self, book_id, book_type=None, name=None, price=None):
        for book in self.books:
            if book.book_id == book_id:
                print("\u2705 已找到你想修改的书籍")
                if book_type:
                    book.book_type = book_type
                if name:
                    if any(b.name == name and b.book_id != book_id for b in self.books):
                        print("\u274c 已有名字相同的书籍！")
                        return
                    book.name = name
                if price:
                    book.price = price
                print("\u2705 更新图书成功！")
                return
        print("\u274c 找不到该书籍")

    def search_book(self, keyword):
        results = [book for book in self.books if keyword.lower() in book.name.lower()]
        if results:
            for book in results:
                print(book)
        else:
            print("\u274c找不到该书籍")

    def display_books(self):
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("\u274c 在书库中没有书籍")

    def run(self):
        while True:
            print("\n请选择如下功能:")
            print("1. 添加图书")
            print("2. 删除图书")
            print("3. 修改图书信息")
            print("4. 查询图书信息")
            print("5. 显示所有图书")
            print("6. 保存图书信息")
            print("7. 退出系统")

            choice = input("请输入你需要的功能序号: ")
            if choice == '1':
                book_id = input("输入图书ID: ")
                book_type = input("输入图书类型: ")
                name = input("输入图书名字: ")
                price = input("输入图书价格: ")
                self.add_book(Book(book_id, book_type, name, price))
            elif choice == '2':
                book_id = input("输入图书ID,并开始执行删除功能: ")
                self.delete_book(book_id)
            elif choice == '3':
                book_id = input("输入图书ID进行修改: ")
                book_type = input("输入你想更换的类型(不换按enter跳过): ")
                name = input("输入新名字(不换按enter跳过): ")
                price = input("输入新价格(不换按enter跳过): ")
                self.modify_book(book_id, book_type if book_type else None, name if name else None, price if price else None)
            elif choice == '4':
                keyword = input("输入关键字进行查找: ")
                self.search_book(keyword)
            elif choice == '5':
                self.display_books()
            elif choice == '6':
                self.save_books()
                #self.upload_file_to_github(self.data_file, "Ellasmemory/manager_system")
                print("\u2705 已经保存图书信息到文件中")
            elif choice == '7':
                print("\u2705 退出系统完成！")
                break
            else:
                print("\u274c 错误的选择，再选择一次")

class Client_Library_System(Manager_Library_System):
    def __init__(self, data_file = "librarys.data", data_file2 = "lent_books.txt"):
        self.data_file = data_file
        self.data_file2 = data_file2
        self.books = []
        self.load_books()
        self.lent_books = []
        self.load_lent_books()

    def load_lent_books(self):
        if os.path.exists(self.data_file2) and os.path.getsize(self.data_file2) > 0:
            with open(self.data_file2, 'rb') as file2:
                self.lent_books = pickle.load(file2)
        else:
            self.lent_books = []

    def lent(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.lent_books.append(book)
                self.books.remove(book)
                self.save_books()
                print("\u2705 图书借阅完成！")
                return
        print("\u274c 找不到该书籍！")

    def return_book(self, book_id):
        for book in self.lent_books:
            if book.book_id == book_id:
                self.books.append(book)
                self.lent_books.remove(book)
                self.save_books()
                print("\u2705 图书归还完成！")
                return
        print("您没有借阅此书，归还失败！")

    def search_lent_book(self):
        if self.lent_books:
            for book in self.lent_books:
                print(book)
        else:
            print("您没有借阅任何书籍")
        
    def save_books(self):
        with open(self.data_file, 'wb') as file:
            pickle.dump(self.books, file)
        with open(self.data_file2, 'wb') as file2:
            pickle.dump(self.lent_books, file2)


    def run(self):
        while True:
            print("----------欢迎来到借阅系统------------")
            print("1、显示书库所有书籍(反正没什么书,部显示出来了)")
            print("2、借书")
            print("3、还书")
            print("4、查看借阅信息")
            print("5、退出")
            choice = int(input("请选择："))
            if choice == 1:
                self.display_books()
            elif choice == 2:
                book_id = input("输入图书ID,并借阅此书: ")
                self.lent(book_id)
            elif choice == 3:
                print("您借阅的书有:")
                for book in self.lent_books:
                    print(book)
                book_id = input("输入图书ID,并还回此书: ")
                self.return_book(book_id)
            elif choice == 4:
                self.search_lent_book()
            elif choice == 5:
                print("感谢您的使用！")
                exit()
            else:
                print("您的输入有误，请重新输入！")

if __name__ == "__main__":
    manager = Manager()
    client = Client()
    status()
    if state == 1:
        client_system = Client_Library_System()
        client_system.run()
    elif state == 2:
        manager_system = Manager_Library_System()
        manager_system.run()
