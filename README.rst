Ushahidi
========

Ushahidi is an application that enables RapidSMS to push messages it receives to Ushahidi using the same interface that is used with FrontlineSMS.

Installation
============

	git clone https://github.com/timbaobjects/rapidsms-ushahidi-app.git ushahidi

Then add ``ushahidi`` to your INSTALLED_APPS setting in your settings.py

Configuration
=============

Here's an example configuration that's included in a typical settings.py of a RapidSMS deployment.

    USHAHIDI_KEYWORD = 'report'
    USHAHIDI_RESPONSE = 'Thank you for your report'

The first setting sets the keyword to look out for to activate the application. In this example, the 
keyword ``report`` is used. Any messages beginning with that keyword is handled by the Ushahidi application.

The second setting configures the response that would be sent for messages processed by the Ushahidi application.
