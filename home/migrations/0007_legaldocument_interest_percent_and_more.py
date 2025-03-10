# Generated by Django 5.1.5 on 2025-03-02 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_legaldocument_bond_amount_legaldocument_obligee_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='legaldocument',
            name='interest_percent',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='lender_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='lender_father_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='object_of_purchase',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='repayment_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='sum_in_words',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='legaldocument',
            name='document_type',
            field=models.CharField(choices=[('will', 'Simple Will'), ('license', 'License Agreement'), ('loan_agreement', 'Loan Agreement'), ('deed_of_hypothecation', 'Deed Of Hypothecation'), ('contract_bond', 'Contract Bond'), ('simple_money_bond', 'Simple Money Bond')], max_length=255),
        ),
    ]
