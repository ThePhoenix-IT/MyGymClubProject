from django.db import models

# Create your models here.

class Member(models.Model):
    memberId = models.AutoField(primary_key=True)
    memberCode = models.CharField(max_length=20)
    memberFullName = models.CharField(max_length=100)
    memberAddress = models.CharField(max_length=100)
    memberPhoneNum = models.IntegerField()

    def __init__(self, memberCode):
        self.memberCode = memberCode

    def __str(self):
        return '%d: %s' % (self.memberCode, self.memberCode)

    class Meta:
        db_table = "member"
        unique_together = ('memberId', 'memberCode')
        ordering = ['memberCode']
