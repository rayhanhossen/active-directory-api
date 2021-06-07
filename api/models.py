from django.db import models


class ADUser(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    manager = models.CharField(max_length=255, null=True, blank=True)
    SAM_account_name = models.CharField(max_length=255, blank=True)
    pager = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    user_account_control = models.IntegerField(default=546, null=True, blank=True)
    office = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    address3 = models.CharField(max_length=255)
    PO = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    division = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    parent_OU = models.CharField(max_length=255)
    band = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)
    status = models.IntegerField(default=0, blank=True, null=True)
    joining_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.full_name
