"""
Comprehensive tests for string-rota app including models, forms, views, and utilities.
"""
from django.test import TestCase, Client
from django.contrib.auth.models import User, Group
from django.urls import reverse
from django.core.exceptions import ValidationError
from datetime import date, time

from .models import (
    Repertoire,
    Section,
    Player,
    Session,
    Project,
    SeatingPosition,
    SeatingPlan,
    PlayerProject,
)
from .forms import (
    SeatingPositionForm,
    EditSeatingPositionForm,
    PlayerProjectForm,
    ReserveForm,
)
from .utilities import (
    get_project,
    get_players,
    get_player,
    get_section,
    get_seating_plan,
    get_not_available_players,
    get_seating_positions,
    get_not_playing_in_playerproject,
    get_playing_in_playerproject,
    get_all_playerproject,
)


class RepertoireModelTest(TestCase):
    """Unit tests for Repertoire model"""

    def setUp(self):
        """Create test repertoire"""
        self.repertoire = Repertoire.objects.create(
            name="Symphony No. 1",
            instrumentation="STR 4442"
        )

    def test_repertoire_str_representation(self):
        """Test string representation of Repertoire"""
        expected = "Symphony No. 1 - STR 4442"
        self.assertEqual(str(self.repertoire), expected)

    def test_repertoire_creation(self):
        """Test repertoire is created correctly"""
        self.assertTrue(isinstance(self.repertoire, Repertoire))
        self.assertEqual(self.repertoire.name, "Symphony No. 1")
        self.assertEqual(self.repertoire.instrumentation, "STR 4442")

    def test_repertoire_verbose_name_plural(self):
        """Test verbose_name_plural is set correctly"""
        self.assertEqual(Repertoire._meta.verbose_name_plural, "repertoire")


class SectionModelTest(TestCase):
    """Unit tests for Section model"""

    def setUp(self):
        """Create test section"""
        self.section = Section.objects.create(
            name="Violin 1",
            default_strength=8
        )

    def test_section_str_representation(self):
        """Test string representation of Section"""
        self.assertEqual(str(self.section), "Violin 1")

    def test_section_creation(self):
        """Test section is created correctly"""
        self.assertTrue(isinstance(self.section, Section))
        self.assertEqual(self.section.name, "Violin 1")
        self.assertEqual(self.section.default_strength, 8)

    def test_section_default_strength(self):
        """Test default_strength defaults to 1"""
        section = Section.objects.create(name="Cello")
        self.assertEqual(section.default_strength, 1)

    def test_section_add_player(self):
        """Test adding player to section"""
        user = User.objects.create_user('testuser', 'test@example.com', 'password')
        player = Player.objects.create(
            first_name="John",
            last_name="Doe",
            section=self.section,
            users_django=user
        )
        self.section.players.add(player)
        self.assertIn(player, self.section.players.all())


class PlayerModelTest(TestCase):
    """Unit tests for Player model"""

    def setUp(self):
        """Create test player"""
        self.section = Section.objects.create(name="Violin 1")
        self.user = User.objects.create_user(
            'player1',
            'player1@example.com',
            'password'
        )
        self.player = Player.objects.create(
            first_name="John",
            last_name="Doe",
            section=self.section,
            users_django=self.user
        )

    def test_player_str_representation(self):
        """Test string representation of Player"""
        self.assertEqual(str(self.player), "John Doe")

    def test_player_creation(self):
        """Test player is created correctly"""
        self.assertTrue(isinstance(self.player, Player))
        self.assertEqual(self.player.first_name, "John")
        self.assertEqual(self.player.last_name, "Doe")

    def test_player_default_values(self):
        """Test player default values"""
        self.assertTrue(self.player.is_contract)
        self.assertEqual(self.player.annual_nfd_quota, 0)
        self.assertEqual(self.player.nfds_used_to_date, 0)
        self.assertEqual(self.player.off_reduced_rep_tot, 0)

    def test_player_optional_notes(self):
        """Test player notes field is optional"""
        self.assertIsNone(self.player.notes)
        self.player.notes = "Excellent player"
        self.player.save()
        self.assertEqual(self.player.notes, "Excellent player")

    def test_player_section_relationship(self):
        """Test player belongs to section"""
        self.assertEqual(self.player.section, self.section)

    def test_player_user_relationship(self):
        """Test player linked to Django user"""
        self.assertEqual(self.player.users_django, self.user)


