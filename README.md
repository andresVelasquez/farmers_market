# farmers_market
an app to help you find farmer's markets in your area

This was my group project at Coding Dojo while working on the Python stack. It uses Django on the back-end. The front-end technologies include JQuery, JQuery UI and Bootstrap. One of the requirements for this hackathon was that we use a US Government API to obtain data. We found one that provided the 19 nearest farmer's markets to a given zip code. Eventually, we integrated Google Maps APIs to calculate zip code as an option. There was a separate file available with more detailed information on each farmer's market though we could not find an API link. What we did then was download the file which was in CSV format, covert it to JSON and served it up internally to reference it that way.

I recently started working on a "wall" page for each market for users to leave comments. However, I'm also working on converting this to a MEAN stack project as well so I may just go forward with the wall on that one.
