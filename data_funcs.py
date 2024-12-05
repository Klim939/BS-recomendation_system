import json

sizes_list = ['XS', 'S', 'M', 'L', 'XL', 'XXl']

def load_data(filename):
    with open(f'data/{filename}', 'r') as f:
        return json.load(f)

def get_size(data, customer_id):
    for i in data:
        if i['customer_id'] == customer_id:
            return i['sizes']

def get_buys(data, customer_id):
    feedback = {'colors': [], 'fabrics': [], 'categories': []}
    for i in data:
        if i['customer_id'] == customer_id:
            for y in i['purchases']:
                if y['color'] not in feedback['colors']:
                    feedback['colors'].append(y['color'])
                if y['fabrics'] not in feedback['fabrics']:
                    feedback['fabrics'].append(y['fabrics'])
                if y['category'] not in feedback['categories']:
                    feedback['categories'].append(y['category'])
            return feedback

def recomend(items, sizes, purchases):
    feedback = []
    for i in items:
        if len(set(i['size']) & set(sizes)) != 0:
            k = 0
            if i['category'] in purchases['categories']:
                k += 1
            if i['color'] in purchases['colors']:
                k += 1
            if i['fabrics'] in purchases['fabrics']:
                k += 1
            if k >= 2:
                feedback.append(i)
    return feedback

def get_buys_by_size(items, sizes):
    feedback = []
    for i in items:
        if len(set(i['size']) & set(sizes)) != 0:
            feedback.append(i)
    return feedback

data = load_data('purchases.json')
data_items = load_data('items.json')
print(recomend(data_items, get_size(data, 3), get_buys(data, 3)))
