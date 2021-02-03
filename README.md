# Lomb-Scargle periodogram 

Python implementation of the Lomb Scargle periodogram in Python from scratch with the goal of discovering exoplanets' periodic signals from aperiodic data. Test data for three exoplanets is given. 

![equation](https://latex.codecogs.com/png.latex?P%28f%29%20%3D%20%5Cfrac%7B1%7D%7B2%7D%20%5Cleft%5B%20%5Cfrac%7B%20%5Cleft%28%20%5Csum_%7Bj%7D%20%5Cfrac%7Bh_%7Bj%7D%20c_%7Bj%7D%7D%7B%5Csigma%5E%7B2%7D_%7Bj%7D%7D%20%5Cright%29%5E%7B2%7D%7D%7B%20%5Csum_%7Bj%7D%20%5Cfrac%7Bc_%7Bj%7D%5E%7B2%7D%7D%7B%5Csigma_%7Bj%7D%5E%7B2%7D%7D%20%7D%20&plus;%20%5Cfrac%7B%20%5Cleft%28%20%5Csum_%7Bj%7D%20%5Cfrac%7Bh_%7Bj%7D%20s_%7Bj%7D%7D%7B%5Csigma%5E%7B2%7D_%7Bj%7D%7D%20%5Cright%29%5E%7B2%7D%7D%7B%20%5Csum_%7Bj%7D%20%5Cfrac%7Bs_%7Bj%7D%5E%7B2%7D%7D%7B%5Csigma_%7Bj%7D%5E%7B2%7D%7D%20%7D%20%5Cright%5D)

When comparing the Lomb-Scargle periodogram presented here in the attached Python file and with the built-in LS periodogram, there are differences. For starters, the built-in periodogram doesn’t take into account the measurement errors for each data point and calculates a general variance, assuming the is was homoscedastic. Furthermore, when comparing the results of my (non-homoschedastic) LS periodogram and the built-in, it is noticeable noticed that most of the times, the built-in periodogram delivers better and more consistent results, showing a less strong dependence on the used frequency ranges.


