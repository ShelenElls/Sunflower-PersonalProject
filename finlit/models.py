from django.db import models

# Create your models here.
# profile model - income ?  
# expenses model 
#  
# 
# .

class Profile(models.Model):
    name = models.CharField(max_length=100)
    expenses = models.ForeignKey()


    @property
    def total_expenses(self):
        return sum(self.expenses)
        
    
    def __str__(self):
        return str(self.name)    

# make a model for income and for expenses foreign key relationship.


class Income(models.Model):
    type_income =[('ACTIVE','Active'), ('PASSIVE', 'Passive')]
    profile = models.ForeignKey("Profile", related_name="income", on_delete=models.CASCADE)
    income_type = models.CharField(max_length=10, choices=type_income, default="ACTIVE") 
        # i want this to be a drop down that selects either, active income
        # passive income, dividends, rental income 
    
    amount = models.PositiveIntegerField(null=True)
    # need this to be a foreign key- and i need it 
    date = models.DateField(null=True)
    # def get_monthly_salary(self):
    #     return self.salary / 12

    @property
    def monthly_income(self):
        total = 0
        for item in Income:
            total += item.amount


    def total_income(self):
        return sum(self.income) 


    def __str__(self):
        return str(self.name)


class Expenses(models.Model):
    type_expense =[('BASE','Base Expenses'), ('Luxury', 'Luxury Expenses')]

    expenses_type = models.CharField(max_length=10, choices=type_expense, default="BASE")
        # i want this to be a drop down that selects either, active income
        # passive income, dividends, rental income 
    
    debt = models.PositiveIntegerField(null=True)
    # need this to be a foreign key- and i need it 
    date = models.DateField(null=True)
    # def get_monthly_salary(self):
def total_expenses(self):
        return sum(self.expenses)
        

