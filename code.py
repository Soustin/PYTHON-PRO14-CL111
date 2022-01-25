import plotly.figure_factory as pff
import plotly.graph_objects as go
import pandas as pd
import statistics
import random
import csv

df = pd.read_csv('data.csv')
time_list = df["reading_time"].tolist()

Fig_population = pff.create_distplot([time_list], ["Reading-Time"], show_hist = False)

mean_population = statistics.mean(time_list)
std_deviation_population = statistics.stdev(time_list)
print("mean-population = ", mean_population, "standard deviation-population = ", std_deviation_population)


def mean_our(counter) :
    dataset = []
    for i in range(1, counter):
        random_index = random.randint(0, len(time_list)-1)
        value = time_list[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


def plotmean(meanlist) :
    dfpl = meanlist
    mean = statistics.mean(dfpl)
    Fig = pff.create_distplot([dfpl], ["Average"], show_hist = False)
    Fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 1], mode = "lines", name = "MEAN"))
    Fig.show()

def setup() :
    mean_list = []
    for i in range(0, 100):
        set_of_means = mean_our(30)
        mean_list.append(set_of_means)
        plotmean(mean_list)
    mean_sample = statistics.mean(mean_list)
    std_deviation_sample = statistics.stdev(mean_list)
    print("mean-sample = ", mean_sample, "standard deviation-sample = ", std_deviation_sample)

    Fig_samp = pff.create_distplot([mean_list], ["Math-Score"], show_hist = False)
    Fig_samp.add_trace(go.Scatter(x=[mean_sample, mean_sample], y=[0, 0.20], mode="lines", name="MEAN"))
    Fig_samp.show()
    Fig_population.show()

    first_std_dev_start, first_std_dev_end = mean_sample - std_deviation_sample, mean_sample + std_deviation_sample
    sec_std_dev_start, sec_std_dev_end = mean_sample - (2*std_deviation_sample), mean_sample + (2*std_deviation_sample)
    third_std_dev_start, third_std_dev_end = mean_sample - (3*std_deviation_sample), mean_sample + (3*std_deviation_sample)

    list_of_data_within_1_std_dev = [result for result in mean_list if result > first_std_dev_start and result < first_std_dev_end]
    list_of_data_within_2_std_dev = [result for result in mean_list if result > sec_std_dev_start and result < sec_std_dev_end]
    list_of_data_within_3_std_dev = [result for result in mean_list if result > third_std_dev_start and result < third_std_dev_end]

    print("Percentage of data lies within first standard deviation", format(len(list_of_data_within_1_std_dev)*100/len(mean_list)))
    print("Percentage of data lies within second standard deviation", format(len(list_of_data_within_2_std_dev)*100/len(mean_list)))
    print("Percentage of data lies within third standard deviation", format(len(list_of_data_within_3_std_dev)*100/len(mean_list)))

    Fig1 = pff.create_distplot([mean_list], ["Reading-List"], show_hist = False)
    Fig1.add_trace(go.Scatter(x = [first_std_dev_start, first_std_dev_start], y = [0, 0.16], mode = "lines", name = "1ST STANDARD DEVIATION START"))
    Fig1.add_trace(go.Scatter(x = [first_std_dev_end, first_std_dev_end], y = [0, 0.16], mode = "lines", name = "1ST STANDARD DEVIATION END"))
    Fig1.add_trace(go.Scatter(x = [sec_std_dev_start, sec_std_dev_start], y = [0, 0.16], mode = "lines", name = "2ND STANDARD DEVIATION START"))
    Fig1.add_trace(go.Scatter(x = [sec_std_dev_end, sec_std_dev_end], y = [0, 0.16], mode = "lines", name = "2ND STANDARD DEVIATION END"))
    Fig1.add_trace(go.Scatter(x = [third_std_dev_start, third_std_dev_start], y = [0, 0.16], mode = "lines", name = "3RD STANDARD DEVIATION START"))
    Fig1.add_trace(go.Scatter(x = [third_std_dev_end, third_std_dev_end], y = [0, 0.16], mode = "lines", name = "3RD STANDARD DEVIATION END"))
    Fig1.add_trace(go.Scatter(x = [mean_list, mean_list], y = [0, 0.16], mode = "lines", name = "MEAN"))
    Fig1.add_trace(go.Scatter(x = [mean_sample, mean_sample], y = [0, 0.16], mode = "lines", name = "NEW SAMPLE MEAN"))
    Fig1.show()

    print(mean_sample)

setup()