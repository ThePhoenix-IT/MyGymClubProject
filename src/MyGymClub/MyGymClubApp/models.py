from django.db import models

# Create your models here.

class Member(models.Model):
    memberId = models.AutoField(primary_key=True)
    memberCode = models.CharField(max_length=20)
    memberFullName = models.CharField(max_length=100)
    memberAddress = models.CharField(max_length=100)
    memberPhoneNum = models.IntegerField()
    creationDate = models.DateTimeField(auto_now_add=True, blank=True)

    def __init__(self, memberCode):
        self.memberCode = memberCode

    def __str(self):
        return '%d: %s' % (self.memberCode, self.memberCode)

    class Meta:
        db_table = "member"
        unique_together = ('memberId', 'memberCode')
        ordering = ['memberCode']
        
        
 class EquipmentStatus(models.Model):
    equipemntStatusId = models.AutoField(primary_key=True)
    equipmentStatusDesc = models.CharField(max_length=50)
    creationDate = models.DateTimeField(auto_now_add=True, blank=True)
    
 class Equipment(models.Model):
    equipemntId = models.AutoField(primary_key=True)
    equipmentCode = models.CharField(max_length=20)
    equipmentStatusId = models.ForeignKey(EquipmentStatus, on_delete=models.CASCADE)
    creationDate = models.DateTimeField(auto_now_add=True, blank=True)
