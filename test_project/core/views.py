from django.views.generic import DetailView

from .models import TestModel


class PDFRenderMixin(object):
    pass


class Index(PDFRenderMixin, DetailView):
    model = TestModel
    template_name = 'core/content.html'
    pdf_template_name = 'core/content.html'

    def get_pdf_footer_content(self):
        return self.object.footer

    def get_pdf_content(self):
        return self.object.content

    def get_pdf_header_content(self):
        return self.object.header
