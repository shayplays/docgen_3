from django import forms
from .models import LegalDocument

class WillForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['name', 'father_name', 'age', 'address', 'executor_name', 'wife_name', 'child_name_1', 'child_name_2', 'flat_no', 'flat_address', 'date', 'month', 'year', 'time']

class LicenseForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['name', 'father_name', 'address', 'date']

class LoanAgreementForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['lender_name', 'borrower_name', 'time', 'loan_amount', 'amount_in_words','loan_period', 'commencement_date', 'termination_date', 'day', 'month', 'year']

class DeedOfHypothecationForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['place', 'day', 'month', 'creditor_name', 'creditor_father_name', 'creditor_age', 'creditor_address', 'borrower_name', 'borrower_father_name', 'borrower_age', 'borrower_address', 'asset_name', 'asset_value', 'manufacturer', 'manufacturer_address', 'advance_payment', 'loan_amount', 'loan_repayment_months', 'start_date', 'interest_rate', 'monthly_payment', 'number_of_missed_installments', 'arbitration_venue']

        