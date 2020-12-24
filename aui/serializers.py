from rest_framework import serializers
from aui.models import Users

class UsersSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(required=False)
    Aadhar_Number = serializers.IntegerField(required=False)
    Is_Active = serializers.BooleanField(required=False)
    street = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    state = serializers.CharField(required=False)
    Postal_Code = serializers.IntegerField(required=False)
    School_or_College_name = serializers.CharField(required=False)
    Year_of_Passing = serializers.IntegerField(required=False)
    percentage = serializers.FloatField(required=False)
    Account_Number = serializers.IntegerField(required=False)
    Bank_Name = serializers.CharField(required=False)
    IFSC_Code = serializers.IntegerField(required=False)
    Full_Name = serializers.CharField(required=False)
    Date_of_birth = serializers.DateField(required=False)
    Blood_Group = serializers.CharField(required=False)
    Contact_Number_1 = serializers.IntegerField(required=False)
    Contact_Number_2 = serializers.IntegerField(required=False)
    Email_ID_1 = serializers.EmailField(required=False)
    Email_ID_2 = serializers.EmailField(required=False)
    Company_Name = serializers.CharField(required=False)
    Job_Role = serializers.CharField(required=False)
    Work_Experience_in_Years = serializers.IntegerField(required=False)
    class Meta:
        model = Users
        fields = '__all__'