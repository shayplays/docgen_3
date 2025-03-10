# Generated by Django 5.1.5 on 2025-03-09 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_legaldocument_area_for_use_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='legaldocument',
            name='business_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='business_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='capital_investment_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='partner_1_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='partner_1_age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='partner_1_father_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='partner_1_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='partner_1_share_of_profit',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='partner_2_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='partner_2_age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='partner_2_father_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='partner_2_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='partner_2_share_of_profit',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='partner_3_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='partner_3_age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='partner_3_father_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='partner_3_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='partner_3_share_of_profit',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='partner_4_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='partner_4_age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='partner_4_father_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='partner_4_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='partner_4_share_of_profit',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='previous_partnership_deed_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='purpose_of_business',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='remuneration_percentage_1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='remuneration_percentage_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='remuneration_percentage_3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='sleeping_partner_names',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='working_partner_1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='working_partner_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='working_partner_3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='legaldocument',
            name='document_type',
            field=models.CharField(choices=[('will', 'Simple Will'), ('license', 'License Agreement'), ('loan_agreement', 'Loan Agreement'), ('deed_of_hypothecation', 'Deed Of Hypothecation'), ('contract_bond', 'Contract Bond'), ('simple_money_bond', 'Simple Money Bond'), ('employee_bond_for_non_compete', 'Employee Bond for Non-Compete'), ('simple_mortgage_deed', 'Simple Mortgage Deed'), ('rent_agreement', 'Rent Agreement (For a term of years)'), ('sale_agreement', 'Agreement For Sale'), ('anticipatory_bail_petition_format', 'Anticipatory Bail Petition Format'), ('deed_of_adoption', 'Deed Of Adoption'), ('leave_and_license_agreement', 'Leave and License Agreement'), ('partnership_deed', 'Partnership Deed')], max_length=255),
        ),
    ]