class SessionModelTest(TestCase):
    """Unit tests for Session model"""

    def setUp(self):
        """Create test session"""
        self.project = Project.objects.create(
            name="Test Project",
            slug="test-project"
        )
        self.session = Session.objects.create(
            date=date.today(),
            start_time=time(19, 30),
            end_time=time(21, 30),
            session_type="CON",
            project=self.project
        )

    def test_session_str_representation(self):
        """Test string representation of Session"""
        expected = f"{self.session.start_time} / {self.session.date} / {self.project}"
        self.assertEqual(str(self.session), expected)

    def test_session_creation(self):
        """Test session is created correctly"""
        self.assertTrue(isinstance(self.session, Session))
        self.assertEqual(self.session.session_type, "CON")

    def test_session_type_choices(self):
        """Test session type choices"""
        session_types = ["REH", "CON", "REC"]
        for session_type in session_types:
            session = Session.objects.create(
                date=date.today(),
                start_time=time(19, 30),
                end_time=time(21, 30),
                session_type=session_type,
                project=self.project
            )
            self.assertEqual(session.session_type, session_type)

    def test_session_repertoire_many_to_many(self):
        """Test session can have multiple repertoire"""
        rep1 = Repertoire.objects.create(
            name="Symphony 1",
            instrumentation="STR 4442"
        )
        rep2 = Repertoire.objects.create(
            name="Symphony 2",
            instrumentation="STR 4442"
        )
        self.session.repertoire.add(rep1, rep2)
        self.assertEqual(self.session.repertoire.count(), 2)


class ProjectModelTest(TestCase):
    """Unit tests for Project model"""

    def setUp(self):
        """Create test project"""
        self.project = Project.objects.create(
            name="Test Project",
            slug="test-project"
        )

    def test_project_str_representation(self):
        """Test string representation of Project"""
        self.assertEqual(str(self.project), "Test Project")

    def test_project_creation(self):
        """Test project is created correctly"""
        self.assertTrue(isinstance(self.project, Project))

    def test_project_slug_uniqueness(self):
        """Test project slug is unique"""
        with self.assertRaises(Exception):
            Project.objects.create(
                name="Another Project",
                slug="test-project"
            )

    def test_project_name_uniqueness(self):
        """Test project name is unique"""
        with self.assertRaises(Exception):
            Project.objects.create(
                name="Test Project",
                slug="another-slug"
            )


class SeatingPlanModelTest(TestCase):
    """Unit tests for SeatingPlan model"""

    def setUp(self):
        """Create test seating plan"""
        self.section = Section.objects.create(name="Violin 1", default_strength=8)
        self.project = Project.objects.create(
            name="Test Project",
            slug="test-project"
        )
        self.seating_plan = SeatingPlan.objects.create(
            project=self.project,
            section=self.section,
            plan_status="D"
        )

    def test_seating_plan_creation(self):
        """Test seating plan is created correctly"""
        self.assertTrue(isinstance(self.seating_plan, SeatingPlan))
        self.assertEqual(self.seating_plan.plan_status, "D")

    def test_seating_plan_str_representation(self):
        """Test string representation of SeatingPlan"""
        expected = f"{self.section} {self.project}"
        self.assertEqual(str(self.seating_plan), expected)

    def test_seating_plan_status_choices(self):
        """Test seating plan status choices"""
        self.assertEqual(self.seating_plan.plan_status, "D")
        self.seating_plan.plan_status = "P"
        self.seating_plan.save()
        self.seating_plan.refresh_from_db()
        self.assertEqual(self.seating_plan.plan_status, "P")

    def test_seating_plan_custom_strength(self):
        """Test custom strength overrides default"""
        self.assertIsNone(self.seating_plan.custom_strength)
        self.seating_plan.custom_strength = 10
        self.seating_plan.save()
        self.assertEqual(self.seating_plan.custom_strength, 10)


