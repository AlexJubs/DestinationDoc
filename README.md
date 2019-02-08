# DestinationDoc
Created by Kat, Alex, Parth and Rahul as a Hackathon Project for McHacks 6

Inspiration
We were inspired to reduce the amount of time it takes to seek medical attention. By directing patients immediately to a doctor specific to their needs, one may reduce the wait time commonly associated with seeking medical aid.

What it does
Destination Doc asks a user how they are feeling at which point it determines what type of doctor a patient needs (by screening for flagged words). It then proceeds to search a 10 km radius for establishments that such as dentist offices, walk-in clinics, physiotherapy centers or other need-specific locations. Using Microsoft's Bing's API, Destination Doc determines which destination is the shortest time away using real-time traffic. A map is then displayed directing the user from their home location to the optimal medical center.

How we built it
We built the application front end using angular and the backend with flask, We incorporated the Cisco meraki, twilio APIs and azure.
