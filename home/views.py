from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import WillForm, LicenseForm, LoanAgreementForm, DeedOfHypothecationForm, BailBondForm, ContractBondForm, SimpleMoneyBondForm, EmployeeBondForm, MortgageDeedForm, RentAgreementForm, SaleAgreementForm
import docx


TEMPLATES = {
    'will': 'Simple-will-LawRato3.docx',
    'license': 'Licence-to-use-Copyright-LawRato2.docx',
    'loan_agreement': 'Loan-Agreement-LawRato3.docx',
    'deed_of_hypothecation': 'Deed-of-Hypothecation-HP-LawRato4.docx',
    'bail_bond': 'Bond-and-Bail-bond-under-CrPC-1973-after-Arrest-under-a-Warrant-LawRato.docx',
    'contract_bond': 'Bond-to-Secure-the-Performance-of-a-Contract-LawRato2.docx',
    'simple_money_bond': 'Simple-Money-Bond-LawRato2.docx',
    'employee_bond_for_non_compete': 'Employee-Bond-for-Non-Compete-LawRato3.docx',
    'simple_mortgage_deed': 'Simple-Mortgage-Deed-LawRato2.docx',
    'rent_agreement': 'Lease-Deed-(for-a-term-of-years)-Rent-Agreement-LawRato3',
    'sale_agreement': 'Agreement-for-Sale-LawRato4',
    

}

FORMS = {
    'will': WillForm,
    'license': LicenseForm,
    'loan_agreement': LoanAgreementForm,
    'deed_of_hypothecation' : DeedOfHypothecationForm,
    'bail_bond': BailBondForm,
    'contract_bond': ContractBondForm,
    'simple_money_bond': SimpleMoneyBondForm,
    'employee_bond_for_non_compete': EmployeeBondForm,
    'simple_mortgage_deed' : MortgageDeedForm,
    'rent_agreement' : RentAgreementForm,
    'sale_agreement' : SaleAgreementForm,
    
}

def select_document(request):
    return render(request, 'select_document.html')

def generate_document(request, doc_type):
    if doc_type not in TEMPLATES:
        return redirect('select_document')
    
    FormClass = FORMS[doc_type]
    
    if request.method == 'POST':
        form = FormClass(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            template_path = TEMPLATES.get(doc_type)
            doc = docx.Document(template_path)
            for para in doc.paragraphs:
                for key, value in data.items():
                    if value:
                        para.text = para.text.replace(f'{{{{{key}}}}}', str(value))
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = f'attachment; filename=generated_{doc_type}.docx'
            doc.save(response)
            return response
    else:
        form = FormClass()
    return render(request, 'generate_document.html', {'form': form, 'doc_type': doc_type})

