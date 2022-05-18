from django.db import models

# Create your models here.
# profile model - income ?  
# expenses model 
#  
# 
# .

class Profile(models.Model):
    name = models.CharField(max_length=100)
    income = models.PositiveIntegerField(null=True)
    expenses = models.SmallIntegerField(null=True)

    def get_monthly_salary(self):
        return self.salary / 12
    
    def __str__(self):
        return str(self.name)


    # def get_monthly_expenses(self):
    #     return self.expenses 