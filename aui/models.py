from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.CharField(max_length=10, unique=True, default=0)
    Aadhar_Number = models.IntegerField(unique=True, primary_key=True, default=0)
    Is_Active = models.BooleanField()
    street = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=10,null=True)
    state = models.CharField(max_length=10,null=True)
    Postal_Code = models.IntegerField(null=True)
    School_or_College_name = models.CharField(max_length=100)
    Year_of_Passing = models.IntegerField()
    percentage = models.FloatField()
    Account_Number = models.IntegerField()
    Bank_Name = models.CharField(max_length=100)
    IFSC_Code = models.IntegerField(unique=True)
    Full_Name = models.CharField(max_length=100)
    Date_of_birth = models.DateField()
    Blood_Group = models.CharField(max_length=100)
    Contact_Number_1 = models.IntegerField()
    Contact_Number_2 = models.IntegerField(null=True, blank=True)
    Email_ID_1 = models.EmailField()
    Email_ID_2 = models.EmailField(null=True, blank=True)
    Company_Name = models.CharField(max_length=100)
    Job_Role = models.CharField(max_length=100)
    Work_Experience_in_Years = models.IntegerField()

    def __str__(self):
        return f"{self.Aadhar_Number}-{self.Full_Name}"