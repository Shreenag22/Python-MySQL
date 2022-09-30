import mysql.connector as connector

class DBHelper:
  def __init__(self):
    self.con = connector.connect(host="localhost",
                                        user="root",
                                        password="Virat@123",
                                        database='pythontest')
    query= 'create table if not exists user(userid int primary key,username varchar(200),phone varchar(12))'
    cur = self.con.cursor()
    cur.execute(query)
    # print("created")

    #Inserting Values
  def insert_user(self,userid,username,phone):
    query = "insert into user(userid,username,phone) values({},'{}','{}')".format(userid,username,phone)
    print(query)
    cur = self.con.cursor()
    cur.execute(query)
    self.con.commit()
    # print("user saved to db")

  #fetching data
  def fetch_all(self):
    query = "select * from user"
    cur =self.con.cursor()
    cur.execute(query)
    for row in cur:
      print("userid:",row[0],) 
      print("username: ",row[1])
      print("phone:",row[2])


    #delete user
  def delete_user(self,userid):
    query = "delete from user where userid ={}".format(userid)
    print(query)
    c = self.con.cursor()
    c.execute(query)
    self.con.commit()
    # print("deleted")

    #update user details
  def update_user(self,userid,Newname,Newnumber):
    query = "update user set username = '{}', phone ='{}'where userid = {}".format(Newname,Newnumber,userid)
    print(query)
    c = self.con.cursor()
    c.execute(query)
    self.con.commit()
    # print("updated")
    

#Main coding
helper = DBHelper()
# helper.insert_user(1452,'shreenag','9449103656')
# helper.insert_user(1453,'Fins','6361329025')
# helper.insert_user(1454,'Shubham','6361326024')
# helper.insert_user(1455,'Daya','6361329064')
# helper.insert_user(1456,'Kiran','6361399024')
# helper.insert_user(1457,'Ashok','6360329024')

# helper.fetch_all()
# helper.delete_user(1457)
# helper.delete_user(1454)py5

# helper.update_user(1455,'Dayasagara','7656565656')
# helper.update_user(1453,'Madathil Fins Abraham','8484848484')

# print("Data: ")
# helper.fetch_all()