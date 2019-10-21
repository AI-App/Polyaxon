class NotebookSerializerMixin(object):

    def get_notebook(self, obj):
        return obj.notebook.id if obj.notebook else None
