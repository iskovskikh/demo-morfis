from django.utils import timezone
from haystack import indexes
from .morfis_models.case import IcdCode


class IcdCodesIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)

    code = indexes.CharField(model_attr='code')
    disease_description =indexes.CharField(model_attr='disease_description')
    parent_code = indexes.CharField(model_attr='parent_code')

    autocomplete = indexes.EdgeNgramField()

    @staticmethod
    def prepare_autocomplete(obj):
        return " ".join((
            obj.code, obj.disease_description
        ))

    def get_model(self):
        return IcdCode

    # def index_queryset(self, using=None):
    #     return self.get_model().objects.all()
        #.filter(
        #     created__lte=timezone.now()
        # )
