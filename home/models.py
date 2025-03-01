from django.db import models

class LegalDocument(models.Model):
    DOCUMENT_CHOICES = [
        ('will', 'Simple Will'),
        ('license', 'License Agreement'),
        ('loan_agreement', 'Loan Agreement'),
        ('deed_of_hypothecation', 'Deed Of Hypothecation'),

    ]
    document_type = models.CharField(max_length=255, choices=DOCUMENT_CHOICES)
    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    address = models.TextField()
    executor_name = models.CharField(max_length=255, blank=True, null=True)
    wife_name = models.CharField(max_length=255, blank=True, null=True)
    child_name_1 = models.CharField(max_length=255, blank=True, null=True)
    child_name_2 = models.CharField(max_length=255, blank=True, null=True)
    flat_no = models.CharField(max_length=50, blank=True, null=True)
    flat_address = models.TextField(blank=True, null=True)
    date = models.CharField(max_length=50)
    month = models.CharField(max_length=50, blank=True, null=True)
    year = models.CharField(max_length=50, blank=True, null=True)
    time = models.CharField(max_length=50, blank=True, null=True)
    
    #loan_agreement
    lender_name = models.CharField(max_length=255, blank=True, null=True)
    borrower_name = models.CharField(max_length=255, blank=True, null=True)
    loan_amount = models.CharField(max_length=50, blank=True, null=True)
    amount_in_words = models.CharField(max_length=255, blank=True, null=True)
    loan_period = models.CharField(max_length=50, blank=True, null=True)
    commencement_date = models.CharField(max_length=50, blank=True, null=True)
    termination_date = models.CharField(max_length=50, blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)

    #deed of hypothecation
    place = models.CharField(max_length=255, blank=True, null=True)
    
    month = models.CharField(max_length=255, blank=True, null=True)
    creditor_name = models.CharField(max_length=255, blank=True, null=True)
    creditor_father_name = models.CharField(max_length=255, blank=True, null=True)
    creditor_age = models.IntegerField(blank=True, null=True)
    creditor_address = models.CharField(max_length=255, blank=True, null=True)
    #borrower_name = models.CharField(max_length=255, blank=True, null=True)
    borrower_father_name = models.CharField(max_length=255, blank=True, null=True)
    borrower_age = models.IntegerField(blank=True, null=True)
    borrower_address = models.CharField(max_length=255, blank=True, null=True)
    asset_name = models.CharField(max_length=255, blank=True, null=True)
    asset_value = models.IntegerField(blank=True, null=True)
    manufacturer = models.CharField(max_length=255, blank=True, null=True)
    manufacturer_address = models.CharField(max_length=255, blank=True, null=True)
    advance_payment = models.IntegerField(blank=True, null=True)
    #loan_amount = models.IntegerField(blank=True, null=True)
    loan_repayment_months = models.IntegerField(blank=True, null=True)
    start_date = models.CharField(max_length=50, blank=True, null=True)
    interest_rate = models.IntegerField(blank=True, null=True)
    monthly_payment = models.IntegerField(blank=True, null=True)
    number_of_missed_installments = models.IntegerField(blank=True, null=True)
    arbitration_venue = models.CharField(max_length=255, blank=True, null=True)




