from tokenize import String
from django.db import models
from numpy import require

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  email = models.CharField(max_length=100)

  def __str__(self):
    return self.email +" "+ self.author

class Category(models.Model):
  type = models.CharField(max_length=200, null=True, blank=True)
  _id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return self.type
class Address(models.Model):
  number = models.CharField(max_length=200, null=True, blank=True)
  street = models.CharField(max_length=200, null=True, blank=True)
  dictrict = models.CharField(max_length=200, null=True, blank=True)
  city = models.CharField(max_length=200, null=True, blank=True)
  _id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return self.number+","+self.street+self.dictrict+","+self.city

class Supplier(models.Model):
  address = models.ForeignKey(Address,on_delete=models.SET_NULL,null=True)
  name = models.CharField(max_length=200, null=True, blank=True)
  phone = models.CharField(max_length=200, null=True, blank=True)
  email = models.CharField(max_length=200, null=True, blank=True)
  avatar = models.CharField(max_length=200, null=True, blank=True)
  _id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return self.name

class Product(models.Model):
  supplier = models.ForeignKey(Supplier,on_delete=models.SET_NULL,null=True)
  name = models.CharField(max_length=200, null=True, blank=True)
  inventory = models.CharField(max_length=200, null=True, blank=True)
  type = models.CharField(max_length=200, null=True, blank=True)
  price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
  discount = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
  avatar = models.CharField(max_length=200, null=True, blank=True)
  createdAt = models.DateTimeField(auto_now_add=True)
  _id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return self.name

class MyUser(models.Model):
  firstname = models.CharField(max_length=200, null=True, blank=True)
  lastname = models.CharField(max_length=200, null=True, blank=True)
  email = models.CharField(max_length=200, null=True, blank=True)
  password = models.CharField(max_length=200, null=True, blank=True)
  gender = models.CharField(max_length=200, null=True, blank=True)
  birthday = models.CharField(max_length=200, null=True, blank=True)
  phone = models.CharField(max_length=200, null=True, blank=True)
  _id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return self.email

class Media(models.Model):
  link = models.CharField(max_length=200, null=True, blank=True)
  _id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
  	return self.link

class Bill(models.Model):
  product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
  user = models.ForeignKey(MyUser,on_delete=models.SET_NULL,null=True,blank=True)
  date_payment = models.CharField(max_length=200, null=True, blank=True)
  date_initialization = models.CharField(max_length=200, null=True, blank=True)
  total = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
  quantity = models.CharField(max_length=200, null=True, blank=True)
  sale_off = models.CharField(max_length=200, null=True, blank=True)

  _id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return str(self.total)+" "+self.quantity

class ProductMedia(models.Model):
  product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
  media = models.ForeignKey(Media,on_delete=models.SET_NULL,null=True)
  _id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
  	return str(self._id)

class Clothes(models.Model):
  product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
  gender = models.CharField(max_length=200, null=True, blank=True)
  material = models.CharField(max_length=200, null=True, blank=True)
  color = models.CharField(max_length=200, null=True, blank=True)
  size = models.CharField(max_length=200, null=True, blank=True)
  _id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
  	return self.material+" "+self.color

class Book(models.Model):
  product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
  author = models.CharField(max_length=200, null=True, blank=True)
  language = models.CharField(max_length=200, null=True, blank=True)
  Date_manufacturing = models.DateTimeField(auto_now_add=True)
  _id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return self.author
class BookCategory(models.Model):
  book = models.ForeignKey(Book,on_delete=models.SET_NULL,null=True)
  category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
  _id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return str(self._id)

class Laptop(models.Model):
  product = models.ForeignKey(Product,on_delete=models.CASCADE)
  CPU = models.CharField(max_length=200, null=True, blank=True)
  GPU = models.CharField(max_length=200, null=True, blank=True)
  VGA = models.CharField(max_length=200, null=True, blank=True)
  screen = models.CharField(max_length=200, null=True, blank=True)
  insurance = models.CharField(max_length=200, null=True, blank=True)
  _id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
  	return self.CPU+" "+self.GPU+" "+self.VGA

class Cart(models.Model):
  total = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
  _id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return str(self._id)

class CartProduct(models.Model):
  cart = models.ForeignKey(Cart,on_delete=models.SET_NULL,null=True)
  product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
  _id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return str(self._id)