# __author__ = 'Hulu_Research'
import sys
import csv
import numpy as np

def ranking_loss(ground_truth, prediction):
    """
    compute the ranking loss define in CBVRP-ICIP2017 Challenge, hosted by Hulu LLC.

    :param ground_truth: A list of indices from 1 to C with order, where C is the number of items in Candidate set.
                         The item in the ith position is the top i relevant item in the candidate set for the
                         testing item.
    :param prediction: A list of floats. The value in the ith position indicates the relevance between the testing item
                       and the ith candidate item. The bigger the value is, the more relevant.
    :return: The ranking loss, a float.
    """
    prediction = np.array(prediction)
    exp_prediction = np.exp(prediction - np.max(prediction))
    sigma = np.sum(exp_prediction)
    metric = 0
    for x in ground_truth:
        score = exp_prediction[x - 1]
        metric = - np.log(score / sigma) + metric
        sigma = sigma - score
    return metric

def read_file(file_path):
    """
    read csv file.
    :param file_path: the path of the csv file
    :return: list of list
    """
    csv_file = file(file_path, 'r')
    reader = csv.reader(csv_file)
    data = []
    for line in reader:
        data.append(list(line))
    return data

if __name__=='__main__':
    g_path = sys.argv[1]
    p_path = sys.argv[2]
    ground_truth_data = read_file(g_path)
    prediction_data = read_file(p_path)
    total = 0
    for i in range(len(prediction_data)):
        prediction = [float(x) for x in prediction_data[i]]
        show_id = int(prediction[0])
        ground_truth = [int(x) for x in ground_truth_data[show_id - 1]]
        metric = ranking_loss(ground_truth[1:], prediction[1:])
        total = total + metric
    print total / len(prediction_data)


