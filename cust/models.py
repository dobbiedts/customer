from django.db import models

# Create your models here.
class customer_tab(models.Model):
    name = models.CharField(max_length = 20, help_text = "Enter customer name")
    sector =  models.CharField(max_length = 20, help_text = "Enter sector", default = None)
    industry = models.CharField(max_length = 20, help_text = "Enter industry", default = None)
    phone = models.CharField(max_length = 20, help_text = "Enter phone number", default = None)
    email = models.EmailField(max_length = 254) 
    gender = models.CharField(max_length = 20, help_text = "Enter customer gender")
    date_birth = models.DateField(null = True, blank = True) 
    
    
    def __str__(self):
        
        return self.name
        return self.sector
        return self.industry
        return self.phone
        return self.email
        return self.gender
        
     
    def get_absolute_url(self):
        """Returns the url to access a particular customer instance."""
        return reverse('customer_tabdetail', args=[str(self.id)])
    
    
    
class account_tab(models.Model):
    postid = models.CharField(max_length = 20, help_text = "Enter account id", default = None)
    title =  models.CharField(max_length = 20, help_text = "Enter account title", default = None)
    customer_id = models.ForeignKey('customer_tab', on_delete=models.SET_NULL, null=True)
    account_bal = models.CharField(max_length = 20, help_text = "Enter account balance", default = None)
    
    def __str__(self):
        
       
        return self.title
        return self.customer_id 
        return self.account_bal
        return self.postid
        