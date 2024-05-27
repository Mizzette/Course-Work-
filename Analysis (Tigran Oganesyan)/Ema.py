class Ema:
    def __init__(self, alpha=1):
        self.alpha = alpha

    def calculate_alpha(self, period):
        return 2 / (period + 1)

    def calculate_ema(self, row):
        ema_arr = []
        smoothing = self.alpha
        period = int(2 / smoothing - 1)
        mean = sum(row[0: period]) / period
        for i in range(period + 1, len(row)):
            mean = mean + smoothing * (row[i] - mean)
            ema_arr.append(mean)
        return (ema_arr)

    def fit_predict(self, df, points):
        data = df
        smoothing = self.alpha
        period = int(2 / smoothing - 1)
        for x in range(points):
            forecast_arr = []
            for i in range(len(data)):
                mean = 0
                tmp = []
                mean = sum(data.iloc[i, :period]) / period
                for j in range(period + 1, len(data.iloc[0, :])):
                    mean = mean + smoothing * (data.iloc[i, j] - mean)
                    tmp.append(mean)
                forecast = smoothing * data.iloc[i, len(data.columns) - 1] + (1 - smoothing) * tmp[-1]
                forecast_arr.append(forecast)
            data[x] = forecast_arr
        prediction = data.iloc[:, -points:]
        df.drop(df.iloc[:, -points:], axis=1, inplace=True)
        return prediction
