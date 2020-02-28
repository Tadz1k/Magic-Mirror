# Magic-Mirror

This is the first version of the 'Magic Mirror' project. I wrote it for educational purposes. Backend is not safe to use, it is not optimal, but in my opinion it is a good start.

Functions: 
- downloading titles of the three latest emails on GMAIL
- graphically presented calendar displaying holidays and marking holidays from work in Poland. Informs you about unusual holidays - for example a day without swearing.
- display of the current weather with a simplified icon
- downloading news from websites based on HTML tags
- downloading and dynamic update of notes (using index.php - change ip:8080 with your local ip address. DDL in mirror_notes.sql)



Things to do before start:
- redesign tkcalendar package - manually delete frames and dropdown menus.
- mail.py - generate auth jsons to get e-mails : https://developers.google.com/gmail/api/quickstart/python. Or disable it in controller.py
- sql_connection.py - a mysql connection is needed to download notes. Fill host, user, passwd and database in this class and in index.php.
- weather.py - replace "KEY API @@@@@" with the generated key on OpenWeatherMap : https://openweathermap.org/current 
