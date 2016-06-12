import ipywidgets as widgets
from traitlets import Unicode, List


class msaWidget(widgets.DOMWidget):
    _view_name = Unicode('msaWidgetView').tag(sync=True)
    _view_module = Unicode('nbextensions/msaWidget').tag(sync=True)
    seqs = []
    js_seqs = []
    url = Unicode(sync=True)

    def plot(self):
        self.js_seqs = seqs

    def importURL(self, url):
        self.url = url
