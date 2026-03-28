from flask import Flask, render_template, request, make_response, redirect, url_for


app = Flask(__name__)
application = app


def _validate_phone(value: str):
    allowed_chars = set("0123456789 ()-.+")
    if any(ch not in allowed_chars for ch in value):
        return (
            False,
            None,
            "Недопустимый ввод. В номере телефона встречаются недопустимые символы.",
        )

    digits = "".join(ch for ch in value if ch.isdigit())
    starts_with_plus7 = value.lstrip().startswith("+7")
    starts_with_8 = value.lstrip().startswith("8")
    expected_digits = 11 if (starts_with_plus7 or starts_with_8) else 10

    if len(digits) != expected_digits:
        return False, None, "Недопустимый ввод. Неверное количество цифр."

    core = digits[1:] if expected_digits == 11 else digits
    formatted = f"8-{core[:3]}-{core[3:6]}-{core[6:8]}-{core[8:10]}"
    return True, formatted, None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/request/url")
def request_url():
    return render_template("request_url.html", params=list(request.args.items()))


@app.route("/request/headers")
def request_headers():
    return render_template("request_headers.html", headers=list(request.headers.items()))


@app.route("/request/cookies")
def request_cookies():
    return render_template("request_cookies.html", cookies=list(request.cookies.items()))


@app.route("/request/cookies/set")
def set_cookie():
    response = make_response(redirect(url_for("request_cookies")))
    response.set_cookie("demo_cookie", "flask_lab2")
    return response


@app.route("/request/form", methods=["GET", "POST"])
def request_form():
    submitted = request.method == "POST"
    form_data = dict(request.form) if submitted else {}
    return render_template("request_form.html", submitted=submitted, form_data=form_data)


@app.route("/phone", methods=["GET", "POST"])
def phone():
    value = ""
    error = None
    formatted = None

    if request.method == "POST":
        value = request.form.get("phone", "")
        valid, formatted, error = _validate_phone(value)
        if not valid:
            formatted = None

    return render_template("phone.html", phone=value, error=error, formatted=formatted)


if __name__ == "__main__":
    app.run(debug=True)
