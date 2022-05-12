from ProdBasket import Product, Basket
import pytest

test_sum = [([Product('Болоньезе', 555), Product('Сок', 50), Product('Наггецы', 255)], 860)]
test_title = [([Product('Болоньезе', 555)], 'Болоньезе'), ([Product('Наггецы', 255)], 'Наггецы')]
test_price = [([Product('Болоньезе', 555)], 555), ([Product('Наггецы', 255)], 255)]

bol = Product('Болоньезе', 555)
sok = Product('Сок', 50)
nag = Product('Наггецы', 255)

add_test = [([bol, sok, nag],
             [bol, sok], nag)]

rem_test = [([bol, sok, nag],
            [bol, sok], nag)]

@pytest.mark.parametrize('products, summa', test_sum)
def test_basket(products, summa):
    basket = Basket()
    for prod in products:
        basket.add(prod)
    assert summa == basket.count_sum()


@pytest.mark.parametrize('title, price', test_title)
def test_name(title, price):
    product = Product(title, price)
    assert product.title == title


@pytest.mark.parametrize('title, price', test_price)
def test_price(title, price):
    product = Product(title, price)
    assert product.price == price

@pytest.mark.parametrize('products, products_two, products_thr', add_test)
def test_add_bask(products, products_two, products_thr):
    basket = Basket(products_two)
    basket.add(products_thr)
    assert basket.basket == products

@pytest.mark.parametrize('products, products_two, products_thr', rem_test)
def test_bask_rem(products, products_two, products_thr):
    basket = Basket(products)
    basket.remove(products_thr)
    assert basket.basket == products_two