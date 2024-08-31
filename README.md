# Historical credibility for movie reviews and its application to weakly supervised classification
This paper was published in [Information Sciences 2023](https://www.sciencedirect.com/science/article/abs/pii/S002002552300155X).
> In this study, we deal with the problem of judging the credibility of movie reviews. The problem is challenging because even experts cannot clearly and efficiently judge the credibility of a movie review and the number of movie reviews is very large. To tackle this problem, we propose historical credibility that judges the credibility of reviews based on the historical ratings and textual reviews written by each reviewer. For this, we present three kinds of criteria that can clearly classify the reviews into trusted or distrusted ones. We validate the effectiveness of the proposed historical credibility through extensive analysis. Specifically, we show that characteristics between the trusted or distrusted reviews are quite distinguishable in terms of three viewpoints: 1) distribution, 2) statistics, and 3) correlation. Then, we present a multimodal-based classification model incorporating the historical credibility-based features with the textual review-based features in a weakly supervised manner to classify a given review as a trusted or distrusted one. Through experiments, we first show that our model is quite efficient because the entire data set is annotated according to the predefined criteria. Indeed, it can annotate 6,400 movie reviews only in 0.09 seconds, which occupies only 0.01% of the total learning time of the proposed classification model. Second, we show that our multimodal-based classification model outperforms the existing textual review-based classification model by 5.99%∼10.53% in terms of the average accuracy. In addition, we clearly confirm that our classification model shows higher accuracy as more data accumulates.
# Run
- Crawling movie review data

```python crawling_revised.py```

Currently, the review service of Naver Movie has been renewed, so the code may not work.
- Analysis

```Run bert_lstm.py```

The example data is intimate stranger
