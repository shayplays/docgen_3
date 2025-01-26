from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .forms import WillDocumentForm
import docx

TEMPLATE_PATH = 'Simple-will-LawRato3.docx'

def generate_document(request):
    if request.method == 'POST':
        form = WillDocumentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            doc = docx.Document(TEMPLATE_PATH)
            for para in doc.paragraphs:
                for key, value in data.items():
                    para.text = para.text.replace(f'{{{{{key}}}}}', str(value))
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename=generated_will.docx'
            doc.save(response)
            return response
    else:
        form = WillDocumentForm()
    return render(request, 'generate_document.html', {'form': form})
