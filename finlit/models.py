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
    
    def __str__(self):
        return str(self.name)    

# make a model for income and for expenses foreign key relationship.


class Income(models.Model):
    type_income =[('ACTIVE','Active'), ('PASSIVE', 'Passive')]
    type_dispurse = [('SALARY', 'Salary'), ('HOURLY', 'Hourly'), ('FLUCTUATING', 'fluctuating')]
    type_separate = [('BONUS', 'Bonus')]
    profile = models.ManyToManyField("Profile", related_name="+")
    income_type = models.CharField(max_length=10, choices=type_income, default="ACTIVE", null=True)
    dispursement_type = models.CharField(max_length=10, choices=type_dispurse, default="HOURLY", null=True)
    separate_compensation = models.CharField(max_length=10, choices=type_separate, default="BONUS", null=True)     
    amount = models.PositiveIntegerField(null=True)
    date_paid = models.DateField(null=True)


    @property
    def monthly_income(self):
        total = 0
        for item in Income['amount']:
            total += item


    def total_income(self):
        return sum(self.income) 


    def __str__(self):
        return str(self.income_type)

# might need to change base expenses and non-essential to something else; 

class Expenses(models.Model):
    type_expense =[('BASE','Base Expenses'), ('NON-ESSENTIAL', 'Non-Essential')]
    expenses_type = models.CharField(max_length=20, choices=type_expense, default="BASE", null=True)
    profile = models.ManyToManyField("Profile", related_name="expenses")
    debt = models.PositiveIntegerField(null=True)
    # need this to be a foreign key- and i need it 
    date_due = models.DateField(null=True)
    plan_date = models.DateField(null=True)
    # ^^ unsure if need plan_date ? 

    # def get_monthly_salary(self):
    @property
    def total_expenses(self):
        return sum(self.expenses)

    def __str__(self):
        return str(self.expenses_type)

            

