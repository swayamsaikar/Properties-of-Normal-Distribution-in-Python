from os import stat
import pandas as pd
import statistics as stats

df = pd.read_csv('StudentsPerformance.csv')["reading score"]


mean = stats.mean(df)
median = stats.median(df)
mode = stats.mode(df)
standard_deviation = stats.stdev(df)

# ** print(mean)
# ** print(standard_deviation)

# ** mean is generally at the center of the data and the first standard deviation is at some distance before and after the mean and same for the second and third deviation
# ** and we are finding the starting and the ending point of the standard deviation
# ** starting point(subtracting the standard deviation by mean)
# ** ending point(adding the standard deviation by mean or mean + standard deviation)
# ** print out the mean and standard deviation for better understanding

first_standard_deviation_start, first_standard_deviation_end = mean - \
    standard_deviation, mean+standard_deviation
second_standard_deviation_start, second_standard_deviation_end = mean - \
    (2*standard_deviation), mean+(2*standard_deviation)
third_standard_deviation_start, third_standard_deviation_end = mean - \
    (3*standard_deviation), mean+(3*standard_deviation)

# !! filtering the data
# !! Here we have to find the values that are greater than the standard deviation start and less than standard deviation end (for three three standard deviations)
values_for_first_standard_deviation = [df for eachScore in df if eachScore >
                                       first_standard_deviation_start and eachScore < first_standard_deviation_end]

values_for_second_standard_deviation = [df for eachScore in df if eachScore >
                                        second_standard_deviation_start and eachScore < second_standard_deviation_end]


values_for_third_standard_deviation = [df for eachScore in df if eachScore >
                                       third_standard_deviation_start and eachScore < third_standard_deviation_end]

print(f"Mean of the Reading Score data is {mean}")
print(f"Median of the Reading Score data is {median}")
print(f"Mode of the Reading Score data is {mode}")
print(
    f"Standard Deviation of the Maths score column data is {standard_deviation}")

print()

# ** finding the percentages of the aboves values that lies inside the 1st,2nd,and 3rd standard deviation
# ! REMEMBER MEAN IS THE CENTER OF THE DATA AND ON THE BASIS OF THAT WE ARE FINDING THE STARTING AND ENDING POINTS
print(f"{len(values_for_first_standard_deviation)*100/len(df)}% of data lies within 1 standard deviation")
print(f"{len(values_for_second_standard_deviation)*100/len(df)}% of data lies within 2 standard deviation")
print(f"{len(values_for_third_standard_deviation)*100/len(df)}% of data lies within 3 standard deviation")


# MADE BY SWAYAM SAI KAR
