# Automated Gender Analysis of Guest Stars on The Simpsons

# Introduction:

This is a gender analysis of guest stars who appeared on "The Simpsons" for the show's first 26 seasons. The data came from a list generated from Wikipedia. 

After a bit of cleaning, I narrowed the data into four columns: **Season, First, Last, Episode**. 'First' refers to first_name, and 'Last' directs to last_name. 

For the sake of my sanity, I elminated the episode numbers and production codes from the original dataset contained in Wikipedia. I named my new dataset, which had been cleaned in Microsoft Excel, to guests-simpsons.csv. 

The idea for this gender analysis came from the **#Oscarssowhite** controversy. For decades, Hollywood has been an industry dominated by white men and women. I wanted to see if the racial and gender disparity applied to The Simpsons, long considered the definitive American TV show of the past 25 years. 

Because I couldn't determine one's race by their name, I wanted to see if The Simpsons had a gender disparity when it came to its guest stars. My hypothesis was that 90% of the guest stars were men. Here's what I found.


# Methodology and Caveats:

I cannot complain much about this dataset. Based on other projects I have seen, this was easy. 

The dataset *originally* came from this URL: https://en.wikipedia.org/wiki/List_of_The_Simpsons_guest_stars
I then cleaned the dataset, converted it to a .csv: http://web.stanford.edu/~snewell/guests-simpsons.csv
I did my work from the .csv file, which didn't need to be wrangled.

I used each guest star's first name to determine their gender. As pointed out by Dan Nguyen, the gender detector, built from Social Security data, is incredibly ethno-centric. It is by no means an authoritative way to determine one's gender. But it gives us a ballpark of the gender breakdown on "The Simpsons."

Some of the caveats include:
The gender detector failed when it said Kelsey Grammer was a woman. The actor, who voiced "Sideshow Bob", was listed as female more than 20 times. This threw off the overall count to a large degree. If you took 20 names away from the 'F' column and put them in the 'M' one, you would have a 40-point swing.

Also, the gender detector failed to read names of bands like Metallica. I don't blame the gender detector for giving an 'NA' in those cases. **Asking the gender detector to determine the gender of bands like R.E.M. was a recipe for disaster.**
In a perfect world, the person creating the dataset would list R.E.M., one of my *favorite* bands of all-time, as: 
	**Michael Stipe, Mike Mills, Peter Buck and Bill Berry**