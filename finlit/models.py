from django.db import models

# Create your models here.
# profile model - income ?  
# expenses model 
#  
# 
# .

class Profile(models.Model):
    name = models.CharField(max_length=100)
    desciption = models.TextField()

    @property
    def total_expenses(self):
        return sum(self.expenses)
        
    
    def __str__(self):
        return str(self.name)    

# make a model for income and for expenses foreign key relationship.


class Income(models.Model):
    type_income =[('ACTIVE','Active'), ('PASSIVE', 'Passive')]
    profile = models.ManyToManyField("Profile", related_name="income")
    income_type = models.CharField(max_length=10, choices=type_income, default="ACTIVE")     
    amount = models.PositiveIntegerField(null=True)
    date = models.DateField(null=True)


    @property
    def monthly_income(self):
        total = 0
        for item in Income:
            total += item.amount


    def total_income(self):
        return sum(self.income) 


    def __str__(self):
        return str(self.income_type)


class Expenses(models.Model):
    type_expense =[('BASE','Base Expenses'), ('Luxury', 'Luxury Expenses')]
    expenses_type = models.CharField(max_length=10, choices=type_expense, default="BASE")
    profile = models.ManyToManyField("Profile", related_name="expenses")
    debt = models.PositiveIntegerField(null=True)
    # need this to be a foreign key- and i need it 
    date = models.DateField(null=True)
    # def get_monthly_salary(self):
    @property
    def total_expenses(self):
        return sum(self.expenses)

    def __str__(self):
        return str(self.expenses_type)

            

