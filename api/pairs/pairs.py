from api.pairs import bp
from api.pairs.pairs_data import PairsData

# Route to get pairs data
# Example http://127.0.0.1:5000/pairs/PF_XBTUSD/PF_DOTUSD/60/3.3/72/4/4
@bp.route('/pairs/<pair_1>/<pair_2>/<int:interval>/<float:beta>/<int:lag>/<int:high_sigma>/<int:low_sigma>')
def get_pairs_data(pair_1, pair_2, interval, beta, lag, high_sigma, low_sigma):
    print(pair_1, pair_2, interval, beta, lag, high_sigma, low_sigma)
    json = PairsData.create_pairs_json(pair_1, pair_2, interval, beta, lag, high_sigma, -low_sigma)
    return json