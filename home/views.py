from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import WillForm, LicenseForm, LoanAgreementForm, DeedOfHypothecationForm
import docx

TEMPLATES = {
    'will': 'Simple-will-LawRato3.docx',
    'license': 'Licence-to-use-Copyright-LawRato2.docx',
    'loan_agreement': 'Loan-Agreement-LawRato3.docx',
    'deed_of_hypothecation': 'Deed-of-Hypothecation-HP-LawRato4.docx'
}

FORMS = {
    'will': WillForm,
    'license': LicenseForm,
    'loan_agreement': LoanAgreementForm,
    'deed_of_hypothecation' : DeedOfHypothecationForm
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
