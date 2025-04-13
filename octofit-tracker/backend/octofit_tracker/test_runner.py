from django.test.runner import DiscoverRunner

class NoDBTestRunner(DiscoverRunner):
    """
    A test runner to test without setting up a database.
    """
    def setup_databases(self, **kwargs):
        pass

    def teardown_databases(self, old_config, **kwargs):
        pass
