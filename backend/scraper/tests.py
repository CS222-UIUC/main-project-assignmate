from django.test import TestCase
from django.urls import reverse
from django.http import JsonResponse
from unittest.mock import patch
from scraper.utils import scrape_prairie_learn_data

class ScraperTests(TestCase):
    
    @patch('scraper.utils.scrape_prairie_learn_data')
    def test_scraper_successful(self, mock_scrape):
        """
        successfully returns data.
        """
        mock_scrape.return_value = {
            'Course 1': [('ASSIGN1', 'https://link1', 'Assignment 1', 'Due Date 1')],
            'Course 2': [('ASSIGN2', 'https://link2', 'Assignment 2', 'Due Date 2')]
        }
        
        response = self.client.get(reverse('scrape_data'))
        
        self.assertEqual(response.status_code, 200)
        
        expected_data = {
            'Course 1': [('ASSIGN1', 'https://link1', 'Assignment 1', 'Due Date 1')],
            'Course 2': [('ASSIGN2', 'https://link2', 'Assignment 2', 'Due Date 2')]
        }
        self.assertJSONEqual(str(response.content, encoding='utf8'), expected_data)
    
    @patch('scraper.utils.scrape_prairie_learn_data')
    def test_scraper_empty(self, mock_scrape):
        """
        returns no data (empty).
        """
        mock_scrape.return_value = {}
        
        response = self.client.get(reverse('scrape_data'))
        
        self.assertEqual(response.status_code, 200)
        
        self.assertJSONEqual(str(response.content, encoding='utf8'), {})
    
    @patch('scraper.utils.scrape_prairie_learn_data')
    def test_scraper_error(self, mock_scrape):
        """
        error occurs during scraping.
        """
        mock_scrape.side_effect = Exception('Scraper error')
        
        response = self.client.get(reverse('scrape_data'))
        
        self.assertEqual(response.status_code, 500)
        
        self.assertContains(response, 'Error', status_code=500)
