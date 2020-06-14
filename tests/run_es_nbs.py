from notebook_test_case import NotebooksTestCase
import unittest

class RunEsNotebooksTestCase(NotebooksTestCase):

    ES_PATHS = ['./notebooks/elasticsearch/tmdb',
                './notebooks/elasticsearch/osc-blog']

    IGNORED_NBS = ['./notebooks/solr/tmdb/evaluation (Solr).ipynb',
                   './notebooks/elasticsearch/tmdb/evaluation.ipynb']


    def test_paths(self):
        return RunEsNotebooksTestCase.ES_PATHS

    def ignored_nbs(self):
        return RunEsNotebooksTestCase.IGNORED_NBS



if __name__ == "__main__":
    unittest.main()
