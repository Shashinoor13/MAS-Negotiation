class UtilityFunction:
    def __init__(self,weights,feature_ranges):
        """
        :param weights: Dict of feature weights (e.g., {"price": 0.5, "warranty": 0.3})
        :param feature_ranges: Dict of min/max for normalization (e.g., {"price": (0, 100)})
        """
        self.weights = weights
        self.feature_ranges = feature_ranges

    def normalize(self,value,min_value,max_value,inverse=False):
        """
        Normalize value between 0 and 1.
        If inverse=True, high values are worse (e.g., price for buyer).
        """
        if min_value == max_value:
            return 0.0
        normalized = (value-min_value)/(max_value-min_value)
        return 1-normalized if inverse else normalized


    def evaluate(self,offer):
        """
        Evaluate utility of an offer.
        """
        score=0.0
        total_weight = sum(self.weights.values())
        for feature,weight in self.weights.items():
            # If the feature is not necessary for negotiation anymore and is not taken into consideration
            if feature not in offer or feature not in self.feature_ranges:
                continue
            
            val = offer[feature]
            min_val,max_val,inverse = self.feature_ranges[feature]

            normalized = self.normalize(val,min_val,max_val,inverse)
            score += weight*normalized
        
        # Returns normalized evaluation between 0 and 1
        return score/total_weight if total_weight != 0 else  0.0
