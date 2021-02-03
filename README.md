# Lomb-Scargle periodogram 

Python implementation of the Lomb Scargle periodogram in Python from scratch with the goal of discovering exoplanets' periodic signals from aperiodic data. Test data for three exoplanets is given. 

When comparing the Lomb-Scargle periodogram presented here in the attached Python file and with the built-in LS periodogram, there are differences. For starters, the built-in periodogram doesn’t take into account the measurement errors for each data point and calculates a general variance, assuming the is was homoscedastic. Furthermore, when comparing the results of my (non-homoschedastic) LS periodogram and the built-in, it is noticeable noticed that most of the times, the built-in periodogram delivers better and more consistent results, showing a less strong dependence on the used frequency ranges.


