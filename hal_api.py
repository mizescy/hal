from flask import Flask, request, jsonify
import hal_lcd as LCD
import hal_input_switch as switch

app = Flask(__name__)
lcd = LCD.lcd()
switch.init()

@app.route("/lcd/display", methods=["POST"])
def display_on_lcd():
    data = request.json
    line = data.get("line", 1)
    message = data.get("message", "")
    lcd.lcd_display_string(message, line)
    return jsonify({"status": "success", "message": "Displayed on LCD"})

@app.route("/switch/state", methods=["GET"])
def get_switch_state():
    state = switch.read_slide_switch()
    return jsonify({"switch_state": state})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
