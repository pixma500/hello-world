import mysql.connector
import datetime


ENTRY=1
LOOK=2
QUIT=3

def main():
	choice=0
	while choice!=QUIT:
		choice=get_menu_choice()
		if choice==ENTRY:
			entry_get()
		if choice==LOOK:
			look()
				
def get_menu_choice():
	print("Меню")
	print('''
	1.Вход/Регистрация
	2.Просмотр товаров
	3.Выход ''')
	choice=int(input("Введите выбранный пункт: "))
	return choice
	
def pokup():
	print("Меню")
	print('''
	2.Выбор товаров
	3.Выход ''')
	choice=int(input("Введите выбранный пункт: "))
	if choice==LOOK:
		look_prod()
	if choice==QUIT:
		v_zakaz()
		main()
	
def look():
	print("Наличие товаров:")
	connect()
	mycursor = mydb.cursor()
	mycursor.execute("SELECT id_prices,product FROM prices ORDER By id_prices ")
	for (id_prices,product) in mycursor:
		print(id_prices,product)
	print("Покупка после регестрации")
	
def entry_get():
	nam=str(input("Введите имя :"))
	phone=input("телефон :")
	password=input("пароль:")
	connect()
	mycursor = mydb.cursor()
	mycursor.execute("SELECT name,password FROM contacts")

	if (nam,password) in mycursor:
		print("Добро пожаловать {}".format(nam))
	else:
		print("Регестрирую")
		sql = "INSERT INTO contacts (name, phone,password) VALUES (%s,%s,%s)"
		val = (nam,phone,password)
		mycursor.execute(sql, val)
		mydb.commit()
	connect()
	mycursor = mydb.cursor()
	mycursor.execute("SELECT id_cont FROM contacts where name=%s " ,(nam,))
	for (id_cont,) in mycursor:
		global d
		d=id_cont
	look_prod()
	
def look_prod():
	connect()
	mycursor = mydb.cursor()
	mycursor.execute("SELECT id_prices,product FROM prices ORDER By id_prices ")
	print("Выберите товар:")
	global n,k
	for (id_prices,product) in mycursor:
		print(id_prices,product)
	n=int(input('Введите номер '))
	k=int(input("и количество "))
	if k<=0:
		look_prod()
	mycursor.execute('''SELECT quantity
	FROM prices INNER JOIN sclad 
	ON prices.id_prices=sclad.id_prices
	Where prices.id_prices= '%s' ''',(n,))
	
	for product in mycursor:
		if product[0]>=k:
			print('Оформляю заказ')
			sql = "INSERT INTO ord (cont,prices,kol,data) VALUES (%s,%s,%s,%s)"
			val = (d,n,k,datetime.date.today())
			mycursor.execute(sql,val)
			mydb.commit()
			sql = "UPDATE sclad SET quantity=quantity-'%s' WHERE id_prices='%s'"
			val = (k,n)
			mycursor.execute(sql,val)
			mydb.commit()
		else:
			print("Такого количества нет" )
			look_prod()
	pokup()

def v_zakaz():
	print("Ваш заказ")
	connect()
	mycursor = mydb.cursor()
	mycursor.execute("SELECT product,prices FROM prices where id_prices=%s",(n,))
	for (product,prices) in mycursor:
		print('{} в количествве {} на сумму {} грн.'.format(product,k,k*prices))

def connect():
	global mydb
	mydb= mysql.connector.connect (
     host = "127.0.0.1" ,
     port = 3307 ,
     user = "root" ,
     password = "2550100",
     database="mydatabase",
     #charset="cp1251"
     )

main()

