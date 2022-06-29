from time import time
from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    desciption = models.TextField()        
    
    def __str__(self):
        return str(self.name)    


class Income(models.Model):
    type_income =[('ACTIVE','Active'), ('PASSIVE', 'Passive')]
    type_dispurse = [('SALARY', 'Salary'), ('HOURLY', 'Hourly'), ('FLUCTUATING', 'fluctuating')]
    pay_period_structure = [('WEEKLY', 'Weekly'), ('BIWEEKLY', 'Bi-Weekly'), 
    ('BIMONTHLY', 'Bi-Monthly'), ('MONTHLY', 'Monthly'), ('QUARTERLY', 'Quarterly'), ('ANNUALLY', 'Annual')]
    type_separate = [('BONUS', 'Bonus')]
    profile = models.ManyToManyField("Profile", related_name="+")
    income_type = models.CharField(max_length=20, choices=type_income, default="ACTIVE", null=True)
    dispursement_type = models.CharField(max_length=20, choices=type_dispurse, default="HOURLY", null=True)
    separate_compensation = models.CharField(max_length=20, choices=type_separate, default="BONUS", null=True)     
    amount_income = models.PositiveIntegerField(null=True)
    amount_hours = models.PositiveIntegerField(null=True)
    date_paid = models.DateField(null=True)

# can use @property to place it on an ecoder by Name in properties field- 
# IncomeEncoder can just use "monthly_income" as a parameter and that funciton
# is now available in the views 

    @property
    def monthly_income(self):
        total = 0
        for item in Income['amount']:
            total += item


    @property
    def pay_hourly_calc(self):
        pay_total_monthly = 0
        if self.income_type['ACTIVE'] == True:
            if self.type_dispurse['HOURLY'] == True:
                if self.amount_hours <= 40:
                    pay_total_weekly += self.amount_income * self.amount_hours
                    pay_total_monthly += pay_total_weekly * 4
                else: 
                    additional_hour = self.amount_hours - 40 
                    pay_total_monthly = (40*self.amount_income + 1.5*self.amount_income*additional_hour)
    
    @property
    def pay_calc_salary(self):
        pay_total_monthly = 0
        if self.income_type['ACTIVE'] == True:
            if self.type_dispurse['SALARY'] == True:
                if self.pay_period_structure['ANNUALLY'] == True:
                    pay_total_monthly += self.amount_income // 12
                if self.pay_period_structure['QUARTERLY'] == True:
                    pay_total_monthly += self.amount_income // 3
                if self.pay_period_structure['BIMONTHLY'] == True:
                    pay_total_monthly += self.amount_income * 2
                if self.pay_period_structure['BIWEEKLY'] == True:
                    pay_total_monthly += (self.amount_income * 26) // 12     
                if self.pay_period_structure['WEEKLY'] == True:
                    pay_total_monthly += (self.amount_income * 52) // 12

    def 


    def __str__(self):
        return str(self.income_type)




# might need to change base expenses and non-essential to something else; 

class Expenses(models.Model):
    type_expense =[('BASE','Base Expenses'), ('NON-ESSENTIAL', 'Non-Essential')]
    expenses_type = models.CharField(max_length=20, choices=type_expense, default="BASE", null=True)
    profile = models.ManyToManyField("Profile", related_name="expenses")
    debt = models.PositiveIntegerField(null=True)
    date_due = models.DateField(null=True)
    plan_date = models.DateField(null=True)
    # ^^ unsure if need plan_date ? 

    # def get_monthly_salary(self):
    @property
    def total_expenses(self):
        return sum(self.expenses)

    def __str__(self):
        return str(self.expenses_type)

            

