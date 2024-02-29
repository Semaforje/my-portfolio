from django.test import TestCase
from .models import Project


# Create your tests here.
def create_project(title):
    """
    Create a project with the given `title`.
    """
    return Project.objects.create(title=title)


class ProjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Project.objects.create(title='Test Project', short_desc='Short description TP',
                               description='Long description for Test Project')

    def test_title_label(self):
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_short_desc_label(self):
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field('short_desc').verbose_name
        self.assertEqual(field_label, 'short desc')

    def test_description_label(self):
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_title_max_length(self):
        project = Project.objects.get(id=1)
        max_length = project._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_get_absolute_url(self):
        project = Project.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(project.get_absolute_url(), '/portfolio/1/')

