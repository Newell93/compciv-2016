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
	**Michael Stipe, Mike Mills, Peter Buck and Bill Berry.**


#Past Research and Articles

My goal is not to label "The Simpsons" as a show that favors male guest stars over females. Rather, I wanted to use it as an example. Does one of America's most-popular TV shows have a jaw-dropping gender gap when it comes to guest stars? I wanted to see if the show was unusually progressive, or if it mirrored Hollywood.

Two articles were particularly helpful.

**The first came from NPR**, and it provided a short summary of an essay Jennifer Lawrence wrote on the gender pay gap in Hollywood. This is crucial for setting the tone. Hollywood is seen by many as unequal when it comes to paying everyone, regardless of gender, equal sums of money for an equal role.

*http://www.npr.org/sections/thetwo-way/2015/10/15/448954732/jennifer-lawrence-hits-a-nerve-with-essay-on-hollywoods-gender-pay-gap*

**The second came from a KPCC interview with Geena Davis.** Davis shared some troubling insight:

"Fewer than 31 percent of all speaking parts go to women."

"American movies feature fewer female characters than movies in South Korea, Russia and China."

*http://www.scpr.org/programs/the-frame/2014/09/23/39476/geena-davis-institute-study-shows-gender-gap-in-fi/*

This applies more to "The Simpsons" than the Jennifer Lawrence article. Hollywood is male-dominated. **How do we change that?**


# How To Use It:

So here we are. Time to test out the project.

**fetch_gender_data.py**: This script downloads the raw files from the Social Security Administration that list the number of babies with a particular name. It spans 1880 to 2014. It dumps this information into *tempdata*, which contains 125 .txt files containing info on baby names for every year from 1880 to 2014.

**wrangle_gender_data.py**: This script selects baby-name records every decade between 1950 and 2014. It then compiles them into a list, which is sorted by descending number of babies given a certain name. For example, more babies were named Michael than any other name.

**fetch_data.py**: This script downloads my .csv file containing information on every guest star on "The Simpsons" in the show's first 26 seasons. It dumps it into your *tempdata* folder, naming itself: **simpsons-guests.csv.** 

**wrangle_data.py**: This script does the same thing as **fetch_data.py.** Just a copy.

**classify.py**: This is arguably the most important script in this project. This extracts the first names of all guest starts from "The Simpsons." Then, comparing it with the data from **wrangle_data.py**, it determines the likelihood that the guest star is male or female. It then appends the gender and first name of the guest star to the existing .csv. 

Also, it provides the gender ratio for each name. The higher the number, the greater the chance that the name is male or female. A name with a ratio of '100' indicates that there's a very good chance the gender detector determined the guest star's gender. A name with a ratio of '51' indicates there's a very good chance the gender dector is confused because so many men and women share the name.

**analyze.py**: This script takes the information from **classify.py** and analyzes it. 

# Analysis:

For example, the analysis finds: Of all the guest stars on "The Simpsons," **the gender detector believes 205 are women, 670 are men and 61 cannot be determined.** The gender disparity exists when counted by season. The second analysis determines the gender of guest starts on each season of the show. **Finally,** it seems like the gender gap may be lessening. I compared the ratio of men to women for each season, not counting the NAs. It seems to be decreasing, meaning more women are appearing than they did before. Still, men outnumber women by a ratio of about 3:1.