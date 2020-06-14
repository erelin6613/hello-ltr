from notebook_test_case import NotebooksTestCase
import unittest

class RunSolrNotebooksTestCase(NotebooksTestCase):

    SOLR_PATHS = ['./notebooks/solr/tmdb']

    IGNORED_NBS = ['./notebooks/solr/tmdb/evaluation (Solr).ipynb',
                   './notebooks/elasticsearch/tmdb/evaluation.ipynb']


    def test_paths(self):
        return RunSolrNotebooksTestCase.SOLR_PATHS

    def ignored_nbs(self):
        return RunSolrNotebooksTestCase.IGNORED_NBS



if __name__ == "__main__":
    unittest.main()
