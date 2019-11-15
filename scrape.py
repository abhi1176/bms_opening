
import os
import requests

from argparse import ArgumentParser
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep

from mailsender import SendEmail

SUBJECT = "Movie tickets are open"
BODY = "BMS bookings for theaters: \"{}\" is open for your movie on BookMyShow @ {}."

EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")

def search_venue(link, venues, to_address):
	if not to_address:
		to_address = EMAIL_ADDRESS
	source = requests.get(link).text
	soup = BeautifulSoup(source, 'lxml')
	for m in soup.find_all('meta'):
		try:
			if m['property'] == 'al:android:url':
				if m['content'].rsplit("/", 1)[1] != link.rsplit("/", 1)[1]:
					print("The url is mapped to past date")
					return True
				else:
					break
		except:
			pass

	found_venues = [venue
		for bms_venue in soup.find_all('a', class_="__venue-name")
			for venue in venues
				if venue.strip().lower() in bms_venue.text.strip().lower()]

	print("Venues found: {}".format(found_venues))
	
	if found_venues:
		se = SendEmail(subject=SUBJECT,
					   body=BODY.format(", ".join(found_venues), link),
					   from_address=EMAIL_ADDRESS,
					   password=EMAIL_PASSWORD,
					   to_address=to_address)
		se.send_email()
		print("Email sent successfully to {}".format(to_address))
		return True
	print("Checked at {}".format(datetime.now()))


if __name__ == "__main__":
	parser = ArgumentParser()
	parser.add_argument("-l", "--bms_link", required=True,
						help="Enter the bookmyshow movie booking page link")
	parser.add_argument("-v", "--venues", nargs='+',
						help="Enter the space separated theaters name")
	parser.add_argument("-t", "--to", nargs='*', help="Enter the theater name")
	parser.add_argument("-f", "--frequency", default=900, type=int,
						help="Enter the frequency to query the url in seconds")
	args = parser.parse_args()
	while True:
		if search_venue(args.bms_link, args.venues, args.to):
			break
		sleep(args.frequency)

# python scrape.py -v "AMB Cinemas" "preston prime" "inorbit" -l "https://in.bookmyshow.com/buytickets/khaidi-hyderabad/movie-hyd-ET00114552-MT/20191114"