class SeatingPositionModelTest(TestCase):
    """Unit tests for SeatingPosition model"""

    def setUp(self):
        """Create test seating position"""
        self.section = Section.objects.create(name="Violin 1", default_strength=8)
        self.project = Project.objects.create(
            name="Test Project",
            slug="test-project"
        )
        self.seating_plan = SeatingPlan.objects.create(
            project=self.project,
            section=self.section
        )
        self.user = User.objects.create_user('player1', 'player1@example.com', 'password')
        self.player = Player.objects.create(
            first_name="John",
            last_name="Doe",
            section=self.section,
            users_django=self.user
        )
        self.seating_position = SeatingPosition.objects.create(
            position_number=1,
            seating_plan=self.seating_plan,
            player=self.player
        )

    def test_seating_position_creation(self):
        """Test seating position is created correctly"""
        self.assertTrue(isinstance(self.seating_position, SeatingPosition))
        self.assertEqual(self.seating_position.position_number, 1)

    def test_seating_position_str_representation(self):
        """Test string representation of SeatingPosition"""
        expected = f"{self.seating_plan} {self.player} {self.seating_position.position_number}"
        self.assertEqual(str(self.seating_position), expected)


class PlayerProjectModelTest(TestCase):
    """Unit tests for PlayerProject model"""

    def setUp(self):
        """Create test player project"""
        self.section = Section.objects.create(name="Violin 1")
        self.project = Project.objects.create(
            name="Test Project",
            slug="test-project"
        )
        self.user = User.objects.create_user('player1', 'player1@example.com', 'password')
        self.player = Player.objects.create(
            first_name="John",
            last_name="Doe",
            section=self.section,
            users_django=self.user
        )
        self.player_project = PlayerProject.objects.create(
            project=self.project,
            player=self.player,
            performance_status="PL"
        )

    def test_player_project_creation(self):
        """Test player project is created correctly"""
        self.assertTrue(isinstance(self.player_project, PlayerProject))

    def test_player_project_str_representation(self):
        """Test string representation of PlayerProject"""
        expected = f"{self.player} {self.project}"
        self.assertEqual(str(self.player_project), expected)

    def test_player_project_status_choices(self):
        """Test player project status choices"""
        statuses = ["PL", "RE", "NA"]
        for status in statuses:
            pp = PlayerProject.objects.create(
                project=self.project,
                player=self.player,
                performance_status=status
            )
            self.assertEqual(pp.performance_status, status)

    def test_player_project_default_values(self):
        """Test player project default values"""
        # Create new instance without specifying performance_status to test defaults
        default_pp = PlayerProject.objects.create(
            project=self.project,
            player=self.player
        )
        self.assertFalse(default_pp.off_reduced_rep)
        self.assertFalse(default_pp.trialist)
        self.assertFalse(default_pp.guest_principal)
        self.assertEqual(default_pp.performance_status, "NA")


# ============================================================================
# FORM TESTS
# ============================================================================

