from notebook_test_case import NotebooksTestCase
import unittest

class RunGeneralNotebooksTestCase(NotebooksTestCase):

    GENERAL_PATHS = ['./notebooks/']

    IGNORED_NBS = ['./notebooks/solr/tmdb/evaluation (Solr).ipynb',
                   './notebooks/elasticsearch/tmdb/evaluation.ipynb']


    def test_paths(self):
        return RunGeneralNotebooksTestCase.GENERAL_PATHS

    def ignored_nbs(self):
        return RunGeneralNotebooksTestCase.IGNORED_NBS



if __name__ == "__main__":
    unittest.main()
