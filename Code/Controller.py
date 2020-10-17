from Code import Model


class Controller:

    @staticmethod
    def updated_model(x0, X, y0, N, n0, N0):
        # processing user input

        x0 = float(x0.text())
        X = float(X.text())
        y0 = float(y0.text())
        N = int(N.text())

        n0 = int(n0.text())
        N0 = int(N0.text())

        # Updating Model in accordance with user input
        return Model.State.update(x0, X, y0, N, n0, N0)
