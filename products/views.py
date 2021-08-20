from django.shortcuts import render


def index(request):
    context = {
        'title': 'Geekshop',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Geekshop - каталог',
        'products': [
            {
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
                'img': 'vendor/img/products/Adidas-hoodie.png',
                'price': 6090,
            },
            {
                'name': 'Синяя куртка The North Face',
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
                'img': 'vendor/img/products/Blue-jacket-The-North-Face.png',
                'price': 23725,
            },
            {
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
                'img': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                'price': 3390,
            },
            {
                'name': 'Черный рюкзак Nike Heritage',
                'description': 'Плотная ткань. Легкий материал.',
                'img': 'vendor/img/products/Black-Nike-Heritage-backpack.png',
                'price': 2340,
            },
            {
                'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                'description': 'Гладкий кожаный верх. Натуральный материал.',
                'img': 'vendor/img/products/Black-Dr-Martens-shoes.png',
                'price': 13590,
            },
            {
                'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
                'img': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
                'price': 2890,
            },
        ]
    }
    return render(request, 'products/products.html', context)
