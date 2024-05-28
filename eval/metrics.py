import pandas as pd
from scipy.stats import spearmanr, kendalltau
from sklearn.metrics import mean_squared_error, cohen_kappa_score


def get_stats(rater1_scores : pd.Series , rater2_scores : pd.Series):
    """
    Accepts two pandas Series of the same length and returns dict of stats
    """
    if len(rater1_scores) != len(rater2_scores):
        raise Exception("Length mismatch")
    spearman_corr = spearmanr(rater1_scores, rater2_scores)
    kendall_tau = kendalltau(rater1_scores, rater2_scores)
    mse = mean_squared_error(rater1_scores, rater2_scores)
    qwk = cohen_kappa_score(rater1_scores, rater2_scores, weights='quadratic')

    
    return {
        'spearman_corr_stat': spearman_corr.statistic,
        'spearman_corr_pval': spearman_corr.pvalue,
        'kendall_tau_stat': kendall_tau.statistic,
        'kendall_tau_pval': kendall_tau.pvalue,
        'mean_square_error': mse,
        'quadratic_weighted_kappa': qwk
    }