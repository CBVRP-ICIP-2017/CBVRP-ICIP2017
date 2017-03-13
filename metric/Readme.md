## Usage
 python cvbrp_icip_metric.py PATH_GROUNDTRUTH PATH_PREDICTION

 PATH_GROUNDTRUTH: Path to a csv file containing the groundtruth top M most relevance item in Candidate set for Show_id
                   in Retrieval Set. The format of the csv file is:
                   Show_id, Candidate_id_1, Candidate_id_2, ..., Candidate_id_M, where Candidate_id_i is the index in
                   the Candidate set that ranked as top i relevant for Show_id in Retrieval set.

 PATH_PREDICTION: Path to a csv file containing the prediction of the relevance between Show_id and each item in Candidate
                  set. The format is: Show_id, score_1, score_2, ..., score_C, where C is the number of items in Candidate
                  set, and score_i is a value predicted by the model indicating the relevance between Show_id and ith item
                  in Candidate set.

 **The participants should submit a prediction file with the same format of PATH_PREDICTION file.**

 We provide an example of GROUNDTRUTH and PREDICTION file. The example files are only used to demonstrated the format of
 submission and has no relationship with the actual data.