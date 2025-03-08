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

class BailBondForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['accused_name', 'accused_address', 'name_of_issuing_court', 'offense', 'name_of_appearing_court', 'appearing_day', 'appearing_month', 'appearing_year', 'bail_amount', 'present_day', 'present_month', 'present_year', 'surety_name', 'surety_address', 'name_of_surety_court', 'name_of_trial_court', 'trial_day', 'trial_month', 'trial_year', 'surety_bail_amount']

class ContractBondForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['obligor_name', 'obligor_address', 'obligee_name', 'sum_to_pay', 'plot_address', 'bond_amount', 'present_day', 'present_month', 'present_year']

class SimpleMoneyBondForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['borrower_name', 'borrower_father_name', 'borrower_address', 'lender_name', 'lender_father_name', 'lender_address', 'sum_to_pay', 'sum_in_words', 'object_of_purchase', 'repayment_amount', 'interest_percent', 'date']

class EmployeeBondForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['employee_name', 'employee_address', 'employee_qualification', 'employer_name', 'compensation_amount', 'type_of_product', 'specific_product', 'trade_secret_details', 'penalty_amount', 'restricted_location', 'non_compete_duration']

class MortgageDeedForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['place_of_execution', 'date', 'mortgagor_name', 'mortgagor_father_name', 'mortgagor_address', 'mortgagee_name', 'mortgagee_father_name', 'mortgagee_address', 'property_number', 'property_location', 'loan_amount', 'consideration_amount', 'payment_due_date', 'repayment_amount', 'interest_percent', 'first_installment_date', 'subsequent_installment_payment_day', 'mortgage_property_number', 'mortgage_property_location']
        
class RentAgreementForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['place_of_execution', 'date', 'lessor_name', 'lessor_address', 'lessee_name', 'lessee_address', 'lease_duration_years', 'property_location', 'lease_start_date', 'monthly_rent_amount', 'first_rent_payment_date', 'interest_percent_on_late_payment', 'municipal_and_other_taxes_amount', 'number_of_months_for_default', 'number_of_months_for_dispute_resolution', 'witness_1_name', 'witness_2_name']

class SaleAgreementForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['date', 'seller_name', 'seller_father_name', 'seller_address', 'purchaser_name', 'purchaser_father_name', 'purchaser_age', 'purchaser_address', 'previous_owner_name', 'date_of_previous_sale', 'purpose_of_sale', 'sale_consideration_amount', 'advance_payment_amount', 'cheque_number', 'date_of_advance_payment', 'balance_payment_amount', 'witness_1_name', 'witness_2_name']

