from django.test import TestCase
from atomic.models import customer


# Create your tests here.
class AtomicTest(TestCase):
    def setUp(self):
        self.db = customer.objects.create(name='frank', balance='20.09')

    def test_atomic_model(self):
        atom = self.db
        self.assertTrue(isinstance(atom, customer))
        self.assertEqual(str(atom), 'frank')
