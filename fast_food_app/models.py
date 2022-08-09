from django.db import models
from accounts.models import User

class Mahsulotlar(models.Model):
	nomi = models.CharField(max_length = 200)
	tarkibi = models.TextField()
	rasmi = models.ImageField(upload_to = 'images/')
	narhi = models.FloatField(max_length = 20)


	def __str__(self):
		return self.nomi


class Comment(models.Model):
	userName = models.CharField(max_length=150,null=True)
	phone = models.CharField(max_length=20)
	email = models.CharField(max_length=50)
	message = models.TextField()
	Data = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return f'{self.userName}' 




# 1-bosqich

#Order ya'niy mahsulotni savatga qushish uchun model
#from django.contrib.auth.models import User


class Order(models.Model):
	customer = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
	date_orderd = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=200,null=True)
	complete = models.BooleanField(default=False,null=True,blank=False)


	'''pastdagi get_total funksiyadan qaytgan qiymatni 
	barcha orderItem(savatdagi mahsulotlar)ni hisoblash uchun'''


	@property #Dekorator
	def get_card_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total


		'''pastdagi quantity (mahsulotlarni sonini ) va barcha orderItem(savatdagi mahsulotlar)
		larni hisoblash uchun'''

	@property #Dekorator
	def get_card_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 


		# String obyektini qaytaradi
	def __str__(self):
		return str(self.id)	


# mahsulotni qachon va kim tomonidan qaysi mahsulot qushilganligni saqlash uchun model

class OrderItem(models.Model):
	product = models.ForeignKey(Mahsulotlar, on_delete=models.SET_NULL,blank=True,null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True,null=True)
	quantity = models.IntegerField(default=0,null=True,blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	#Mahsulotni narxni soniga kopaytrb beradi

	@property # Dekorator
	def get_total(self):
		total = self.product.narhi * self.quantity 
		return total

	#String obyektni qaytaradi	
	def	__str__(self):
		return str(self.id)