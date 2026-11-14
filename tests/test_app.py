import math
import os
import unittest
import numpy as np
from app import app, resource_path, ALLOWED_MATH


class GitPatchWaveTestCase(unittest.TestCase):
    """Test suite for GitPatch Wave Flask application endpoints and calculations."""

    def setUp(self):
        """Set up Flask test client and application test context."""
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_resource_path_dev_mode(self):
        """Verify resource_path resolves existing project directories."""
        templates_path = resource_path('templates')
        static_path = resource_path('static')
        self.assertTrue(os.path.isdir(templates_path))
        self.assertTrue(os.path.isdir(static_path))

    def test_intro_route(self):
        """Verify the introduction splash page loads successfully."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        content = response.data.decode('utf-8')
        self.assertIn('GIT:PATCH WAVE', content)
        self.assertIn('/plotter', content)

    def test_plotter_route(self):
        """Verify the main wave plotter page loads successfully."""
        response = self.client.get('/plotter')
        self.assertEqual(response.status_code, 200)
        content = response.data.decode('utf-8')
        self.assertIn('plotCanvas', content)
        self.assertIn('MERGE WAVES (SUM)', content)

    def test_calculate_wave_basic(self):
        """Verify calculation of a simple sinusoidal wave."""
        response = self.client.get('/calculate_wave', query_string={
            't': 0,
            'eq0': 'sin(x)',
            'minX': -10,
            'maxX': 10
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()

        self.assertIn('x', data)
        self.assertIn('lines', data)
        self.assertIn('superposition', data)
        self.assertEqual(len(data['x']), 1000)
        self.assertEqual(len(data['lines']), 1)
        self.assertEqual(len(data['lines'][0]), 1000)
        self.assertEqual(len(data['superposition']), 1000)

        # Check values match mathematical sine function
        expected_sin = np.sin(np.array(data['x'])).tolist()
        np.testing.assert_allclose(data['lines'][0], expected_sin, rtol=1e-5, atol=1e-5)
        np.testing.assert_allclose(data['superposition'], expected_sin, rtol=1e-5, atol=1e-5)

    def test_calculate_wave_multiple_and_superposition(self):
        """Verify superposition correctly computes the sum of multiple wave lines."""
        response = self.client.get('/calculate_wave', query_string={
            't': 0,
            'eq0': 'sin(x)',
            'eq1': 'cos(x)',
            'minX': -5,
            'maxX': 5
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()

        self.assertEqual(len(data['lines']), 2)
        line0 = np.array(data['lines'][0])
        line1 = np.array(data['lines'][1])
        superposition = np.array(data['superposition'])

        expected_sum = line0 + line1
        np.testing.assert_allclose(superposition, expected_sum, rtol=1e-5, atol=1e-5)

    def test_calculate_wave_with_custom_variables(self):
        """Verify equation evaluation using custom dynamic variables."""
        response = self.client.get('/calculate_wave', query_string={
            't': 1.0,
            'eq0': 'A*sin(k*x-w*t)',
            'A': 2.0,
            'k': 0.5,
            'w': 1.5,
            'minX': -5,
            'maxX': 5
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()

        x = np.array(data['x'])
        expected = 2.0 * np.sin(0.5 * x - 1.5 * 1.0)
        np.testing.assert_allclose(data['lines'][0], expected.tolist(), rtol=1e-5, atol=1e-5)

    def test_calculate_wave_power_syntax_conversion(self):
        """Verify caret operator (^) is converted to exponentiation (**)."""
        response = self.client.get('/calculate_wave', query_string={
            't': 0,
            'eq0': 'x^2',
            'minX': -3,
            'maxX': 3
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()

        x = np.array(data['x'])
        expected = x ** 2
        np.testing.assert_allclose(data['lines'][0], expected.tolist(), rtol=1e-5, atol=1e-5)

    def test_calculate_wave_constant_output(self):
        """Verify constant numerical equations return uniform arrays."""
        response = self.client.get('/calculate_wave', query_string={
            't': 0,
            'eq0': '4.5',
            'minX': -2,
            'maxX': 2
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()

        self.assertTrue(all(val == 4.5 for val in data['lines'][0]))
        self.assertTrue(all(val == 4.5 for val in data['superposition']))

    def test_calculate_wave_mathematical_functions(self):
        """Verify allowed mathematical functions and constants are available."""
        eq = "sqrt(abs(cos(x))) + exp(0) + log(e) + pi * 0"
        response = self.client.get('/calculate_wave', query_string={
            't': 0,
            'eq0': eq,
            'minX': -1,
            'maxX': 1
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()

        self.assertNotIn('error', data)
        self.assertEqual(len(data['lines'][0]), 1000)

    def test_calculate_wave_syntax_error_handling(self):
        """Verify invalid syntax returns an error payload without crashing."""
        response = self.client.get('/calculate_wave', query_string={
            't': 0,
            'eq0': 'sin(x++',
            'minX': -5,
            'maxX': 5
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('error', data)

    def test_calculate_wave_undefined_variable_handling(self):
        """Verify reference to an undefined variable returns an error payload."""
        response = self.client.get('/calculate_wave', query_string={
            't': 0,
            'eq0': 'undefined_var*sin(x)',
            'minX': -5,
            'maxX': 5
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('error', data)

    def test_static_files_accessible(self):
        """Verify static JavaScript resources are properly served."""
        response = self.client.get('/static/script.js')
        self.assertEqual(response.status_code, 200)
        self.assertIn('plotCanvas', response.data.decode('utf-8'))
        response.close()


if __name__ == '__main__':
    unittest.main()
