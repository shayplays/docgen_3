from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import WillForm, LicenseForm, LoanAgreementForm, DeedOfHypothecationForm, BailBondForm, ContractBondForm, SimpleMoneyBondForm, EmployeeBondForm, MortgageDeedForm, RentAgreementForm, SaleAgreementForm, BailPetitionForm, DeedOfAdoptionForm, LeaveAndLicenseAgreementForm, PartnershipAgreementForm, DeedOfGiftOfImmoveablePropertyForm, MemorandumRecordingFamilySettlementForm, PartitionDeedForm,SeparationAgreementForm
import docx
from django.shortcuts import render



TEMPLATES = {
    'will': 'Simple-will-LawRato3.docx',
    'license': 'Licence-to-use-Copyright-LawRato2.docx',
    'loan agreement': 'Loan-Agreement-LawRato3.docx',
    'deed of hypothecation': 'Deed-of-Hypothecation-HP-LawRato4.docx',
    'bail bond': 'Bond-and-Bail-bond-under-CrPC-1973-after-Arrest-under-a-Warrant-LawRato.docx',
    'contract bond': 'Bond-to-Secure-the-Performance-of-a-Contract-LawRato2.docx',
    'simple money bond': 'Simple-Money-Bond-LawRato2.docx',
    'employee bond for non compete': 'Employee-Bond-for-Non-Compete-LawRato3.docx',
    'simple mortgage deed': 'Simple-Mortgage-Deed-LawRato2.docx',
    'rent agreement': 'Lease-Deed-(for-a-term-of-years)-Rent-Agreement-LawRato3.docx',
    'sale agreement': 'Agreement-for-Sale-LawRato4.docx',
    'bail petition' : 'Anticipatory-Bail-Petition-Format-LawRato.docx',
    'deed of adoption': 'Deed-of-Adoption-LawRato2.docx',
    'leave and license agreement': 'Leave-and-License-Agreement-LawRato2.docx',
    'partnership deed' : 'Partnership-Deed-LawRato3.docx',
    'deed of gift of immovable property': 'Deed-of-Gift-of-Moveable-Property-Immovable-LawRato4.docx',
    'memorandum recording family settlement': 'Memorandum-Recording-Family-Settlement-LawRato2.docx',
    'partition deed' : 'Partition-Deed-LawRato4.docx',
    'separation agreement': 'Separation-Agreement-between-Husband-and-Wife-LawRato2.docx',
    
}

FORMS = {
    'will': WillForm,
    'license': LicenseForm,
    'loan agreement': LoanAgreementForm,
    'deed of hypothecation' : DeedOfHypothecationForm,
    'bail bond': BailBondForm,
    'contract bond': ContractBondForm,
    'simple money bond': SimpleMoneyBondForm,
    'employee bond for non compete': EmployeeBondForm,
    'simple mortgage deed' : MortgageDeedForm,
    'rent agreement' : RentAgreementForm,
    'sale agreement' : SaleAgreementForm,
    'bail petition' : BailPetitionForm,
    'deed of adoption' : DeedOfAdoptionForm,
    'leave and license agreement': LeaveAndLicenseAgreementForm,
    'partnership deed' : PartnershipAgreementForm,
    'deed of gift of immovable property': DeedOfGiftOfImmoveablePropertyForm,
    'memorandum recording family settlement' : MemorandumRecordingFamilySettlementForm,
    'partition deed' : PartitionDeedForm,
    'separation agreement': SeparationAgreementForm,

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


# Define document categories and their corresponding documents
CATEGORY_DOCUMENTS = {
    'will': {
        'Simple Will': '/will/',
    },
    'banking': {
        'Loan Agreement': '/loan agreement/',
        'Deed Of Hypothecation' : '/deed of hypothecation/',

    },
    'bonds': {
        'Bail Bond': '/bail bond/',
        'Bond to Secure Performance of a Contract': '/contract bond/',
        'Employee Bond for Non-Compete': '/employee bond for non compete/',
        'Simple Money Bond': '/simple money bond/',
    },
    'contracts': {
        'Rent Agreement (for a term of years)': '/rent agreement/',
        'Simple Mortgage Deed': '/simple mortgage deed/',
        'Leave and License Agreement': '/leave and license agreement/',

    },
    'corporate': {
        'Agreement for Sale': '/sale agreement/',
        'Partnership Deed': '/partnership deed/',

    },
    'criminal': {
        'Anticipatory Bail Petition Form' : '/bail petition/',

    },
    'divorceandfamilylaw' : {
        'Deed Of Adoption' : '/deed of adoption/',
        'Deed Of Gift Of Immovable Property' : '/deed of gift of immovable property/',
        'Memorandum Recording Family Settlement' : '/memorandum recording family settlement/',
        'Partition Deed': '/partition deed/',
        'Separation Agreement': '/separation agreement/',


    },
    'trademarkandcopyright' : {
        'License to use Copyright' : '/license/',

    },

}

def category_documents(request, category_name):
    """View to display documents for a selected category."""
    documents = CATEGORY_DOCUMENTS.get(category_name, {})
    
    if not documents:
        return render(request, '404.html', {"message": "Category not found"})
    
    return render(request, 'category_documents.html', {
        'category': category_name.replace('_', ' ').title(),
        'documents': documents
    })
