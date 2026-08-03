def leap_year(year):
    #The program determines if a year is a leap year
    return((year%4==0 and year%100!=0) or (year%100==0 and year%400==0))
  