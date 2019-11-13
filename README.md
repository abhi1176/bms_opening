# bms_opening
Get e-mail when BookMyShow ticket counter opens sale at your favorite venue/theater

BookMyShow is a popular web platform to book movie tickets online.
Often, I myself visit the page to check whether or not movie tickets of my favorite show at my favorite theater are open for sale.
This python code intends to perform that task automatically and notify me through email if the sale is on.

The scrape.py takes three command line arguments
  1. Theater name (-v)
  2. BMS weblink to the movie booking page (-l)
  3. Email address to where we want the email to be sent (-t) [optional] (If not provided, email is sent to the sender email)


> Before running the script make sure you exported your `gmail address` and password saved to your ~/.bash_profile and/or ~/.bashrc file as EMAIL_USER and EMAIL_PASSWORD respectively

> Considering turning "Allow less secure apps" 'ON' @ https://myaccount.google.com/lesssecureapps

python scrape.py -v "AMB Cinemas" -l "https://in.bookmyshow.com/buytickets/doctor-sleep-hyderabad/movie-hyd-ET00104940-MT/20191114" -t test.user@gmail.com
