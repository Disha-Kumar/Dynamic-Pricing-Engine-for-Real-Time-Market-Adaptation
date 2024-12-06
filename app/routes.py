from flask import Flask, jsonify, render_template
from data.collect_data import get_competitor_prices, get_inventory_levels
from data.process_data import process_data
from ml.train_model import train_model
from app.models import adjust_prices

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_prices', methods=['GET'])
def get_prices():
    competitor_prices = get_competitor_prices()
    inventory_levels = get_inventory_levels()
    demand = [100, 150, 200, 250, 300]  # Example demand data
    df = process_data(competitor_prices, inventory_levels, demand)
    model = train_model(df)
    predicted_prices = model.predict(df[['competitor_prices', 'inventory_levels', 'demand']].values)
    adjusted_prices = adjust_prices(predicted_prices)
    return jsonify({'adjusted_prices': adjusted_prices.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
