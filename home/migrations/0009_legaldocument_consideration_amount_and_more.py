# Generated by Django 5.1.5 on 2025-03-03 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_legaldocument_compensation_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='legaldocument',
            name='consideration_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='first_installment_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='mortgage_property_location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='mortgage_property_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='mortgagee_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='mortgagee_father_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='mortgagee_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='mortgagor_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='mortgagor_father_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='mortgagor_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='payment_due_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='place_of_execution',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='property_location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='property_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='subsequent_installment_payment_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='legaldocument',
            name='document_type',
            field=models.CharField(choices=[('will', 'Simple Will'), ('license', 'License Agreement'), ('loan_agreement', 'Loan Agreement'), ('deed_of_hypothecation', 'Deed Of Hypothecation'), ('contract_bond', 'Contract Bond'), ('simple_money_bond', 'Simple Money Bond'), ('employee_bond_for_non_compete', 'Employee Bond for Non-Compete'), ('simple_mortgage_deed', 'Simple Mortgage Deed')], max_length=255),
        ),
        migrations.AlterField(
            model_name='legaldocument',
            name='loan_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='legaldocument',
            name='repayment_amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
