from django.test import TestCase

# Create your tests here.
# email_handler/tests.py

from django.test import TestCase
from django.core import mail
from django.urls import reverse

class EmailHandlerTests(TestCase):

    def test_send_test_email(self):
        """Test that the test email is sent and contains the correct content."""
        
        # Trigger the email sending by calling the URL
        response = self.client.get(reverse('send_email'))
        
        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)
        
        # Check that one message has been sent
        self.assertEqual(len(mail.outbox), 1)
        
        # Verify the subject
        self.assertEqual(mail.outbox[0].subject, "Hello from Django Email Handler")
        
        # Verify the sender
        self.assertEqual(mail.outbox[0].from_email, 'mongodeebee@myyahoo.com')
        
        # Verify the recipient
        self.assertEqual(mail.outbox[0].to, ['annapoorna.narayan@gmail.com'])
        
        # Verify the message body
        self.assertEqual(mail.outbox[0].body, "This is a test email sent from our Django email handler.")
        
    def test_multiple_emails(self):
        """Test that multiple emails can be sent."""
        
        # Send the email multiple times
        for _ in range(3):
            self.client.get(reverse('send_email'))
        
        # Check that three messages have been sent
        self.assertEqual(len(mail.outbox), 3)