class SeatingPositionFormTest(TestCase):
    """Unit tests for SeatingPositionForm"""

    def setUp(self):
        """Create test data for form tests"""
        self.section = Section.objects.create(name="Violin 1", default_strength=3)
        self.project = Project.objects.create(
            name="Test Project",
            slug="test-project"
        )
        self.seating_plan = SeatingPlan.objects.create(
            project=self.project,
            section=self.section
        )
        self.user1 = User.objects.create_user('player1', 'player1@example.com', 'password')
        self.user2 = User.objects.create_user('player2', 'player2@example.com', 'password')
        self.player1 = Player.objects.create(
            first_name="John",
            last_name="Doe",
            section=self.section,
            users_django=self.user1
        )
        self.player2 = Player.objects.create(
            first_name="Jane",
            last_name="Smith",
            section=self.section,
            users_django=self.user2
        )

    def test_form_fields_present(self):
        """Test form has correct fields"""
        form = SeatingPositionForm(self.section, self.seating_plan)
        self.assertIn('player', form.fields)
        self.assertIn('position_number', form.fields)

    def test_form_player_queryset_filtered(self):
        """Test form only shows unallocated players"""
        SeatingPosition.objects.create(
            position_number=1,
            seating_plan=self.seating_plan,
            player=self.player1
        )
        form = SeatingPositionForm(self.section, self.seating_plan)
        queryset = form.fields['player'].queryset
        self.assertNotIn(self.player1, queryset)
        self.assertIn(self.player2, queryset)

    def test_form_valid_position_number(self):
        """Test form accepts valid position number"""
        form_data = {
            'player': self.player1.id,
            'position_number': 1
        }
        form = SeatingPositionForm(self.section, self.seating_plan, data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_position_number_too_high(self):
        """Test form rejects position number above strength"""
        form_data = {
            'player': self.player1.id,
            'position_number': 5
        }
        form = SeatingPositionForm(self.section, self.seating_plan, data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('position_number', form.errors)

    def test_form_invalid_position_number_zero(self):
        """Test form rejects position number below 1"""
        form_data = {
            'player': self.player1.id,
            'position_number': 0
        }
        form = SeatingPositionForm(self.section, self.seating_plan, data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_invalid_duplicate_position(self):
        """Test form rejects duplicate position number"""
        SeatingPosition.objects.create(
            position_number=1,
            seating_plan=self.seating_plan,
            player=self.player1
        )
        form_data = {
            'player': self.player2.id,
            'position_number': 1
        }
        form = SeatingPositionForm(self.section, self.seating_plan, data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_with_custom_strength(self):
        """Test form respects custom seating plan strength"""
        self.seating_plan.custom_strength = 2
        self.seating_plan.save()
        form_data = {
            'player': self.player1.id,
            'position_number': 3
        }
        form = SeatingPositionForm(self.section, self.seating_plan, data=form_data)
        self.assertFalse(form.is_valid())


class EditSeatingPositionFormTest(TestCase):
    """Unit tests for EditSeatingPositionForm"""

    def setUp(self):
        """Create test data for form tests"""
        self.section = Section.objects.create(name="Violin 1", default_strength=3)
        self.project = Project.objects.create(
            name="Test Project",
            slug="test-project"
        )
        self.seating_plan = SeatingPlan.objects.create(
            project=self.project,
            section=self.section
        )
        self.user1 = User.objects.create_user('player1', 'player1@example.com', 'password')
        self.user2 = User.objects.create_user('player2', 'player2@example.com', 'password')
        self.player1 = Player.objects.create(
            first_name="John",
            last_name="Doe",
            section=self.section,
            users_django=self.user1
        )
        self.player2 = Player.objects.create(
            first_name="Jane",
            last_name="Smith",
            section=self.section,
            users_django=self.user2
        )
        self.seating_position = SeatingPosition.objects.create(
            position_number=1,
            seating_plan=self.seating_plan,
            player=self.player1
        )

    def test_form_shows_only_position_number(self):
        """Test edit form only shows position_number field"""
        form = EditSeatingPositionForm(
            self.section,
            self.seating_plan,
            instance=self.seating_position
        )
        self.assertIn('position_number', form.fields)
        self.assertNotIn('player', form.fields)

    def test_form_valid_unchanged_position(self):
        """Test form accepts unchanged position number"""
        form_data = {'position_number': 1}
        form = EditSeatingPositionForm(
            self.section,
            self.seating_plan,
            data=form_data,
            instance=self.seating_position
        )
        self.assertTrue(form.is_valid())

    def test_form_valid_changed_position(self):
        """Test form accepts changed position number"""
        form_data = {'position_number': 2}
        form = EditSeatingPositionForm(
            self.section,
            self.seating_plan,
            data=form_data,
            instance=self.seating_position
        )
        self.assertTrue(form.is_valid())

    def test_form_invalid_duplicate_different_position(self):
        """Test form rejects duplicate position when changing"""
        SeatingPosition.objects.create(
            position_number=2,
            seating_plan=self.seating_plan,
            player=self.player2
        )
        form_data = {'position_number': 2}
        form = EditSeatingPositionForm(
            self.section,
            self.seating_plan,
            data=form_data,
            instance=self.seating_position
        )
        self.assertFalse(form.is_valid())


class PlayerProjectFormTest(TestCase):
    """Unit tests for PlayerProjectForm"""

    def setUp(self):
        """Create test data"""
        self.section = Section.objects.create(name="Violin 1")
        self.project = Project.objects.create(
            name="Test Project",
            slug="test-project"
        )
        self.user = User.objects.create_user('player1', 'player1@example.com', 'password')
        self.player = Player.objects.create(
            first_name="John",
            last_name="Doe",
            section=self.section,
            users_django=self.user
        )
        self.player_project = PlayerProject.objects.create(
            project=self.project,
            player=self.player
        )

    def test_form_fields(self):
        """Test form has off_reduced_rep field"""
        form = PlayerProjectForm()
        self.assertIn('off_reduced_rep', form.fields)

    def test_form_valid_off_reduced_rep_false(self):
        """Test form accepts off_reduced_rep false"""
        form_data = {'off_reduced_rep': False}
        form = PlayerProjectForm(data=form_data, instance=self.player_project)
        self.assertTrue(form.is_valid())

    def test_form_valid_off_reduced_rep_true(self):
        """Test form accepts off_reduced_rep true"""
        form_data = {'off_reduced_rep': True}
        form = PlayerProjectForm(data=form_data, instance=self.player_project)
        self.assertTrue(form.is_valid())


class ReserveFormTest(TestCase):
    """Unit tests for ReserveForm"""

    def setUp(self):
        """Create test data"""
        self.section = Section.objects.create(name="Violin 1")
        self.project = Project.objects.create(
            name="Test Project",
            slug="test-project"
        )
        self.seating_plan = SeatingPlan.objects.create(
            project=self.project,
            section=self.section
        )
        self.user1 = User.objects.create_user('player1', 'player1@example.com', 'password')
        self.user2 = User.objects.create_user('player2', 'player2@example.com', 'password')
        self.player1 = Player.objects.create(
            first_name="John",
            last_name="Doe",
            section=self.section,
            users_django=self.user1
        )
        self.player2 = Player.objects.create(
            first_name="Jane",
            last_name="Smith",
            section=self.section,
            users_django=self.user2
        )

    def test_form_shows_unallocated_players(self):
        """Test form only shows players not allocated to seating plan"""
        SeatingPosition.objects.create(
            position_number=1,
            seating_plan=self.seating_plan,
            player=self.player1
        )
        form = ReserveForm(self.section, self.seating_plan)
        queryset = form.fields['player'].queryset
        self.assertNotIn(self.player1, queryset)
        self.assertIn(self.player2, queryset)

    def test_form_valid_player_selection(self):
        """Test form accepts valid player selection"""
        form_data = {'player': self.player1.id}
        form = ReserveForm(self.section, self.seating_plan, data=form_data)
        self.assertTrue(form.is_valid())


# ============================================================================
# UTILITY TESTS
# ============================================================================

# ============================================================================
# INTEGRATION/VIEW TESTS
# ============================================================================

class HomeViewTest(TestCase):
    """Integration tests for Home view"""

    def setUp(self):
        """Create test data and client"""
        self.client = Client()
        self.user = User.objects.create_user(
            'testuser',
            'test@example.com',
            'password123'
        )
        self.office_group = Group.objects.create(name='Office')
        self.section = Section.objects.create(name="Violin 1")
        self.player = Player.objects.create(
            first_name="John",
            last_name="Doe",
            section=self.section,
            users_django=self.user
        )
        self.project = Project.objects.create(
            name="Test Project",
            slug="test-project"
        )

    def test_home_view_requires_login(self):
        """Test home view redirects to login if not authenticated"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

    def test_home_view_loads_for_logged_in_user(self):
        """Test home view loads for authenticated user"""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'string_rota/home.html')

    def test_home_view_contains_projects(self):
        """Test home view contains projects in context"""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('home'))
        self.assertIn('projects', response.context)
        self.assertIn(self.project, response.context['projects'])

    def test_home_view_office_group_check(self):
        """Test home view checks office group"""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('home'))
        self.assertIn('office', response.context)


class RotaViewTest(TestCase):
    """Integration tests for Rota view"""

    def setUp(self):
        """Create test data"""
        self.client = Client()
        self.user = User.objects.create_user(
            'testuser',
            'test@example.com',
            'password123'
        )
        self.section = Section.objects.create(name="Violin 1", default_strength=2)
        self.player = Player.objects.create(
            first_name="John",
            last_name="Doe",
            section=self.section,
            users_django=self.user
        )
        self.project = Project.objects.create(
            name="Test Project",
            slug="test-project"
        )
        self.seating_plan = SeatingPlan.objects.create(
            project=self.project,
            section=self.section,
            plan_status="P"
        )
        PlayerProject.objects.create(
            project=self.project,
            player=self.player,
            performance_status="PL"
        )

    def test_rota_view_requires_login(self):
        """Test rota view requires authentication"""
        response = self.client.get(
            reverse('rota', args=['test-project'])
        )
        self.assertEqual(response.status_code, 302)

    def test_rota_view_loads_for_player(self):
        """Test rota view loads for player user"""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(
            reverse('rota', args=['test-project'])
        )
        self.assertEqual(response.status_code, 200)

    def test_rota_view_contains_seating_positions(self):
        """Test rota view includes seating positions"""
        self.client.login(username='testuser', password='password123')
        SeatingPosition.objects.create(
            position_number=1,
            seating_plan=self.seating_plan,
            player=self.player
        )
        response = self.client.get(
            reverse('rota', args=['test-project'])
        )
        self.assertIn('seating_positions', response.context)

    def test_rota_view_handles_no_seating_plan(self):
        """Test rota view handles missing seating plan with redirect"""
        new_section = Section.objects.create(name="Cello")
        new_player = Player.objects.create(
            first_name="Jane",
            last_name="Smith",
            section=new_section
        )
        new_user = User.objects.create_user(
            'newuser',
            'new@example.com',
            'password123'
        )
        new_player.users_django = new_user
        new_player.save()

        self.client.login(username='newuser', password='password123')
        response = self.client.get(
            reverse('rota', args=['test-project']),
            follow=False
        )
        # View should redirect to home when no seating plan exists for player's section
        self.assertIn(response.status_code, [302, 404])


class AddSeatingPositionViewTest(TestCase):
    """Integration tests for AddSeatingPosition view"""

    def setUp(self):
        """Create test data"""
        self.client = Client()
        self.user = User.objects.create_user(
            'testuser',
            'test@example.com',
            'password123'
        )
        self.office_group = Group.objects.create(name='Office')
        self.section = Section.objects.create(name="Violin 1", default_strength=2)
        self.player = Player.objects.create(
            first_name="John",
            last_name="Doe",
            section=self.section,
            users_django=self.user
        )
        self.project = Project.objects.create(
            name="Test Project",
            slug="test-project"
        )
        self.seating_plan = SeatingPlan.objects.create(
            project=self.project,
            section=self.section
        )
        PlayerProject.objects.create(
            project=self.project,
            player=self.player,
            performance_status="NA"
        )

    def test_add_seating_position_view_get(self):
        """Test add seating position view loads form"""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(
            reverse('add_sp', args=['test-project', self.seating_plan.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('seating_position_form', response.context)

    def test_add_seating_position_view_post_valid(self):
        """Test add seating position post with valid data"""
        self.client.login(username='testuser', password='password123')
        data = {
            'player': self.player.id,
            'position_number': 1,
            'off_reduced_rep': False
        }
        response = self.client.post(
            reverse('add_sp', args=['test-project', self.seating_plan.id]),
            data=data
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            SeatingPosition.objects.filter(position_number=1).exists()
        )

    def test_add_seating_position_updates_player_project_status(self):
        """Test adding seating position updates PlayerProject status"""
        self.client.login(username='testuser', password='password123')
        data = {
            'player': self.player.id,
            'position_number': 1,
            'off_reduced_rep': False
        }
        self.client.post(
            reverse('add_sp', args=['test-project', self.seating_plan.id]),
            data=data
        )
        player_project = PlayerProject.objects.get(
            player=self.player,
            project=self.project
        )
        self.assertEqual(player_project.performance_status, "PL")


class DeleteSeatingPositionViewTest(TestCase):
    """Integration tests for DeleteSeatingPosition view"""

    def setUp(self):
        """Create test data"""
        self.client = Client()
        self.user = User.objects.create_user(
            'testuser',
            'test@example.com',
            'password123'
        )
        self.section = Section.objects.create(name="Violin 1")
        self.player = Player.objects.create(
            first_name="John",
            last_name="Doe",
            section=self.section,
            users_django=self.user
        )
        self.project = Project.objects.create(
            name="Test Project",
            slug="test-project"
        )
        self.seating_plan = SeatingPlan.objects.create(
            project=self.project,
            section=self.section
        )
        self.seating_position = SeatingPosition.objects.create(
            position_number=1,
            seating_plan=self.seating_plan,
            player=self.player
        )
        self.player_project = PlayerProject.objects.create(
            project=self.project,
            player=self.player,
            performance_status="PL",
            off_reduced_rep=True
        )

    def test_delete_seating_position(self):
        """Test seating position deletion"""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(
            reverse('delete_sp', args=['test-project', self.seating_position.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            SeatingPosition.objects.filter(id=self.seating_position.id).exists()
        )

    def test_delete_seating_position_resets_player_project(self):
        """Test deletion resets player project status and off_reduced_rep"""
        self.client.login(username='testuser', password='password123')
        self.client.get(
            reverse('delete_sp', args=['test-project', self.seating_position.id])
        )
        self.player_project.refresh_from_db()
        self.assertEqual(self.player_project.performance_status, "NA")
        self.assertFalse(self.player_project.off_reduced_rep)


class ToggleSeatingPlanStatusViewTest(TestCase):
    """Integration tests for ToggleSeatingPlanStatus view"""

    def setUp(self):
        """Create test data"""
        self.client = Client()
        self.user = User.objects.create_user(
            'testuser',
            'test@example.com',
            'password123'
        )
        self.section = Section.objects.create(name="Violin 1")
        self.player = Player.objects.create(
            first_name="John",
            last_name="Doe",
            section=self.section,
            users_django=self.user
        )
        self.project = Project.objects.create(
            name="Test Project",
            slug="test-project"
        )
        self.seating_plan = SeatingPlan.objects.create(
            project=self.project,
            section=self.section,
            plan_status="D"
        )

    def test_toggle_status_draft_to_published(self):
        """Test toggling status from draft to published"""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(
            reverse(
                'toggle_seating_plan_status',
                args=['test-project', self.seating_plan.id]
            )
        )
        self.seating_plan.refresh_from_db()
        self.assertEqual(self.seating_plan.plan_status, "P")

    def test_toggle_status_published_to_draft(self):
        """Test toggling status from published to draft"""
        self.seating_plan.plan_status = "P"
        self.seating_plan.save()

        self.client.login(username='testuser', password='password123')
        self.client.get(
            reverse(
                'toggle_seating_plan_status',
                args=['test-project', self.seating_plan.id]
            )
        )
        self.seating_plan.refresh_from_db()
        self.assertEqual(self.seating_plan.plan_status, "D")


class ReserveViewTest(TestCase):
    """Integration tests for Reserve view"""

    def setUp(self):
        """Create test data"""
        self.client = Client()
        self.user1 = User.objects.create_user(
            'player1',
            'player1@example.com',
            'password123'
        )
        self.user2 = User.objects.create_user(
            'player2',
            'player2@example.com',
            'password123'
        )
        self.section = Section.objects.create(name="Violin 1", default_strength=1)
        self.player1 = Player.objects.create(
            first_name="John",
            last_name="Doe",
            section=self.section,
            users_django=self.user1
        )
        self.player2 = Player.objects.create(
            first_name="Jane",
            last_name="Smith",
            section=self.section,
            users_django=self.user2
        )
        self.project = Project.objects.create(
            name="Test Project",
            slug="test-project"
        )
        self.seating_plan = SeatingPlan.objects.create(
            project=self.project,
            section=self.section
        )
        SeatingPosition.objects.create(
            position_number=1,
            seating_plan=self.seating_plan,
            player=self.player1
        )
        self.seating_plan.players.add(self.player1)
        
        self.pp1 = PlayerProject.objects.create(
            project=self.project,
            player=self.player1,
            performance_status="PL"
        )
        self.pp2 = PlayerProject.objects.create(
            project=self.project,
            player=self.player2,
            performance_status="NA"
        )

    def test_reserve_view_get(self):
        """Test reserve view GET request"""
        self.client.login(username='player1', password='password123')
        response = self.client.get(
            reverse('reserve', args=['test-project'])
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('reserve_form', response.context)

    def test_reserve_view_post_set_reserve(self):
        """Test setting a player as reserve"""
        self.client.login(username='player1', password='password123')
        data = {'player': self.player2.id}
        response = self.client.post(
            reverse('reserve', args=['test-project']),
            data=data
        )
        self.pp2.refresh_from_db()
        self.assertEqual(self.pp2.performance_status, "RE")

    def test_reserve_view_post_toggle_reserve_off(self):
        """Test toggling reserve status off"""
        self.pp2.performance_status = "RE"
        self.pp2.save()

        self.client.login(username='player1', password='password123')
        data = {'player': self.player2.id}
        self.client.post(
            reverse('reserve', args=['test-project']),
            data=data
        )
        self.pp2.refresh_from_db()
        self.assertEqual(self.pp2.performance_status, "NA")

    def test_reserve_view_only_one_reserve(self):
        """Test only one player can be reserve"""
        self.user3 = User.objects.create_user(
            'player3',
            'player3@example.com',
            'password123'
        )
        self.player3 = Player.objects.create(
            first_name="Bob",
            last_name="Johnson",
            section=self.section,
            users_django=self.user3
        )
        self.pp3 = PlayerProject.objects.create(
            project=self.project,
            player=self.player3,
            performance_status="NA"
        )

        self.client.login(username='player1', password='password123')
        # Set player2 as reserve
        data = {'player': self.player2.id}
        self.client.post(
            reverse('reserve', args=['test-project']),
            data=data
        )

        # Try to set player3 as reserve
        data = {'player': self.player3.id}
        self.client.post(
            reverse('reserve', args=['test-project']),
            data=data
        )

        self.pp2.refresh_from_db()
        self.pp3.refresh_from_db()
        # player2 should no longer be reserve
        self.assertEqual(self.pp2.performance_status, "NA")
        # player3 should be reserve
        self.assertEqual(self.pp3.performance_status, "RE")
