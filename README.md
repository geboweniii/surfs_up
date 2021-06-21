# Overview of the analysis
This analysis consisted of Jupyter notebooks used for the analysis of weather data contained in an SQLite database using SQLAlchemy. Using SQLAlchemy, weather data contained in hawaii.sqlite database was reviewed to produced the results contained below. The dataset includes both temperature and precipitation measurements in Hawaii from 2010 to 2017. One of the two tables included measurement data including the station, date, and the recorded precipitation and temperature. Also included was station information with geographic coordinates and elevation. Key differences in Hawaii weather data between the months of December and June were queried and retrieved for this analysis.

# Results
The summary statistics for temperature measurements in Hawaii for the months of June and December are shown below. These results reveal the following:

- Higher average temperature in June than December
- December temperature data has larger range between high and low temps (27 °F differene) than that of June (21 °F differene) with greater fluctation in temps as evidenced in the standard deviation results.
- Interquartile ranges between June and December data are distinct but comparable.

![alt text](https://github.com/geboweniii/surfs_up/blob/main/Images/JuneTemps.PNG)

![alt text](https://github.com/geboweniii/surfs_up/blob/main/Images/DecTemps.PNG)

# Summary

On average, recorded temperature was higher in June than December by 3.9 °F. There is larger variation in December data seen in increased standard deviation indicating December temperatures reaching those of June. Further, both months exhibit comparable maximum temperatures. Despite greater variability in temperatures in the month of December, both months exhibit comfortable conditions amenable to proposed business prospects.

