# Zendesk-Ticket-Viewer

This is a Python script that connects to the Zendesk API and displays tickets from my account to users. This script was written for the Zendesk Coding Challenge.

#Instructions

To use this script, download zendesk.py and ensure you have Python3 installed on your machine. In the command line, navigate to the directory that holds 'zendesk.py' and enter 'Python3 zendesk.py' to run the script. At this point, you will be greeted with instructions.

The second file, 'zendeskTest.py', holds a unit test for 'zendesk.py'. Due to the nature of the script, this test is quite limited, as the key testable feature of 'zendesk.py' is the ability to propery connect with the Zendesk api and retrieve the tickets in my account. In order to test this, place both files in the same directory, navigate to this directory, and enter 'python -m unittest zendeskTest' in the command line. If 'OK' is output, 'zendesk.py' is working properly.
