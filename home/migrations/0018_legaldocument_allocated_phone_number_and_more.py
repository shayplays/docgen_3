# Generated by Django 5.1.5 on 2025-03-10 07:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_legaldocument_donee_address_legaldocument_donee_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='legaldocument',
            name='allocated_phone_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='bank_balance_1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='bank_balance_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='bank_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='bank_name_1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='branch_name_1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='charitable_trust_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='company_name_1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='company_name_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='date_of_agreement',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='deceased_person_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='dispute_subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='donated_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='execution_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='expenses_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='family_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='first_party_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='first_party_father_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='first_party_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='karta_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='liabilities_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='net_capital_of_family',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='other_member_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='partition_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='party_1_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='party_1_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='party_2_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='party_2_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='party_3_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='party_3_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='phone_number_1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='phone_number_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='recipient_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='relationship_between_party_1_and_party_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='second_party_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='second_party_father_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='second_party_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='shares_count_1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='shares_value_1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='shares_value_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='third_party_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='third_party_father_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='third_party_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='total_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='legaldocument',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='legaldocument',
            name='document_type',
            field=models.CharField(choices=[('will', 'Simple Will'), ('license', 'License Agreement'), ('loan_agreement', 'Loan Agreement'), ('deed_of_hypothecation', 'Deed Of Hypothecation'), ('contract_bond', 'Contract Bond'), ('simple_money_bond', 'Simple Money Bond'), ('employee_bond_for_non_compete', 'Employee Bond for Non-Compete'), ('simple_mortgage_deed', 'Simple Mortgage Deed'), ('rent_agreement', 'Rent Agreement (For a term of years)'), ('sale_agreement', 'Agreement For Sale'), ('anticipatory_bail_petition_format', 'Anticipatory Bail Petition Format'), ('deed_of_adoption', 'Deed Of Adoption'), ('leave_and_license_agreement', 'Leave and License Agreement'), ('partnership_deed', 'Partnership Deed'), ('deed_of_gift_of_immovable_property', 'Deed of Gift of Immovable Property'), ('memorandum_recording_family_settlement', 'Memorandum Recording Family Settlement'), ('partition_deed', 'Partition Deed')], max_length=255),
        ),
    ]
