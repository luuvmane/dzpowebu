from flask import Flask, render_template_string

app = Flask(__name__)

html_content = """
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/css/bootstrap.min.css" rel="stylesheet">

    <title>Bootstrap Example</title>
  </head>
  <body>
    <div class="container mt-5">
      <div class="row">
        <div class="col-md-6">
          <!-- Card Component -->
          <div class="card">
            <img src="https://via.placeholder.com/150" class="card-img-top" alt="Product Image">
            <div class="card-body">
              <h5 class="card-title">Product Title</h5>
              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
              <a href="#" class="btn btn-success">Купить</a>
            </div>
          </div>
        </div>
        <div class="col-md-6">
          <!-- Form Component -->
          <form>
            <div class="mb-3">
              <label for="name" class="form-label">Имя</label>
              <input type="text" class="form-control" id="name" placeholder="Введите ваше имя">
            </div>
            <div class="mb-3">
              <label for="email" class="form-label">Email</label>
              <input type="email" class="form-control" id="email" placeholder="Введите ваш email">
            </div>
            <button type="submit" class="btn btn-primary">Отправить</button>
          </form>
        </div>
      </div>
      <div class="row mt-5">
        <div class="col-12">
          <!-- FAQ Section -->
          <div class="accordion" id="faqAccordion">
            <div class="accordion-item">
              <h2 class="accordion-header" id="headingOne">
                <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                  Как купить?
                </button>
              </h2>
              <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#faqAccordion">
                <div class="accordion-body">
                  Чтобы купить товар, добавьте его в корзину и оформите заказ.
                </div>
              </div>
            </div>
            <div class="accordion-item">
              <h2 class="accordion-header" id="headingTwo">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                  Как доставить?
                </button>
              </h2>
              <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#faqAccordion">
                <div class="accordion-body">
                  Мы доставляем товар по всему миру. Оформите заказ, укажите адрес, и мы доставим его в течение 7-14 дней.
                </div>
              </div>
            </div>
            <div class="accordion-item">
              <h2 class="accordion-header" id="headingThree">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                  Какая гарантия?
                </button>
              </h2>
              <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#faqAccordion">
                <div class="accordion-body">
                  На все наши товары предоставляется гарантия 12 месяцев с момента покупки.
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bootstrap JS -->
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
  </body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
